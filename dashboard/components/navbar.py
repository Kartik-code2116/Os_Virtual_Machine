"""Top navigation bar for the KernelSim learning workspace."""

import streamlit as st


PAGE_LABELS = {
    "home": ("Learning lab", "A practical place to explore how operating systems work."),
    "concepts": ("Explore the concepts", "Build a clear mental model before you run a simulation."),
    "simulator": ("Run a simulation", "Change the workload and watch the kernel respond."),
    "benchmark": ("Compare algorithms", "See how scheduling choices change the results."),
}


def render_navbar(active_page: str = "home") -> None:
    label, description = PAGE_LABELS.get(active_page, PAGE_LABELS["home"])
    st.markdown(
        f"""
        <div class="ks-topnav">
            <div class="ks-topnav-brand">
                <div class="ks-topnav-logo">K</div>
                <div>
                    <div class="ks-topnav-name">Kernel<span>Sim</span></div>
                    <div class="ks-topnav-caption">OPEN LEARNING LAB</div>
                </div>
            </div>
            <div class="ks-topnav-context">
                <span class="ks-topnav-kicker">{label}</span>
                <span class="ks-topnav-description">{description}</span>
            </div>
            <div class="ks-topnav-right">
                <div class="ks-engine-pill"><span class="pulse-dot"></span> SIMULATOR READY</div>
                <div class="ks-open-pill">FREE · NO ACCOUNT</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if active_page == "home":
        # Quick navigation bar for the landing page since sidebar is hidden here
        st.markdown('<div style="height: 10px;"></div>', unsafe_allow_html=True)
        _, c1, c2, c3, _ = st.columns([1.5, 1, 1, 1, 1.5], gap="small")
        with c1:
            if st.button("📖 OS Concepts", key="top_nav_concepts", use_container_width=True):
                st.session_state.pending_navigation = "concepts"
                st.rerun()
        with c2:
            if st.button("⚙️ Simulator", key="top_nav_simulator", use_container_width=True):
                st.session_state.pending_navigation = "simulator"
                st.rerun()
        with c3:
            if st.button("↗️ Benchmark", key="top_nav_benchmark", use_container_width=True):
                st.session_state.pending_navigation = "benchmark"
                st.rerun()
        st.markdown('<div style="height: 10px;"></div>', unsafe_allow_html=True)
