"""
OS Kernel & VM Hypervisor Simulator  —  Professional Edition
=============================================================
A premium educational platform for learning Operating System concepts
through live C++ simulation and interactive visualizations.
"""

import html
from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from cpp_backend import run_cpp_simulation

# ─────────────────────────────────────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="KernelSim — OS Learning Platform",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────────────────
# GLOBAL CSS  —  Premium, human-made, educational SaaS feel
# ─────────────────────────────────────────────────────────────────────────────
GLOBAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

/* ── Streamlit chrome reset ── */
#MainMenu, footer, header            { visibility: hidden !important; }
div[data-testid="stToolbar"]         { display: none !important; }
div[data-testid="stDecoration"]      { display: none !important; }
div[data-testid="stStatusWidget"]    { display: none !important; }
.stAppDeployButton                   { display: none !important; }
div[data-testid="stSidebarCollapseButton"] { display: none !important; }

/* ── CSS Variables ── */
:root {
    --void:        #04080f;
    --surface:     #0b1120;
    --card:        #0f1829;
    --card-alt:    #131e30;
    --border:      #1d2d44;
    --border-glow: rgba(99, 179, 237, 0.25);
    --cyan:        #63b3ed;
    --cyan-bright: #90cdf4;
    --green:       #48bb78;
    --amber:       #ed8936;
    --rose:        #fc8181;
    --purple:      #9f7aea;
    --text:        #e2e8f0;
    --muted:       #718096;
    --mono:        'JetBrains Mono', monospace;
    --sans:        'Inter', -apple-system, sans-serif;
}

/* ── Global base ── */
html, body, [class*="css"], .stApp {
    font-family: var(--sans);
    color: var(--text);
    background-color: var(--void) !important;
}

.stApp {
    background-image:
        radial-gradient(ellipse at 20% 10%, rgba(99,179,237,0.05) 0%, transparent 55%),
        radial-gradient(ellipse at 80% 85%, rgba(72,187,120,0.03) 0%, transparent 55%);
}

/* ── Top Navigation Bar ── */
.top-nav {
    position: sticky;
    top: 0;
    z-index: 999;
    background: rgba(11, 17, 32, 0.96);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--border);
    padding: 0 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 60px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.5);
}

.nav-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    text-decoration: none;
}

.nav-logo {
    width: 32px;
    height: 32px;
    background: linear-gradient(135deg, #63b3ed 0%, #48bb78 100%);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 16px;
    font-weight: 800;
    color: #04080f;
    font-family: var(--mono);
    flex-shrink: 0;
}

.nav-brand-name {
    font-size: 1.1rem;
    font-weight: 700;
    color: #fff;
    letter-spacing: -0.3px;
}

.nav-brand-name span {
    color: var(--cyan);
}

.nav-links {
    display: flex;
    align-items: center;
    gap: 6px;
}

.nav-link {
    font-size: 0.85rem;
    font-weight: 500;
    padding: 6px 14px;
    border-radius: 6px;
    color: var(--muted);
    cursor: pointer;
    transition: all 0.15s ease;
    white-space: nowrap;
}

.nav-link:hover, .nav-link.active {
    color: var(--text);
    background: rgba(99,179,237,0.1);
}

.nav-link.active {
    color: var(--cyan);
    border: 1px solid rgba(99,179,237,0.25);
}

.nav-cta {
    background: linear-gradient(135deg, #2b6cb0, #2c7a7b);
    color: #fff !important;
    border-radius: 8px;
    font-weight: 600;
    padding: 7px 16px;
    border: none;
    cursor: pointer;
    font-size: 0.84rem;
    display: flex;
    align-items: center;
    gap: 6px;
    transition: all 0.2s ease;
    box-shadow: 0 2px 10px rgba(43,108,176,0.35);
}

.nav-cta:hover {
    box-shadow: 0 4px 20px rgba(43,108,176,0.55);
    transform: translateY(-1px);
}

.nav-status {
    display: flex;
    align-items: center;
    gap: 6px;
    font-family: var(--mono);
    font-size: 0.72rem;
    color: var(--green);
    background: rgba(72,187,120,0.08);
    border: 1px solid rgba(72,187,120,0.2);
    padding: 4px 10px;
    border-radius: 20px;
}

.status-dot {
    width: 7px;
    height: 7px;
    background: var(--green);
    border-radius: 50%;
    animation: pulse 2s infinite;
    box-shadow: 0 0 6px var(--green);
}

@keyframes pulse {
    0%, 100% { opacity: 1; transform: scale(1); }
    50%       { opacity: 0.5; transform: scale(0.8); }
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
}

[data-testid="stSidebar"] .stMarkdown { padding: 0 !important; }

.sidebar-section {
    padding: 20px 20px 10px 20px;
}

.sidebar-logo-block {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 20px 20px 16px 20px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 8px;
}

.sidebar-logo {
    width: 36px;
    height: 36px;
    background: linear-gradient(135deg, #63b3ed 0%, #48bb78 100%);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 800;
    color: #04080f;
    font-family: var(--mono);
    flex-shrink: 0;
}

.sidebar-brand { font-size: 1rem; font-weight: 700; color: #fff; }
.sidebar-brand span { color: var(--cyan); }
.sidebar-tagline { font-size: 0.72rem; color: var(--muted); margin-top: 2px; }

.sidebar-nav-label {
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--muted);
    padding: 0 20px;
    margin: 16px 0 6px 0;
}

.sidebar-nav-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 9px 20px;
    cursor: pointer;
    border-radius: 0;
    transition: all 0.15s ease;
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--muted);
    border-left: 2px solid transparent;
}

.sidebar-nav-item:hover {
    background: rgba(99,179,237,0.07);
    color: var(--text);
}

.sidebar-nav-item.active {
    background: rgba(99,179,237,0.1);
    color: var(--cyan);
    border-left-color: var(--cyan);
}

.sidebar-nav-icon { font-size: 1rem; width: 20px; text-align: center; }

.sidebar-info-card {
    margin: 16px;
    background: rgba(99,179,237,0.06);
    border: 1px solid rgba(99,179,237,0.15);
    border-radius: 10px;
    padding: 14px 16px;
}

.sidebar-info-title {
    font-size: 0.75rem;
    font-weight: 700;
    color: var(--cyan);
    margin-bottom: 6px;
}

.sidebar-info-text {
    font-size: 0.72rem;
    color: var(--muted);
    line-height: 1.6;
}

.sidebar-os-badge {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    font-family: var(--mono);
    font-size: 0.65rem;
    padding: 3px 8px;
    border-radius: 4px;
    margin: 2px 0;
    white-space: nowrap;
}

.badge-green  { background: rgba(72,187,120,0.1);  color: var(--green);  border: 1px solid rgba(72,187,120,0.2);  }
.badge-cyan   { background: rgba(99,179,237,0.1);  color: var(--cyan);   border: 1px solid rgba(99,179,237,0.2);  }
.badge-amber  { background: rgba(237,137,54,0.1);  color: var(--amber);  border: 1px solid rgba(237,137,54,0.2);  }
.badge-purple { background: rgba(159,122,234,0.1); color: var(--purple); border: 1px solid rgba(159,122,234,0.2); }
.badge-rose   { background: rgba(252,129,129,0.1); color: var(--rose);   border: 1px solid rgba(252,129,129,0.2); }

/* ── Landing Page ── */
.hero-section {
    text-align: center;
    padding: 70px 20px 50px;
    max-width: 900px;
    margin: 0 auto;
}

.hero-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    font-family: var(--mono);
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--cyan);
    background: rgba(99,179,237,0.08);
    border: 1px solid rgba(99,179,237,0.2);
    padding: 6px 16px;
    border-radius: 20px;
    margin-bottom: 28px;
}

.hero-title {
    font-size: clamp(2.2rem, 5vw, 3.6rem);
    font-weight: 800;
    color: #fff;
    line-height: 1.1;
    letter-spacing: -1.5px;
    margin-bottom: 20px;
}

.hero-title .accent { color: var(--cyan); }
.hero-title .accent2 { color: var(--green); }

.hero-subtitle {
    font-size: 1.1rem;
    color: var(--muted);
    line-height: 1.7;
    max-width: 640px;
    margin: 0 auto 36px;
}

.hero-buttons {
    display: flex;
    gap: 14px;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 50px;
}

.hero-btn-primary {
    background: linear-gradient(135deg, #2b6cb0, #2c7a7b);
    color: #fff;
    border: none;
    padding: 13px 28px;
    border-radius: 10px;
    font-size: 0.95rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 4px 20px rgba(43,108,176,0.4);
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 8px;
}

.hero-btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(43,108,176,0.55);
}

.hero-btn-secondary {
    background: transparent;
    color: var(--text);
    border: 1px solid var(--border);
    padding: 13px 28px;
    border-radius: 10px;
    font-size: 0.95rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.2s ease;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 8px;
}

.hero-btn-secondary:hover {
    border-color: var(--cyan);
    color: var(--cyan);
}

/* ── Feature Cards Grid ── */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
    margin: 0 0 40px;
}

.feature-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 24px;
    transition: all 0.2s ease;
    position: relative;
    overflow: hidden;
}

.feature-card::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: 14px;
    background: linear-gradient(135deg, transparent, transparent);
    opacity: 0;
    transition: opacity 0.2s ease;
}

