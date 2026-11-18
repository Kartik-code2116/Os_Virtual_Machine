"""
navbar.py
─────────
Top navigation header for KernelSim.
Displays:
- KernelSim Brand Logo & Subtitle
- Active Section Indicator
- C++ Engine Status Pill
- Direct, Reliable Theme Toggle Button
- Quick Navigation Bar on the Landing Page
"""

import streamlit as st


PAGE_LABELS = {
    "home": ("Learning lab", "A practical place to explore how operating systems work."),
    "concepts": ("Explore the concepts", "Build a clear mental model before you run a simulation."),
    "simulator": ("Run a simulation", "Change the workload and watch the kernel respond."),
    "benchmark": ("Compare algorithms", "See how scheduling choices change the results."),
}


def render_navbar(active_page: str = "home") -> None:
    label, description = PAGE_LABELS.get(active_page, PAGE_LABELS["home"])
    current_theme = st.session_state.get("theme", "premium")

    # Top brand bar with direct interactive theme toggle button
    c_brand, c_status, c_toggle = st.columns([2.3, 1.2, 1.1], vertical_alignment="center")

    with c_brand:
        st.markdown(
            f"""
            <div class="ks-topnav-brand">
                <div class="ks-topnav-logo">K</div>
                <div>
                    <div class="ks-topnav-name">Kernel<span>Sim</span></div>
                    <div class="ks-topnav-caption">OS KERNEL & VM HYPERVISOR</div>
                </div>
                <div class="ks-topnav-context">
                    <span class="ks-topnav-kicker">{label}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c_status:
        st.markdown(
            """
            <div style="display:flex; justify-content:center; align-items:center;">
                <div class="ks-engine-pill"><span class="pulse-dot"></span> C++ ENGINE ONLINE</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c_toggle:
        if current_theme == "premium":
            btn_label = "🌙 Dark Mode"
            btn_help = "Switch to Deep Dark Cyber Theme"
        else:
            btn_label = "🌿 Premium Sage"
            btn_help = "Switch to Premium Soft Sage Theme"

        if st.button(btn_label, key="ks_global_theme_toggle_btn", help=btn_help, use_container_width=True):
            st.session_state.theme = "dark" if current_theme == "premium" else "premium"
            st.rerun()

    # On the landing page, display quick jump buttons since the sidebar is hidden
    if active_page == "home":
        st.markdown('<div style="height: 10px;"></div>', unsafe_allow_html=True)
        _, q1, q2, q3, _ = st.columns([1.5, 1.2, 1.2, 1.2, 1.5], gap="small")
        with q1:
            if st.button("📖 OS Concepts", key="top_nav_concepts", use_container_width=True):
                st.session_state.pending_navigation = "concepts"
                st.rerun()
        with q2:
            if st.button("⚙️ Simulator", key="top_nav_simulator", use_container_width=True):
                st.session_state.pending_navigation = "simulator"
                st.rerun()
        with q3:
            if st.button("↗️ Benchmark", key="top_nav_benchmark", use_container_width=True):
                st.session_state.pending_navigation = "benchmark"
                st.rerun()
        st.markdown('<div style="height: 14px;"></div>', unsafe_allow_html=True)
