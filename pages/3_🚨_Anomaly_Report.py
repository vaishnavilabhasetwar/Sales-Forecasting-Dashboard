import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="Sales Anomaly Monitor",
    page_icon="🚨",
    layout="wide"
)

# ============================================================
# RISK METRICS OVERRIDE CSS WITH ALERT LIGHT ANIMATIONS
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background-color: #060913 !important;
    color: #F3F4F6 !important;
}
.stApp { background: #060913 !important; }

/* 🌀 ANIMATIONS */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes textShimmer {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
@keyframes threatGlow {
    0% { border-color: rgba(239, 68, 68, 0.25); box-shadow: 0 10px 30px rgba(0,0,0,0.4); }
    50% { border-color: rgba(244, 63, 94, 0.6); box-shadow: 0 10px 30px rgba(244, 63, 94, 0.15); }
    100% { border-color: rgba(239, 68, 68, 0.25); box-shadow: 0 10px 30px rgba(0,0,0,0.4); }
}

.hero-danger {
    background: linear-gradient(135deg, rgba(220, 38, 38, 0.15) 0%, rgba(17, 24, 39, 0.05) 100%);
    backdrop-filter: blur(12px);
    padding: 40px;
    border-radius: 24px;
    border: 1px solid rgba(239, 68, 68, 0.25);
    text-align: center;
    margin-bottom: 35px;
    animation: fadeInUp 0.8s ease-out, threatGlow 4s infinite ease-in-out;
}

.shimmer-danger-title {
    margin:0; 
    font-weight:800; 
    font-size:36px; 
    color:#FFF; 
    letter-spacing:-1px;
    background: linear-gradient(90deg, #FFF, #EF4444, #FDA4AF, #FFF);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: textShimmer 4s linear infinite;
}

.kpi-anomaly {
    background: rgba(17, 24, 39, 0.6);
    border-radius: 18px;
    padding: 25px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    text-align: center;
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    animation: fadeInUp 1s ease-out backwards;
}

.kpi-anomaly:hover {
    transform: translateY(-5px);
    border-color: #EF4444;
    box-shadow: 0 15px 30px rgba(239, 68, 68, 0.2);
}

.kpi-anomaly-value {
    font-size: 32px;
    font-weight: 800;
    color: #F43F5E;
}

.box-card {
    background: rgba(17, 24, 39, 0.6);
    padding: 25px;
    border-radius: 18px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    margin-top: 25px;
}

[data-testid="stSidebar"] {
    background-color: #04060E !important;
    border-right: 1px solid rgba(255, 255, 255, 0.06);
}

.footer-container {
    text-align: center;
    color: #6B7280;
    font-size: 14px;
    margin-top: 70px;
    padding: 30px 0;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# HERO SECTION
# ============================================================
st.markdown("""
<div class='hero-danger'>
    <h1 class="shimmer-danger-title">🚨 Sales Anomaly Monitoring Dashboard</h1>
    <h4 style='margin:8px 0; color:#FDA4AF; font-weight:500;'>AI Powered Sales Risk Detection using Isolation Forest</h4>
    <p style='margin:0; opacity:0.8;'>Monitor unusual sales behaviour, identify abnormal transactions, and support business decision making.</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# LOAD DATA
# ============================================================
anomaly_df = pd.read_csv("weekly_sales_anomalies.csv")
anomaly_df["Order Date"] = pd.to_datetime(anomaly_df["Order Date"])

# ============================================================
# SIDEBAR
# ============================================================
st.sidebar.title("⚙ Dashboard Controls")
st.sidebar.markdown("---")
show_only = st.sidebar.checkbox("Show Only Anomalies", value=False)

df = anomaly_df[anomaly_df["Anomaly"] == "Anomaly"] if show_only else anomaly_df

# ============================================================
# KPI CALCULATIONS
# ============================================================
total_points = len(anomaly_df)
total_anomalies = (anomaly_df["Anomaly"] == "Anomaly").sum()
anomaly_rate = (total_anomalies / total_points) * 100
highest_sale = anomaly_df["Total_Sales"].max()

# ============================================================
# KPI CARDS
# ============================================================
st.subheader("📊 Monitoring Overview")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"<div class='kpi-anomaly' style='animation-delay: 0.1s;'><div>🚨</div><div class='kpi-anomaly-value'>{total_anomalies}</div><div style='color:#9CA3AF; font-size:14px;'>Total Anomalies</div></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='kpi-anomaly' style='animation-delay: 0.2s;'><div>📊</div><div class='kpi-anomaly-value'>{anomaly_rate:.2f}%</div><div style='color:#9CA3AF; font-size:14px;'>Anomaly Rate</div></div>", unsafe_allow_html=True)
with c3:
    st.markdown(f"<div class='kpi-anomaly' style='animation-delay: 0.3s;'><div>💰</div><div class='kpi-anomaly-value'>${highest_sale:,.0f}</div><div style='color:#9CA3AF; font-size:14px;'>Highest Weekly Sales</div></div>", unsafe_allow_html=True)

status, status_color = ("🟢 Stable", "#10B981") if anomaly_rate <= 5 else (("🟡 Medium Risk", "#F59E0B") if anomaly_rate <= 10 else ("🔴 High Risk", "#EF4444"))
with c4:
    st.markdown(f"<div class='kpi-anomaly' style='animation-delay: 0.4s;'><div>🛡️</div><div class='kpi-anomaly-value' style='color:{status_color};'>{status}</div><div style='color:#9CA3AF; font-size:14px;'>System Health</div></div>", unsafe_allow_html=True)

# ============================================================
# SALES TREND WITH ANOMALIES
# ============================================================
st.write("")
st.markdown("""
<div class='box-card'>
    <h2 style='margin:0; color:#FB7185; font-size:22px;'>📈 Weekly Sales Monitoring</h2>
    <p style='color:#9CA3AF; margin-top:5px;'>Real-time visualization of weekly sales with detected anomalies highlighted.</p>
</div>
""", unsafe_allow_html=True)

anomalies = anomaly_df[anomaly_df["Anomaly"] == "Anomaly"]
normal_sales = anomaly_df[anomaly_df["Anomaly"] != "Anomaly"]

fig = px.line(normal_sales, x="Order Date", y="Total_Sales", template="plotly_dark")
fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white",
    hovermode="x unified", xaxis_title="Week", yaxis_title="Sales ($)",
    xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.05)")
)
fig.update_traces(line=dict(color="#38BDF8", width=3), mode="lines")

fig.add_scatter(
    x=anomalies["Order Date"], y=anomalies["Total_Sales"], mode="markers+text",
    text=["🚨"] * len(anomalies), textposition="top center",
    marker=dict(color="#EF4444", size=14, line=dict(color="white", width=1.5)), name="Anomaly"
)
st.plotly_chart(fig, use_container_width=True)

# ============================================================
# RISK DASHBOARD
# ============================================================
st.subheader("🛡 Risk Monitoring")
r1, r2 = st.columns(2)

with r1:
    if anomaly_rate < 5:
        st.success("### 🟢 LOW RISK\nSales remain stable. No significant abnormal activity detected. Business operations appear healthy.")
    elif anomaly_rate < 10:
        st.warning("### 🟡 MEDIUM RISK\nModerate abnormal activity detected. Monitor inventory and demand fluctuations.")
    else:
        st.error("### 🔴 HIGH RISK\nHigh number of anomalies detected. Immediate business investigation is recommended.")

with r2:
    timeline = anomalies[["Order Date", "Total_Sales"]].sort_values("Order Date", ascending=False)
    st.markdown("### 🚨 Latest Detected Anomalies")
    st.dataframe(timeline, use_container_width=True, hide_index=True)

# ============================================================
# AI BUSINESS INSIGHTS
# ============================================================
st.write("")
st.markdown("<div class='box-card'><h2 style='margin:0; color:#FB7185; font-size:22px;'>🤖 AI Business Insights</h2></div>", unsafe_allow_html=True)

if anomaly_rate < 5:
    insight = "### ✅ Sales Performance is Stable\n**Observations**\n- Very few abnormal sales patterns detected.\n- Sales follow a consistent trend.\n- Current inventory strategy appears effective.\n\n**Recommendation**\n- Continue existing inventory planning.\n- Monitor sales weekly.\n- Maintain current promotional strategy."
elif anomaly_rate < 10:
    insight = "### ⚠ Moderate Risk Detected\n**Observations**\n- Some unusual sales spikes or drops detected.\n- Possible seasonal or promotional impact.\n\n**Recommendation**\n- Review affected weeks.\n- Verify marketing campaigns.\n- Monitor inventory for fast-moving products."
else:
    insight = "### 🚨 High Business Risk\n**Observations**\n- Large number of anomalies detected.\n- Sales pattern is unstable.\n\n**Recommendation**\n- Investigate abnormal transactions.\n- Review supply chain issues.\n- Check pricing errors.\n- Verify demand forecasting."

st.info(insight)

# ============================================================
# EXECUTIVE SUMMARY
# ============================================================
st.write("")
st.markdown("<div class='box-card'><h2 style='margin:0; color:#38BDF8; font-size:22px;'>📋 Executive Summary</h2></div>", unsafe_allow_html=True)

st.success(f"""
### Sales Monitoring Summary
**Total Weeks Analysed:** {total_points}
**Detected Anomalies:** {total_anomalies}
**Anomaly Rate:** {anomaly_rate:.2f}%
**Highest Weekly Sales:** ${highest_sale:,.2f}
**Detection Algorithm:** Isolation Forest
""")

# ============================================================
# DETAILED ANOMALY TABLE
# ============================================================
st.write("")
st.markdown("<div class='box-card'><h2 style='margin:0; color:#FBBF24; font-size:22px;'>📊 Detailed Anomaly Report</h2></div>", unsafe_allow_html=True)
st.dataframe(anomalies.style.format({"Total_Sales": "${:,.2f}"}), use_container_width=True, hide_index=True)

# ============================================================
# PROJECT HIGHLIGHTS
# ============================================================
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='box-card'><h3>🎯 Business Value</h3>✔ Detect abnormal behavior<br>✔ Improve inventory planning<br>✔ Support demand forecasting<br>✔ Reduce financial risk</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='box-card'><h3>🧠 Machine Learning</h3><b>Algorithm:</b> Isolation Forest<br><b>Purpose:</b> Unsupervised Risk Matrix Outlier Detection</div>", unsafe_allow_html=True)

# ============================================================
# FOOTER
# ============================================================
st.markdown(
"""
<div class='footer-container'>
    Developed by <span style="color:#EF4444; font-weight:600;">Vaishnavi Labhasetwar</span><br>
    <span style='font-size: 12px; color: #4B5563; margin-top: 5px; display: block;'>Sales Deflection Core System Perimeter • All Rights Reserved © 2026</span>
</div>
""", unsafe_allow_html=True)