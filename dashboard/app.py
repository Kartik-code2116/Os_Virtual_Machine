"""
app.py
──────
Root entrypoint for the KernelSim platform.
Orchestrates:
- Global styling injection
- Persistent session state initialization
- Top Navigation Bar
- Dynamic Sidebar Navigation
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
    page_title="KernelSim — OS & VM Hypervisor Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. Inject CSS Stylesheet
inject_styles()

# 3. Session State Initialization
if "processes" not in st.session_state:
    st.session_state.processes = [p.copy() for p in PRESETS["Standard Mix"]]
if "nav_selection" not in st.session_state:
    st.session_state.nav_selection = "home"

# 4. Sticky Top Navigation Bar
render_navbar(st.session_state.nav_selection)

# 5. Sidebar Navigation
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
