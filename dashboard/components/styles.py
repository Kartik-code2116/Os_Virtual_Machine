"""
styles.py
─────────
Theme-aware stylesheet for KernelSim.
Supports both Dark Mode (default) and Light Mode.
Call inject_styles(theme='dark'|'light') at the top of every run.
"""

import streamlit as st


def get_css(theme: str = "dark") -> str:
    is_dark = (theme == "dark")

    if is_dark:
        # Dark Theme Palette (Cyberpunk / Modern Deep Void)
        vars_css = """
        --void:         #04080f;
        --surface:      #0a111f;
        --card:         #0e1828;
        --card2:        #121d30;
        --border:       #1a2a40;
        --border-hover: #2d4160;
        --cyan:         #38bdf8;
        --green:        #10b981;
        --amber:        #f59e0b;
        --rose:         #f43f5e;
        --purple:       #818cf8;
        --teal:         #14b8a6;
        --text:         #f1f5f9;
        --text-heading: #ffffff;
        --muted:        #94a3b8;
        --track-bg:     #1a273c;
        --hud-bg:       #070c16;
        --topnav-bg:    rgba(10, 17, 31, 0.95);
        --sidebar-bg:   #080d18;
        --shadow:       0 8px 32px rgba(0,0,0,0.45);
        """
        bg_radial = """
        radial-gradient(ellipse at 12% 8%, rgba(56, 189, 248, 0.05) 0%, transparent 48%),
        radial-gradient(ellipse at 88% 88%, rgba(16, 185, 129, 0.04) 0%, transparent 48%)
        """
        btn_sec_bg = "#121d30"
        btn_sec_border = "#1f3048"
        btn_sec_text = "#e2e8f0"
        input_bg = "#0e1828"
        input_border = "#1a2a40"
        input_text = "#f1f5f9"
        tab_list_bg = "#0e1828"
        tab_selected_bg = "#18263d"
    else:
        # Light Theme Palette (Clean, High-Readability Studio Light)
        vars_css = """
        --void:         #f8fafc;
        --surface:      #ffffff;
        --card:         #ffffff;
        --card2:        #f1f5f9;
        --border:       #e2e8f0;
        --border-hover: #cbd5e1;
        --cyan:         #0284c7;
        --green:        #16a34a;
        --amber:        #d97706;
        --rose:         #e11d48;
        --purple:       #7c3aed;
        --teal:         #0d9488;
        --text:         #1e293b;
        --text-heading: #0f172a;
        --muted:        #64748b;
        --track-bg:     #e2e8f0;
        --hud-bg:       #f8fafc;
        --topnav-bg:    rgba(255, 255, 255, 0.95);
        --sidebar-bg:   #f8fafc;
        --shadow:       0 4px 20px rgba(0,0,0,0.06);
        """
        bg_radial = """
        radial-gradient(ellipse at 12% 8%, rgba(2, 132, 199, 0.04) 0%, transparent 48%),
        radial-gradient(ellipse at 88% 88%, rgba(22, 163, 74, 0.03) 0%, transparent 48%)
        """
        btn_sec_bg = "#ffffff"
        btn_sec_border = "#cbd5e1"
        btn_sec_text = "#1e293b"
        input_bg = "#ffffff"
        input_border = "#cbd5e1"
        input_text = "#0f172a"
        tab_list_bg = "#f1f5f9"
        tab_selected_bg = "#ffffff"

    return f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,300;0,14..32,400;0,14..32,500;0,14..32,600;0,14..32,700;0,14..32,800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

/* ─── RESET STREAMLIT CHROME ─── */
#MainMenu, footer, header                     {{ visibility: hidden !important; }}
div[data-testid="stToolbar"]                  {{ display: none !important; }}
div[data-testid="stDecoration"]               {{ display: none !important; }}
div[data-testid="stStatusWidget"]             {{ display: none !important; }}
.stAppDeployButton                            {{ display: none !important; }}
div[data-testid="stSidebarCollapseButton"]    {{ display: none !important; }}
section[data-testid="stSidebar"] > div:first-child {{ padding-top: 0 !important; }}
div[data-testid="stSidebarNav"]               {{ display: none !important; }}

/* ─── CSS VARIABLES ─── */
:root {{
    {vars_css}
    --mono:        'JetBrains Mono', monospace;
    --sans:        'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --radius:      12px;
    --radius-sm:   8px;
}}

/* ─── BASE APPS ─── */
html, body, [class*="css"], .stApp {{
    font-family: var(--sans) !important;
    color: var(--text) !important;
    background-color: var(--void) !important;
}}