.feature-card:hover {
    border-color: rgba(99,179,237,0.3);
    transform: translateY(-3px);
    box-shadow: 0 12px 40px rgba(0,0,0,0.4);
}

.feature-icon {
    width: 48px;
    height: 48px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    margin-bottom: 16px;
}

.icon-cyan   { background: rgba(99,179,237,0.12); }
.icon-green  { background: rgba(72,187,120,0.12); }
.icon-amber  { background: rgba(237,137,54,0.12); }
.icon-purple { background: rgba(159,122,234,0.12); }
.icon-rose   { background: rgba(252,129,129,0.12); }
.icon-teal   { background: rgba(56,178,172,0.12); }

.feature-title {
    font-size: 1rem;
    font-weight: 700;
    color: #fff;
    margin-bottom: 8px;
}

.feature-desc {
    font-size: 0.84rem;
    color: var(--muted);
    line-height: 1.65;
}

/* ── Concepts Section ── */
.section-header {
    text-align: center;
    margin-bottom: 36px;
}

.section-label {
    font-family: var(--mono);
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--green);
    margin-bottom: 10px;
}

.section-title {
    font-size: clamp(1.6rem, 3vw, 2.4rem);
    font-weight: 800;
    color: #fff;
    letter-spacing: -1px;
    margin-bottom: 10px;
}

.section-desc {
    font-size: 0.95rem;
    color: var(--muted);
    max-width: 540px;
    margin: 0 auto;
    line-height: 1.65;
}

.concept-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 20px 22px;
    margin-bottom: 14px;
}

.concept-header {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    margin-bottom: 10px;
}

.concept-number {
    width: 32px;
    height: 32px;
    border-radius: 8px;
    background: rgba(99,179,237,0.12);
    border: 1px solid rgba(99,179,237,0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--mono);
    font-size: 0.75rem;
    font-weight: 700;
    color: var(--cyan);
    flex-shrink: 0;
}

.concept-title { font-size: 0.95rem; font-weight: 700; color: #fff; }
.concept-subtitle { font-size: 0.75rem; color: var(--cyan); margin-top: 2px; font-family: var(--mono); }
.concept-body { font-size: 0.82rem; color: var(--muted); line-height: 1.65; }

/* ── Algorithm Cards ── */
.algo-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
    height: 100%;
}

.algo-title {
    font-size: 0.95rem;
    font-weight: 700;
    color: #fff;
    margin-bottom: 6px;
}

.algo-badge {
    display: inline-block;
    font-family: var(--mono);
    font-size: 0.65rem;
    font-weight: 600;
    padding: 2px 8px;
    border-radius: 4px;
    margin-bottom: 10px;
}

.algo-desc { font-size: 0.8rem; color: var(--muted); line-height: 1.6; }

.algo-metric {
    margin-top: 12px;
    font-family: var(--mono);
    font-size: 0.72rem;
}

.metric-row {
    display: flex;
    justify-content: space-between;
    padding: 3px 0;
    color: var(--muted);
}

.metric-row span:last-child { color: var(--text); }

/* ── Simulator Panel ── */
.sim-header {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 24px 28px;
    margin-bottom: 24px;
}

.sim-header-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 8px;
}

.sim-title { font-size: 1.3rem; font-weight: 700; color: #fff; }
.sim-desc  { font-size: 0.84rem; color: var(--muted); margin-top: 4px; }

.sim-badges {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

/* ── KPI Grid ── */
.kpi-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 14px;
    margin-bottom: 28px;
}

.kpi-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px 18px;
    position: relative;
    overflow: hidden;
}

.kpi-card::after {
    content: '';
    position: absolute;
    left: 0; top: 0;
    width: 3px; height: 100%;
    border-radius: 12px 0 0 12px;
    background: var(--cyan);
}

.kpi-card.green::after  { background: var(--green);  }
.kpi-card.amber::after  { background: var(--amber);  }
.kpi-card.rose::after   { background: var(--rose);   }
.kpi-card.purple::after { background: var(--purple); }

.kpi-label {
    font-family: var(--mono);
    font-size: 0.65rem;
    font-weight: 600;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 6px;
}

.kpi-value {
    font-family: var(--mono);
    font-size: 1.5rem;
    font-weight: 700;
    color: #fff;
    line-height: 1.1;
}

.kpi-sub {
    font-size: 0.72rem;
    color: var(--muted);
    margin-top: 4px;
}

/* ── CPU HUD ── */
.cpu-hud {
    background: #07101e;
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px 18px;
    margin-bottom: 16px;
}

.hud-title {
    font-family: var(--mono);
    font-size: 0.7rem;
    font-weight: 700;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    border-bottom: 1px solid var(--border);
    padding-bottom: 8px;
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
}

.reg-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
    gap: 8px;
}

.reg-box {
    background: rgba(0,0,0,0.3);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 8px 12px;
}

.reg-name {
    font-family: var(--mono);
    font-size: 0.63rem;
    color: var(--cyan);
    font-weight: 700;
    margin-bottom: 2px;
    letter-spacing: 0.5px;
}

.reg-val {
    font-family: var(--mono);
    font-size: 1rem;
    font-weight: 700;
    color: #fff;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    background: var(--card);
    padding: 6px;
    border-radius: 10px;
    border: 1px solid var(--border);
}

.stTabs [data-baseweb="tab"] {
    font-family: var(--sans);
    font-size: 0.8rem;
    font-weight: 600;
    padding: 8px 16px;
    border-radius: 7px;
    color: var(--muted);
    background: transparent;
    border: none;
    transition: all 0.15s ease;
}

.stTabs [aria-selected="true"] {
    background: rgba(99,179,237,0.12) !important;
    color: var(--cyan) !important;
    border: 1px solid rgba(99,179,237,0.2) !important;
}

/* ── Terminal ── */
.terminal {
    background: #03060e;
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px 16px;
    font-family: var(--mono);
    font-size: 0.77rem;
    color: #a0aec0;
    line-height: 1.65;
    max-height: 380px;
    overflow-y: auto;
}

.log-line { display: flex; gap: 10px; padding: 2px 0; border-bottom: 1px solid rgba(255,255,255,0.03); }
.log-t    { color: var(--cyan); font-weight: 600; min-width: 70px; flex-shrink: 0; }
.log-s    { color: var(--green); font-weight: 600; min-width: 90px; flex-shrink: 0; }
.log-m    { color: #cbd5e0; }

/* ── Memory Bar ── */
.mem-bar-wrap {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px;
    margin-bottom: 16px;
}

.mem-bar-label {
    font-family: var(--mono);
    font-size: 0.7rem;
    color: var(--muted);
    margin-bottom: 8px;
    display: flex;
    justify-content: space-between;
}

.mem-bar {
    display: flex;
    height: 44px;
    border-radius: 6px;
    overflow: hidden;
    border: 1px solid var(--border);
}

.mem-seg {
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--mono);
    font-size: 0.68rem;
    font-weight: 700;
    color: #000;
    overflow: hidden;
    white-space: nowrap;
    padding: 0 4px;
    text-overflow: ellipsis;
    border-right: 1px solid rgba(0,0,0,0.3);
}

/* ── Section divider ── */
.divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 32px 0;
}

/* ── Buttons ── */
button[kind="primary"] {
    background: linear-gradient(135deg, #2b6cb0, #2c7a7b) !important;
    border: none !important;
    font-family: var(--sans) !important;
    font-weight: 600 !important;
    border-radius: 8px !important;
    box-shadow: 0 2px 12px rgba(43,108,176,0.3) !important;
    transition: all 0.2s ease !important;
}

button[kind="primary"]:hover {
    box-shadow: 0 4px 20px rgba(43,108,176,0.5) !important;
    transform: translateY(-1px) !important;
}

button[kind="secondary"] {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    font-family: var(--sans) !important;
    border-radius: 8px !important;
}

button[kind="secondary"]:hover {
    border-color: var(--cyan) !important;
    color: var(--cyan) !important;
}

/* ── Selectboxes / Inputs ── */
div[data-baseweb="select"] > div {
    background-color: var(--card) !important;
    border-color: var(--border) !important;
    border-radius: 8px !important;
}

div[data-baseweb="input"] > div {
    background-color: var(--card) !important;
    border-color: var(--border) !important;
    border-radius: 8px !important;
}

div[data-testid="stDataEditor"] {
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
}

/* ── Info boxes ── */
.info-box {
    background: rgba(99,179,237,0.06);
    border: 1px solid rgba(99,179,237,0.18);
    border-left: 3px solid var(--cyan);
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 0.84rem;
    color: var(--muted);
    line-height: 1.6;
    margin-bottom: 16px;
}

.info-box strong { color: var(--text); }

/* ── Stats row ── */
.stats-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
    padding: 32px 0;
    text-align: center;
    border-top: 1px solid var(--border);
    border-bottom: 1px solid var(--border);
    margin: 32px 0;
}

.stat-num {
    font-size: 2.4rem;
    font-weight: 800;
    color: #fff;
    letter-spacing: -1px;
    line-height: 1;
}

.stat-num span { color: var(--cyan); }
.stat-label { font-size: 0.82rem; color: var(--muted); margin-top: 6px; }

