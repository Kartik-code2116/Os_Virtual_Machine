"""
styles.py
─────────
Theme-aware stylesheet for KernelSim.
Supports:
  - 'premium': The original, soft sage/forest human-made theme (DEFAULT)
  - 'dark': Deep cyberpunk/OLED dark void theme
"""

import streamlit as st


def get_css(theme: str = "premium") -> str:
    is_premium = (theme == "premium")

    if is_premium:
        # ─── PREMIUM SAGE / FOREST THEME (DEFAULT) ───
        vars_css = """
        --void:         #18261f;
        --surface:      #141e19;
        --card:         #1a2721;
        --card2:        #202f26;
        --border:       #304036;
        --border-hover: #607b66;
        --cyan:         #a8d5c1;
        --green:        #a8d5c1;
        --amber:        #e5bc83;
        --rose:         #e49b8a;
        --purple:       #c0b1dc;
        --teal:         #89c7b8;
        --text:         #edf2ed;
        --text-heading: #edf2ed;
        --muted:        #9aa99f;
        --track-bg:     #33443a;
        --hud-bg:       #111a15;
        --topnav-bg:    rgba(23, 35, 30, 0.94);
        --sidebar-bg:   #141e19;
        --shadow:       0 12px 36px rgba(0,0,0,0.18);
        """
        bg_radial = """
        radial-gradient(ellipse at 80% 0%, rgba(119,164,137,0.09), transparent 40%),
        radial-gradient(ellipse at 0% 50%, rgba(103,137,115,0.06), transparent 38%)
        """
        btn_prim_bg = "#bdd8c5"
        btn_prim_color = "#18251d"
        btn_prim_hover = "#cce2d1"
        btn_prim_shadow = "rgba(117,157,126,0.22)"
        btn_sec_bg = "#202e26"
        btn_sec_border = "#3b4b40"
        btn_sec_color = "#d4ded6"
        btn_sec_hover_border = "#849b88"
        btn_sec_hover_color = "#e7eee8"
        input_bg = "#202d26"
        input_border = "#3b4a40"
        input_color = "#edf2ed"
        tab_list_bg = "#1b2821"
        tab_list_border = "#344238"
        tab_sel_bg = "#293b30"
        tab_sel_color = "#c3d9c8"
        tab_sel_border = "#405846"
        reg_box_bg = "rgba(0,0,0,0.16)"
        reg_box_border = "#2e3d33"
        visual_card_bg = "linear-gradient(145deg, #25372c, #1b2922 72%)"
        visual_card_border = "#3a5141"
        path_card_bg = "linear-gradient(145deg, #1d2a23, #19251f)"
        step_num_bg = "#526d59"
        welcome_pill_bg = "#203027"
        welcome_pill_border = "#3b5041"
        welcome_pill_color = "#c3d9c8"
        engine_pill_bg = "#23342a"
        engine_pill_border = "#3a5040"
        engine_pill_color = "#bdd8c5"
        pulse_color = "#9bc9a7"
        sidebar_logo_bg = "#bdd8c5"
        sidebar_logo_color = "#19261f"
    else:
        # ─── DEEP CYBER DARK THEME ───
        vars_css = """
        --void:         #04080f;
        --surface:      #070c16;
        --card:         #0b121f;
        --card2:        #0e1828;
        --border:       #172338;
        --border-hover: #2d4568;
        --cyan:         #38bdf8;
        --green:        #10b981;
        --amber:        #f59e0b;
        --rose:         #f43f5e;
        --purple:       #818cf8;
        --teal:         #14b8a6;
        --text:         #f1f5f9;
        --text-heading: #ffffff;
        --muted:        #8899ac;
        --track-bg:     #172438;
        --hud-bg:       #050912;
        --topnav-bg:    rgba(7, 12, 22, 0.95);
        --sidebar-bg:   #070c16;
        --shadow:       0 12px 36px rgba(0,0,0,0.45);
        """
        bg_radial = """
        radial-gradient(ellipse at 12% 8%, rgba(56, 189, 248, 0.06) 0%, transparent 48%),
        radial-gradient(ellipse at 88% 88%, rgba(16, 185, 129, 0.05) 0%, transparent 48%)
        """
        btn_prim_bg = "linear-gradient(135deg, #0284c7 0%, #0f766e 100%)"
        btn_prim_color = "#ffffff"
        btn_prim_hover = "linear-gradient(135deg, #0369a1 0%, #0d9488 100%)"
        btn_prim_shadow = "rgba(56, 189, 248, 0.35)"
        btn_sec_bg = "#0e1828"
        btn_sec_border = "#1e304b"
        btn_sec_color = "#d8e2ec"
        btn_sec_hover_border = "#38bdf8"
        btn_sec_hover_color = "#38bdf8"
        input_bg = "#0e1828"
        input_border = "#1a2a40"
        input_color = "#f1f5f9"
        tab_list_bg = "#0b121f"
        tab_list_border = "#172338"
        tab_sel_bg = "#16243b"
        tab_sel_color = "#38bdf8"
        tab_sel_border = "#233857"
        reg_box_bg = "rgba(0,0,0,0.25)"
        reg_box_border = "#1a2a40"
        visual_card_bg = "linear-gradient(145deg, #0e1828, #070c16 75%)"
        visual_card_border = "#1e304b"
        path_card_bg = "linear-gradient(145deg, #0e1828, #0a111e)"
        step_num_bg = "#0284c7"
        welcome_pill_bg = "#0e1828"
        welcome_pill_border = "#1e304b"
        welcome_pill_color = "#38bdf8"
        engine_pill_bg = "#0b1a20"
        engine_pill_border = "#13383a"
        engine_pill_color = "#10b981"
        pulse_color = "#10b981"
        sidebar_logo_bg = "#38bdf8"
        sidebar_logo_color = "#04080f"

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
    --radius:      14px;
    --radius-sm:   10px;
}}