.stApp {{
    background-image: {bg_radial};
}}

/* ─── SIDEBAR ─── */
[data-testid="stSidebar"] {{
    background: var(--sidebar-bg) !important;
    border-right: 1px solid var(--border) !important;
    width: 250px !important;
}}
[data-testid="stSidebar"] > div {{ padding: 0 !important; }}
[data-testid="stSidebar"] .stMarkdown {{ padding: 0 !important; }}
[data-testid="stSidebar"] .block-container {{ padding: 0 !important; }}

/* ─── SIDEBAR COMPONENTS ─── */
.ks-sidebar-brand {{
    display: flex; align-items: center; gap: 10px;
    padding: 20px 18px 16px; border-bottom: 1px solid var(--border);
}}
.ks-sidebar-logo {{
    width: 34px; height: 34px;
    background: linear-gradient(135deg, var(--cyan) 0%, var(--green) 100%);
    border-radius: 9px; display: flex; align-items: center; justify-content: center;
    font-family: var(--mono); font-size: 16px; font-weight: 800; color: #ffffff;
    flex-shrink: 0;
}}
.ks-sidebar-name  {{ font-size: 1.05rem; font-weight: 750; color: var(--text-heading); line-height: 1.1; }}
.ks-sidebar-name span {{ color: var(--cyan); }}
.ks-sidebar-tag   {{ font-size: 0.65rem; color: var(--muted); margin-top: 3px; }}

.ks-nav-label {{
    font-size: 0.62rem; font-weight: 750; letter-spacing: 1.6px;
    text-transform: uppercase; color: var(--muted); padding: 18px 18px 6px;
}}

[data-testid="stSidebar"] [role="radiogroup"] {{ gap: 4px; padding: 0 12px; }}
[data-testid="stSidebar"] [role="radiogroup"] label {{
    border: 1px solid transparent; border-radius: var(--radius-sm); padding: 8px 12px;
    transition: all .15s ease; cursor: pointer; color: var(--text) !important;
}}
[data-testid="stSidebar"] [role="radiogroup"] label:hover {{
    background: rgba(56, 189, 248, 0.08); border-color: rgba(56, 189, 248, 0.15);
}}
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {{
    background: rgba(56, 189, 248, 0.12); border-color: var(--cyan); font-weight: 600;
}}

.ks-status-pill {{
    display: inline-flex; align-items: center; gap: 6px;
    font-family: var(--mono); font-size: 0.64rem; font-weight: 600;
    padding: 3px 9px; border-radius: 20px; white-space: nowrap;
}}
.pill-green  {{ background: rgba(16, 185, 129, 0.1); color: var(--green); border: 1px solid rgba(16, 185, 129, 0.25); }}
.pill-cyan   {{ background: rgba(56, 189, 248, 0.1); color: var(--cyan);  border: 1px solid rgba(56, 189, 248, 0.25); }}
.pill-amber  {{ background: rgba(245, 158, 11, 0.1); color: var(--amber); border: 1px solid rgba(245, 158, 11, 0.25); }}
.pill-purple {{ background: rgba(129, 140, 248, 0.1);color: var(--purple);border: 1px solid rgba(129, 140, 248, 0.25); }}
.pill-rose   {{ background: rgba(244, 63, 94, 0.1); color: var(--rose);  border: 1px solid rgba(244, 63, 94, 0.25); }}

.pulse-dot {{
    width: 7px; height: 7px; border-radius: 50%;
    background: var(--green); box-shadow: 0 0 6px var(--green);
    animation: pulse 2s infinite;
}}
@keyframes pulse {{ 0%,100%{{opacity:1;transform:scale(1)}} 50%{{opacity:0.4;transform:scale(0.75)}} }}

.ks-sidebar-info {{
    margin: 14px 12px; padding: 13px 15px;
    background: var(--card2); border: 1px solid var(--border);
    border-radius: var(--radius-sm);
}}
.ks-sidebar-info-title {{ font-size: 0.74rem; font-weight: 700; color: var(--cyan); margin-bottom: 5px; }}
.ks-sidebar-info-body  {{ font-size: 0.72rem; color: var(--muted); line-height: 1.6; }}

