"""Learning-first navigation and a small orientation panel."""

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
                    <div class="ks-sidebar-tag">Learn by seeing it happen</div>
                </div>
            </div>
            <div class="ks-nav-label">YOUR LEARNING PATH</div>
            """,
            unsafe_allow_html=True,
        )

        page_names = {
            "home": "🏡  Start here",
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

        st.markdown(
            """
            <div class="ks-sidebar-note">
                <div class="ks-sidebar-note-icon">✦</div>
                <div class="ks-sidebar-info-title">A good place to begin</div>
                <div class="ks-sidebar-info-body">
                    Start with a short concept, then open the simulator and change one thing at a time.
                    There is no account or setup to complete.
                </div>
            </div>
            <div class="ks-sidebar-engine">
                <span class="ks-sidebar-engine-dot"></span>
                <span><b>Learning lab</b><br>Powered by a native C++ engine</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        return selected
