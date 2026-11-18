"""
styles.py
─────────
Central CSS design system for KernelSim.
Call `inject_styles()` at the top of every page.
"""

import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# Design Tokens (reference in Python strings if needed)
# ─────────────────────────────────────────────────────────────────────────────
COLORS = {
    "void":       "#04080f",
    "surface":    "#0a111f",
    "card":       "#0e1828",
    "card_alt":   "#111f33",
    "border":     "#1a2a40",
    "cyan":       "#60b8f5",
    "green":      "#46c97a",
    "amber":      "#f0953a",
    "rose":       "#f47b7b",
    "purple":     "#a07eea",
    "teal":       "#36c4b0",
    "text":       "#dde4ef",
    "muted":      "#637080",
}

# ─────────────────────────────────────────────────────────────────────────────
# Full CSS stylesheet
# ─────────────────────────────────────────────────────────────────────────────
_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,300;0,14..32,400;0,14..32,500;0,14..32,600;0,14..32,700;0,14..32,800;0,14..32,900&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

/* ─── RESET STREAMLIT CHROME ─── */
#MainMenu, footer, header                     { visibility: hidden !important; }
div[data-testid="stToolbar"]                  { display: none !important; }
div[data-testid="stDecoration"]               { display: none !important; }
div[data-testid="stStatusWidget"]             { display: none !important; }
.stAppDeployButton                            { display: none !important; }
div[data-testid="stSidebarCollapseButton"]    { display: none !important; }
section[data-testid="stSidebar"] > div:first-child { padding-top: 0 !important; }
div[data-testid="stSidebarNav"]               { display: none !important; }

/* ─── CSS VARIABLES ─── */
:root {
    --void:    #04080f;
    --surface: #0a111f;
    --card:    #0e1828;
    --card2:   #111f33;
    --border:  #1a2a40;
    --cyan:    #60b8f5;
    --green:   #46c97a;
    --amber:   #f0953a;
    --rose:    #f47b7b;
    --purple:  #a07eea;
    --teal:    #36c4b0;
    --text:    #dde4ef;
    --muted:   #637080;
    --mono:    'JetBrains Mono', monospace;
    --sans:    'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --radius:  10px;
    --radius-sm: 6px;
    --shadow:  0 4px 24px rgba(0,0,0,0.5);
}

/* ─── BASE ─── */
html, body, [class*="css"], .stApp {
    font-family: var(--sans) !important;
    color: var(--text) !important;
    background-color: var(--void) !important;
}

.stApp {
    background-image:
        radial-gradient(ellipse at 10% 5%,  rgba(96,184,245,0.045) 0%, transparent 50%),
        radial-gradient(ellipse at 90% 90%, rgba(70,201,122,0.03)  0%, transparent 55%),
        radial-gradient(ellipse at 50% 50%, rgba(160,126,234,0.02) 0%, transparent 70%);
}

/* ─── SIDEBAR ─── */
[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
    width: 240px !important;
}
[data-testid="stSidebar"] > div { padding: 0 !important; }
[data-testid="stSidebar"] .stMarkdown { padding: 0 !important; }
[data-testid="stSidebar"] .block-container { padding: 0 !important; }

