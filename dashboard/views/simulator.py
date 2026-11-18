"""
simulator.py
────────────
Interactive simulation workspace:
- Presets & Process Data Editor
- Engine Parameters (Algorithm, Quantum, RAM)
- Subprocess Dispatch via cpp_backend
- Telemetry KPI Grid
- Cycle Scrubber (Clock tick step-through)
- Gantt Chart, Memory Map, PCB Table, Logs, and Data Export
"""

import html
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from cpp_backend import run_cpp_simulation
from utils.constants import PRESETS, PID_COLORS, RESULT_KEYS
from utils.helpers import validate_processes, read_metric, plotly_dark_layout, cpu_state_at_tick


def render_simulator_page():
    st.markdown(
        """
        <div class="ks-page-header">
            <div class="ks-page-eyebrow">⚙️ SIMULATION ENGINE</div>
            <div class="ks-page-title">Virtual Machine & OS Kernel Simulator</div>
            <div class="ks-page-subtitle">
                Configure your process descriptor table, select an algorithm, and dispatch the native C++ engine.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Workload presets
    st.markdown('<div class="ks-label">🎯 LOAD WORKLOAD PRESET</div>', unsafe_allow_html=True)
    p_cols = st.columns(len(PRESETS))
    for idx, (p_name, p_data) in enumerate(PRESETS.items()):
        with p_cols[idx]:
            if st.button(p_name, key=f"sim_preset_{idx}", use_container_width=True):
                st.session_state.processes = [p.copy() for p in p_data]
                st.rerun()

    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)

    # Process Editor Table
    st.markdown('<div class="ks-label">📋 PROCESS CONTROL BLOCK (PCB) DESCRIPTORS</div>', unsafe_allow_html=True)
    edited_df = st.data_editor(
        pd.DataFrame(st.session_state.processes),
        num_rows="dynamic",
        use_container_width=True,
        hide_index=True,
        key="ks_process_editor",
        column_config={
            "PID": st.column_config.NumberColumn("PID", min_value=1, step=1, help="Process ID"),
            "Arrival": st.column_config.NumberColumn("Arrival Tick", min_value=0, step=1, help="Simulation arrival clock"),
            "Burst": st.column_config.NumberColumn("Burst (Ticks)", min_value=1, step=1, help="CPU cycles requested"),
            "Priority": st.column_config.NumberColumn("Priority Rank", min_value=1, step=1, help="Lower value = higher priority"),
            "Memory": st.column_config.NumberColumn("RAM (MB)", min_value=1, step=1, help="Continuous memory footprint"),
        },
    )
    st.session_state.processes = edited_df.to_dict("records")

    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)

    # Hardware & Scheduling Knobs
    col_algo, col_quantum, col_ram = st.columns([2, 1.2, 1.5])
    with col_algo:
        algorithm = st.selectbox(
            "CPU Scheduling Policy",
            ["FCFS", "SJF", "Priority", "Round Robin"],
            index=3,
            help="Core algorithm dispatched inside the C++ engine.",
        )
    with col_quantum:
        quantum = st.number_input(
            "Time Quantum (τ)",
            min_value=1,
            value=2,
            step=1,
            disabled=(algorithm != "Round Robin"),
            help="Slicing interval for Round Robin.",
        )
    with col_ram:
        total_memory = st.number_input(
            "Physical RAM Capacity (MB)",
            min_value=50,
            value=512,
            step=50,
            help="Simulated MMU limit.",
        )

    # Action Triggers
    b1, b2 = st.columns([2.5, 1.5])
    with b1:
        run_sim = st.button("▶  DISPATCH C++ KERNEL SIMULATION", type="primary", use_container_width=True)
    with b2:
        run_bench = st.button("⚡  BENCHMARK ALL 4 POLICIES", type="secondary", use_container_width=True)

    # Simulation Dispatch
    if run_sim:
        for k in RESULT_KEYS:
            st.session_state.pop(k, None)
        try:
            validated = validate_processes(edited_df, total_memory, quantum)
            out = run_cpp_simulation(
                validated.to_dict("records"),
                algorithm,
                int(quantum),
                int(total_memory),
            )
            for k, v in out.items():
                st.session_state[k] = v
            st.session_state.algorithm = algorithm
            st.session_state.total_memory = int(total_memory)
            st.session_state.quantum = int(quantum)
            st.toast(f"Simulation completed: [{algorithm}]", icon="⚡")
        except Exception as e:
            st.error(f"Hardware / Simulation Exception: {e}")

    if run_bench:
        try:
            validated = validate_processes(edited_df, total_memory, quantum)
            b_data = []
            with st.spinner("Synthesizing multi-algorithm benchmark via C++ engine..."):
                for alg in ["FCFS", "SJF", "Priority", "Round Robin"]:
                    res = run_cpp_simulation(
                        validated.to_dict("records"),
                        alg,
                        int(quantum),
                        int(total_memory),
                    )
                    rdf = res["results"]
                    summ = res["summary"]
                    b_data.append({
                        "Algorithm": alg,
                        "Avg Waiting": round(float(rdf["Waiting"].mean()), 2),
                        "Avg Turnaround": round(float(rdf["Turnaround"].mean()), 2),
                        "Avg Memory Wait": round(float(rdf["Memory Wait"].mean()), 2),
                        "Context Switches": int(read_metric(summ, "Context switches")),
                        "CPU Utilization (%)": read_metric(summ, "CPU utilization"),
                        "Elapsed Time": int(read_metric(summ, "Elapsed time")),
                    })
                # Set active algorithm output
                p_out = run_cpp_simulation(
                    validated.to_dict("records"),
                    algorithm,
                    int(quantum),
                    int(total_memory),
                )
                for k, v in p_out.items():
                    st.session_state[k] = v
                st.session_state.algorithm = algorithm
                st.session_state.total_memory = int(total_memory)
                st.session_state.quantum = int(quantum)
                st.session_state.benchmark_results = pd.DataFrame(b_data)
            st.toast("Benchmark matrix synthesized successfully!", icon="📊")
        except Exception as e:
            st.error(f"Benchmark Failure: {e}")

    # Output Presentation
    if "results" in st.session_state:
        result_df = st.session_state.results
        timeline_df = st.session_state.timeline
        memory_df = st.session_state.memory_events
        state_df = st.session_state.state_events
        cpu_df = st.session_state.cpu_events
        summary = st.session_state.summary
        algo_used = st.session_state.algorithm
        ram_cap = st.session_state.total_memory

        elapsed_time = int(read_metric(summary, "Elapsed time"))
        busy_time = int(read_metric(summary, "Busy time"))
        ctx_switches = int(read_metric(summary, "Context switches"))
        cpu_util = read_metric(summary, "CPU utilization")
        avg_wait = result_df["Waiting"].mean()
        avg_turnaround = result_df["Turnaround"].mean()
        peak_ram = int(memory_df["UsedMB"].max())

        st.markdown('<hr class="ks-divider">', unsafe_allow_html=True)
        st.markdown('<div class="ks-label">📡 ENGINE TELEMETRY SNAPSHOT</div>', unsafe_allow_html=True)

        st.markdown(
            f"""
            <div class="ks-kpi-grid">
                <div class="ks-kpi">
                    <div class="ks-kpi-label">Policy</div>
                    <div class="ks-kpi-value" style="color:#60b8f5; font-size:1.15rem;">{algo_used}</div>
                    <div class="ks-kpi-sub">τ = {st.session_state.quantum if algo_used == 'Round Robin' else 'N/A'}</div>
                </div>
                <div class="ks-kpi green">
                    <div class="ks-kpi-label">CPU Utilization</div>
                    <div class="ks-kpi-value" style="color:#46c97a;">{cpu_util:.1f}%</div>
                    <div class="ks-kpi-sub">{busy_time} busy / {elapsed_time} total ticks</div>
                </div>
                <div class="ks-kpi amber">
                    <div class="ks-kpi-label">Context Switches</div>
                    <div class="ks-kpi-value" style="color:#f0953a;">{ctx_switches}</div>
                    <div class="ks-kpi-sub">{int(result_df["Execution Slices"].sum())} execution slices</div>
                </div>
                <div class="ks-kpi purple">
                    <div class="ks-kpi-label">Avg Waiting Time</div>
                    <div class="ks-kpi-value" style="color:#a07eea;">{avg_wait:.2f}</div>
                    <div class="ks-kpi-sub">Ticks in ready queue</div>
                </div>
                <div class="ks-kpi">
                    <div class="ks-kpi-label">Avg Turnaround</div>
                    <div class="ks-kpi-value" style="color:#60b8f5;">{avg_turnaround:.2f}</div>
                    <div class="ks-kpi-sub">Submission to exit latency</div>
                </div>
                <div class="ks-kpi rose">
                    <div class="ks-kpi-label">Peak Memory</div>
                    <div class="ks-kpi-value" style="color:#f47b7b;">{peak_ram} <span style="font-size:0.8rem;">MB</span></div>
                    <div class="ks-kpi-sub">{peak_ram / ram_cap * 100:.1f}% of {ram_cap} MB capacity</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Clock Scrubber
        st.markdown('<div class="ks-label">🔬 CYCLE-BY-CYCLE HARDWARE STEPPER</div>', unsafe_allow_html=True)
        col_scrub, col_status = st.columns([4, 1])
        with col_scrub:
            scrub_t = st.slider(
                "Hardware System Clock Tick (T)",
                min_value=0,
                max_value=max(1, elapsed_time),
                value=0,
                step=1,
            )
        with col_status:
            status_txt = "EXECUTING" if scrub_t < elapsed_time else "COMPLETED"
            status_col = "#46c97a" if scrub_t < elapsed_time else "#f0953a"
            st.markdown(
                f"""
                <div style="font-family:var(--mono); font-size:0.75rem; background:#06101e; border:1px solid #1a2a40; padding:10px 14px; border-radius:6px; margin-top:14px;">
                    <div>SYS_CLK: <span style="color:#60b8f5; font-weight:700;">T = {scrub_t:02d}</span></div>
                    <div style="color:{status_col}; font-weight:600; margin-top:3px;">● {status_txt}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Extract CPU State at Scrub Tick
        state = cpu_state_at_tick(scrub_t, timeline_df, cpu_df, result_df)

        hud_c1, hud_c2 = st.columns(2)
        with hud_c1:
            c_color = "#46c97a" if state["cpu_running"] else "#f0953a"
            st.markdown(
                f"""
                <div class="ks-cpu-hud">
                    <div class="ks-hud-title">
                        <span>VIRTUAL CPU CORE 0</span>
                        <span style="color:{c_color};">● {state['curr_proc_str']}</span>
                    </div>
                    <div class="ks-reg-grid">
                        <div class="ks-reg-box"><div class="ks-reg-name">PROGRAM COUNTER</div><div class="ks-reg-val" style="color:#60b8f5;">{state['pc_val']}</div></div>
                        <div class="ks-reg-box"><div class="ks-reg-name">R0 (ACCUMULATOR)</div><div class="ks-reg-val">{state['r0']}</div></div>
                        <div class="ks-reg-box"><div class="ks-reg-name">R1 (SLICE COUNT)</div><div class="ks-reg-val">{state['r1']}</div></div>
                        <div class="ks-reg-box"><div class="ks-reg-name">R2 (LAST TICK)</div><div class="ks-reg-val">{state['r2']}</div></div>
                        <div class="ks-reg-box"><div class="ks-reg-name">R3 (PID TAG)</div><div class="ks-reg-val">{state['r3']}</div></div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with hud_c2:
            rq_pills = " ".join([f'<span class="ks-status-pill pill-cyan">PID {p}</span>' for p in state["ready_pids"]]) or '<span style="color:#637080;">Queue empty</span>'
            mw_pills = " ".join([f'<span class="ks-status-pill pill-amber">PID {p}</span>' for p in state["mem_wait_pids"]]) or '<span style="color:#637080;">No blocked processes</span>'
            st.markdown(
                f"""
                <div class="ks-cpu-hud">
                    <div class="ks-hud-title">
                        <span>DISPATCHER & ADMISSION QUEUES (T = {scrub_t})</span>
                    </div>
                    <div style="font-family:var(--mono); font-size:0.75rem;">
                        <div style="margin-bottom:10px;">
                            <div style="color:#637080; font-size:0.65rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:4px;">Ready Queue (Admitted into RAM):</div>
                            <div style="display:flex; gap:6px; flex-wrap:wrap;">{rq_pills}</div>
                        </div>
                        <div>
                            <div style="color:#f0953a; font-size:0.65rem; text-transform:uppercase; letter-spacing:1px; margin-bottom:4px;">Waiting for Memory (Admission Blocked):</div>
                            <div style="display:flex; gap:6px; flex-wrap:wrap;">{mw_pills}</div>
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # Tabbed Workspace
        tabs = st.tabs([
            "📈 Gantt Timeline",
            "💾 Memory Map (MMU)",
            "📋 Process Control Block (PCB)",
            "🔄 CPU & State Events",
            "📡 Kernel Ring Buffer (DMESG)",
            "📥 Diagnostics & Export",
        ])

        with tabs[0]:
            st.markdown('<div class="ks-label">GANTT EXECUTION BLOCKS OVER TIME</div>', unsafe_allow_html=True)
            g_fig = go.Figure()
            for _, b in timeline_df.iterrows():
                p_name = str(b["Process"])
                b_start = int(b["Start"])
                b_end = int(b["End"])
                b_dur = int(b["Duration"])
                pid = int(p_name.replace("P", "").strip()) if "P" in p_name else 0
                color = PID_COLORS.get(pid, "#60b8f5")

                g_fig.add_trace(go.Bar(
                    x=[b_dur],
                    y=["CPU Core 0"],
                    base=[b_start],
                    orientation="h",
                    name=p_name,
                    text=[f"{p_name} ({b_dur}t)"],
                    textposition="inside",
                    marker=dict(color=color, line=dict(color="#04080f", width=1)),
                    hovertemplate=f"<b>{p_name}</b><br>Start: {b_start}<br>End: {b_end}<br>Duration: {b_dur} ticks<extra></extra>",
                ))

            g_fig.add_vline(
                x=scrub_t,
                line_dash="dot",
                line_color="#60b8f5",
                line_width=2,
                annotation_text=f"T={scrub_t}",
                annotation_position="top",
                annotation_font=dict(color="#60b8f5", size=11, family="JetBrains Mono"),
            )
            g_fig.update_layout(
                barmode="overlay",
                **plotly_dark_layout(
                    height=240,
                    xaxis=dict(
                        title=dict(text="System Clock Ticks", font=dict(family="JetBrains Mono", color="#637080")),
                        range=[0, max(1, elapsed_time)],
                        dtick=1,
                        showgrid=True,
                        gridcolor="#1a2a40",
                        tickfont=dict(family="JetBrains Mono", color="#637080"),
                    ),
                    yaxis=dict(showticklabels=True, tickfont=dict(family="JetBrains Mono", color="#60b8f5", size=12)),
                    showlegend=True,
                    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(family="JetBrains Mono", color="#dde4ef", size=10)),
                )
            )
            st.plotly_chart(g_fig, use_container_width=True)
            st.dataframe(timeline_df[["Process", "Start", "End", "Duration"]], use_container_width=True, hide_index=True)

        with tabs[1]:
            # Physical RAM Visual Segment Bar
            free_ram = ram_cap - state["used_ram_at_t"]
            mem_segs = []
            cur_offset = 0

            for p_in in state["in_ram_pids"]:
                p_row = result_df[result_df["PID"] == p_in].iloc[0]
                p_mem = int(p_row["Memory (MB)"])
                pct = (p_mem / ram_cap) * 100
                color = PID_COLORS.get(p_in, "#60b8f5")
                mem_segs.append(f'<div class="ks-mem-seg" style="width:{pct:.1f}%; background:{color};" title="PID {p_in}: {p_mem}MB">PID {p_in} ({p_mem}MB)</div>')
                cur_offset += p_mem

            if free_ram > 0:
                free_pct = (free_ram / ram_cap) * 100
                mem_segs.append(f'<div class="ks-mem-seg" style="width:{free_pct:.1f}%; background:#1a2a40; color:#637080;" title="FREE RAM: {free_ram}MB">FREE ({free_ram}MB)</div>')

            st.markdown(
                f"""
                <div class="ks-mem-bar-wrap">
                    <div class="ks-mem-bar-label">
                        <span style="color:#60b8f5;">PHYSICAL RAM ALLOCATION SNAPSHOT (T = {scrub_t})</span>
                        <span>USED: {state['used_ram_at_t']} / {ram_cap} MB ({state['used_ram_at_t'] / ram_cap * 100:.1f}%)</span>
                    </div>
                    <div class="ks-mem-bar">{''.join(mem_segs)}</div>
                    <div style="display:flex; justify-content:space-between; font-family:var(--mono); font-size:0.65rem; color:#637080; margin-top:5px;">
                        <span>BASE: 0x0000</span><span>LIMIT: 0x{ram_cap:04X} ({ram_cap} MB)</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

            # Continuous RAM Curve
            fig_mem = go.Figure()
            fig_mem.add_trace(go.Scatter(
                x=memory_df["Time"],
                y=memory_df["UsedMB"],
                mode="lines+markers",
                line=dict(shape="hv", color="#60b8f5", width=2.5),
                marker=dict(size=6, color="#46c97a"),
                name="Used RAM",
                hovertemplate="Time: %{x} ticks<br>Used RAM: %{y} MB<extra></extra>",
            ))
            fig_mem.add_hline(
                y=ram_cap,
                line_dash="dash",
                line_color="#f47b7b",
                annotation_text=f"RAM CAPACITY ({ram_cap} MB)",
                annotation_font=dict(color="#f47b7b", family="JetBrains Mono"),
            )
            fig_mem.update_layout(
                **plotly_dark_layout(
                    height=280,
                    xaxis=dict(title=dict(text="Simulation Clock Ticks", font=dict(family="JetBrains Mono", color="#637080")), showgrid=True, gridcolor="#1a2a40", tickfont=dict(family="JetBrains Mono", color="#637080")),
                    yaxis=dict(title=dict(text="Memory (MB)", font=dict(family="JetBrains Mono", color="#637080")), range=[0, ram_cap * 1.15], showgrid=True, gridcolor="#1a2a40", tickfont=dict(family="JetBrains Mono", color="#637080")),
                )
            )
            st.plotly_chart(fig_mem, use_container_width=True)
            st.dataframe(memory_df, use_container_width=True, hide_index=True)

        with tabs[2]:
            display_pcb = result_df.copy()
            display_pcb["Registers"] = display_pcb.apply(lambda r: f"[{r['R0']}, {r['R1']}, {r['R2']}, {r['R3']}]", axis=1)
            display_pcb["PC"] = display_pcb["Program Counter"].apply(lambda pc: f"0x{int(pc):04X}")
            st.dataframe(
                display_pcb[[
                    "PID", "State", "Priority", "Arrival", "Admission Time", "Memory Wait",
                    "Burst", "First Start", "Completion", "Turnaround", "Waiting",
                    "PC", "Registers", "Execution Slices", "Context Switches", "Memory (MB)",
                ]],
                use_container_width=True,
                hide_index=True,
            )

        with tabs[3]:
            st.markdown('<div class="ks-label">VIRTUAL HARDWARE EXECUTION TRACE</div>', unsafe_allow_html=True)
            st.dataframe(cpu_df, use_container_width=True, hide_index=True)
            st.markdown('<div class="ks-label" style="margin-top:14px;">PROCESS STATE TRANSITION TRAIL</div>', unsafe_allow_html=True)
            st.dataframe(state_df, use_container_width=True, hide_index=True)

        with tabs[4]:
            logs = [(0, "KERN_BOOT", f"Kernel initialized | Physical RAM: {ram_cap} MB | Policy: {algo_used}")]
            for _, m in memory_df.iterrows():
                logs.append((int(m["Time"]), "MMU_ALLOC", f"Process {m['PID']} {m['Event']} | RAM in use: {m['UsedMB']}/{ram_cap} MB"))
            for _, s in state_df.iterrows():
                f_st = s.get("Previous State", s.get("From", "Unknown"))
                t_st = s.get("New State", s.get("To", "Unknown"))
                logs.append((int(s["Time"]), "SCHED_STATE", f"PID {s['PID']} state changed: [{f_st}] ➔ [{t_st}]"))
            for _, c in cpu_df.iterrows():
                ev = str(c.get("Event", ""))
                fr = str(c.get("From PID", "-"))
                to = str(c.get("To PID", "-"))
                try:
                    pc = int(c.get("PC", 0))
                except Exception:
                    pc = 0
                dur = c.get("Duration", 0)
                if ev == "CONTEXT SWITCH":
                    logs.append((int(c["Time"]), "SCHED_CTX", f"Context switch: PID {fr} preempted ➔ PID {to} dispatched (Saved PC: 0x{pc:04X})"))
                else:
                    logs.append((int(c["Time"]), "CPU_EXEC", f"Executed PID {to} for {dur} ticks. PC: 0x{pc:04X}"))

            logs.sort(key=lambda x: x[0])
            dmesg_html = "".join([
                f'<div class="ks-log-line"><span class="ks-log-t">[{t:04d}.00]</span>'
                f'<span class="ks-log-s">[{html.escape(str(s))}]</span>'
                f'<span class="ks-log-m">{html.escape(str(m))}</span></div>'
                for t, s, m in logs
            ])
            st.markdown(f'<div class="ks-terminal">{dmesg_html}</div>', unsafe_allow_html=True)

        with tabs[5]:
            st.markdown('<div class="ks-label">C++ RAW SUMMARY TEXT</div>', unsafe_allow_html=True)
            st.code(st.session_state.summary_text, language="text")
            st.caption(f"C++ Engine Output Directory: {st.session_state.output_dir}")

            st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
            ec1, ec2, ec3 = st.columns(3)
            with ec1:
                st.download_button("📥 Export Process Results (CSV)", result_df.to_csv(index=False), "process_results.csv", "text/csv", use_container_width=True)
                st.download_button("📥 Export MMU Events (CSV)", memory_df.to_csv(index=False), "memory_events.csv", "text/csv", use_container_width=True)
            with ec2:
                st.download_button("📥 Export Gantt Timeline (CSV)", timeline_df.to_csv(index=False), "timeline.csv", "text/csv", use_container_width=True)
                st.download_button("📥 Export State Events (CSV)", state_df.to_csv(index=False), "state_events.csv", "text/csv", use_container_width=True)
            with ec3:
                st.download_button("📥 Export CPU Events (CSV)", cpu_df.to_csv(index=False), "cpu_events.csv", "text/csv", use_container_width=True)
                st.download_button("📥 Export Kernel Summary (TXT)", st.session_state.summary_text, "summary.txt", "text/plain", use_container_width=True)
