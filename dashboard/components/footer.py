"""Quiet, consistent footer across the learning workspace."""

import streamlit as st


def render_footer() -> None:
    st.markdown(
        """
        <div class="ks-footer">
            <div class="ks-footer-inner">
                <div class="ks-footer-brand"><span class="ks-footer-mark">K</span><span>Kernel<strong>Sim</strong></span></div>
                <div class="ks-footer-note">A little closer to understanding how computers think.</div>
                <div class="ks-footer-meta"><span>OPEN LEARNING LAB</span><span class="ks-footer-separator">·</span><span>POWERED BY C++</span></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