/* ─── BASE ─── */
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
    padding: 22px 19px 18px; border-bottom: 1px solid var(--border);
}}
.ks-sidebar-logo {{
    width: 34px; height: 34px; border-radius: 11px;
    background: {sidebar_logo_bg}; color: {sidebar_logo_color};
    display: flex; align-items: center; justify-content: center;
    font-family: var(--mono); font-size: 15px; font-weight: 800;
    flex-shrink: 0;
}}
.ks-sidebar-name  {{ font-size: 1.05rem; font-weight: 750; color: var(--text-heading); line-height: 1.1; }}
.ks-sidebar-name span {{ color: var(--cyan); }}
.ks-sidebar-tag   {{ font-size: 0.68rem; color: var(--muted); margin-top: 3px; }}

.ks-nav-label {{
    font-size: 0.62rem; font-weight: 750; letter-spacing: 1.4px;
    text-transform: uppercase; color: var(--muted); padding: 18px 19px 7px;
}}

[data-testid="stSidebar"] [role="radiogroup"] {{ gap: 4px; padding: 0 10px; }}
[data-testid="stSidebar"] [role="radiogroup"] label {{
    border: 1px solid transparent; border-radius: 9px; padding: 7px 11px;
    transition: all .15s ease; cursor: pointer; color: var(--text) !important;
}}
[data-testid="stSidebar"] [role="radiogroup"] label:hover {{
    background: var(--card2);
}}
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {{
    background: var(--card2); border-color: var(--border-hover); font-weight: 600;
}}

.ks-sidebar-note {{
    margin: 24px 14px 16px; padding: 15px 16px;
    background: var(--card2); border: 1px solid var(--border);
    border-radius: 13px;
}}
.ks-sidebar-note-icon {{ color: var(--cyan); font-size: 1rem; margin-bottom: 8px; }}
.ks-sidebar-info-title {{ color: var(--text-heading); font-size: 0.78rem; font-weight: 700; margin-bottom: 5px; }}
.ks-sidebar-info-body  {{ color: var(--muted); line-height: 1.65; font-size: 0.73rem; }}

.ks-sidebar-engine {{
    margin: 0 17px; display: flex; gap: 9px; align-items: center;
    color: var(--muted); font-size: 0.68rem; line-height: 1.55;
}}
.ks-sidebar-engine b {{ color: var(--text-heading); font-weight: 600; }}
.ks-sidebar-engine-dot, .ks-live-dot {{
    width: 8px; height: 8px; border-radius: 50%;
    background: {pulse_color}; box-shadow: 0 0 0 4px rgba(168,213,193,.15);
    flex: 0 0 auto;
}}