/* ─── SIDEBAR COMPONENTS ─── */
.ks-sidebar-brand {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 20px 18px 16px;
    border-bottom: 1px solid var(--border);
}
.ks-sidebar-logo {
    width: 34px; height: 34px;
    background: linear-gradient(135deg, #60b8f5 0%, #46c97a 100%);
    border-radius: 9px;
    display: flex; align-items: center; justify-content: center;
    font-family: var(--mono); font-size: 16px; font-weight: 800; color: var(--void);
    flex-shrink: 0;
}
.ks-sidebar-name  { font-size: 1rem; font-weight: 700; color: #fff; line-height: 1.1; }
.ks-sidebar-name span { color: var(--cyan); }
.ks-sidebar-tag   { font-size: 0.65rem; color: var(--muted); margin-top: 2px; }

.ks-nav-label {
    font-size: 0.6rem; font-weight: 700;
    letter-spacing: 1.8px; text-transform: uppercase;
    color: var(--muted); padding: 14px 18px 4px;
}

.ks-nav-item {
    display: flex; align-items: center; gap: 10px;
    padding: 10px 18px; cursor: pointer;
    font-size: 0.84rem; font-weight: 500; color: var(--muted);
    border-left: 2px solid transparent;
    transition: all 0.15s ease; text-decoration: none;
}
.ks-nav-item:hover  { background: rgba(96,184,245,0.07); color: var(--text); border-left-color: rgba(96,184,245,0.3); }
.ks-nav-item.active { background: rgba(96,184,245,0.1); color: var(--cyan); border-left-color: var(--cyan); font-weight: 600; }
.ks-nav-icon        { font-size: 1rem; width: 18px; text-align: center; }

.ks-status-pill {
    display: flex; align-items: center; gap: 6px;
    font-family: var(--mono); font-size: 0.63rem; font-weight: 600;
    padding: 3px 9px; border-radius: 20px; white-space: nowrap;
}
.pill-green  { background: rgba(70,201,122,0.1); color: var(--green); border: 1px solid rgba(70,201,122,0.2); }
.pill-cyan   { background: rgba(96,184,245,0.1); color: var(--cyan);  border: 1px solid rgba(96,184,245,0.2); }
.pill-amber  { background: rgba(240,149,58,0.1); color: var(--amber); border: 1px solid rgba(240,149,58,0.2); }
.pill-purple { background: rgba(160,126,234,0.1);color: var(--purple);border: 1px solid rgba(160,126,234,0.2); }
.pill-rose   { background: rgba(244,123,123,0.1);color: var(--rose);  border: 1px solid rgba(244,123,123,0.2); }

.pulse-dot {
    width: 7px; height: 7px; border-radius: 50%;
    background: var(--green); box-shadow: 0 0 6px var(--green);
    animation: pulse 2s infinite;
}
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.4;transform:scale(0.75)} }

.ks-sidebar-info {
    margin: 12px; padding: 12px 14px;
    background: rgba(96,184,245,0.05);
    border: 1px solid rgba(96,184,245,0.14);
    border-radius: var(--radius-sm);
}
.ks-sidebar-info-title { font-size: 0.72rem; font-weight: 700; color: var(--cyan); margin-bottom: 5px; }
.ks-sidebar-info-body  { font-size: 0.7rem; color: var(--muted); line-height: 1.6; }