/* ─── TOP NAV BAR ─── */
.ks-topnav-wrap {{
    background: var(--topnav-bg);
    border-bottom: 1px solid var(--border);
    padding: 10px 24px;
    margin-bottom: 16px;
    backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
    box-shadow: var(--shadow);
    border-radius: var(--radius);
}}
.ks-topnav-brand {{ display: flex; align-items: center; gap: 12px; }}
.ks-topnav-logo  {{
    width: 34px; height: 34px;
    background: linear-gradient(135deg, var(--cyan) 0%, var(--green) 100%);
    border-radius: 9px; display: flex; align-items: center; justify-content: center;
    font-family: var(--mono); font-size: 15px; font-weight: 800; color: #ffffff;
    flex-shrink: 0;
}}
.ks-topnav-name {{ font-size: 1.05rem; font-weight: 750; color: var(--text-heading); }}
.ks-topnav-name span {{ color: var(--cyan); }}
.ks-topnav-caption {{ font-size: 0.58rem; font-family: var(--mono); color: var(--muted); letter-spacing: 1.2px; font-weight: 700; }}
.ks-topnav-context {{ display: flex; flex-direction: column; gap: 2px; margin-left: 12px; border-left: 1px solid var(--border); padding-left: 12px; }}
.ks-topnav-kicker {{ font-size: 0.8rem; font-weight: 700; color: var(--text-heading); }}
.ks-engine-pill  {{
    display: flex; align-items: center; gap: 6px;
    font-family: var(--mono); font-size: 0.65rem; font-weight: 600;
    color: var(--green); background: rgba(16, 185, 129, 0.08);
    border: 1px solid rgba(16, 185, 129, 0.25); padding: 5px 12px;
    border-radius: 20px;
}}

/* ─── PAGE HEADER BLOCK ─── */
.ks-page-header {{
    padding: 24px 0 20px;
    border-bottom: 1px solid var(--border);
    margin-bottom: 24px;
}}
.ks-page-eyebrow {{
    font-family: var(--mono); font-size: 0.65rem; font-weight: 700;
    letter-spacing: 2px; text-transform: uppercase;
    color: var(--cyan); margin-bottom: 8px;
}}
.ks-page-title {{
    font-size: clamp(1.6rem, 3.5vw, 2.3rem);
    font-weight: 800; color: var(--text-heading);
    letter-spacing: -1px; margin-bottom: 8px; line-height: 1.15;
}}
.ks-page-subtitle {{
    font-size: 0.92rem; color: var(--muted);
    max-width: 620px; line-height: 1.7;
}}

/* ─── CARDS ─── */
.ks-card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 20px 22px;
    box-shadow: var(--shadow);
}}
.ks-card-hover {{
    transition: transform 0.18s ease, border-color 0.18s ease, box-shadow 0.18s ease;
}}
.ks-card-hover:hover {{
    transform: translateY(-3px);
    border-color: var(--border-hover);
    box-shadow: 0 12px 36px rgba(0,0,0,0.14);
}}
.ks-card-title  {{ font-size: 0.95rem; font-weight: 700; color: var(--text-heading); margin-bottom: 6px; }}
.ks-card-body   {{ font-size: 0.83rem; color: var(--muted); line-height: 1.65; }}
.ks-icon-box {{
    width: 44px; height: 44px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px; margin-bottom: 14px;
}}
.icon-cyan   {{ background: rgba(56, 189, 248, 0.12); }}
.icon-green  {{ background: rgba(16, 185, 129, 0.12); }}
.icon-amber  {{ background: rgba(245, 158, 11, 0.12); }}
.icon-purple {{ background: rgba(129, 140, 248, 0.12); }}
.icon-rose   {{ background: rgba(244, 63, 94, 0.12); }}
.icon-teal   {{ background: rgba(20, 184, 166, 0.12); }}

/* ─── KPI GRID ─── */
.ks-kpi-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(155px, 1fr));
    gap: 14px; margin-bottom: 24px;
}}
.ks-kpi {{
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 15px 17px;
    position: relative; overflow: hidden;
    box-shadow: var(--shadow);
}}
.ks-kpi::after {{
    content: ''; position: absolute; left: 0; top: 0;
    width: 3.5px; height: 100%; border-radius: var(--radius) 0 0 var(--radius);
    background: var(--cyan);
}}
.ks-kpi.green::after  {{ background: var(--green); }}
.ks-kpi.amber::after  {{ background: var(--amber); }}
.ks-kpi.rose::after   {{ background: var(--rose);  }}
.ks-kpi.purple::after {{ background: var(--purple);}}
.ks-kpi-label {{ font-family: var(--mono); font-size: 0.62rem; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; }}
.ks-kpi-value {{ font-family: var(--mono); font-size: 1.45rem; font-weight: 700; color: var(--text-heading); line-height: 1.1; }}
.ks-kpi-sub   {{ font-size: 0.72rem; color: var(--muted); margin-top: 4px; }}