/* ─── TOP NAV BAR ─── */
.ks-topnav-brand {{ display: flex; align-items: center; gap: 11px; }}
.ks-topnav-logo  {{
    width: 34px; height: 34px; border-radius: 10px;
    background: {sidebar_logo_bg}; color: {sidebar_logo_color};
    display: flex; align-items: center; justify-content: center;
    font-family: var(--mono); font-size: 15px; font-weight: 800;
    flex-shrink: 0;
}}
.ks-topnav-name {{ font-size: 1rem; font-weight: 750; color: var(--text-heading); }}
.ks-topnav-name span {{ color: var(--cyan); }}
.ks-topnav-caption {{ font-size: 0.55rem; font-family: var(--mono); color: var(--muted); letter-spacing: 1.4px; margin-top: 2px; font-weight: 700; }}
.ks-topnav-context {{ display: flex; flex-direction: column; gap: 2px; margin-left: 12px; border-left: 1px solid var(--border); padding-left: 12px; }}
.ks-topnav-kicker {{ font-size: 0.79rem; font-weight: 650; color: var(--text-heading); }}

.ks-engine-pill {{
    display: inline-flex; align-items: center; gap: 6px;
    font-family: var(--mono); font-size: 0.62rem; font-weight: 600;
    color: {engine_pill_color}; background: {engine_pill_bg};
    border: 1px solid {engine_pill_border}; padding: 5px 12px;
    border-radius: 20px;
}}
.pulse-dot {{
    width: 7px; height: 7px; border-radius: 50%;
    background: {pulse_color}; box-shadow: 0 0 6px rgba(168,213,193,.5);
    animation: pulse 2s infinite;
}}
@keyframes pulse {{ 0%,100%{{opacity:1;transform:scale(1)}} 50%{{opacity:0.4;transform:scale(0.75)}} }}

/* ─── CARDS & TILES ─── */
.ks-card, .ks-kpi, .ks-algo-card, .ks-concept, .ks-step, .ks-panel {{
    background: var(--card); border: 1px solid var(--border);
    border-radius: 13px; box-shadow: var(--shadow);
}}
.ks-card-hover:hover, .ks-algo-card:hover {{
    border-color: var(--border-hover);
    box-shadow: 0 12px 30px rgba(0,0,0,.22);
    transform: translateY(-2px);
    transition: all .2s ease;
}}
.ks-card {{ padding: 20px 22px; }}
.ks-card-title, .ks-algo-name, .ks-concept-title, .ks-step-title, .ks-panel-title {{
    color: var(--text-heading); font-size: 0.95rem; font-weight: 700; margin-bottom: 6px;
}}
.ks-card-body, .ks-algo-desc, .ks-concept-body, .ks-concept-bullets li, .ks-step-desc {{
    color: var(--muted); font-size: 0.83rem; line-height: 1.65;
}}
.ks-icon-box {{
    width: 44px; height: 44px; border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 20px; margin-bottom: 14px;
}}
.icon-cyan   {{ background: rgba(168, 213, 193, 0.15); }}
.icon-green  {{ background: rgba(168, 213, 193, 0.15); }}
.icon-amber  {{ background: rgba(229, 188, 131, 0.15); }}
.icon-purple {{ background: rgba(192, 177, 220, 0.15); }}
.icon-rose   {{ background: rgba(228, 155, 138, 0.15); }}
.icon-teal   {{ background: rgba(137, 199, 184, 0.15); }}

/* ─── KPI METRICS ─── */
.ks-kpi-grid {{
    display: grid; grid-template-columns: repeat(auto-fit, minmax(155px, 1fr));
    gap: 13px; margin-bottom: 24px;
}}
.ks-kpi {{
    padding: 15px 17px; position: relative; overflow: hidden;
}}
.ks-kpi::after {{
    content: ''; position: absolute; left: 0; top: 0;
    width: 3.5px; height: 100%; border-radius: 13px 0 0 13px;
    background: var(--cyan);
}}
.ks-kpi.green::after  {{ background: var(--green); }}
.ks-kpi.amber::after  {{ background: var(--amber); }}
.ks-kpi.rose::after   {{ background: var(--rose);  }}
.ks-kpi.purple::after {{ background: var(--purple);}}
.ks-kpi-label {{ font-family: var(--mono); font-size: 0.62rem; font-weight: 700; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 5px; }}
.ks-kpi-value {{ font-family: var(--mono); font-size: 1.45rem; font-weight: 700; color: var(--text-heading); line-height: 1.1; }}
.ks-kpi-sub   {{ font-size: 0.72rem; color: var(--muted); margin-top: 4px; }}