/* ─── TOP NAV BAR ─── */
.ks-topnav {
    position: sticky; top: 0; z-index: 999;
    background: rgba(10, 17, 31, 0.95);
    backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px);
    border-bottom: 1px solid var(--border);
    padding: 0 28px;
    display: flex; align-items: center; justify-content: space-between;
    height: 58px;
    box-shadow: 0 2px 20px rgba(0,0,0,0.5);
}
.ks-topnav-brand { display: flex; align-items: center; gap: 10px; }
.ks-topnav-logo  {
    width: 30px; height: 30px;
    background: linear-gradient(135deg, #60b8f5 0%, #46c97a 100%);
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-family: var(--mono); font-size: 14px; font-weight: 800; color: var(--void);
}
.ks-topnav-name { font-size: 1rem; font-weight: 700; color: #fff; }
.ks-topnav-name span { color: var(--cyan); }
.ks-topnav-links { display: flex; gap: 2px; }
.ks-topnav-link {
    font-size: 0.82rem; font-weight: 500; padding: 6px 12px;
    border-radius: 6px; color: var(--muted); cursor: pointer;
    transition: all 0.15s ease;
}
.ks-topnav-link:hover { color: var(--text); background: rgba(255,255,255,0.05); }
.ks-topnav-right { display: flex; align-items: center; gap: 10px; }
.ks-engine-pill  {
    display: flex; align-items: center; gap: 6px;
    font-family: var(--mono); font-size: 0.68rem; font-weight: 600;
    color: var(--green); background: rgba(70,201,122,0.08);
    border: 1px solid rgba(70,201,122,0.2); padding: 4px 10px;
    border-radius: 20px;
}

/* ─── PAGE HEADER BLOCK ─── */
.ks-page-header {
    padding: 32px 0 24px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 28px;
}
.ks-page-eyebrow {
    font-family: var(--mono); font-size: 0.65rem; font-weight: 700;
    letter-spacing: 2px; text-transform: uppercase;
    color: var(--cyan); margin-bottom: 8px;
}
.ks-page-title {
    font-size: clamp(1.6rem, 3.5vw, 2.3rem);
    font-weight: 800; color: #fff;
    letter-spacing: -1px; margin-bottom: 8px; line-height: 1.1;
}
.ks-page-subtitle {
    font-size: 0.9rem; color: var(--muted);
    max-width: 600px; line-height: 1.7;
}

/* ─── CARDS ─── */
.ks-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 20px 22px;
}
.ks-card-hover {
    transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease;
}
.ks-card-hover:hover {
    transform: translateY(-3px);
    border-color: rgba(96,184,245,0.28);
    box-shadow: 0 10px 36px rgba(0,0,0,0.4);
}
.ks-card-title  { font-size: 0.95rem; font-weight: 700; color: #fff; margin-bottom: 6px; }
.ks-card-body   { font-size: 0.82rem; color: var(--muted); line-height: 1.65; }
.ks-icon-box {
    width: 46px; height: 46px; border-radius: 11px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px; margin-bottom: 14px;
}
.icon-cyan   { background: rgba(96,184,245,0.12); }
.icon-green  { background: rgba(70,201,122,0.12); }
.icon-amber  { background: rgba(240,149,58,0.12); }
.icon-purple { background: rgba(160,126,234,0.12); }
.icon-rose   { background: rgba(244,123,123,0.12); }
.icon-teal   { background: rgba(54,196,176,0.12); }

/* ─── KPI GRID ─── */
.ks-kpi-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(155px, 1fr));
    gap: 14px; margin-bottom: 26px;
}
.ks-kpi {
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 15px 17px;
    position: relative; overflow: hidden;
}
.ks-kpi::after {
    content: ''; position: absolute; left: 0; top: 0;
    width: 3px; height: 100%; border-radius: var(--radius) 0 0 var(--radius);
    background: var(--cyan);
}
.ks-kpi.green::after  { background: var(--green); }
.ks-kpi.amber::after  { background: var(--amber); }
.ks-kpi.rose::after   { background: var(--rose);  }
.ks-kpi.purple::after { background: var(--purple);}
.ks-kpi-label { font-family: var(--mono); font-size: 0.62rem; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; }
.ks-kpi-value { font-family: var(--mono); font-size: 1.45rem; font-weight: 700; color: #fff; line-height: 1.1; }
.ks-kpi-sub   { font-size: 0.7rem; color: var(--muted); margin-top: 3px; }

/* ─── CPU HUD ─── */
.ks-cpu-hud {
    background: #060f1e; border: 1px solid var(--border);
    border-radius: var(--radius); padding: 15px 18px; margin-bottom: 14px;
}
.ks-hud-title {
    font-family: var(--mono); font-size: 0.65rem; font-weight: 700;
    color: var(--muted); text-transform: uppercase; letter-spacing: 1px;
    display: flex; justify-content: space-between; align-items: center;
    border-bottom: 1px solid var(--border); padding-bottom: 8px; margin-bottom: 11px;
}
.ks-reg-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(115px, 1fr)); gap: 8px; }
.ks-reg-box  { background: rgba(0,0,0,0.3); border: 1px solid var(--border); border-radius: 5px; padding: 8px 11px; }
.ks-reg-name { font-family: var(--mono); font-size: 0.6rem; color: var(--cyan); font-weight: 700; margin-bottom: 2px; letter-spacing: 0.5px; }
.ks-reg-val  { font-family: var(--mono); font-size: 0.95rem; font-weight: 700; color: #fff; }

/* ─── TERMINAL / LOG ─── */
.ks-terminal {
    background: #02060e; border: 1px solid var(--border);
    border-radius: var(--radius); padding: 14px 16px;
    font-family: var(--mono); font-size: 0.74rem; color: #9eaec0;
    line-height: 1.65; max-height: 400px; overflow-y: auto;
}
.ks-log-line { display: flex; gap: 10px; padding: 2px 0; border-bottom: 1px solid rgba(255,255,255,0.03); }
.ks-log-t    { color: var(--cyan);  font-weight: 600; min-width: 70px; flex-shrink: 0; }
.ks-log-s    { color: var(--green); font-weight: 600; min-width: 90px; flex-shrink: 0; }
.ks-log-m    { color: #c0cad8; }

/* ─── MEMORY BAR ─── */
.ks-mem-bar-wrap {
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 14px 16px; margin-bottom: 14px;
}
.ks-mem-bar-label {
    font-family: var(--mono); font-size: 0.68rem; color: var(--muted);
    display: flex; justify-content: space-between; margin-bottom: 7px;
}
.ks-mem-bar  { display: flex; height: 42px; border-radius: 5px; overflow: hidden; border: 1px solid var(--border); }
.ks-mem-seg  {
    display: flex; align-items: center; justify-content: center;
    font-family: var(--mono); font-size: 0.65rem; font-weight: 700;
    color: #000; overflow: hidden; white-space: nowrap; padding: 0 4px;
    text-overflow: ellipsis; border-right: 1px solid rgba(0,0,0,0.25);
}

/* ─── ALGO CARDS ─── */
.ks-algo-card {
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 20px; height: 100%;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}
.ks-algo-card:hover { border-color: rgba(96,184,245,0.3); box-shadow: 0 8px 30px rgba(0,0,0,0.4); }
.ks-algo-name  { font-size: 1.1rem; font-weight: 800; color: #fff; margin-bottom: 4px; }
.ks-algo-full  { font-size: 0.75rem; color: var(--muted); margin-bottom: 10px; }
.ks-algo-badge {
    display: inline-block; font-family: var(--mono);
    font-size: 0.62rem; font-weight: 700; padding: 2px 8px;
    border-radius: 4px; margin-bottom: 12px;
}
.ks-algo-desc  { font-size: 0.8rem; color: var(--muted); line-height: 1.65; margin-bottom: 14px; }
.ks-algo-pros-cons { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 12px; }
.ks-algo-list-label { font-size: 0.65rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; }
.ks-algo-list li { font-size: 0.72rem; color: var(--muted); margin-bottom: 3px; }

/* ─── CONCEPT CARDS ─── */
.ks-concept {
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 22px 24px; margin-bottom: 14px;
    transition: border-color 0.2s ease;
}
.ks-concept:hover { border-color: rgba(96,184,245,0.25); }
.ks-concept-header { display: flex; align-items: flex-start; gap: 14px; margin-bottom: 12px; }
.ks-concept-num {
    width: 32px; height: 32px; border-radius: 8px; flex-shrink: 0;
    background: rgba(96,184,245,0.1); border: 1px solid rgba(96,184,245,0.2);
    display: flex; align-items: center; justify-content: center;
    font-family: var(--mono); font-size: 0.72rem; font-weight: 800; color: var(--cyan);
}
.ks-concept-title    { font-size: 1rem; font-weight: 700; color: #fff; margin-bottom: 2px; }
.ks-concept-subtitle { font-family: var(--mono); font-size: 0.7rem; color: var(--cyan); }
.ks-concept-body     { font-size: 0.82rem; color: var(--muted); line-height: 1.7; }
.ks-concept-bullets  { margin: 10px 0 0; padding-left: 18px; }
.ks-concept-bullets li { font-size: 0.8rem; color: var(--muted); margin-bottom: 3px; }

/* ─── SECTION HEADER ─── */
.ks-section-header { text-align: center; margin-bottom: 32px; }
.ks-section-eyebrow {
    font-family: var(--mono); font-size: 0.65rem; font-weight: 700;
    letter-spacing: 2px; text-transform: uppercase; color: var(--green); margin-bottom: 8px;
}
.ks-section-title {
    font-size: clamp(1.5rem, 3vw, 2.2rem); font-weight: 800; color: #fff;
    letter-spacing: -0.8px; margin-bottom: 8px; line-height: 1.15;
}
.ks-section-desc { font-size: 0.88rem; color: var(--muted); max-width: 520px; margin: 0 auto; line-height: 1.7; }

/* ─── STEP CARDS ─── */
.ks-step {
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 22px 18px; text-align: center;
}
.ks-step-num {
    width: 44px; height: 44px;
    background: linear-gradient(135deg, #2563eb, #0d9488);
    border-radius: 50%; display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem; font-weight: 800; color: #fff; margin: 0 auto 14px;
    box-shadow: 0 4px 14px rgba(37,99,235,0.4);
}
.ks-step-icon  { font-size: 1.5rem; margin-bottom: 10px; }
.ks-step-title { font-size: 0.9rem; font-weight: 700; color: #fff; margin-bottom: 7px; }
.ks-step-desc  { font-size: 0.78rem; color: var(--muted); line-height: 1.6; }

/* ─── HERO ─── */
.ks-hero { text-align: center; padding: 65px 20px 50px; max-width: 920px; margin: 0 auto; }
.ks-hero-pill {
    display: inline-flex; align-items: center; gap: 7px;
    font-family: var(--mono); font-size: 0.68rem; font-weight: 700;
    letter-spacing: 1.8px; text-transform: uppercase;
    color: var(--cyan); background: rgba(96,184,245,0.08);
    border: 1px solid rgba(96,184,245,0.2); padding: 5px 14px;
    border-radius: 20px; margin-bottom: 26px; cursor: default;
}
.ks-hero-title {
    font-size: clamp(2rem, 5.5vw, 3.8rem); font-weight: 900; color: #fff;
    line-height: 1.08; letter-spacing: -2px; margin-bottom: 20px;
}
.ks-hero-title .hl-cyan   { color: var(--cyan); }
.ks-hero-title .hl-green  { color: var(--green); }
.ks-hero-subtitle {
    font-size: 1.05rem; color: var(--muted); line-height: 1.75;
    max-width: 620px; margin: 0 auto 36px;
}
.ks-stats-row {
    display: grid; grid-template-columns: repeat(3, 1fr);
    gap: 20px; padding: 28px 0;
    border-top: 1px solid var(--border); border-bottom: 1px solid var(--border);
    margin: 32px 0;
}
.ks-stat-num  { font-size: 2.4rem; font-weight: 900; color: #fff; letter-spacing: -1.5px; line-height: 1; }
.ks-stat-num span { color: var(--cyan); }
.ks-stat-label { font-size: 0.8rem; color: var(--muted); margin-top: 5px; }

/* ─── VERDICT BOX ─── */
.ks-verdict {
    background: var(--card); border: 1px solid var(--border);
    border-left: 3px solid var(--green);
    border-radius: var(--radius); padding: 18px 22px; margin-top: 16px;
}
.ks-verdict-title  { font-size: 0.8rem; font-weight: 700; color: var(--green); margin-bottom: 10px; }
.ks-verdict-row    { font-family: var(--mono); font-size: 0.77rem; color: var(--muted); margin-bottom: 7px; display: flex; gap: 6px; align-items: flex-start; }
.ks-verdict-row em { font-style: normal; color: var(--text); font-weight: 600; }
.ks-verdict-row b  { font-style: normal; color: var(--cyan); }

/* ─── INFO BOX ─── */
.ks-info-box {
    background: rgba(96,184,245,0.05);
    border: 1px solid rgba(96,184,245,0.16);
    border-left: 3px solid var(--cyan);
    border-radius: var(--radius-sm); padding: 12px 16px;
    font-size: 0.82rem; color: var(--muted); line-height: 1.65;
}
.ks-info-box strong { color: var(--text); }

/* ─── DIVIDER ─── */
.ks-divider { border: none; border-top: 1px solid var(--border); margin: 28px 0; }

/* ─── STREAMLIT WIDGETS OVERRIDES ─── */
button[kind="primary"] {
    background: linear-gradient(135deg, #2563eb 0%, #0d9488 100%) !important;
    border: none !important; border-radius: 8px !important;
    font-family: var(--sans) !important; font-weight: 600 !important;
    box-shadow: 0 2px 14px rgba(37,99,235,0.3) !important;
    transition: all 0.2s ease !important;
    letter-spacing: 0.2px !important;
}
button[kind="primary"]:hover {
    box-shadow: 0 4px 22px rgba(37,99,235,0.5) !important;
    transform: translateY(-1px) !important;
}
button[kind="secondary"] {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
    font-family: var(--sans) !important;
    border-radius: 8px !important;
    transition: all 0.15s ease !important;
}
button[kind="secondary"]:hover {
    border-color: var(--cyan) !important;
    color: var(--cyan) !important;
}

div[data-baseweb="select"] > div {
    background-color: var(--card) !important;
    border-color: var(--border) !important;
    border-radius: 8px !important;
    font-family: var(--sans) !important;
}
div[data-baseweb="input"] > div {
    background-color: var(--card) !important;
    border-color: var(--border) !important;
    border-radius: 8px !important;
}
div[data-testid="stDataEditor"] {
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 4px; background: var(--card);
    padding: 5px; border-radius: var(--radius);
    border: 1px solid var(--border);
}
.stTabs [data-baseweb="tab"] {
    font-family: var(--sans); font-size: 0.78rem; font-weight: 600;
    padding: 7px 15px; border-radius: 7px; color: var(--muted);
    background: transparent; border: none; transition: all 0.15s ease;
}
.stTabs [aria-selected="true"] {
    background: rgba(96,184,245,0.1) !important;
    color: var(--cyan) !important;
    border: 1px solid rgba(96,184,245,0.2) !important;
}

div[data-testid="stSlider"] > div { accent-color: var(--cyan); }

/* ─── FOOTER ─── */
.ks-footer {
    background: var(--surface); border-top: 1px solid var(--border);
    padding: 24px 28px; margin-top: 60px;
}
.ks-footer-inner {
    display: flex; justify-content: space-between; align-items: center;
    flex-wrap: wrap; gap: 14px;
}
.ks-footer-brand { font-weight: 700; color: #fff; font-size: 0.9rem; }
.ks-footer-brand span { color: var(--cyan); }
.ks-footer-text  { font-size: 0.74rem; color: var(--muted); line-height: 1.6; margin-top: 3px; }

/* ─── SCROLLBAR ─── */
::-webkit-scrollbar       { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: var(--surface); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #2a3d58; }

/* ─── SIM PANEL HEADER ─── */
.ks-panel {
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 20px 24px; margin-bottom: 20px;
}
.ks-panel-title { font-size: 1.1rem; font-weight: 700; color: #fff; }
.ks-panel-desc  { font-size: 0.82rem; color: var(--muted); margin-top: 4px; }

/* ─── SECTION LABEL INLINE ─── */
.ks-label {
    font-family: var(--mono); font-size: 0.65rem; font-weight: 700;
    letter-spacing: 1.5px; text-transform: uppercase;
    color: var(--muted); margin-bottom: 8px;
}

/* ─── QUEUE BADGE ─── */
.ks-q-badge {
    display: inline-flex; align-items: center;
    font-family: var(--mono); font-size: 0.65rem; font-weight: 700;
    padding: 2px 8px; border-radius: 4px;
}
</style>
"""


def inject_styles() -> None:
    """Call this once at the top of every page to inject the global CSS."""
    st.markdown(_CSS, unsafe_allow_html=True)