/* ─── CPU HUD ─── */
.ks-cpu-hud {{
    background: var(--hud-bg); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 15px 18px; margin-bottom: 14px;
    box-shadow: var(--shadow);
}}
.ks-hud-title {{
    font-family: var(--mono); font-size: 0.66rem; font-weight: 700;
    color: var(--muted); text-transform: uppercase; letter-spacing: 1px;
    display: flex; justify-content: space-between; align-items: center;
    border-bottom: 1px solid var(--border); padding-bottom: 8px; margin-bottom: 11px;
}}
.ks-reg-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(115px, 1fr)); gap: 8px; }}
.ks-reg-box  {{ background: var(--card2); border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 8px 11px; }}
.ks-reg-name {{ font-family: var(--mono); font-size: 0.62rem; color: var(--cyan); font-weight: 700; margin-bottom: 2px; letter-spacing: 0.5px; }}
.ks-reg-val  {{ font-family: var(--mono); font-size: 0.95rem; font-weight: 700; color: var(--text-heading); }}

/* ─── TERMINAL / LOG ─── */
.ks-terminal {{
    background: var(--hud-bg); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 14px 16px;
    font-family: var(--mono); font-size: 0.75rem; color: var(--text);
    line-height: 1.65; max-height: 400px; overflow-y: auto;
    box-shadow: var(--shadow);
}}
.ks-log-line {{ display: flex; gap: 10px; padding: 2.5px 0; border-bottom: 1px solid rgba(125,125,125,0.08); }}
.ks-log-t    {{ color: var(--cyan);  font-weight: 600; min-width: 70px; flex-shrink: 0; }}
.ks-log-s    {{ color: var(--green); font-weight: 600; min-width: 90px; flex-shrink: 0; }}
.ks-log-m    {{ color: var(--text); }}

/* ─── MEMORY BAR ─── */
.ks-mem-bar-wrap {{
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 14px 16px; margin-bottom: 14px;
    box-shadow: var(--shadow);
}}
.ks-mem-bar-label {{
    font-family: var(--mono); font-size: 0.68rem; color: var(--muted);
    display: flex; justify-content: space-between; margin-bottom: 7px;
}}
.ks-mem-bar  {{ display: flex; height: 42px; border-radius: 6px; overflow: hidden; border: 1px solid var(--border); }}
.ks-mem-seg  {{
    display: flex; align-items: center; justify-content: center;
    font-family: var(--mono); font-size: 0.65rem; font-weight: 700;
    color: #ffffff; overflow: hidden; white-space: nowrap; padding: 0 4px;
    text-overflow: ellipsis; border-right: 1px solid rgba(0,0,0,0.25);
}}

/* ─── CONCEPT CARDS ─── */
.ks-concept {{
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 22px 24px; margin-bottom: 14px;
    box-shadow: var(--shadow); transition: border-color 0.2s ease;
}}
.ks-concept:hover {{ border-color: var(--border-hover); }}
.ks-concept-header {{ display: flex; align-items: flex-start; gap: 14px; margin-bottom: 12px; }}
.ks-concept-num {{
    width: 32px; height: 32px; border-radius: 8px; flex-shrink: 0;
    background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.25);
    display: flex; align-items: center; justify-content: center;
    font-family: var(--mono); font-size: 0.72rem; font-weight: 800; color: var(--cyan);
}}
.ks-concept-title    {{ font-size: 1rem; font-weight: 700; color: var(--text-heading); margin-bottom: 2px; }}
.ks-concept-subtitle {{ font-family: var(--mono); font-size: 0.7rem; color: var(--cyan); }}
.ks-concept-body     {{ font-size: 0.83rem; color: var(--muted); line-height: 1.7; }}
.ks-concept-bullets  {{ margin: 10px 0 0; padding-left: 18px; }}
.ks-concept-bullets li {{ font-size: 0.81rem; color: var(--muted); margin-bottom: 4px; }}

/* ─── SECTION HEADER ─── */
.ks-section-header {{ text-align: center; margin-bottom: 32px; }}
.ks-section-eyebrow {{
    font-family: var(--mono); font-size: 0.65rem; font-weight: 700;
    letter-spacing: 2px; text-transform: uppercase; color: var(--green); margin-bottom: 8px;
}}
.ks-section-title {{
    font-size: clamp(1.5rem, 3vw, 2.2rem); font-weight: 800; color: var(--text-heading);
    letter-spacing: -0.8px; margin-bottom: 8px; line-height: 1.15;
}}
.ks-section-desc {{ font-size: 0.88rem; color: var(--muted); max-width: 520px; margin: 0 auto; line-height: 1.7; }}

