"""
helpers.py
──────────
Shared utility functions used across all dashboard pages.
"""

import pandas as pd
import plotly.graph_objects as go


# ─────────────────────────────────────────────────────────────────────────────
# Process Validation
# ─────────────────────────────────────────────────────────────────────────────

def validate_processes(dataframe: pd.DataFrame, total_memory: int, quantum: int) -> pd.DataFrame:
    """
    Validate the user-supplied process descriptor table.
    Returns a cleaned, sorted DataFrame or raises ValueError with a user-readable message.
    """
    required = ["PID", "Arrival", "Burst", "Priority", "Memory"]

    if dataframe.empty:
        raise ValueError("Process table is empty — add at least one process.")

    df = dataframe[required].copy()

    if df.isnull().any().any():
        raise ValueError("All PCB fields (PID, Arrival, Burst, Priority, Memory) must be filled.")

    for col in required:
        try:
            vals = pd.to_numeric(df[col], errors="raise")
        except Exception:
            raise ValueError(f"Column '{col}' must contain integer values only.")
        df[col] = vals.astype(int)

    if (df["PID"] <= 0).any():
        raise ValueError("Process IDs must be positive integers (> 0).")
    if df["PID"].duplicated().any():
        raise ValueError("Duplicate PID detected — each process must have a unique ID.")
    if (df["Arrival"] < 0).any():
        raise ValueError("Arrival time cannot be negative.")
    if (df[["Burst", "Priority", "Memory"]] <= 0).any().any():
        raise ValueError("Burst time, Priority, and Memory must all be > 0.")
    if (df["Memory"] > int(total_memory)).any():
        raise ValueError(
            f"One or more processes require more RAM than the system total ({total_memory} MB). "
            "Either reduce per-process memory or increase the Physical RAM setting."
        )
    if int(quantum) <= 0:
        raise ValueError("Time quantum must be ≥ 1 tick.")

    return df.sort_values(["Arrival", "PID"]).reset_index(drop=True)


# ─────────────────────────────────────────────────────────────────────────────
# Metric Reader
# ─────────────────────────────────────────────────────────────────────────────

def read_metric(summary_dict: dict, key: str, default: float = 0.0) -> float:
    """Safely read a numeric metric from the C++ engine summary dict."""
    val = summary_dict.get(key)
    if val is None:
        return default
    try:
        return float(str(val).replace("%", "").strip())
    except (ValueError, AttributeError):
        return default


# ─────────────────────────────────────────────────────────────────────────────
# Plotly Layout Factory
# ─────────────────────────────────────────────────────────────────────────────

def plotly_dark_layout(height: int = 300, **overrides) -> dict:
    """
    Returns a base Plotly update_layout dict styled for the dark KernelSim theme.
    Pass keyword overrides to customise individual keys.
    """
    base = dict(
        paper_bgcolor="#06101e",
        plot_bgcolor="#030810",
        height=height,
        margin=dict(l=20, r=20, t=38, b=36),
        font=dict(family="JetBrains Mono", color="#718096"),
        xaxis=dict(
            showgrid=True,
            gridcolor="#1a2740",
            gridwidth=1,
            tickfont=dict(family="JetBrains Mono", color="#718096", size=10),
            linecolor="#1a2740",
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor="#1a2740",
            gridwidth=1,
            tickfont=dict(family="JetBrains Mono", color="#718096", size=10),
            linecolor="#1a2740",
        ),
    )
    base.update(overrides)
    return base


# ─────────────────────────────────────────────────────────────────────────────
# CPU State Extractor (used by Simulator page at a given scrub tick)
# ─────────────────────────────────────────────────────────────────────────────

def cpu_state_at_tick(
    scrub_t: int,
    timeline_df: pd.DataFrame,
    cpu_df: pd.DataFrame,
    result_df: pd.DataFrame,
) -> dict:
    """
    Returns a dict describing the full CPU + memory + queue state at clock tick `scrub_t`.
    Keys: curr_proc_str, cpu_running, proc_num, pc_val, r0, r1, r2, r3,
          in_ram_pids, ready_pids, mem_wait_pids, used_ram_at_t
    """
    active = timeline_df[(timeline_df["Start"] <= scrub_t) & (timeline_df["End"] > scrub_t)]
    if not active.empty:
        curr_proc_str = str(active.iloc[0]["Process"])
        cpu_running   = True
        proc_num      = int(curr_proc_str.replace("P", "").strip()) if "P" in curr_proc_str else -1
    else:
        curr_proc_str = "IDLE"
        cpu_running   = False
        proc_num      = -1

    latest = cpu_df[cpu_df["Time"] <= scrub_t]
    if not latest.empty:
        lev    = latest.iloc[-1]
        pc_val = f"0x{int(lev['PC']):04X}"
        raw    = str(lev["Registers"])
        regs   = (raw.split(";") + ["0", "0", "0", "0"])[:4] if ";" in raw else ["0", "0", "0", "0"]
        r0, r1, r2, r3 = regs
    else:
        pc_val = "0x0000"
        r0 = r1 = r2 = r3 = "0"

    in_ram_pids: list[int]      = []
    ready_pids: list[int]       = []
    mem_wait_pids: list[int]    = []
    used_ram_at_t: int          = 0

    for _, pr in result_df.iterrows():
        pid  = int(pr["PID"])
        arr  = int(pr["Arrival"])
        adm  = int(pr["Admission Time"])
        comp = int(pr["Completion"])
        mem  = int(pr["Memory (MB)"])

        if adm <= scrub_t < comp:
            in_ram_pids.append(pid)
            used_ram_at_t += mem
            if pid != proc_num:
                ready_pids.append(pid)
        elif arr <= scrub_t < adm:
            mem_wait_pids.append(pid)

    return dict(
        curr_proc_str=curr_proc_str,
        cpu_running=cpu_running,
        proc_num=proc_num,
        pc_val=pc_val,
        r0=r0, r1=r1, r2=r2, r3=r3,
        in_ram_pids=in_ram_pids,
        ready_pids=ready_pids,
        mem_wait_pids=mem_wait_pids,
        used_ram_at_t=used_ram_at_t,
    )