/* ── Footer ── */
.footer-bar {
    background: var(--surface);
    border-top: 1px solid var(--border);
    padding: 24px 32px;
    margin-top: 60px;
}

.footer-inner {
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
    max-width: 1200px;
    margin: 0 auto;
}

.footer-brand { font-weight: 700; color: #fff; font-size: 0.95rem; }
.footer-brand span { color: var(--cyan); }
.footer-text { font-size: 0.78rem; color: var(--muted); line-height: 1.6; }
.footer-links { display: flex; gap: 20px; }
.footer-link { font-size: 0.8rem; color: var(--muted); text-decoration: none; }
.footer-link:hover { color: var(--cyan); }

/* ── Stepthrough panel ── */
.step-panel {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px 18px;
}

.step-panel-title {
    font-family: var(--mono);
    font-size: 0.7rem;
    font-weight: 700;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 1px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid var(--border);
    padding-bottom: 8px;
    margin-bottom: 12px;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--surface); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #2d3748; }

/* ── Preset buttons ── */
.preset-btn-row { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 14px; }

/* ── How it works step ── */
.how-step {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px;
    text-align: center;
}

.step-num {
    width: 44px;
    height: 44px;
    background: linear-gradient(135deg, #2b6cb0, #2c7a7b);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.1rem;
    font-weight: 800;
    color: #fff;
    margin: 0 auto 14px;
    box-shadow: 0 4px 14px rgba(43,108,176,0.4);
}

.step-title { font-size: 0.95rem; font-weight: 700; color: #fff; margin-bottom: 8px; }
.step-desc  { font-size: 0.8rem; color: var(--muted); line-height: 1.6; }

/* Radio buttons in sidebar */
div[data-testid="stRadio"] > label { 
    display: none;
}
div[data-testid="stRadio"] div[role="radiogroup"] {
    gap: 0 !important;
}
div[data-testid="stRadio"] label[data-baseweb="radio"] {
    display: flex !important;
    align-items: center;
    gap: 10px;
    padding: 9px 20px;
    cursor: pointer;
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--muted);
    border-left: 2px solid transparent;
    transition: all 0.15s ease;
}
div[data-testid="stRadio"] label[data-baseweb="radio"]:hover {
    background: rgba(99,179,237,0.07);
    color: var(--text);
}
div[data-testid="stRadio"] [data-checked="true"] {
    color: var(--cyan);
    border-left: 2px solid var(--cyan);
    background: rgba(99,179,237,0.1);
}
div[data-testid="stRadio"] span:first-child { display: none; }
</style>
"""
st.markdown(GLOBAL_CSS, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# DATA & PRESETS
# ─────────────────────────────────────────────────────────────────────────────
PRESETS = {
    "Standard Mix": [
        {"PID": 1, "Arrival": 0, "Burst": 5, "Priority": 2, "Memory": 100},
        {"PID": 2, "Arrival": 1, "Burst": 3, "Priority": 1, "Memory": 150},
        {"PID": 3, "Arrival": 2, "Burst": 4, "Priority": 3, "Memory": 200},
        {"PID": 4, "Arrival": 4, "Burst": 2, "Priority": 2, "Memory": 100},
    ],
    "Convoy Effect": [
        {"PID": 1, "Arrival": 0, "Burst": 12, "Priority": 2, "Memory": 80},
        {"PID": 2, "Arrival": 1, "Burst": 2,  "Priority": 1, "Memory": 50},
        {"PID": 3, "Arrival": 2, "Burst": 1,  "Priority": 1, "Memory": 60},
        {"PID": 4, "Arrival": 3, "Burst": 2,  "Priority": 3, "Memory": 40},
    ],
    "Memory Stress": [
        {"PID": 1, "Arrival": 0, "Burst": 6, "Priority": 2, "Memory": 180},
        {"PID": 2, "Arrival": 1, "Burst": 4, "Priority": 1, "Memory": 140},
        {"PID": 3, "Arrival": 2, "Burst": 5, "Priority": 3, "Memory": 100},
        {"PID": 4, "Arrival": 3, "Burst": 3, "Priority": 2, "Memory": 90},
    ],
    "Priority Chaos": [
        {"PID": 1, "Arrival": 0, "Burst": 4, "Priority": 4, "Memory": 70},
        {"PID": 2, "Arrival": 1, "Burst": 5, "Priority": 1, "Memory": 90},
        {"PID": 3, "Arrival": 2, "Burst": 3, "Priority": 2, "Memory": 80},
        {"PID": 4, "Arrival": 3, "Burst": 2, "Priority": 3, "Memory": 60},
    ],
    "RR Thrash": [
        {"PID": 1, "Arrival": 0, "Burst": 8, "Priority": 2, "Memory": 60},
        {"PID": 2, "Arrival": 0, "Burst": 7, "Priority": 2, "Memory": 80},
        {"PID": 3, "Arrival": 1, "Burst": 6, "Priority": 1, "Memory": 70},
        {"PID": 4, "Arrival": 2, "Burst": 5, "Priority": 3, "Memory": 90},
    ],
}

PID_COLORS = {
    1: "#63b3ed", 2: "#48bb78", 3: "#ed8936",
    4: "#9f7aea", 5: "#fc8181", 6: "#38b2ac",
    7: "#f6e05e", 8: "#b794f4",
}

RESULT_KEYS = [
    "results", "timeline", "memory_events", "state_events",
    "cpu_events", "summary", "summary_text", "output_dir",
    "algorithm", "total_memory", "quantum", "benchmark_results",
]

# Session state defaults
if "processes" not in st.session_state:
    st.session_state.processes = [p.copy() for p in PRESETS["Standard Mix"]]
if "page" not in st.session_state:
    st.session_state.page = "🏠 Home"


# ─────────────────────────────────────────────────────────────────────────────
# TOP NAVIGATION BAR
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="top-nav">
    <div class="nav-brand">
        <div class="nav-logo">K</div>
        <div>
            <div class="nav-brand-name">Kernel<span>Sim</span></div>
        </div>
    </div>
    <div class="nav-links">
        <span class="nav-link">Documentation</span>
        <span class="nav-link">OS Concepts</span>
        <span class="nav-link">Algorithms</span>
        <span class="nav-link">About</span>
    </div>
    <div style="display:flex; align-items:center; gap:12px;">
        <div class="nav-status">
            <div class="status-dot"></div>
            ENGINE ONLINE
        </div>
        <button class="nav-cta">▶ Launch Simulator</button>
    </div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR — Navigation & Info Panel
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-logo-block">
        <div class="sidebar-logo">K</div>
        <div>
            <div class="sidebar-brand">Kernel<span>Sim</span></div>
            <div class="sidebar-tagline">OS Learning Platform v2.0</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-nav-label">Navigation</div>', unsafe_allow_html=True)

    page = st.radio(
        "nav",
        ["🏠 Home", "📚 OS Concepts", "⚙️ Simulator", "📊 Benchmark"],
        index=["🏠 Home", "📚 OS Concepts", "⚙️ Simulator", "📊 Benchmark"].index(
            st.session_state.page
        ),
        label_visibility="collapsed",
    )
    st.session_state.page = page

    st.markdown('<div class="sidebar-nav-label" style="margin-top:20px;">Engine Status</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="padding: 0 16px; margin-bottom: 10px;">
        <div style="display:flex; flex-direction:column; gap:5px;">
            <span class="sidebar-os-badge badge-green">● KERNEL: ONLINE (x86_64)</span>
            <span class="sidebar-os-badge badge-cyan">⚡ vm_engine.exe — C++ NATIVE</span>
            <span class="sidebar-os-badge badge-amber">🔒 RING 0 — KERNEL MODE</span>
            <span class="sidebar-os-badge badge-purple">📦 MSVC C++17 — Compiled</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sidebar-nav-label" style="margin-top:16px;">Algorithms</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="padding: 0 16px; margin-bottom: 10px;">
        <div style="display:flex; flex-direction:column; gap:5px;">
            <span class="sidebar-os-badge badge-cyan">FCFS — Non-Preemptive</span>
            <span class="sidebar-os-badge badge-green">SJF — Shortest Job First</span>
            <span class="sidebar-os-badge badge-purple">Priority — Non-Preemptive</span>
            <span class="sidebar-os-badge badge-amber">Round Robin — Preemptive</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sidebar-info-card">
        <div class="sidebar-info-title">💡 Did You Know?</div>
        <div class="sidebar-info-text">
            Modern OS kernels like Linux run with scheduling algorithms similar to what you're simulating here — using
            <strong style="color:#e2e8f0;">Completely Fair Scheduler (CFS)</strong>, which is a variation of Priority scheduling.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="padding: 16px; border-top: 1px solid #1d2d44; margin-top: 10px;">
        <div style="font-size:0.72rem; color:#4a5568; text-align:center; line-height:1.6;">
            Built for OS Education<br>
            C++ Engine · Streamlit UI<br>
            © 2024 KernelSim Project
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────────────────────────────────────
def validate_processes(dataframe, total_memory, quantum):
    required = ["PID", "Arrival", "Burst", "Priority", "Memory"]
    if dataframe.empty:
        raise ValueError("Process table is empty. Add at least one process.")
    df = dataframe[required].copy()
    if df.isnull().any().any():
        raise ValueError("All PCB fields must be filled in.")
    for col in required:
        vals = pd.to_numeric(df[col], errors="raise")
        df[col] = vals.astype(int)
    if (df["PID"] <= 0).any():
        raise ValueError("Process IDs must be > 0.")
    if df["PID"].duplicated().any():
        raise ValueError("Duplicate PID found.")
    if (df["Arrival"] < 0).any():
        raise ValueError("Arrival time cannot be negative.")
    if (df[["Burst", "Priority", "Memory"]] <= 0).any().any():
        raise ValueError("Burst, Priority, and Memory must be > 0.")
    if (df["Memory"] > int(total_memory)).any():
        raise ValueError(f"A process requires more RAM than the system total ({total_memory} MB).")
    if int(quantum) <= 0:
        raise ValueError("Time quantum must be ≥ 1.")
    return df.sort_values(["Arrival", "PID"]).reset_index(drop=True)


def read_metric(summary_dict, key, default=0.0):
    val = summary_dict.get(key)
    if val is None:
        return default
    try:
        return float(str(val).replace("%", "").strip())
    except (ValueError, AttributeError):
        return default


def plotly_dark_layout(height=300, **kw):
    base = dict(
        paper_bgcolor="#07101e",
        plot_bgcolor="#04080f",
        height=height,
        margin=dict(l=20, r=20, t=35, b=35),
        font=dict(family="JetBrains Mono", color="#718096"),
        xaxis=dict(showgrid=True, gridcolor="#1d2d44", tickfont=dict(family="JetBrains Mono", color="#718096")),
        yaxis=dict(showgrid=True, gridcolor="#1d2d44", tickfont=dict(family="JetBrains Mono", color="#718096")),
    )
    base.update(kw)
    return base


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: HOME — LANDING PAGE
# ─────────────────────────────────────────────────────────────────────────────
if page == "🏠 Home":

    # Hero
    st.markdown("""
    <div class="hero-section">
        <div class="hero-eyebrow">
            <span>⚡</span> Powered by Native C++ Engine
        </div>
        <h1 class="hero-title">
            Learn Operating Systems<br>
            <span class="accent">by Simulating</span> the <span class="accent2">Kernel</span>
        </h1>
        <p class="hero-subtitle">
            KernelSim is an interactive educational platform that brings OS concepts to life —
            visualize CPU scheduling, memory management, process states, and context switching
            through a real-time C++ simulation engine.
        </p>
        <div class="hero-buttons">
            <a class="hero-btn-primary" href="?">
                ▶ &nbsp;Launch Simulator
            </a>
            <a class="hero-btn-secondary" href="?">
                📚 &nbsp;Explore OS Concepts
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Stats row
    st.markdown("""
    <div class="stats-row">
        <div>
            <div class="stat-num">4<span>+</span></div>
            <div class="stat-label">Scheduling Algorithms</div>
        </div>
        <div>
            <div class="stat-num">7<span>+</span></div>
            <div class="stat-label">OS Concepts Simulated</div>
        </div>
        <div>
            <div class="stat-num">∞</div>
            <div class="stat-label">Process Configurations</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # What you will learn
    st.markdown("""
    <div class="section-header" style="margin-top:40px;">
        <div class="section-label">✦ What You'll Learn</div>
        <div class="section-title">Core OS Concepts, Visualized</div>
        <p class="section-desc">
            Every simulation runs a real C++ kernel engine and shows you exactly what
            happens inside the OS — tick by tick.
        </p>
    </div>
    """, unsafe_allow_html=True)

    fc1, fc2, fc3 = st.columns(3)
    cards = [
        ("⚙️", "icon-cyan",   "CPU Scheduling",        "Watch FCFS, SJF, Priority, and Round Robin algorithms dispatch processes on the simulated CPU core in real time."),
        ("🧠", "icon-green",  "Process State Machine",  "Follow a process through 5 lifecycle states: New → Waiting for Memory → Ready → Running → Terminated."),
        ("💾", "icon-amber",  "Memory Management",      "See how the OS Long-Term Scheduler controls RAM admission and prevents memory over-subscription."),
        ("🔄", "icon-purple", "Context Switching",       "Count every CPU context switch and understand the overhead it adds — visualized on the Gantt chart."),
        ("📋", "icon-rose",   "Process Control Blocks",  "Inspect the full PCB of each process — PID, registers, PC, timing, state, and scheduling metadata."),
        ("📡", "icon-teal",   "Telemetry & Metrics",     "Measure Turnaround Time, Waiting Time, CPU Utilization %, and Memory Wait per scheduling run."),
    ]

    for col, (icon, ic_cls, title, desc) in zip([fc1, fc2, fc3, fc1, fc2, fc3], cards):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <div class="feature-icon {ic_cls}">{icon}</div>
                <div class="feature-title">{title}</div>
                <div class="feature-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # How it works
    st.markdown("""
    <div class="section-header">
        <div class="section-label">✦ How It Works</div>
        <div class="section-title">Three Simple Steps</div>
    </div>
    """, unsafe_allow_html=True)

    h1, h2, h3, h4 = st.columns(4)
    steps = [
        ("1", "🖊️", "Configure Processes", "Enter process parameters: PID, arrival time, burst time, priority, and memory requirement — or pick a preset scenario."),
        ("2", "⚙️", "Choose Algorithm",     "Select a CPU scheduling policy: FCFS, SJF, Priority, or Round Robin. Set the time quantum and total RAM available."),
        ("3", "▶",  "Run Simulation",       "Hit Dispatch and the native C++ engine runs the full kernel simulation — in milliseconds."),
        ("4", "📊", "Analyze Results",       "Explore interactive Gantt charts, memory maps, process tables, CPU register states, and kernel logs."),
    ]
    for col, (num, icon, title, desc) in zip([h1, h2, h3, h4], steps):
        with col:
            st.markdown(f"""
            <div class="how-step">
                <div class="step-num">{num}</div>
                <div style="font-size:1.5rem; margin-bottom:10px;">{icon}</div>
                <div class="step-title">{title}</div>
                <div class="step-desc">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # Algorithms preview
    st.markdown("""
    <div class="section-header">
        <div class="section-label">✦ Algorithms</div>
        <div class="section-title">Four Scheduling Disciplines</div>
        <p class="section-desc">Each algorithm makes different tradeoffs between fairness, throughput, and response time.</p>
    </div>
    """, unsafe_allow_html=True)

    ac1, ac2, ac3, ac4 = st.columns(4)
    algos = [
        ("FCFS", "badge-cyan",   "#63b3ed", "Non-Preemptive",
         "First Come, First Served executes processes strictly in arrival order. Simple but can cause the convoy effect.",
         [("Fairness","Arrival Order"), ("Overhead","None"), ("Best For","Batch jobs")]),
        ("SJF",  "badge-green",  "#48bb78", "Non-Preemptive",
         "Shortest Job First picks the process with the smallest burst time. Minimizes average waiting time but requires burst prediction.",
         [("Fairness","Burst-biased"), ("Overhead","None"), ("Best For","Interactive systems")]),
        ("PRIO", "badge-purple", "#9f7aea", "Non-Preemptive",
         "Priority Scheduling serves the highest-priority process next. Can starve low-priority processes without aging.",
         [("Fairness","Priority-biased"), ("Overhead","None"), ("Best For","Real-time systems")]),
        ("RR",   "badge-amber",  "#ed8936", "Preemptive",
         "Round Robin slices CPU time into equal quanta and rotates between ready processes — the basis of modern fair schedulers.",
         [("Fairness","Equal slices"), ("Overhead","Highest"), ("Best For","Time-sharing")]),
    ]
    for col, (name, bcls, color, atype, desc, metrics) in zip([ac1, ac2, ac3, ac4], algos):
        metric_html = "".join([f'<div class="metric-row"><span>{k}</span><span>{v}</span></div>' for k, v in metrics])
        with col:
            st.markdown(f"""
            <div class="algo-card">
                <div class="algo-title">{name}</div>
                <span class="algo-badge {bcls}" style="color:{color};">{atype}</span>
                <div class="algo-desc">{desc}</div>
                <div class="algo-metric">{metric_html}</div>
            </div>
            """, unsafe_allow_html=True)

    # CTA
    st.markdown("""
    <div style="text-align:center; padding: 60px 20px 40px;">
        <div class="section-label" style="margin-bottom:16px;">✦ Ready to Explore?</div>
        <h2 style="font-size:2rem; font-weight:800; color:#fff; letter-spacing:-1px; margin-bottom:12px;">
            Start Your First Simulation
        </h2>
        <p style="font-size:0.95rem; color:#718096; max-width:480px; margin:0 auto 28px; line-height:1.7;">
            Jump into the Simulator tab, pick a preset, choose an algorithm and hit Dispatch —
            your OS kernel runs in milliseconds.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Navigate button
    if st.button("▶  Open the Simulator  →", type="primary", use_container_width=False):
        st.session_state.page = "⚙️ Simulator"
        st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: OS CONCEPTS
# ─────────────────────────────────────────────────────────────────────────────
elif page == "📚 OS Concepts":

    st.markdown("""
    <div style="padding: 36px 0 24px;">
        <div class="section-label">📚 Learning Module</div>
        <div class="section-title" style="text-align:left; font-size:2rem; letter-spacing:-0.8px;">Operating System Concepts</div>
        <p style="font-size:0.9rem; color:#718096; margin-top:8px; max-width:620px; line-height:1.7;">
            Everything you see in the simulator is based on real kernel subsystem theory.
            Understand each concept before you simulate it — or simulate first and read the theory after.
        </p>
    </div>
    """, unsafe_allow_html=True)

    concepts = [
        ("01", "Process Control Block (PCB)",
         "task_struct / struct Process",
         """The PCB is the kernel's representation of a process. It stores everything the OS needs
         to manage and resume a process: its identity (PID), state, scheduling metadata, memory mapping,
         register snapshot, and accounting statistics. In Linux this is called <strong style='color:#e2e8f0;'>task_struct</strong>.
         In this simulator it maps to <strong style='color:#63b3ed;'>struct Process</strong> in C++.""",
         ["PID — unique identifier", "Burst / Remaining CPU time", "Priority level", "Memory footprint (MB)",
          "Program Counter (PC)", "Registers R0–R3", "State, Arrival, Completion, Turnaround, Waiting"]),

        ("02", "5-State Process Lifecycle",
         "New → Waiting for Memory → Ready → Running → Terminated",
         """Real OS kernels track process lifecycle state. This simulator implements an extended 5-state
         model that adds <strong style='color:#ed8936;'>Waiting for Memory</strong> — a state between creation
         and scheduling that models what happens when physical RAM is exhausted and processes queue for
         admission (similar to swapping in real OSes).""",
         ["New — process created, not yet admitted",
          "Waiting for Memory — RAM unavailable, blocked by Long-Term Scheduler",
          "Ready — in RAM, waiting for CPU in Ready Queue",
          "Running — actively executing on CPU",
          "Terminated — completed, memory released back to pool"]),

        ("03", "CPU Scheduling Algorithms",
         "FCFS · SJF · Priority · Round Robin",
         """The scheduler is the core of the OS kernel — it decides which process gets the CPU next.
         Non-preemptive schedulers (FCFS, SJF, Priority) let a running process hold the CPU until it
         finishes. Preemptive schedulers (Round Robin) interrupt it after a fixed time quantum
         (<strong style='color:#63b3ed;'>τ</strong>), causing a context switch.""",
         ["FCFS — arrival order, can cause convoy effect",
          "SJF — minimizes avg waiting time, needs burst prediction",
          "Priority — urgency-based, risk of starvation without aging",
          "Round Robin — fair time-slicing, basis of modern schedulers"]),

        ("04", "Context Switching",
         "Dispatcher · PCB Save · PCB Restore",
         """Context switching is the act of saving the current process's state (registers, PC) into
         its PCB and loading the next process's saved state. It is pure overhead — the CPU does no
         useful work during a switch. Round Robin maximizes switches; FCFS minimizes them. This
         simulator records every switch with timestamps.""",
         ["Triggered when time quantum expires (RR) or process finishes",
          "CPU state saved to old PCB (R0, R1, R2, R3, PC)",
          "New process's PCB loaded onto CPU",
          "Context switch count is a key performance metric"]),

        ("05", "Memory Management & Admission Control",
         "Long-Term Scheduler · MMU · Base-Limit Registers",
         """When RAM is limited, the Long-Term Scheduler (also called the Job Scheduler) controls
         which processes are admitted into the Ready Queue. Processes that cannot fit in memory are
         held in a <strong style='color:#ed8936;'>Waiting for Memory</strong> queue until running
         processes terminate and release their allocation. The simulator tracks allocation and
         deallocation events chronologically.""",
         ["Fixed physical RAM capacity (configurable MB)",
          "Admission uses first-fit by arrival order",
          "Memory wait time = Admission Time − Arrival Time",
          "Memory map shown as Base / Limit segment strip"]),

        ("06", "Virtual CPU & Register Simulation",
         "PC · R0 · R1 · R2 · R3",
         """The simulator maintains a virtual register file per process, updated on every execution
         slice. This models how a real CPU saves hardware register state to the PCB on context switch.
         The Program Counter (PC) tracks instruction pointer progress.""",
         ["PC — cumulative execution ticks (instruction pointer)",
          "R0 — accumulated CPU time (accumulator register)",
          "R1 — total execution slices granted",
          "R2 — timestamp of last slice completion",
          "R3 — PID verification register"]),

        ("07", "Performance Metrics",
         "TAT · WT · MWT · CPU Utilization",
         """Measuring scheduler efficiency requires well-defined metrics. These are the standard
         formulas used in every OS textbook and in the simulator's output:""",
         ["Turnaround Time (TAT) = Completion − Arrival",
          "Waiting Time (WT) = TAT − Burst − Memory Wait",
          "Memory Wait Time (MWT) = Admission − Arrival",
          "CPU Utilization = (Busy Time / Elapsed Time) × 100%",
          "Context Switches — total preemptions between processes"]),
    ]

    for num, title, subtitle, body, bullets in concepts:
        bullet_html = "".join([f'<li style="color:#718096; font-size:0.82rem; padding:2px 0;">{b}</li>' for b in bullets])
        st.markdown(f"""
        <div class="concept-card">
            <div class="concept-header">
                <div class="concept-number">{num}</div>
                <div>
                    <div class="concept-title">{title}</div>
                    <div class="concept-subtitle">{subtitle}</div>
                </div>
            </div>
            <div class="concept-body" style="margin-bottom:10px;">{body}</div>
            <ul style="margin:0; padding-left:20px; margin-top:8px;">
                {bullet_html}
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box" style="margin-top:24px;">
        <strong>✅ Ready to simulate?</strong> Every concept above is directly observable in the
        <strong>⚙️ Simulator</strong> tab. Run a simulation and cross-reference what you see with
        these definitions.
    </div>
    """, unsafe_allow_html=True)

    if st.button("▶  Go to Simulator", type="primary"):
        st.session_state.page = "⚙️ Simulator"
        st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: SIMULATOR
# ─────────────────────────────────────────────────────────────────────────────
elif page == "⚙️ Simulator":

    # ── Sim header
    st.markdown("""
    <div class="sim-header">
        <div class="sim-header-top">
            <div>
                <div class="sim-title">⚙️ OS Kernel Simulator</div>
                <div class="sim-desc">Configure processes, pick a scheduling algorithm, and dispatch the C++ kernel engine.</div>
            </div>
            <div class="sim-badges">
                <span class="sidebar-os-badge badge-green">● KERNEL ONLINE</span>
                <span class="sidebar-os-badge badge-cyan">C++ vm_engine.exe</span>
                <span class="sidebar-os-badge badge-amber">x86_64 Simulation</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Presets
    st.markdown("**🎯 Load a Preset Workload**")
    preset_cols = st.columns(5)
    for idx, (p_name, p_data) in enumerate(PRESETS.items()):
        with preset_cols[idx]:
            if st.button(p_name, key=f"preset_{idx}", use_container_width=True):
                st.session_state.processes = [p.copy() for p in p_data]
                st.rerun()

    st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)

    # ── Process Table
    st.markdown("**📋 Process Descriptor Table (PCB Input)**")
    edited_df = st.data_editor(
        pd.DataFrame(st.session_state.processes),
        num_rows="dynamic",
        use_container_width=True,
        hide_index=True,
        key="process_editor",
        column_config={
            "PID":      st.column_config.NumberColumn("PID",            min_value=1, step=1, help="Unique Process ID"),
            "Arrival":  st.column_config.NumberColumn("Arrival Time",   min_value=0, step=1, help="Clock tick when process arrives"),
            "Burst":    st.column_config.NumberColumn("CPU Burst",       min_value=1, step=1, help="Total CPU ticks required"),
            "Priority": st.column_config.NumberColumn("Priority",        min_value=1, step=1, help="Lower = Higher priority"),
            "Memory":   st.column_config.NumberColumn("Memory (MB)",     min_value=1, step=1, help="RAM required for admission"),
        },
    )
    st.session_state.processes = edited_df.to_dict("records")

    st.markdown('<div style="height:8px;"></div>', unsafe_allow_html=True)

    # ── Scheduler Controls
    col_algo, col_quantum, col_ram = st.columns([2, 1.2, 1.5])
    with col_algo:
        algorithm = st.selectbox(
            "🧠 Scheduling Algorithm",
            ["FCFS", "SJF", "Priority", "Round Robin"],
            index=3,
            help="CPU scheduling policy run by the C++ engine.",
        )
    with col_quantum:
        quantum = st.number_input(
            "⏱ Time Quantum (τ)",
            min_value=1, value=2, step=1,
            disabled=(algorithm != "Round Robin"),
            help="Time slice for Round Robin. Ignored for other algorithms.",
        )
    with col_ram:
        total_memory = st.number_input(
            "💾 Physical RAM (MB)",
            min_value=50, value=512, step=50,
            help="Total simulated RAM. Processes queue if RAM is exhausted.",
        )

    # ── Dispatch Buttons
    st.markdown('<div style="height:8px;"></div>', unsafe_allow_html=True)
    btn1, btn2 = st.columns([2.5, 1.5])
    with btn1:
        run_sim = st.button("▶  DISPATCH KERNEL SIMULATION", type="primary", use_container_width=True)
    with btn2:
        run_benchmark = st.button("⚡  BENCHMARK ALL 4 ALGORITHMS", type="secondary", use_container_width=True)

    # ── Dispatch logic
    if run_sim:
        for k in RESULT_KEYS:
            st.session_state.pop(k, None)
        try:
            validated_df = validate_processes(edited_df, total_memory, quantum)
            output = run_cpp_simulation(
                validated_df.to_dict("records"), algorithm, int(quantum), int(total_memory)
            )
            for key, value in output.items():
                st.session_state[key] = value
            st.session_state.algorithm    = algorithm
            st.session_state.total_memory = int(total_memory)
            st.session_state.quantum      = int(quantum)
            st.toast(f"✅ Simulation complete — [{algorithm}]", icon="⚡")
        except Exception as err:
            st.error(f"⚠️ Simulation Error: {err}")

    if run_benchmark:
        try:
            validated_df = validate_processes(edited_df, total_memory, quantum)
            bench_data = []
            with st.spinner("Running benchmark across all 4 algorithms..."):
                for alg in ["FCFS", "SJF", "Priority", "Round Robin"]:
                    res = run_cpp_simulation(
                        validated_df.to_dict("records"), alg, int(quantum), int(total_memory)
                    )
                    rdf  = res["results"]
                    summ = res["summary"]
                    bench_data.append({
                        "Algorithm":          alg,
                        "Avg Waiting":        round(float(rdf["Waiting"].mean()), 2),
                        "Avg Turnaround":     round(float(rdf["Turnaround"].mean()), 2),
                        "Avg Memory Wait":    round(float(rdf["Memory Wait"].mean()), 2),
                        "Context Switches":   int(read_metric(summ, "Context switches")),
                        "CPU Utilization (%)": read_metric(summ, "CPU utilization"),
                        "Elapsed Time":       int(read_metric(summ, "Elapsed time")),
                    })
                primary = run_cpp_simulation(
                    validated_df.to_dict("records"), algorithm, int(quantum), int(total_memory)
                )
                for key, value in primary.items():
                    st.session_state[key] = value
                st.session_state.algorithm        = algorithm
                st.session_state.total_memory     = int(total_memory)
                st.session_state.quantum          = int(quantum)
                st.session_state.benchmark_results = pd.DataFrame(bench_data)
            st.toast("📊 Benchmark complete!", icon="📊")
        except Exception as err:
            st.error(f"⚠️ Benchmark Error: {err}")

    # ── Results Panel
    if "results" not in st.session_state:
        st.markdown("""
        <div style="text-align:center; padding:60px 20px;">
            <div style="font-size:3rem; margin-bottom:16px;">🚀</div>
            <div style="font-size:1.1rem; font-weight:600; color:#e2e8f0; margin-bottom:8px;">Ready to Simulate</div>
            <div style="font-size:0.85rem; color:#718096; max-width:400px; margin:0 auto; line-height:1.7;">
                Configure your process table, pick a scheduling algorithm, then click
                <strong style="color:#63b3ed;">Dispatch Kernel Simulation</strong> to see the results.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        result_df  = st.session_state.results
        timeline_df = st.session_state.timeline
        memory_df   = st.session_state.memory_events
        state_df    = st.session_state.state_events
        cpu_df      = st.session_state.cpu_events
        summary     = st.session_state.summary
        algo_used   = st.session_state.algorithm
        ram_cap     = st.session_state.total_memory

        elapsed_time  = int(read_metric(summary, "Elapsed time"))
        busy_time     = int(read_metric(summary, "Busy time"))
        ctx_switches  = int(read_metric(summary, "Context switches"))
        cpu_util      = read_metric(summary, "CPU utilization")
        avg_wait      = result_df["Waiting"].mean()
        avg_turnaround = result_df["Turnaround"].mean()
        peak_ram      = int(memory_df["UsedMB"].max())

        # ── KPI Cards
        st.markdown('<hr class="divider">', unsafe_allow_html=True)
        st.markdown("**📡 Simulation Telemetry**")
        st.markdown(f"""
        <div class="kpi-grid">
            <div class="kpi-card">
                <div class="kpi-label">Algorithm</div>
                <div class="kpi-value" style="font-size:1.1rem; color:#63b3ed;">{algo_used}</div>
                <div class="kpi-sub">τ = {st.session_state.quantum if algo_used=="Round Robin" else "N/A"}</div>
            </div>
            <div class="kpi-card green">
                <div class="kpi-label">CPU Utilization</div>
                <div class="kpi-value" style="color:#48bb78;">{cpu_util:.1f}%</div>
                <div class="kpi-sub">{busy_time} busy / {elapsed_time} total ticks</div>
            </div>
            <div class="kpi-card amber">
                <div class="kpi-label">Context Switches</div>
                <div class="kpi-value" style="color:#ed8936;">{ctx_switches}</div>
                <div class="kpi-sub">{int(result_df["Execution Slices"].sum())} total slices</div>
            </div>
            <div class="kpi-card purple">
                <div class="kpi-label">Avg Waiting Time</div>
                <div class="kpi-value" style="color:#9f7aea;">{avg_wait:.2f}</div>
                <div class="kpi-sub">Ticks in Ready Queue</div>
            </div>
            <div class="kpi-card">
                <div class="kpi-label">Avg Turnaround</div>
                <div class="kpi-value" style="color:#63b3ed;">{avg_turnaround:.2f}</div>
                <div class="kpi-sub">Submit → Exit latency</div>
            </div>
            <div class="kpi-card rose">
                <div class="kpi-label">Peak RAM Usage</div>
                <div class="kpi-value" style="color:#fc8181;">{peak_ram} <span style="font-size:0.9rem;">MB</span></div>
                <div class="kpi-sub">{peak_ram/ram_cap*100:.1f}% of {ram_cap} MB</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ── Clock Scrubber
        st.markdown("**🕐 Interactive Clock Cycle Replay**")
        sc_col, sc_info = st.columns([4, 1])
        with sc_col:
            scrub_t = st.slider(
                "System Clock Tick (T)",
                min_value=0, max_value=max(1, elapsed_time), value=0, step=1,
                help="Inspect CPU register state, ready queue, and RAM allocation at tick T.",
            )
        with sc_info:
            status_col = "#48bb78" if scrub_t < elapsed_time else "#ed8936"
            status_txt = "EXECUTING" if scrub_t < elapsed_time else "HALTED"
            st.markdown(f"""
            <div style="font-family:var(--mono); font-size:0.78rem; background:#07101e; border:1px solid #1d2d44; padding:12px 14px; border-radius:8px; margin-top:14px;">
                <div>T = <span style="color:#63b3ed; font-weight:700;">{scrub_t:02d}</span></div>
                <div style="color:{status_col}; font-weight:600; margin-top:4px;">● {status_txt}</div>
            </div>
            """, unsafe_allow_html=True)

        # CPU state at scrub_t
        active_block = timeline_df[(timeline_df["Start"] <= scrub_t) & (timeline_df["End"] > scrub_t)]
        if not active_block.empty:
            curr_proc_str = str(active_block.iloc[0]["Process"])
            cpu_running   = True
            proc_num      = int(curr_proc_str.replace("P","").strip()) if "P" in curr_proc_str else -1
        else:
            curr_proc_str = "IDLE"
            cpu_running   = False
            proc_num      = -1

        latest_cpu = cpu_df[cpu_df["Time"] <= scrub_t]
        if not latest_cpu.empty:
            lev     = latest_cpu.iloc[-1]
            pc_val  = f"0x{int(lev['PC']):04X}"
            reg_raw = str(lev["Registers"])
            if ";" in reg_raw:
                regs = reg_raw.split(";")
                r0, r1, r2, r3 = (regs+["0","0","0","0"])[:4]
            else:
                r0=r1=r2=r3="0"
        else:
            pc_val = "0x0000"; r0=r1=r2=r3="0"

        in_ram_pids, ready_pids, mem_wait_pids, used_ram_at_t = [], [], [], 0
        for _, pr in result_df.iterrows():
            pid=int(pr["PID"]); arr=int(pr["Arrival"]); adm=int(pr["Admission Time"])
            comp=int(pr["Completion"]); mem=int(pr["Memory (MB)"])
            if adm <= scrub_t < comp:
                in_ram_pids.append(pid); used_ram_at_t += mem
                if pid != proc_num: ready_pids.append(pid)
            elif arr <= scrub_t < adm:
                mem_wait_pids.append(pid)

        hud_l, hud_r = st.columns(2)
        with hud_l:
            status_color = "#48bb78" if cpu_running else "#ed8936"
            st.markdown(f"""
            <div class="cpu-hud">
                <div class="hud-title">
                    <span>VIRTUAL CPU CORE 0</span>
                    <span style="color:{status_color};">● {curr_proc_str}</span>
                </div>
                <div class="reg-grid">
                    <div class="reg-box"><div class="reg-name">PROGRAM COUNTER</div><div class="reg-val" style="color:#63b3ed;">{pc_val}</div></div>
                    <div class="reg-box"><div class="reg-name">R0 — ACCUMULATOR</div><div class="reg-val">{r0}</div></div>
                    <div class="reg-box"><div class="reg-name">R1 — DATA</div><div class="reg-val">{r1}</div></div>
                    <div class="reg-box"><div class="reg-name">R2 — INDEX</div><div class="reg-val">{r2}</div></div>
                    <div class="reg-box"><div class="reg-name">R3 — STATUS</div><div class="reg-val">{r3}</div></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        with hud_r:
            rq_html  = " ".join([f'<span class="sidebar-os-badge badge-cyan">PID {p}</span>' for p in ready_pids]) or '<span style="color:#4a5568;">Queue empty</span>'
            mwq_html = " ".join([f'<span class="sidebar-os-badge badge-amber">PID {p}</span>' for p in mem_wait_pids]) or '<span style="color:#4a5568;">None</span>'
            st.markdown(f"""
            <div class="cpu-hud">
                <div class="hud-title"><span>SCHEDULER QUEUES (T = {scrub_t})</span></div>
                <div style="font-family:var(--mono); font-size:0.78rem;">
                    <div style="margin-bottom:12px;">
                        <div style="color:#718096; font-size:0.68rem; letter-spacing:1px; text-transform:uppercase; margin-bottom:6px;">READY QUEUE (IN RAM)</div>
                        <div style="display:flex; gap:5px; flex-wrap:wrap;">{rq_html}</div>
                    </div>
                    <div>
                        <div style="color:#718096; font-size:0.68px; letter-spacing:1px; text-transform:uppercase; margin-bottom:6px;">MEMORY BLOCKED QUEUE</div>
                        <div style="display:flex; gap:5px; flex-wrap:wrap;">{mwq_html}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # ── Tabs
        st.markdown('<div style="height:12px;"></div>', unsafe_allow_html=True)
        tabs = st.tabs([
            "📈 Gantt Chart",
            "💾 Memory Map",
            "📋 Process Table (PCB)",
            "🔄 CPU Event Log",
            "📡 Kernel Syslog",
            "📥 Export Data",
        ])

        # Tab 1: Gantt
        with tabs[0]:
            st.markdown('<div style="font-size:0.8rem; color:#718096; margin-bottom:10px; font-family:var(--mono);">CPU DISPATCH GANTT — EXECUTION BLOCKS PER CLOCK TICK</div>', unsafe_allow_html=True)
            fig = go.Figure()
            for _, b in timeline_df.iterrows():
                p_name = str(b["Process"])
                b_s = int(b["Start"]); b_e = int(b["End"]); b_d = int(b["Duration"])
                pid = int(p_name.replace("P","").strip()) if "P" in p_name else 0
                color = PID_COLORS.get(pid, "#63b3ed")
                fig.add_trace(go.Bar(
                    x=[b_d], y=["CPU Core 0"], base=[b_s], orientation="h",
                    name=p_name, text=[f"{p_name} ({b_d}t)"], textposition="inside",
                    marker=dict(color=color, line=dict(color="#04080f", width=1)),
                    hovertemplate=f"<b>{p_name}</b><br>Start: {b_s}<br>End: {b_e}<br>Duration: {b_d} ticks<extra></extra>",
                ))
            fig.add_vline(x=scrub_t, line_dash="dot", line_color="#63b3ed", line_width=2,
                          annotation_text=f"T={scrub_t}", annotation_position="top",
                          annotation_font=dict(color="#63b3ed", size=11, family="JetBrains Mono"))
            fig.update_layout(
                barmode="overlay", **plotly_dark_layout(height=240,
                xaxis=dict(title=dict(text="Clock Ticks", font=dict(family="JetBrains Mono", color="#718096")),
                           range=[0, max(1, elapsed_time)], dtick=1, showgrid=True, gridcolor="#1d2d44",
                           tickfont=dict(family="JetBrains Mono", color="#718096")),
                yaxis=dict(showticklabels=True, tickfont=dict(family="JetBrains Mono", color="#63b3ed", size=12)),
                showlegend=True,
                legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1,
                            font=dict(family="JetBrains Mono", color="#e2e8f0", size=10)),
            ))
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(timeline_df[["Process","Start","End","Duration"]], use_container_width=True, hide_index=True)

        # Tab 2: Memory
        with tabs[1]:
            free_at_t = ram_cap - used_ram_at_t
            segs_html = []
            cur = 0
            for pid_m in in_ram_pids:
                pr = result_df[result_df["PID"]==pid_m].iloc[0]
                mem = int(pr["Memory (MB)"])
                pct = mem/ram_cap*100
                color = PID_COLORS.get(pid_m, "#63b3ed")
                segs_html.append(f'<div class="mem-seg" style="width:{pct:.1f}%;background:{color};" title="PID {pid_m}: {mem}MB">PID {pid_m} ({mem}MB)</div>')
                cur += mem
            if free_at_t > 0:
                segs_html.append(f'<div class="mem-seg" style="width:{free_at_t/ram_cap*100:.1f}%;background:#1d2d44;color:#718096;" title="FREE: {free_at_t}MB">FREE ({free_at_t}MB)</div>')

            st.markdown(f"""
            <div class="mem-bar-wrap">
                <div class="mem-bar-label">
                    <span style="color:#63b3ed;">RAM SNAPSHOT — T = {scrub_t}</span>
                    <span>USED: {used_ram_at_t} / {ram_cap} MB ({used_ram_at_t/ram_cap*100:.1f}%)</span>
                </div>
                <div class="mem-bar">{''.join(segs_html)}</div>
                <div style="display:flex; justify-content:space-between; font-family:var(--mono); font-size:0.65rem; color:#4a5568; margin-top:5px;">
                    <span>BASE: 0x0000</span><span>LIMIT: 0x{ram_cap:04X} ({ram_cap} MB)</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

            fig_mem = go.Figure()
            fig_mem.add_trace(go.Scatter(
                x=memory_df["Time"], y=memory_df["UsedMB"],
                mode="lines+markers", line=dict(shape="hv", color="#63b3ed", width=2),
                marker=dict(size=5, color="#48bb78"), name="Used RAM",
                hovertemplate="T=%{x} ticks<br>Used: %{y} MB<extra></extra>",
            ))
            fig_mem.add_hline(y=ram_cap, line_dash="dash", line_color="#fc8181",
                              annotation_text=f"RAM LIMIT ({ram_cap} MB)",
                              annotation_font=dict(color="#fc8181", family="JetBrains Mono"))
            fig_mem.update_layout(**plotly_dark_layout(height=280,
                xaxis=dict(title=dict(text="Clock Ticks", font=dict(family="JetBrains Mono",color="#718096")),
                           showgrid=True, gridcolor="#1d2d44", tickfont=dict(family="JetBrains Mono",color="#718096")),
                yaxis=dict(title=dict(text="Memory (MB)", font=dict(family="JetBrains Mono",color="#718096")),
                           range=[0, ram_cap*1.15], showgrid=True, gridcolor="#1d2d44",
                           tickfont=dict(family="JetBrains Mono",color="#718096")),
            ))
            st.plotly_chart(fig_mem, use_container_width=True)
            st.dataframe(memory_df, use_container_width=True, hide_index=True)

        # Tab 3: PCB Table
        with tabs[2]:
            pcb_disp = result_df.copy()
            pcb_disp["Registers"] = pcb_disp.apply(lambda r: f"[{r['R0']}, {r['R1']}, {r['R2']}, {r['R3']}]", axis=1)
            pcb_disp["PC"]        = pcb_disp["Program Counter"].apply(lambda v: f"0x{int(v):04X}")
            st.dataframe(
                pcb_disp[["PID","State","Priority","Arrival","Admission Time","Memory Wait",
                           "Burst","First Start","Completion","Turnaround","Waiting",
                           "PC","Registers","Execution Slices","Context Switches","Memory (MB)"]],
                use_container_width=True, hide_index=True
            )

        # Tab 4: CPU Events
        with tabs[3]:
            st.markdown('<div style="font-size:0.78rem; color:#718096; margin-bottom:8px; font-family:var(--mono);">VIRTUAL CPU EXECUTION TRACE — SLICE & CONTEXT SWITCH LOG</div>', unsafe_allow_html=True)
            st.dataframe(cpu_df, use_container_width=True, hide_index=True)
            st.markdown('<div style="font-size:0.78rem; color:#718096; margin:14px 0 8px; font-family:var(--mono);">PROCESS STATE TRANSITION TRAIL</div>', unsafe_allow_html=True)
            st.dataframe(state_df, use_container_width=True, hide_index=True)

        # Tab 5: Kernel Syslog (dmesg)
        with tabs[4]:
            log_lines = [(0, "KERN_BOOT", f"KernelSim initialized | RAM: {ram_cap}MB | Policy: {algo_used}")]
            for _, m in memory_df.iterrows():
                log_lines.append((int(m["Time"]), "MMU", f"PID {m['PID']} {m['Event']} | Used: {m['UsedMB']}/{ram_cap}MB"))
            for _, s in state_df.iterrows():
                fs = s.get("Previous State", s.get("From", "?"))
                ts = s.get("New State", s.get("To", "?"))
                log_lines.append((int(s["Time"]), "SCHED", f"PID {s['PID']} [{fs}] → [{ts}]"))
            for _, c in cpu_df.iterrows():
                ev = str(c.get("Event",""))
                fr = str(c.get("From PID","-")); to = str(c.get("To PID","-"))
                try: pc = int(c.get("PC",0))
                except: pc = 0
                dur = c.get("Duration",0)
                if ev == "CONTEXT SWITCH":
                    log_lines.append((int(c["Time"]), "CTX", f"Switch PID {fr} → PID {to} | Saved PC: 0x{pc:04X}"))
                else:
                    log_lines.append((int(c["Time"]), "CPU", f"Exec PID {to} for {dur} ticks | PC: 0x{pc:04X}"))
            log_lines.sort(key=lambda x: x[0])
            dmesg = "".join([
                f'<div class="log-line"><span class="log-t">[{t:04d}.00]</span>'
                f'<span class="log-s">[{html.escape(str(s))}]</span>'
                f'<span class="log-m">{html.escape(str(m))}</span></div>'
                for t, s, m in log_lines
            ])
            st.markdown(f'<div class="terminal">{dmesg}</div>', unsafe_allow_html=True)

        # Tab 6: Export
        with tabs[5]:
            st.markdown('<div style="font-size:0.78rem; color:#718096; margin-bottom:14px; font-family:var(--mono);">C++ NATIVE OUTPUT — DOWNLOAD SIMULATION RESULTS</div>', unsafe_allow_html=True)
            with st.expander("View C++ Engine Summary Output", expanded=True):
                st.code(st.session_state.summary_text, language="text")
                st.caption(f"Output directory: {st.session_state.output_dir}")

            ec1, ec2, ec3 = st.columns(3)
            with ec1:
                st.download_button("📥 Process Results (CSV)", result_df.to_csv(index=False), "process_results.csv", "text/csv", use_container_width=True)
                st.download_button("📥 Memory Events (CSV)", memory_df.to_csv(index=False), "memory_events.csv", "text/csv", use_container_width=True)
            with ec2:
                st.download_button("📥 Gantt Timeline (CSV)", timeline_df.to_csv(index=False), "timeline.csv", "text/csv", use_container_width=True)
                st.download_button("📥 State Transitions (CSV)", state_df.to_csv(index=False), "state_transitions.csv", "text/csv", use_container_width=True)
            with ec3:
                st.download_button("📥 CPU Events (CSV)", cpu_df.to_csv(index=False), "cpu_events.csv", "text/csv", use_container_width=True)
                st.download_button("📥 Kernel Summary (TXT)", st.session_state.summary_text, "kernel_summary.txt", "text/plain", use_container_width=True)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE: BENCHMARK
# ─────────────────────────────────────────────────────────────────────────────
elif page == "📊 Benchmark":

    st.markdown("""
    <div style="padding: 36px 0 24px;">
        <div class="section-label">📊 Performance Analysis</div>
        <div class="section-title" style="text-align:left; font-size:2rem; letter-spacing:-0.8px;">Algorithm Benchmark Matrix</div>
        <p style="font-size:0.9rem; color:#718096; margin-top:8px; max-width:620px; line-height:1.7;">
            Compare all four scheduling algorithms side-by-side on the same workload.
            Go to the Simulator tab, run a benchmark, and come back here to analyze the results.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if "benchmark_results" not in st.session_state:
        st.markdown("""
        <div style="text-align:center; padding:70px 20px;">
            <div style="font-size:3rem; margin-bottom:16px;">📊</div>
            <div style="font-size:1.1rem; font-weight:600; color:#e2e8f0; margin-bottom:10px;">No Benchmark Data Yet</div>
            <div style="font-size:0.85rem; color:#718096; max-width:400px; margin:0 auto; line-height:1.7;">
                Go to <strong style="color:#63b3ed;">⚙️ Simulator</strong>, configure your workload and hit
                <strong style="color:#63b3ed;">⚡ BENCHMARK ALL 4 ALGORITHMS</strong>.
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("▶  Go to Simulator", type="primary"):
            st.session_state.page = "⚙️ Simulator"
            st.rerun()
    else:
        bench = st.session_state.benchmark_results
        st.dataframe(bench, use_container_width=True, hide_index=True)

        # Comparative chart
        b_fig = go.Figure()
        metrics_to_plot = [
            ("Avg Waiting",      "#63b3ed"),
            ("Avg Turnaround",   "#9f7aea"),
            ("Context Switches", "#ed8936"),
        ]
        for metric, color in metrics_to_plot:
            b_fig.add_trace(go.Bar(
                x=bench["Algorithm"], y=bench[metric],
                name=metric, marker_color=color,
            ))
        b_fig.update_layout(
            barmode="group", **plotly_dark_layout(height=360,
            xaxis=dict(title=dict(text="Scheduling Algorithm", font=dict(family="JetBrains Mono",color="#718096")),
                       tickfont=dict(family="JetBrains Mono",color="#e2e8f0"), gridcolor="#1d2d44"),
            yaxis=dict(title=dict(text="Ticks / Count", font=dict(family="JetBrains Mono",color="#718096")),
                       tickfont=dict(family="JetBrains Mono",color="#718096"), gridcolor="#1d2d44"),
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1,
                        font=dict(family="JetBrains Mono", color="#e2e8f0")),
        ))
        st.plotly_chart(b_fig, use_container_width=True)

        # Verdict
        best_wait   = bench.loc[bench["Avg Waiting"].idxmin()]
        best_switch = bench.loc[bench["Context Switches"].idxmin()]
        best_cpu    = bench.loc[bench["CPU Utilization (%)"].idxmax()]

        st.markdown(f"""
        <div style="background:#0f1829; border:1px solid #1d2d44; border-left:3px solid #48bb78; border-radius:10px; padding:18px 22px; margin-top:16px;">
            <div style="font-size:0.85rem; font-weight:700; color:#48bb78; margin-bottom:12px;">🏆 Analysis Verdict</div>
            <div style="font-family:var(--mono); font-size:0.8rem; display:flex; flex-direction:column; gap:8px;">
                <div style="color:#718096;">
                    <span style="color:#e2e8f0;">MINIMUM WAIT TIME:</span>
                    <span style="color:#63b3ed;"> {best_wait["Algorithm"]}</span>
                    achieved the lowest average waiting time
                    <span style="color:#48bb78;"> ({best_wait["Avg Waiting"]} ticks)</span>
                </div>
                <div style="color:#718096;">
                    <span style="color:#e2e8f0;">MINIMUM OVERHEAD:</span>
                    <span style="color:#63b3ed;"> {best_switch["Algorithm"]}</span>
                    had the fewest context switches
                    <span style="color:#ed8936;"> ({best_switch["Context Switches"]})</span>
                </div>
                <div style="color:#718096;">
                    <span style="color:#e2e8f0;">BEST CPU UTILIZATION:</span>
                    <span style="color:#63b3ed;"> {best_cpu["Algorithm"]}</span>
                    achieved
                    <span style="color:#9f7aea;"> {best_cpu["CPU Utilization (%)"]:.1f}% CPU utilization</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # CPU Utilization radar
        st.markdown('<div style="height:16px;"></div>', unsafe_allow_html=True)
        util_fig = go.Figure(go.Bar(
            x=bench["Algorithm"], y=bench["CPU Utilization (%)"],
            marker=dict(
                color=bench["CPU Utilization (%)"],
                colorscale=[[0,"#1d2d44"],[0.5,"#2b6cb0"],[1,"#48bb78"]],
                showscale=True,
                colorbar=dict(tickfont=dict(family="JetBrains Mono",color="#718096")),
            ),
            text=[f"{v:.1f}%" for v in bench["CPU Utilization (%)"]],
            textposition="outside", textfont=dict(family="JetBrains Mono", color="#e2e8f0"),
            hovertemplate="<b>%{x}</b><br>CPU Util: %{y:.1f}%<extra></extra>",
        ))
        util_fig.update_layout(
            title=dict(text="CPU Utilization by Algorithm", font=dict(family="JetBrains Mono", color="#718096", size=12)),
            **plotly_dark_layout(height=300,
            yaxis=dict(title=dict(text="Utilization (%)", font=dict(family="JetBrains Mono",color="#718096")),
                       range=[0,110], showgrid=True, gridcolor="#1d2d44",
                       tickfont=dict(family="JetBrains Mono",color="#718096")),
            xaxis=dict(tickfont=dict(family="JetBrains Mono",color="#e2e8f0"), gridcolor="#1d2d44"),
        ))
        st.plotly_chart(util_fig, use_container_width=True)


# ─────────────────────────────────────────────────────────────────────────────
# FOOTER BAR (all pages)
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer-bar">
    <div class="footer-inner">
        <div>
            <div class="footer-brand">Kernel<span>Sim</span> — OS Learning Platform</div>
            <div class="footer-text" style="margin-top:4px;">
                An interactive simulator for learning Operating System concepts through live C++ kernel execution.
            </div>
        </div>
        <div style="text-align:right;">
            <div class="footer-text">
                Built with <strong style="color:#e2e8f0;">C++ (vm_engine)</strong> + <strong style="color:#e2e8f0;">Python Streamlit</strong><br>
                Concepts: PCB · Scheduling · MMU · Context Switching · Process States
            </div>
            <div style="margin-top:8px;">
                <span class="sidebar-os-badge badge-green" style="margin-right:5px;">● Engine Online</span>
                <span class="sidebar-os-badge badge-cyan">C++17 MSVC x64</span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
