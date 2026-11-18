"""
sidebar.py
──────────
Unified custom sidebar with page navigation and live system telemetry.
"""

import streamlit as st


def render_sidebar(active_page: str = "home") -> str:
    """
    Renders custom styled sidebar and returns the selected page identifier.
    Options: 'home', 'concepts', 'simulator', 'benchmark'
    """
    with st.sidebar:
        st.markdown(
            """
            <div class="ks-sidebar-brand">
                <div class="ks-sidebar-logo">K</div>
                <div>
                    <div class="ks-sidebar-name">Kernel<span>Sim</span></div>
                    <div class="ks-sidebar-tag">OS Learning Platform</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('<div class="ks-nav-label">Navigation</div>', unsafe_allow_html=True)

        page_names = {
            "home": "🏠 Home / Overview",
            "concepts": "📚 OS Concepts",
            "simulator": "⚙️ Kernel Simulator",
            "benchmark": "📊 Algorithm Benchmark",
        }

        # Page selection mapped to radio keys
        options = list(page_names.keys())
        idx = options.index(active_page) if active_page in options else 0

        selected = st.radio(
            "Navigation",
            options=options,
            format_func=lambda x: page_names[x],
            index=idx,
            label_visibility="collapsed",
            key="ks_sidebar_nav_radio",
        )

        st.markdown('<div class="ks-nav-label" style="margin-top:16px;">System State</div>', unsafe_allow_html=True)

        st.markdown(
            """
            <div style="padding: 0 16px 12px 16px; display:flex; flex-direction:column; gap:6px;">
                <span class="ks-status-pill pill-green">
                    <span class="pulse-dot"></span> KERNEL: ONLINE (x86_64)
                </span>
                <span class="ks-status-pill pill-cyan">
                    ⚡ vm_engine.exe — C++ NATIVE
                </span>
                <span class="ks-status-pill pill-purple">
                    🔒 RING 0 — PRIVILEGED
                </span>
                <span class="ks-status-pill pill-amber">
                    📦 MMU: DYNAMIC ADMISSION
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="ks-sidebar-info">
                <div class="ks-sidebar-info-title">💡 Kernel Note</div>
                <div class="ks-sidebar-info-body">
                    Processes arrive in the <b>New</b> state and move to <b>Waiting for Memory</b>
                    if RAM is full, mirroring long-term admission schedulers in modern operating systems.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        return selected