/* ─── CPU HUD & REGISTERS ─── */
.ks-cpu-hud, .ks-terminal {{
    background: var(--hud-bg); border: 1px solid var(--border);
    border-radius: 13px;
}}
.ks-cpu-hud {{ padding: 15px 18px; margin-bottom: 14px; }}
.ks-hud-title {{
    font-family: var(--mono); font-size: 0.66rem; font-weight: 700;
    color: var(--muted); text-transform: uppercase; letter-spacing: 1px;
    display: flex; justify-content: space-between; align-items: center;
    border-bottom: 1px solid var(--border); padding-bottom: 8px; margin-bottom: 11px;
}}
.ks-reg-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(115px, 1fr)); gap: 8px; }}
.ks-reg-box  {{ background: {reg_box_bg}; border: 1px solid {reg_box_border}; border-radius: 8px; padding: 8px 11px; }}
.ks-reg-name {{ font-family: var(--mono); font-size: 0.62rem; color: var(--cyan); font-weight: 700; margin-bottom: 2px; letter-spacing: 0.5px; }}
.ks-reg-val  {{ font-family: var(--mono); font-size: 0.95rem; font-weight: 700; color: var(--text-heading); }}

/* ─── TERMINAL / LOG ─── */
.ks-terminal {{
    padding: 14px 16px; font-family: var(--mono); font-size: 0.74rem; color: var(--text);
    line-height: 1.65; max-height: 400px; overflow-y: auto;
}}
.ks-log-line {{ display: flex; gap: 10px; padding: 2.5px 0; border-bottom: 1px solid rgba(125,125,125,0.08); }}
.ks-log-t    {{ color: var(--cyan);  font-weight: 600; min-width: 70px; flex-shrink: 0; }}
.ks-log-s    {{ color: var(--green); font-weight: 600; min-width: 90px; flex-shrink: 0; }}
.ks-log-m    {{ color: var(--text); }}

/* ─── MEMORY BAR ─── */
.ks-mem-bar-wrap {{
    background: var(--card); border: 1px solid var(--border);
    border-radius: 13px; padding: 14px 16px; margin-bottom: 14px;
}}
.ks-mem-bar-label {{
    font-family: var(--mono); font-size: 0.68rem; color: var(--muted);
    display: flex; justify-content: space-between; margin-bottom: 7px;
}}
.ks-mem-bar  {{ display: flex; height: 42px; border-radius: 6px; overflow: hidden; border: 1px solid var(--border); }}
.ks-mem-seg  {{
    display: flex; align-items: center; justify-content: center;
    font-family: var(--mono); font-size: 0.65rem; font-weight: 700;
    color: #141e19; overflow: hidden; white-space: nowrap; padding: 0 4px;
    text-overflow: ellipsis; border-right: 1px solid rgba(0,0,0,0.25);
}}

/* ─── STATUS PILLS ─── */
.ks-status-pill {{
    display: inline-flex; align-items: center; gap: 6px;
    font-family: var(--mono); font-size: 0.64rem; font-weight: 600;
    padding: 3px 9px; border-radius: 20px; white-space: nowrap;
}}
.pill-green  {{ background: rgba(168, 213, 193, 0.12); color: var(--green); border: 1px solid rgba(168, 213, 193, 0.25); }}
.pill-cyan   {{ background: rgba(168, 213, 193, 0.12); color: var(--cyan);  border: 1px solid rgba(168, 213, 193, 0.25); }}
.pill-amber  {{ background: rgba(229, 188, 131, 0.12); color: var(--amber); border: 1px solid rgba(229, 188, 131, 0.25); }}
.pill-purple {{ background: rgba(192, 177, 220, 0.12); color: var(--purple);border: 1px solid rgba(192, 177, 220, 0.25); }}
.pill-rose   {{ background: rgba(228, 155, 138, 0.12); color: var(--rose);  border: 1px solid rgba(228, 155, 138, 0.25); }}

