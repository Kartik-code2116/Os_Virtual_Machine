"""Top navigation bar for the KernelSim learning workspace with theme toggle."""

import streamlit as st


PAGE_LABELS = {
    "home": ("Learning lab", "A practical place to explore how operating systems work."),
    "concepts": ("Explore the concepts", "Build a clear mental model before you run a simulation."),
    "simulator": ("Run a simulation", "Change the workload and watch the kernel respond."),
    "benchmark": ("Compare algorithms", "See how scheduling choices change the results."),
}


def render_navbar(active_page: str = "home") -> None:
    label, description = PAGE_LABELS.get(active_page, PAGE_LABELS["home"])
    current_theme = st.session_state.get("theme", "dark")
    is_dark = (current_theme == "dark")

    # Top brand bar with interactive theme toggle
    c_brand, c_status, c_toggle = st.columns([2.2, 1.4, 0.9], vertical_alignment="center")

    with c_brand:
        st.markdown(
            f"""
            <div class="ks-topnav-brand">
                <div class="ks-topnav-logo">K</div>
                <div>
                    <div class="ks-topnav-name">Kernel<span>Sim</span></div>
                    <div class="ks-topnav-caption">OPEN LEARNING LAB</div>
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
        toggle_label = "☀️ Light" if is_dark else "🌙 Dark"
        toggle_help = "Switch to Light Theme" if is_dark else "Switch to Dark Theme"
        if st.button(toggle_label, key="ks_global_theme_toggle", help=toggle_help, use_container_width=True):
            st.session_state.theme = "light" if is_dark else "dark"
            st.rerun()

    # On the landing page, display quick jump buttons since the sidebar is hidden
    if active_page == "home":
        st.markdown('<div style="height: 6px;"></div>', unsafe_allow_html=True)
        _, q1, q2, q3, _ = st.columns([1.5, 1, 1, 1, 1.5], gap="small")
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
        st.markdown('<div style="height: 12px;"></div>', unsafe_allow_html=True)