/* ─── STEP CARDS ─── */
.ks-step {{
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 22px 18px; text-align: center;
    box-shadow: var(--shadow);
}}
.ks-step-num {{
    width: 44px; height: 44px;
    background: linear-gradient(135deg, var(--cyan), var(--teal));
    border-radius: 50%; display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem; font-weight: 800; color: #ffffff; margin: 0 auto 14px;
    box-shadow: 0 4px 14px rgba(56,189,248,0.3);
}}
.ks-step-icon  {{ font-size: 1.5rem; margin-bottom: 10px; }}
.ks-step-title {{ font-size: 0.92rem; font-weight: 700; color: var(--text-heading); margin-bottom: 7px; }}
.ks-step-desc  {{ font-size: 0.8rem; color: var(--muted); line-height: 1.6; }}

/* ─── HERO & LANDING ─── */
.ks-welcome {{ display: flex; align-items: center; gap: 8px; font-size: 0.65rem; font-weight: 750; letter-spacing: 1.5px; color: var(--cyan); }}
.ks-welcome-mark {{ width: 8px; height: 8px; border-radius: 50%; background: var(--cyan); box-shadow: 0 0 8px var(--cyan); }}
.ks-home-title {{
    font-size: clamp(2.4rem, 4.5vw, 3.8rem); font-weight: 850;
    color: var(--text-heading); letter-spacing: -1.8px; line-height: 1.1; margin: 16px 0 16px;
}}
.ks-home-copy {{ font-size: 1rem; color: var(--muted); line-height: 1.75; margin-bottom: 24px; max-width: 560px; }}
.ks-hero-assurance {{ margin-top: 14px; color: var(--muted); font-size: 0.72rem; }}
.ks-hero-assurance span {{ color: var(--cyan); }}

.ks-visual-card {{
    background: var(--card); border: 1px solid var(--border);
    border-radius: 18px; padding: 22px 24px; box-shadow: var(--shadow);
}}
.ks-visual-top {{ display: flex; justify-content: space-between; font-size: 0.65rem; font-family: var(--mono); color: var(--muted); }}
.ks-live-dot {{ width: 7px; height: 7px; border-radius: 50%; background: var(--green); display: inline-block; margin-right: 5px; }}
.ks-visual-title {{ font-size: 1.18rem; font-weight: 750; color: var(--text-heading); margin-top: 18px; }}
.ks-visual-subtitle {{ font-size: 0.76rem; color: var(--muted); margin: 3px 0 16px; }}
.ks-process-row {{ display: grid; grid-template-columns: 28px 1fr 54px; align-items: center; gap: 10px; margin: 12px 0; }}
.ks-process-id {{ font-family: var(--mono); font-size: 0.74rem; font-weight: 700; color: var(--text-heading); }}
.ks-process-track {{ height: 8px; border-radius: 6px; background: var(--track-bg); overflow: hidden; }}
.ks-track-fill {{ display: block; height: 100%; border-radius: 6px; }}
.fill-mint {{ background: var(--green); }}
.fill-blue {{ background: var(--cyan); }}
.fill-peach {{ background: var(--amber); }}
.ks-process-state {{ font-size: 0.55rem; font-family: var(--mono); font-weight: 700; text-align: right; }}
.state-running {{ color: var(--green); }}
.state-ready {{ color: var(--cyan); }}
.state-waiting {{ color: var(--amber); }}
.ks-visual-callout {{ margin-top: 18px; padding: 10px 12px; border-radius: 8px; background: var(--card2); font-size: 0.72rem; color: var(--text); }}
.ks-visual-footer {{ display: flex; justify-content: space-between; margin-top: 14px; padding-top: 12px; border-top: 1px solid var(--border); font-size: 0.6rem; font-family: var(--mono); color: var(--muted); }}