/* ─── CONCEPT CARDS ─── */
.ks-concept {{
    padding: 22px 24px; margin-bottom: 14px;
    transition: border-color 0.2s ease;
}}
.ks-concept-header {{ display: flex; align-items: flex-start; gap: 14px; margin-bottom: 12px; }}
.ks-concept-num {{
    width: 32px; height: 32px; border-radius: 8px; flex-shrink: 0;
    background: rgba(168, 213, 193, 0.12); border: 1px solid rgba(168, 213, 193, 0.25);
    display: flex; align-items: center; justify-content: center;
    font-family: var(--mono); font-size: 0.72rem; font-weight: 800; color: var(--cyan);
}}
.ks-concept-title    {{ font-size: 1rem; font-weight: 700; color: var(--text-heading); margin-bottom: 2px; }}
.ks-concept-subtitle {{ font-family: var(--mono); font-size: 0.7rem; color: var(--cyan); }}
.ks-concept-body     {{ font-size: 0.83rem; color: var(--muted); line-height: 1.7; }}
.ks-concept-bullets  {{ margin: 10px 0 0; padding-left: 18px; }}
.ks-concept-bullets li {{ font-size: 0.81rem; color: var(--muted); margin-bottom: 4px; }}

/* ─── STEP CARDS ─── */
.ks-step {{ padding: 22px 18px; text-align: center; }}
.ks-step-num {{
    width: 44px; height: 44px;
    background: {step_num_bg};
    border-radius: 50%; display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem; font-weight: 800; color: #ffffff; margin: 0 auto 14px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.2);
}}
.ks-step-icon  {{ font-size: 1.5rem; margin-bottom: 10px; }}
.ks-step-title {{ font-size: 0.92rem; font-weight: 700; color: var(--text-heading); margin-bottom: 7px; }}
.ks-step-desc  {{ font-size: 0.8rem; color: var(--muted); line-height: 1.6; }}

/* ─── HERO & LANDING ─── */
.ks-welcome {{ display: flex; align-items: center; gap: 8px; font-size: 0.65rem; font-weight: 750; letter-spacing: 1.5px; color: var(--cyan); }}
.ks-welcome-mark {{ width: 8px; height: 8px; border-radius: 50%; background: var(--cyan); box-shadow: 0 0 8px var(--cyan); }}
.ks-home-title {{
    font-size: clamp(2.4rem, 4.5vw, 3.8rem); font-weight: 800;
    color: var(--text-heading); letter-spacing: -1.8px; line-height: 1.1; margin: 16px 0 16px;
}}
.ks-home-copy {{ font-size: 1rem; color: var(--muted); line-height: 1.75; margin-bottom: 24px; max-width: 560px; }}
.ks-hero-assurance {{ margin-top: 14px; color: var(--muted); font-size: 0.72rem; }}
.ks-hero-assurance span {{ color: var(--cyan); }}

.ks-visual-card {{
    background: {visual_card_bg}; border: 1px solid {visual_card_border};
    border-radius: 18px; padding: 22px 24px; box-shadow: 0 24px 50px rgba(0,0,0,.2);
}}
.ks-visual-top {{ display: flex; justify-content: space-between; font-size: 0.65rem; font-family: var(--mono); color: var(--muted); }}
.ks-visual-title {{ font-size: 1.18rem; font-weight: 750; color: var(--text-heading); margin-top: 18px; }}
.ks-visual-subtitle {{ font-size: 0.76rem; color: var(--muted); margin: 3px 0 16px; }}
.ks-process-row {{ display: grid; grid-template-columns: 28px 1fr 54px; align-items: center; gap: 10px; margin: 12px 0; }}
.ks-process-id {{ font-family: var(--mono); font-size: 0.74rem; font-weight: 700; color: var(--text-heading); }}
.ks-process-track {{ height: 8px; border-radius: 6px; background: var(--track-bg); overflow: hidden; }}
.ks-track-fill {{ display: block; height: 100%; border-radius: 6px; }}
.fill-mint  {{ background: var(--cyan); }}
.fill-blue  {{ background: var(--teal); }}
.fill-peach {{ background: var(--amber); }}
.ks-process-state {{ font-size: 0.55rem; font-family: var(--mono); font-weight: 700; text-align: right; }}
.state-running {{ color: var(--cyan); }}
.state-ready   {{ color: var(--teal); }}
.state-waiting {{ color: var(--amber); }}
.ks-visual-callout {{ margin-top: 18px; padding: 10px 12px; border-radius: 8px; background: rgba(0,0,0,.2); font-size: 0.72rem; color: var(--text); }}
.ks-visual-footer {{ display: flex; justify-content: space-between; margin-top: 14px; padding-top: 12px; border-top: 1px solid var(--border); font-size: 0.6rem; font-family: var(--mono); color: var(--muted); }}

