"""
navbar.py
─────────
Top navigation bar rendered on every page.
"""

import streamlit as st


def render_navbar(active_page: str = "") -> None:
    """
    Render the sticky top nav bar.
    `active_page` is used only for visual reference; navigation is handled
    by the sidebar and st.switch_page().
    """
    st.markdown(
        """
        <div class="ks-topnav">
            <div class="ks-topnav-brand">
                <div class="ks-topnav-logo">K</div>
                <div class="ks-topnav-name">Kernel<span>Sim</span></div>
            </div>
            <div class="ks-topnav-links">
                <span class="ks-topnav-link">Home</span>
                <span class="ks-topnav-link">OS Concepts</span>
                <span class="ks-topnav-link">Simulator</span>
                <span class="ks-topnav-link">Benchmark</span>
            </div>
            <div class="ks-topnav-right">
                <div class="ks-engine-pill">
                    <div class="pulse-dot"></div>
                    C++ ENGINE ONLINE
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
