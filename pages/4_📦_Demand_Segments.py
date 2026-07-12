import streamlit as st
import pandas as pd
import plotly.express as px

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(
    page_title="Product Demand Intelligence",
    page_icon="📦",
    layout="wide"
)

# =============================
# HIGH-END DARK GLASSMORPHIC CSS WITH MOTION ENHANCEMENTS
# =============================
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

.header-title-box {
    text-align: center;
    background: linear-gradient(90deg, #6366F1, #22D3EE, #6366F1);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -1px;
    margin-top: 10px;
    animation: textShimmer 4s linear infinite;
}

.subtext {
    text-align: center;
    color: #9CA3AF;
    font-size: 16px;
    margin-bottom: 35px;
    animation: fadeInUp 1s ease-out;
}

.kpi-box-card {
    background: rgba(17, 24, 39, 0.6);
    padding: 25px;
    border-radius: 18px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    text-align: center;
    animation: fadeInUp 1.2s cubic-bezier(0.16, 1, 0.3, 1) backwards;
    transition: all 0.3s ease;
}

.kpi-box-card:hover {
    transform: translateY(-5px);
    border-color: #22D3EE;
    box-shadow: 0 15px 30px rgba(34, 211, 238, 0.15);
}

.kpi-box-metric {
    font-size: 28px;
    font-weight: 800;
    color: #22D3EE;
    margin-top: 4px;
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

# =============================
# HEADER
# =============================
st.markdown("<div class='header-title-box'>📦 Product Demand Intelligence</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>AI-powered K-Means Segmentation Dashboard</div>", unsafe_allow_html=True)

# =============================
# LOAD DATA
# =============================
cluster_df = pd.read_csv("clustering_results.csv")

# =============================
# SIDEBAR FILTERS
# =============================
st.sidebar.title("⚙️ Filters")

clusters = st.sidebar.multiselect(
    "Select Cluster",
    cluster_df["Cluster_Name"].unique(),
    default=cluster_df["Cluster_Name"].unique()
)

filtered_df = cluster_df[cluster_df["Cluster_Name"].isin(clusters)]

# =============================
# KPI METRICS
# =============================
total_products = filtered_df["Sub-Category"].nunique()
avg_sales = filtered_df["Total_Sales"].mean()
avg_growth = filtered_df["Sales_Growth_Rate"].mean()
avg_order = filtered_df["Average_Order_Value"].mean()

st.markdown("### 📊 Key Performance Indicators")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"<div class='kpi-box-card' style='animation-delay: 0.1s;'><div>📦</div><div class='kpi-box-metric'>{total_products}</div><p style='color:#9CA3AF; margin:0;'>Total Products</p></div>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<div class='kpi-box-card' style='animation-delay: 0.2s;'><div>💰</div><div class='kpi-box-metric'>${avg_sales:,.2f}</div><p style='color:#9CA3AF; margin:0;'>Avg Sales</p></div>", unsafe_allow_html=True)
with c3:
    st.markdown(f"<div class='kpi-box-card' style='animation-delay: 0.3s;'><div>📈</div><div class='kpi-box-metric'>{avg_growth:.2f}%</div><p style='color:#9CA3AF; margin:0;'>Avg Growth Rate</p></div>", unsafe_allow_html=True)
with c4:
    st.markdown(f"<div class='kpi-box-card' style='animation-delay: 0.4s;'><div>🧾</div><div class='kpi-box-metric'>${avg_order:,.2f}</div><p style='color:#9CA3AF; margin:0;'>Avg Order Value</p></div>", unsafe_allow_html=True)

# =============================
# CLUSTER SUMMARY
# =============================
st.write("")
st.markdown("### 📌 Cluster Summary")

summary = filtered_df.groupby("Cluster_Name").agg({
    "Sub-Category": "count", "Total_Sales": "mean", "Sales_Growth_Rate": "mean", "Average_Order_Value": "mean"
}).round(2)
summary.rename(columns={"Sub-Category": "No. of Products"}, inplace=True)

st.dataframe(summary, use_container_width=True)

# =============================
# SCATTER PLOT
# =============================
st.markdown("### 📊 Demand Segmentation Map")

fig = px.scatter(
    filtered_df, x="Total_Sales", y="Average_Order_Value", color="Cluster_Name",
    size="Sales_Volatility", hover_name="Sub-Category", template="plotly_dark",
    title="Product Demand Segments (K-Means Clustering)"
)
fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font_color="white")
fig.update_traces(marker=dict(opacity=0.85, line=dict(width=1, color="white")))
st.plotly_chart(fig, use_container_width=True)

# =============================
# PRODUCT TABLE
# =============================
st.markdown("### 📋 Product Cluster Details")
st.dataframe(filtered_df[["Sub-Category", "Cluster_Name", "Total_Sales", "Sales_Growth_Rate", "Average_Order_Value"]], use_container_width=True)

# =============================
# STRATEGY SECTION
# =============================
st.markdown("### 💡 Stocking Strategy Insights")
st.markdown("""
<div style="background:rgba(17, 24, 39, 0.6); padding:25px; border-radius:14px; border:1px solid rgba(255,255,255,0.05);">
    <p style='margin-top:0;'><b>📌 Key Business Strategy Matrix:</b></p>
    • Premium products ➡ Maintain high availability and priority stock<br><br>
    • High volume items ➡ Optimize inventory turnover<br><br>
    • Stable demand products ➡ Maintain balanced stock levels<br><br>
    • Emerging products ➡ Increase stock gradually based on trend validation
</div>
""", unsafe_allow_html=True)

# ==========================================================
# FOOTER COMPONENT
# ==========================================================
st.markdown(
"""
<div class='footer-container'>
    Developed by <span style="color:#22D3EE; font-weight:600;">Vaishnavi Labhasetwar</span><br>
    <span style='font-size: 12px; color: #4B5563; margin-top: 5px; display: block;'>K-Means Cluster Optimization Subspace • All Rights Reserved © 2026</span>
</div>
""", unsafe_allow_html=True)