.ks-path-card {{
    background: var(--card); border: 1px solid var(--border);
    border-radius: var(--radius); padding: 20px; box-shadow: var(--shadow);
    height: 180px; display: flex; flex-direction: column; justify-content: space-between;
}}
.ks-path-card-top {{ display: flex; justify-content: space-between; align-items: center; }}
.ks-path-number {{ font-family: var(--mono); font-size: 0.68rem; font-weight: 700; color: var(--cyan); }}
.ks-path-icon {{ width: 34px; height: 34px; border-radius: 8px; background: var(--card2); display: flex; align-items: center; justify-content: center; font-size: 1rem; }}
.ks-path-title {{ font-size: 0.95rem; font-weight: 700; color: var(--text-heading); margin-top: 8px; }}
.ks-path-copy {{ font-size: 0.78rem; color: var(--muted); line-height: 1.6; }}

/* ─── VERDICT BOX ─── */
.ks-verdict {{
    background: var(--card); border: 1px solid var(--border);
    border-left: 3.5px solid var(--green);
    border-radius: var(--radius); padding: 18px 22px; margin-top: 16px;
    box-shadow: var(--shadow);
}}
.ks-verdict-title  {{ font-size: 0.82rem; font-weight: 750; color: var(--green); margin-bottom: 10px; }}
.ks-verdict-row    {{ font-family: var(--mono); font-size: 0.78rem; color: var(--muted); margin-bottom: 7px; display: flex; gap: 6px; align-items: flex-start; }}
.ks-verdict-row em {{ font-style: normal; color: var(--text); font-weight: 600; }}
.ks-verdict-row b  {{ font-style: normal; color: var(--cyan); }}

/* ─── DIVIDER ─── */
.ks-divider {{ border: none; border-top: 1px solid var(--border); margin: 28px 0; }}

/* ─── STREAMLIT WIDGETS OVERRIDES ─── */
button[kind="primary"] {{
    background: linear-gradient(135deg, var(--cyan) 0%, var(--teal) 100%) !important;
    color: #ffffff !important;
    border: none !important; border-radius: var(--radius-sm) !important;
    font-family: var(--sans) !important; font-weight: 650 !important;
    box-shadow: 0 3px 14px rgba(56, 189, 248, 0.28) !important;
    transition: all 0.2s ease !important;
}}
button[kind="primary"]:hover {{
    box-shadow: 0 5px 22px rgba(56, 189, 248, 0.45) !important;
    transform: translateY(-1px) !important;
}}
button[kind="secondary"] {{
    background: {btn_sec_bg} !important;
    border: 1px solid {btn_sec_border} !important;
    color: {btn_sec_text} !important;
    font-family: var(--sans) !important; font-weight: 550 !important;
    border-radius: var(--radius-sm) !important;
    transition: all 0.15s ease !important;
}}
button[kind="secondary"]:hover {{
    border-color: var(--cyan) !important;
    color: var(--cyan) !important;
}}

div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {{
    background-color: {input_bg} !important;
    border-color: {input_border} !important;
    color: {input_text} !important;
    border-radius: var(--radius-sm) !important;
}}
div[data-testid="stDataEditor"] {{
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
}}

.stTabs [data-baseweb="tab-list"] {{
    gap: 4px; background: {tab_list_bg};
    padding: 5px; border-radius: var(--radius);
    border: 1px solid var(--border);
}}
.stTabs [data-baseweb="tab"] {{
    font-family: var(--sans); font-size: 0.78rem; font-weight: 600;
    padding: 7px 15px; border-radius: var(--radius-sm); color: var(--muted);
    background: transparent; border: none; transition: all 0.15s ease;
}}
.stTabs [aria-selected="true"] {{
    background: {tab_selected_bg} !important;
    color: var(--cyan) !important;
    border: 1px solid var(--border) !important;
}}

/* ─── FOOTER ─── */
.ks-footer {{
    background: var(--surface); border-top: 1px solid var(--border);
    padding: 24px 28px; margin-top: 60px;
}}
.ks-footer-inner {{
    display: flex; justify-content: space-between; align-items: center;
    flex-wrap: wrap; gap: 14px;
}}
.ks-footer-brand {{ font-weight: 750; color: var(--text-heading); font-size: 0.92rem; }}
.ks-footer-brand span {{ color: var(--cyan); }}
.ks-footer-text  {{ font-size: 0.76rem; color: var(--muted); line-height: 1.6; margin-top: 3px; }}

.ks-label {{
    font-family: var(--mono); font-size: 0.65rem; font-weight: 700;
    letter-spacing: 1.5px; text-transform: uppercase;
    color: var(--muted); margin-bottom: 8px;
}}
</style>
"""


def inject_styles(theme: str = "dark") -> None:
    """Call this once at the top of every run to inject the theme-appropriate CSS."""
    st.markdown(get_css(theme), unsafe_allow_html=True)
