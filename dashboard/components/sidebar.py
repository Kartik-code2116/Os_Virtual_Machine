"""
sidebar.py
──────────
Learning-first navigation and orientation panel.
Visible on Concepts, Simulator, and Benchmark pages (hidden on Landing page).
"""

import streamlit as st


def render_sidebar(active_page: str = "home") -> str:
    """Render the learning sidebar and return the selected view."""
    with st.sidebar:
        st.markdown(
            """
            <div class="ks-sidebar-brand">
                <div class="ks-sidebar-logo">K</div>
                <div>
                    <div class="ks-sidebar-name">Kernel<span>Sim</span></div>
                    <div class="ks-sidebar-tag">OS Kernel & VM Platform</div>
                </div>
            </div>
            <div class="ks-nav-label">YOUR LEARNING PATH</div>
            """,
            unsafe_allow_html=True,
        )

        page_names = {
            "home": "🏡  Start here (Landing)",
            "concepts": "📖  Learn the basics",
            "simulator": "⚙️  Try the simulator",
            "benchmark": "↗️  Compare results",
        }
        options = list(page_names)
        idx = options.index(active_page) if active_page in options else 0
        selected = st.radio(
            "Learning path",
            options=options,
            format_func=lambda x: page_names[x],
            index=idx,
            label_visibility="collapsed",
            key="ks_sidebar_nav_radio",
        )

        # Prominent Theme Toggle in the Sidebar
        st.markdown('<div class="ks-nav-label" style="margin-top:16px;">THEME / APPEARANCE</div>', unsafe_allow_html=True)
        current_theme = st.session_state.get("theme", "premium")
        if current_theme == "premium":
            side_btn_label = "🌙 Switch to Dark Mode"
            side_btn_help = "Switch to Deep Dark Cyber Theme"
        else:
            side_btn_label = "🌿 Switch to Premium Theme"
            side_btn_help = "Switch to Soft Sage Premium Theme"

        if st.button(side_btn_label, key="ks_sidebar_theme_toggle_btn", help=side_btn_help, use_container_width=True):
            st.session_state.theme = "dark" if current_theme == "premium" else "premium"
            st.rerun()

        st.markdown(
            """
            <div class="ks-sidebar-note">
                <div class="ks-sidebar-note-icon">✦</div>
                <div class="ks-sidebar-info-title">A good place to begin</div>
                <div class="ks-sidebar-info-body">
                    Start with a short concept, then open the simulator and change one parameter at a time.
                    The native C++ engine executes deterministically.
                </div>
            </div>
            <div class="ks-sidebar-engine">
                <span class="ks-sidebar-engine-dot"></span>
                <span><b>Engine Status</b><br>Powered by native C++17 x64</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        return selected
