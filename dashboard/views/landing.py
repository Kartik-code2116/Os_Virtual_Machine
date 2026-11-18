"""Friendly starting point for the KernelSim learning experience."""

import streamlit as st


def _go_to(page: str) -> None:
    st.session_state["pending_navigation"] = page
    st.rerun()


def render_landing_page() -> None:
    left, right = st.columns([1.12, 0.88], gap="large", vertical_alignment="center")
    with left:
        st.markdown(
            """
            <div class="ks-welcome"><span class="ks-welcome-mark"></span> A HANDS-ON INTRODUCTION TO OPERATING SYSTEMS</div>
            <h1 class="ks-home-title">See what happens<br>inside your computer.</h1>
            <p class="ks-home-copy">
                An operating system makes thousands of small decisions every second.
                Explore those decisions in a friendly, interactive lab—no special setup or account needed.
            </p>
            """,
            unsafe_allow_html=True,
        )
        a, b = st.columns([1.25, 1], gap="small")
        with a:
            if st.button("Start with the simulator  →", type="primary", use_container_width=True):
                _go_to("simulator")
        with b:
            if st.button("Explore the basics", type="secondary", use_container_width=True):
                _go_to("concepts")
        st.markdown(
            '<div class="ks-hero-assurance"><span>✓</span> Free to explore <span>·</span> Learn at your own pace <span>·</span> Reset and try again</div>',
            unsafe_allow_html=True,
        )

    with right:
        st.markdown(
            """
            <div class="ks-visual-card">
                <div class="ks-visual-top"><div><span class="ks-live-dot"></span> INSIDE THE KERNEL</div><span class="ks-visual-clock">TICK 08</span></div>
                <div class="ks-visual-title">One CPU. Three processes.</div>
                <div class="ks-visual-subtitle">The scheduler decides who gets the next turn.</div>
                <div class="ks-process-row"><span class="ks-process-id">P1</span><div class="ks-process-track"><i class="ks-track-fill fill-mint" style="width:72%"></i></div><span class="ks-process-state state-running">RUNNING</span></div>
                <div class="ks-process-row"><span class="ks-process-id">P2</span><div class="ks-process-track"><i class="ks-track-fill fill-blue" style="width:48%"></i></div><span class="ks-process-state state-ready">READY</span></div>
                <div class="ks-process-row"><span class="ks-process-id">P3</span><div class="ks-process-track"><i class="ks-track-fill fill-peach" style="width:30%"></i></div><span class="ks-process-state state-waiting">WAITING</span></div>
                <div class="ks-visual-callout"><span>↳</span> Change the scheduling rule and see who runs next.</div>
                <div class="ks-visual-footer"><span>CPU SCHEDULING</span><span>ROUND ROBIN <b>●</b></span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="ks-home-section-head">
            <div><div class="ks-section-eyebrow">A SIMPLE LEARNING PATH</div><div class="ks-section-title">Understand it. Try it. Compare it.</div></div>
            <p>Move from the big idea to the tiny details, one experiment at a time.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3, gap="medium")
    cards = [
        ("01", "Get the intuition", "Learn how processes, memory, and the CPU fit together with short, plain-language explanations.", "📘", "concepts"),
        ("02", "Run your own experiment", "Choose a workload, pick a scheduling rule, and step through what the operating system does.", "⚙️", "simulator"),
        ("03", "See what changed", "Compare algorithms side by side and connect the results to the choices you made.", "↗", "benchmark"),
    ]
    for column, (number, title, copy, icon, destination) in zip((c1, c2, c3), cards):
        with column:
            st.markdown(
                f'<div class="ks-path-card"><div class="ks-path-card-top"><span class="ks-path-number">{number}</span><span class="ks-path-icon">{icon}</span></div><div class="ks-path-title">{title}</div><div class="ks-path-copy">{copy}</div></div>',
                unsafe_allow_html=True,
            )
            if st.button(f"{title}  →", key=f"home_path_{destination}", use_container_width=True):
                _go_to(destination)

    st.markdown(
        """
        <div class="ks-home-bottom">
            <div><span class="ks-bottom-spark">✳</span><div><b>Curious about the details?</b><p>Follow a process from arrival to completion, inspect its saved registers, and watch memory become available again.</p></div></div>
            <span class="ks-bottom-tag">BUILT FOR LEARNING BY DOING</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
