"""
app.py
──────
Root entrypoint for the KernelSim platform.
Orchestrates:
- Global styling injection
- Persistent session state initialization
- Top Navigation Bar
- Dynamic Sidebar Navigation (hidden on Landing page, visible on other pages)
- View dispatching (Landing, Concepts, Simulator, Benchmark)
- Footer Bar
"""

import sys
from pathlib import Path
import streamlit as st

# Ensure dashboard root is in sys.path so modules import reliably
DASHBOARD_ROOT = Path(__file__).resolve().parent
if str(DASHBOARD_ROOT) not in sys.path:
    sys.path.insert(0, str(DASHBOARD_ROOT))

from components.styles import inject_styles
from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.footer import render_footer

from views.landing import render_landing_page
from views.concepts import render_concepts_page
from views.simulator import render_simulator_page
from views.benchmark import render_benchmark_page

from utils.constants import PRESETS

# 1. Page Configuration
st.set_page_config(
    page_title="KernelSim — Learn how computers work",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Session State Initialization
if "theme" not in st.session_state:
    st.session_state.theme = "premium"
if "processes" not in st.session_state:
    st.session_state.processes = [p.copy() for p in PRESETS["Standard Mix"]]
if "nav_selection" not in st.session_state:
    st.session_state.nav_selection = "home"
if "pending_navigation" in st.session_state:
    destination = st.session_state.pop("pending_navigation")
    st.session_state.nav_selection = destination
    st.session_state.ks_sidebar_nav_radio = destination

# 3. Inject Theme Stylesheet
inject_styles(st.session_state.theme)

# 4. Sticky Top Navigation Bar
render_navbar(st.session_state.nav_selection)

# 5. Sidebar Navigation — only shown on non-landing pages
if st.session_state.nav_selection == "home":
    # Completely hide sidebar on the landing page
    st.markdown(
        """
        <style>
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        div[data-testid="stSidebarCollapsedControl"] {
            display: none !important;
        }
        .main .block-container {
            max-width: 1240px !important;
            padding-left: 2.5rem !important;
            padding-right: 2.5rem !important;
            margin: 0 auto !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    # Sidebar is visible on Concepts, Simulator, and Benchmark pages
    selected_page = render_sidebar(st.session_state.nav_selection)
    if selected_page != st.session_state.nav_selection:
        st.session_state.nav_selection = selected_page
        st.rerun()

# 6. Main View Router
current = st.session_state.nav_selection

if current == "home":
    render_landing_page()
elif current == "concepts":
    render_concepts_page()
elif current == "simulator":
    render_simulator_page()
elif current == "benchmark":
    render_benchmark_page()
else:
    render_landing_page()

# 7. Global Footer
render_footer()
