"""
concepts.py
───────────
Detailed educational view explaining the operating systems principles
modelled inside the simulation engine.
"""

import streamlit as st


def render_concepts_page():
    st.markdown(
        """
        <div class="ks-page-header">
            <div class="ks-page-eyebrow">📚 EDUCATIONAL CURRICULUM</div>
            <div class="ks-page-title">Operating System Concepts & Mechanics</div>
            <div class="ks-page-subtitle">
                A structured breakdown of the kernel subsystems, mathematical formulas,
                and architectural designs simulated inside the C++ engine.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    concepts = [
        (
            "01",
            "Process Control Block (PCB)",
            "struct Process / task_struct",
            """
            The PCB is the kernel's primary data structure representing an active process.
            It encapsulates the execution context, resource ownership, and scheduling state.
            In this engine, each PCB maintains:
            """,
            [
                "Process ID (PID): Unique integer identifier.",
                "Timing Profiles: Arrival tick, requested CPU burst ticks, remaining burst ticks.",
                "Priority Rank: Numerical rank (lower value represents higher dispatch urgency).",
                "Memory Size: Contiguous physical RAM requirements (MB).",
                "Virtual Register File: Program Counter (PC) and 4 General Purpose Registers (R0–R3).",
                "Performance Accounting: First dispatch tick, termination tick, total turnaround, waiting time, and context switch counts.",
            ],
        ),
        (
            "02",
            "Extended 5-State Process Lifecycle",
            "New ➔ Waiting for Memory ➔ Ready ➔ Running ➔ Terminated",
            """
            Unlike basic theoretical models that assume infinite RAM, real operating systems
            cannot admit processes into memory without verifying capacity. This engine models:
            """,
            [
                "New: Process has been created in the workload description.",
                "Waiting for Memory (Admission Queue): The process has arrived at the clock, but total active RAM cannot satisfy its demand. It stalls until running processes free capacity.",
                "Ready: The MMU has granted contiguous RAM, and the process is enqueued into the CPU dispatcher queue.",
                "Running: Dispatched to Virtual CPU Core 0 for a time slice or full burst.",
                "Terminated: CPU burst completed. The MMU immediately reclaims its RAM footprint, triggering evaluation of the Waiting for Memory queue.",
            ],
        ),
        (
            "03",
            "CPU Scheduling Policies",
            "FCFS · SJF · Priority · Round Robin",
            """
            The scheduler governs CPU multiplexing. Each algorithm balances fairness, latency,
            and throughput differently:
            """,
            [
                "First-Come, First-Served (FCFS): Non-preemptive. Dispatches processes in chronological order of arrival. Susceptible to the Convoy Effect.",
                "Shortest Job First (SJF): Non-preemptive. Selects the process with the shortest burst time. Provably optimal for minimizing average waiting time.",
                "Priority Scheduling: Non-preemptive. Selects the ready process with the highest priority rank (lowest numerical integer).",
                "Round Robin (RR): Preemptive. Grants each ready process a fixed time quantum (τ). If incomplete, the process is preempted and re-enqueued.",
            ],
        ),
        (
            "04",
            "Context Switching Overhead",
            "Hardware State Persistence & Dispatch Latency",
            """
            A context switch occurs when the scheduler halts one process and dispatches another.
            During this interval:
            """,
            [
                "The current execution context (Program Counter, registers) is serialized into the PCB.",
                "The incoming process's saved registers are restored to the CPU.",
                "Context switches introduce overhead without advancing application work; Round Robin with small quanta generates higher switch counts.",
            ],
        ),
        (
            "05",
            "Memory Management & Admission Control",
            "Physical Memory Bounds & Dynamic Deallocation",
            """
            The Memory Management Unit (MMU) acts as the gatekeeper for system stability:
            """,
            [
                "Fixed Physical Memory Limit: The kernel enforces a strict RAM capacity (e.g. 512 MB).",
                "Admission Control: Sum of allocated memory must never exceed total RAM capacity.",
                "Deallocation Triggers: When a process reaches the Terminated state, its memory is instantly freed, immediately waking the admission scanner.",
            ],
        ),
        (
            "06",
            "Mathematical Telemetry & Performance Formulas",
            "Evaluating Scheduling Performance",
            """
            Standard metrics for quantifying scheduling efficiency:
            """,
            [
                "Turnaround Time (TAT) = Completion Time − Arrival Time",
                "Waiting Time (WT) = Turnaround Time − Burst Time − Memory Wait Time",
                "Memory Wait Time (MWT) = Admission Time − Arrival Time",
                "CPU Utilization (%) = (Total Busy Execution Ticks / Total Simulation Ticks) × 100",
            ],
        ),
    ]

    for num, title, subtitle, desc, points in concepts:
        pts_html = "".join([f"<li>{p}</li>" for p in points])
        st.markdown(
            f"""
            <div class="ks-concept">
                <div class="ks-concept-header">
                    <div class="ks-concept-num">{num}</div>
                    <div>
                        <div class="ks-concept-title">{title}</div>
                        <div class="ks-concept-subtitle">{subtitle}</div>
                    </div>
                </div>
                <div class="ks-concept-body">{desc}</div>
                <ul class="ks-concept-bullets">{pts_html}</ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div style="height:20px;"></div>', unsafe_allow_html=True)
    c1, _ = st.columns([2, 3])
    with c1:
        if st.button("▶  Launch Simulator to Test These Concepts", type="primary"):
            st.session_state["nav_selection"] = "simulator"
            st.rerun()
