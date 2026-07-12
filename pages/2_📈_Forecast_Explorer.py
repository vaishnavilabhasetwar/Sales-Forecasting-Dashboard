import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="Forecast Explorer",
    page_icon="🔮",
    layout="wide"
)

# ==========================================================
# PROFESSIONAL DARK GLASS UI CSS WITH FLUID ANIMATIONS
# ==========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background-color: #060913 !important;
    color: #F3F4F6 !important;
}
.stApp { background: #060913 !important; }

/* 🌀 ANIMATION DEFINITIONS */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes textShimmer {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
@keyframes borderGlow {
    0% { border-color: rgba(6, 182, 212, 0.2); }
    50% { border-color: rgba(99, 102, 241, 0.5); }
    100% { border-color: rgba(6, 182, 212, 0.2); }
}

/* Animated Glass Hero Banner */
.hero-container {
    background: linear-gradient(135deg, rgba(37, 99, 235, 0.2) 0%, rgba(6, 182, 212, 0.05) 100%);
    backdrop-filter: blur(12px);
    padding: 40px;
    border-radius: 24px;
    color: white;
    margin-bottom: 35px;
    border: 1px solid rgba(6, 182, 212, 0.2);
    text-align: center;
    animation: fadeInUp 0.8s ease-out, borderGlow 6s infinite ease-in-out;
}

.shimmer-forecast-title {
    margin:0; 
    font-weight:800; 
    font-size:36px; 
    letter-spacing:-1px;
    background: linear-gradient(90deg, #FFF, #38BDF8, #6366F1, #FFF);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: textShimmer 4s linear infinite;
}

/* Premium KPI Panels */
.kpi-card {
    background: rgba(17, 24, 39, 0.6);
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.05);
    transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    animation: fadeInUp 1s ease-out backwards;
}

.kpi-card:hover {
    transform: translateY(-8px);
    border-color: #3B82F6;
    box-shadow: 0 15px 30px rgba(59, 130, 246, 0.15);
}

.kpi-value {
    font-size: 30px;
    font-weight: 800;
    color: #00F2FE;
    margin-top: 4px;
    letter-spacing: -1px;
}

.box-panel {
    background: rgba(17, 24, 39, 0.6);
    border-radius: 18px;
    padding: 25px;
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

# ==========================================================
# HERO SECTION
# ==========================================================
st.markdown("""
<div class='hero-container'>
    <h1 class="shimmer-forecast-title">🔮 Forecast Explorer</h1>
    <h4 style='margin:8px 0; color:#38BDF8; font-weight:500;'>AI Powered Sales Forecasting Dashboard</h4>
    <p style='margin:0; opacity:0.8;'>Predict future sales using the trained <b>XGBoost Regression Model</b>.</p>
</div>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR
# ==========================================================
st.sidebar.title("⚙ Forecast Controls")
st.sidebar.markdown("---")
st.sidebar.write("""
Choose a business segment and forecast horizon.
The dashboard will display predicted sales and
model performance.
""")

# ==========================================================
# LOAD MODEL METRICS
# ==========================================================
metrics = joblib.load("models/model_metrics.pkl")

# ==========================================================
# FORECAST DATA
# ==========================================================
forecast_data = {
    "Furniture":[7620.11,6863.42,10816.44],
    "Technology":[15192.01,12475.71,26697.01],
    "Office Supplies":[15785.54,7166.62,11664.19],
    "West Region":[11607.54,22672.50,22078.09],
    "East Region":[7056.06,4788.89,9713.36]
}

months = ["Jan 2019", "Feb 2019", "Mar 2019"]

segment = st.sidebar.selectbox("Select Category / Region", list(forecast_data.keys()))
forecast_horizon = st.sidebar.slider("Forecast Horizon (Months)", 1, 3, 3)

forecast_df = pd.DataFrame({
    "Month": months[:forecast_horizon],
    "Forecasted Sales": forecast_data[segment][:forecast_horizon]
})

total_forecast = forecast_df["Forecasted Sales"].sum()
avg_forecast = forecast_df["Forecasted Sales"].mean()
highest_month = forecast_df["Forecasted Sales"].max()

# ==========================================================
# KPI CARDS
# ==========================================================
st.markdown("<h3 style='font-size:20px; font-weight:700; color:#FFF;'>📊 Forecast Summary</h3>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"<div class='kpi-card' style='animation-delay: 0.1s;'><div style='font-size:32px;'>💰</div><div class='kpi-value'>${total_forecast:,.0f}</div><div style='color:#9CA3AF; font-size:14px;'>Total Forecast Sales</div></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='kpi-card' style='animation-delay: 0.2s;'><div style='font-size:32px;'>📈</div><div class='kpi-value'>${avg_forecast:,.0f}</div><div style='color:#9CA3AF; font-size:14px;'>Average Monthly Sales</div></div>", unsafe_allow_html=True)
with c3:
    st.markdown(f"<div class='kpi-card' style='animation-delay: 0.3s;'><div style='font-size:32px;'>🚀</div><div class='kpi-value'>${highest_month:,.0f}</div><div style='color:#9CA3AF; font-size:14px;'>Highest Forecast Month</div></div>", unsafe_allow_html=True)

# ==========================================================
# FORECAST TABLE
# ==========================================================
st.write("")
st.markdown("""
<div class='box-panel'>
    <h3 style='margin:0; color:#00F2FE;'>📋 Forecast Results</h3>
</div>
""", unsafe_allow_html=True)

st.dataframe(
    forecast_df.style.format({"Forecasted Sales": "${:,.2f}"}),
    use_container_width=True,
    hide_index=True
)

# ==========================================================
# FORECAST CHART
# ==========================================================
fig = px.line(
    forecast_df, x="Month", y="Forecasted Sales", markers=True,
    title=f"{segment} Sales Forecast", template="plotly_dark"
)

fig.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    title_font_size=20, font=dict(color="white", size=14),
    hovermode="x unified", xaxis_title="Forecast Month", yaxis_title="Predicted Sales ($)"
)

fig.update_traces(
    line=dict(color="#00F2FE", width=4),
    marker=dict(size=10, color="#6366F1"),
    text=[f"${x:,.0f}" for x in forecast_df["Forecasted Sales"]],
    textposition="top center"
)
st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# MODEL PERFORMANCE
# ==========================================================
st.subheader("🧠 Model Performance")
m1, m2, m3 = st.columns(3)

with m1:
    st.markdown(f"<div class='kpi-card'><div style='font-size:32px;'>🎯</div><div class='kpi-value' style='color:#EC4899;'>{metrics['MAE']:,.2f}</div><div style='color:#9CA3AF; font-size:14px;'>Mean Absolute Error</div></div>", unsafe_allow_html=True)
with m2:
    st.markdown(f"<div class='kpi-card'><div style='font-size:32px;'>📉</div><div class='kpi-value' style='color:#EC4899;'>{metrics['RMSE']:,.2f}</div><div style='color:#9CA3AF; font-size:14px;'>Root Mean Square Error</div></div>", unsafe_allow_html=True)
with m3:
    st.markdown(f"<div class='kpi-card'><div style='font-size:32px;'>📊</div><div class='kpi-value' style='color:#EC4899;'>{metrics['MAPE']:.2f}%</div><div style='color:#9CA3AF; font-size:14px;'>Mean Absolute Percentage Error</div></div>", unsafe_allow_html=True)

# ==========================================================
# AI BUSINESS INSIGHTS
# ==========================================================
st.write("")
st.markdown("""
<div class='box-panel'>
    <h3 style='margin:0; color:#38BDF8;'>🤖 AI Business Recommendation</h3>
</div>
""", unsafe_allow_html=True)

if segment == "Technology":
    recommendation = """
✅ Technology products are forecasted to maintain strong demand.
**Recommendation**
- Increase inventory levels.
- Prioritize promotional campaigns.
- Ensure sufficient stock to avoid shortages.
"""
elif segment == "Furniture":
    recommendation = """
✅ Furniture demand is expected to remain moderate.
**Recommendation**
- Maintain balanced inventory.
- Monitor seasonal fluctuations.
- Focus on premium products.
"""
elif segment == "Office Supplies":
    recommendation = """
✅ Office Supplies show relatively stable demand.
**Recommendation**
- Keep regular stock levels.
- Avoid overstocking.
- Continue recurring replenishment.
"""
elif "Region" in segment:
    recommendation = f"""
✅ {segment} shows healthy forecasted sales.
**Recommendation**
- Allocate additional marketing budget.
- Improve regional inventory planning.
- Track monthly sales performance closely.
"""
else:
    recommendation = "Monitor sales closely and adjust inventory based on monthly demand."

st.info(recommendation)

# ==========================================================
# FORECAST TREND SUMMARY
# ==========================================================
st.write("")
trend = forecast_df["Forecasted Sales"].iloc[-1] - forecast_df["Forecasted Sales"].iloc[0]

if trend > 0:
    trend_msg = "📈 Upward Trend"
    trend_color = "#10B981"
elif trend < 0:
    trend_msg = "📉 Downward Trend"
    trend_color = "#EF4444"
else:
    trend_msg = "➡ Stable Trend"
    trend_color = "#3B82F6"

st.markdown(f"""
<div class='box-panel'>
    <h3 style="margin-top:0; color:#38BDF8;">📊 Forecast Trend Summary</h3>
    <p style='font-size:16px;'><b>Trend:</b> <span style="color:{trend_color}; font-weight:700; font-size:18px;">{trend_msg}</span></p>
    <p style='color:#9CA3AF; margin-bottom:0;'>The forecast indicates how sales are expected to move over the selected horizon. This insight can support inventory planning, production scheduling, and business strategy.</p>
</div>
""", unsafe_allow_html=True)

# ==========================================================
# MODEL INFORMATION
# ==========================================================
st.write("")
st.markdown("""
<div class='box-panel'>
    <h3 style='margin-top:0; color:#38BDF8;'>🧠 Best Forecasting Model</h3>
    <table style="width:100%; color:white; font-size:15px; border-collapse:collapse;">
        <tr style='border-bottom:1px solid rgba(255,255,255,0.05);'><td style='padding:10px 0;'><b>Algorithm</b></td><td>XGBoost Regressor</td></tr>
        <tr style='border-bottom:1px solid rgba(255,255,255,0.05);'><td style='padding:10px 0;'><b>Why Selected?</b></td><td>Lowest prediction error and strong generalization performance.</td></tr>
        <tr><td style='padding:10px 0;'><b>Strengths</b></td><td style='color:#9CA3AF;'>✔ High Accuracy &nbsp;&nbsp; ✔ Handles Non-linear Relationships &nbsp;&nbsp; ✔ Fast Prediction &nbsp;&nbsp; ✔ Suitable for Business Forecasting</td></tr>
    </table>
</div>
""", unsafe_allow_html=True)

# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================
st.write("")
st.success(f"""
### 📌 Executive Summary
• Segment Selected: **{segment}**
• Forecast Horizon: **{forecast_horizon} Month(s)**
• Total Forecast Sales: **${total_forecast:,.2f}**
• Average Monthly Sales: **${avg_forecast:,.2f}**
• Model Used: **XGBoost Regressor**
""")

# ==========================================================
# FOOTER COMPONENT
# ==========================================================
st.markdown(
"""
<div class='footer-container'>
    Developed by <span style="color:#00F2FE; font-weight:600;">Vaishnavi Labhasetwar</span><br>
    <span style='font-size: 12px; color: #4B5563; margin-top: 5px; display: block;'>Corporate AI Forecasting Module • All Rights Reserved © 2026</span>
</div>
""", unsafe_allow_html=True)