"""
landing.py
──────────
Professional landing page module displaying:
- Hero banner & value proposition
- High-level platform statistics
- Interactive learning cards for OS concepts
- Three-step workflow guide
- Comparison summary of scheduling policies
"""

import streamlit as st


def render_landing_page():
    # Hero Section
    st.markdown(
        """
        <div class="ks-hero">
            <div class="ks-hero-pill">
                <span>⚡</span> POWERED BY NATIVE C++ KERNEL ENGINE
            </div>
            <h1 class="ks-hero-title">
                Learn Operating Systems<br>
                <span class="hl-cyan">By Simulating</span> the <span class="hl-green">Kernel</span>
            </h1>
            <p class="ks-hero-subtitle">
                An interactive, high-fidelity platform bringing OS theory into practice.
                Observe CPU scheduling, MMU memory admission, context switching, and register states
                running in deterministic real-time.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Hero Action Buttons
    c_btn1, c_btn2, _ = st.columns([1.5, 1.5, 3])
    with c_btn1:
        if st.button("▶  Launch Simulator", type="primary", use_container_width=True):
            st.session_state["nav_selection"] = "simulator"
            st.rerun()
    with c_btn2:
        if st.button("📚  Explore Concepts", type="secondary", use_container_width=True):
            st.session_state["nav_selection"] = "concepts"
            st.rerun()

    # Core Stats Row
    st.markdown(
        """
        <div class="ks-stats-row">
            <div>
                <div class="ks-stat-num">4<span>+</span></div>
                <div class="ks-stat-label">Scheduling Policies (FCFS, SJF, Priority, RR)</div>
            </div>
            <div>
                <div class="ks-stat-num">7<span>+</span></div>
                <div class="ks-stat-label">Hardware & OS Subsystems Simulated</div>
            </div>
            <div>
                <div class="ks-stat-num">100<span>%</span></div>
                <div class="ks-stat-label">Native C++ Deterministic Execution</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Visual Feature Grid
    st.markdown(
        """
        <div class="ks-section-header" style="margin-top: 40px;">
            <div class="ks-section-eyebrow">✦ WHAT YOU WILL LEARN</div>
            <div class="ks-section-title">Core Subsystems Visualized</div>
            <p class="ks-section-desc">
                Go beyond theoretical textbooks. Observe how the operating system manages physical memory,
                switches execution contexts, and schedules competing processes.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class="ks-card ks-card-hover" style="margin-bottom:16px;">
                <div class="ks-icon-box icon-cyan">⚙️</div>
                <div class="ks-card-title">Preemptive CPU Scheduling</div>
                <div class="ks-card-body">
                    Inspect how Round Robin slices execution cycles, causes context switches, and balances CPU share across ready processes.
                </div>
            </div>
            <div class="ks-card ks-card-hover">
                <div class="ks-icon-box icon-purple">🔄</div>
                <div class="ks-card-title">Hardware Context Switching</div>
                <div class="ks-card-body">
                    Track the overhead incurred when saving and restoring state across processes with instruction pointer and register persistence.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="ks-card ks-card-hover" style="margin-bottom:16px;">
                <div class="ks-icon-box icon-green">🧠</div>
                <div class="ks-card-title">Extended 5-State Machine</div>
                <div class="ks-card-body">
                    Follow processes through New → Waiting for Memory → Ready → Running → Terminated states with complete transition history.
                </div>
            </div>
            <div class="ks-card ks-card-hover">
                <div class="ks-icon-box icon-rose">📋</div>
                <div class="ks-card-title">Process Control Block (PCB)</div>
                <div class="ks-card-body">
                    Inspect the task_struct metadata: Program Counter (PC), registers R0–R3, arrival, memory bounds, and turnaround metrics.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div class="ks-card ks-card-hover" style="margin-bottom:16px;">
                <div class="ks-icon-box icon-amber">💾</div>
                <div class="ks-card-title">RAM & Admission Control</div>
                <div class="ks-card-body">
                    Observe how the Long-Term Scheduler stalls processes when physical memory is exhausted and re-evaluates queues on termination.
                </div>
            </div>
            <div class="ks-card ks-card-hover">
                <div class="ks-icon-box icon-teal">📊</div>
                <div class="ks-card-title">Multi-Algorithm Benchmarking</div>
                <div class="ks-card-body">
                    Run identical workloads through all 4 algorithms concurrently to measure waiting times, turnaround times, and CPU utilization.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<hr class="ks-divider">', unsafe_allow_html=True)

    # 3-Step Guided Workflow
    st.markdown(
        """
        <div class="ks-section-header">
            <div class="ks-section-eyebrow">✦ GUIDED WORKFLOW</div>
            <div class="ks-section-title">How To Experiment</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    s1, s2, s3 = st.columns(3)
    with s1:
        st.markdown(
            """
            <div class="ks-step">
                <div class="ks-step-num">1</div>
                <div class="ks-step-icon">📝</div>
                <div class="ks-step-title">Configure Process Workload</div>
                <div class="ks-step-desc">
                    Select a curated scenario (e.g., Convoy Effect, Memory Contention) or enter your own custom process descriptors.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with s2:
        st.markdown(
            """
            <div class="ks-step">
                <div class="ks-step-num">2</div>
                <div class="ks-step-icon">⚡</div>
                <div class="ks-step-title">Dispatch C++ Kernel</div>
                <div class="ks-step-desc">
                    Choose an algorithm, set the time quantum and physical RAM capacity, then dispatch the native C++ engine.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with s3:
        st.markdown(
            """
            <div class="ks-step">
                <div class="ks-step-num">3</div>
                <div class="ks-step-icon">🔬</div>
                <div class="ks-step-title">Step-Through & Analyze</div>
                <div class="ks-step-desc">
                    Use the interactive clock scrubber to inspect cycle-by-cycle register states, memory allocation bars, and timeline Gantt graphs.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div style="height:30px;"></div>', unsafe_allow_html=True)
