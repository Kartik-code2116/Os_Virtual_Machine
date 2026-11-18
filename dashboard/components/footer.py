"""
footer.py
─────────
Shared footer bar rendered on every page.
"""

import streamlit as st


def render_footer() -> None:
    st.markdown(
        """
        <div class="ks-footer">
            <div class="ks-footer-inner">
                <div>
                    <div class="ks-footer-brand">Kernel<span>Sim</span> — OS Learning Platform</div>
                    <div class="ks-footer-text">
                        An interactive educational simulator for Operating System kernel concepts.<br>
                        Powered by a native <strong style="color:#dde4ef">C++ vm_engine</strong> and
                        <strong style="color:#dde4ef">Python Streamlit</strong>.
                    </div>
                </div>
                <div style="text-align:right;">
                    <div style="display:flex; gap:6px; justify-content:flex-end; flex-wrap:wrap; margin-bottom:6px;">
                        <span class="ks-status-pill pill-green">
                            <div class="pulse-dot"></div> ENGINE ONLINE
                        </span>
                        <span class="ks-status-pill pill-cyan">C++17 MSVC x64</span>
                        <span class="ks-status-pill pill-purple">Streamlit 1.67</span>
                    </div>
                    <div class="ks-footer-text">
                        Concepts: PCB · CPU Scheduling · MMU · Context Switching · Process States
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