.ks-path-card {{
    background: {path_card_bg}; border: 1px solid var(--border);
    border-radius: var(--radius); padding: 20px; box-shadow: var(--shadow);
    height: 180px; display: flex; flex-direction: column; justify-content: space-between;
}}
.ks-path-card-top {{ display: flex; justify-content: space-between; align-items: center; }}
.ks-path-number {{ font-family: var(--mono); font-size: 0.68rem; font-weight: 700; color: var(--cyan); }}
.ks-path-icon {{ width: 34px; height: 34px; border-radius: 8px; background: var(--card2); display: flex; align-items: center; justify-content: center; font-size: 1rem; color: var(--cyan); }}
.ks-path-title {{ font-size: 0.95rem; font-weight: 700; color: var(--text-heading); margin-top: 8px; }}
.ks-path-copy {{ font-size: 0.78rem; color: var(--muted); line-height: 1.6; }}

/* ─── VERDICT BOX ─── */
.ks-verdict {{
    background: var(--card); border: 1px solid var(--border);
    border-left: 3.5px solid var(--green);
    border-radius: var(--radius); padding: 18px 22px; margin-top: 16px;
}}
.ks-verdict-title  {{ font-size: 0.82rem; font-weight: 750; color: var(--green); margin-bottom: 10px; }}
.ks-verdict-row    {{ font-family: var(--mono); font-size: 0.78rem; color: var(--muted); margin-bottom: 7px; display: flex; gap: 6px; align-items: flex-start; }}
.ks-verdict-row em {{ font-style: normal; color: var(--text); font-weight: 600; }}
.ks-verdict-row b  {{ font-style: normal; color: var(--cyan); }}

/* ─── DIVIDER ─── */
.ks-divider {{ border: none; border-top: 1px solid var(--border); margin: 28px 0; }}

/* ─── STREAMLIT WIDGETS OVERRIDES ─── */
button[kind="primary"] {{
    background: {btn_prim_bg} !important;
    color: {btn_prim_color} !important;
    border: none !important; border-radius: 10px !important;
    font-family: var(--sans) !important; font-weight: 650 !important;
    box-shadow: 0 3px 12px {btn_prim_shadow} !important;
    transition: all 0.2s ease !important;
}}
button[kind="primary"]:hover {{
    background: {btn_prim_hover} !important;
    box-shadow: 0 5px 18px {btn_prim_shadow} !important;
    transform: translateY(-1px) !important;
}}
button[kind="secondary"] {{
    background: {btn_sec_bg} !important;
    border: 1px solid {btn_sec_border} !important;
    color: {btn_sec_color} !important;
    font-family: var(--sans) !important; font-weight: 550 !important;
    border-radius: 10px !important;
    transition: all 0.15s ease !important;
}}
button[kind="secondary"]:hover {{
    border-color: {btn_sec_hover_border} !important;
    color: {btn_sec_hover_color} !important;
}}

div[data-baseweb="select"] > div, div[data-baseweb="input"] > div {{
    background-color: {input_bg} !important;
    border-color: {input_border} !important;
    color: {input_color} !important;
    border-radius: 10px !important;
}}
div[data-testid="stDataEditor"] {{
    border: 1px solid var(--border) !important;
    border-radius: var(--radius) !important;
}}

.stTabs [data-baseweb="tab-list"] {{
    gap: 4px; background: {tab_list_bg};
    padding: 5px; border-radius: var(--radius);
    border: 1px solid {tab_list_border};
}}
.stTabs [data-baseweb="tab"] {{
    font-family: var(--sans); font-size: 0.78rem; font-weight: 600;
    padding: 7px 15px; border-radius: 8px; color: var(--muted);
    background: transparent; border: none; transition: all 0.15s ease;
}}
.stTabs [aria-selected="true"] {{
    background: {tab_sel_bg} !important;
    color: {tab_sel_color} !important;
    border: 1px solid {tab_sel_border} !important;
}}

/* ─── FOOTER ─── */
.ks-footer {{
    background: var(--surface); border-top: 1px solid var(--border);
    padding: 22px 34px; margin-top: 70px;
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


def inject_styles(theme: str = "premium") -> None:
    """Call this once at the top of every page to inject the active theme CSS."""
    st.markdown(get_css(theme), unsafe_allow_html=True)
