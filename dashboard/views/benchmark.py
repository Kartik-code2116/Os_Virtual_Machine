"""
benchmark.py
────────────
Multi-algorithm performance benchmark matrix:
- Comparative latency, waiting time, and context switches
- Grouped Plotly visualizer
- Algorithmic efficiency verdict
"""

import plotly.graph_objects as go
import streamlit as st
from utils.helpers import plotly_dark_layout


def render_benchmark_page():
    st.markdown(
        """
        <div class="ks-page-header">
            <div class="ks-page-eyebrow">📊 PERFORMANCE MATRIX</div>
            <div class="ks-page-title">Multi-Algorithm Benchmark & Analysis</div>
            <div class="ks-page-subtitle">
                Side-by-side comparison of FCFS, SJF, Priority, and Round Robin under the exact same process workload.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "benchmark_results" not in st.session_state:
        st.markdown(
            """
            <div style="text-align:center; padding:70px 20px;">
                <div style="font-size:3rem; margin-bottom:14px;">📊</div>
                <div style="font-size:1.15rem; font-weight:700; color:#dde4ef; margin-bottom:8px;">No Benchmark Dataset Generated Yet</div>
                <div style="font-size:0.85rem; color:#637080; max-width:440px; margin:0 auto 24px; line-height:1.7;">
                    To evaluate and compare all algorithms concurrently, visit the <b>Kernel Simulator</b> and click
                    <span style="color:#60b8f5;">⚡ BENCHMARK ALL 4 POLICIES</span>.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        c1, _ = st.columns([2, 3])
        with c1:
            if st.button("▶  Open Simulator to Run Benchmark", type="primary"):
                st.session_state["nav_selection"] = "simulator"
                st.rerun()
        return

    bench = st.session_state.benchmark_results
    st.dataframe(bench, use_container_width=True, hide_index=True)

    # Comparative Metric Graph
    st.markdown('<div class="ks-label" style="margin-top:20px;">COMPARATIVE METRIC DISTRIBUTION</div>', unsafe_allow_html=True)
    b_fig = go.Figure()
    b_fig.add_trace(go.Bar(
        x=bench["Algorithm"],
        y=bench["Avg Waiting"],
        name="Avg Waiting Time",
        marker_color="#60b8f5",
    ))
    b_fig.add_trace(go.Bar(
        x=bench["Algorithm"],
        y=bench["Avg Turnaround"],
        name="Avg Turnaround Time",
        marker_color="#a07eea",
    ))
    b_fig.add_trace(go.Bar(
        x=bench["Algorithm"],
        y=bench["Context Switches"],
        name="Context Switches",
        marker_color="#f0953a",
    ))

    b_fig.update_layout(
        barmode="group",
        **plotly_dark_layout(
            height=360,
            xaxis=dict(title=dict(text="Scheduling Discipline", font=dict(family="JetBrains Mono", color="#637080")), tickfont=dict(family="JetBrains Mono", color="#dde4ef"), gridcolor="#1a2a40"),
            yaxis=dict(title=dict(text="Clock Ticks / Count", font=dict(family="JetBrains Mono", color="#637080")), tickfont=dict(family="JetBrains Mono", color="#637080"), gridcolor="#1a2a40"),
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1, font=dict(family="JetBrains Mono", color="#dde4ef")),
        )
    )
    st.plotly_chart(b_fig, use_container_width=True)

    # Automated Architectural Verdict
    best_wait = bench.loc[bench["Avg Waiting"].idxmin()]
    best_switch = bench.loc[bench["Context Switches"].idxmin()]
    best_cpu = bench.loc[bench["CPU Utilization (%)"].idxmax()]

    st.markdown(
        f"""
        <div class="ks-verdict">
            <div class="ks-verdict-title">🏆 KERNEL PERFORMANCE VERDICT</div>
            <div class="ks-verdict-row">
                <span>●</span>
                <div><em>LOWEST LATENCY:</em> <b>{best_wait['Algorithm']}</b> produced the minimal average waiting time ({best_wait['Avg Waiting']} ticks).</div>
            </div>
            <div class="ks-verdict-row">
                <span>●</span>
                <div><em>LOWEST OVERHEAD:</em> <b>{best_switch['Algorithm']}</b> generated the fewest context switches ({best_switch['Context Switches']} switches).</div>
            </div>
            <div class="ks-verdict-row">
                <span>●</span>
                <div><em>PEAK UTILIZATION:</em> <b>{best_cpu['Algorithm']}</b> achieved the highest CPU utilization ({best_cpu['CPU Utilization (%)']:.1f}%).</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
