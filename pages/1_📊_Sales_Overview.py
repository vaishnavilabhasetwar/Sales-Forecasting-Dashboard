import streamlit as st
import pandas as pd
import plotly.express as px

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(
    page_title="Sales Overview Dashboard",
    page_icon="📊",
    layout="wide"
)

# =============================
# PREMIUM DARK ANIMATED OVERRIDES
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

/* 🌀 KEYFRAME ANIMATIONS */
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
@keyframes textShimmer {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
@keyframes metricPulse {
    0% { border-color: rgba(255,255,255,0.05); }
    50% { border-color: rgba(0, 242, 254, 0.4); box-shadow: 0 0 15px rgba(0, 242, 254, 0.1); }
    100% { border-color: rgba(255,255,255,0.05); }
}

/* Elegant Animated Glass Header */
.header-container {
    background: linear-gradient(135deg, rgba(37, 99, 235, 0.2) 0%, rgba(15, 23, 42, 0.1) 100%);
    backdrop-filter: blur(10px);
    padding: 35px;
    border-radius: 20px;
    border: 1px solid rgba(37, 99, 235, 0.25);
    margin-bottom: 35px;
    text-align: center;
    animation: fadeInUp 0.8s ease-out;
}

.shimmer-header {
    margin:0; 
    font-size:36px; 
    font-weight:800; 
    background: linear-gradient(90deg, #FFF, #00F2FE, #FFF);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: textShimmer 5s linear infinite;
    letter-spacing:-1px;
}

/* Glass Metrics Cards with Pulses & Hover Float */
.kpi-metric-card {
    background: rgba(17, 24, 39, 0.6);
    border-radius: 18px;
    padding: 25px 20px;
    text-align: center;
    border: 1px solid rgba(255, 255, 255, 0.05);
    box-shadow: 0 15px 30px rgba(0,0,0,0.25);
    animation: fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1) backwards, metricPulse 4s infinite ease-in-out;
    transition: all 0.3s ease;
}

.kpi-metric-card:hover {
    transform: translateY(-5px);
    border-color: #00F2FE !important;
    box-shadow: 0 20px 35px rgba(0, 242, 254, 0.15);
}

.kpi-metric-value {
    font-size: 28px;
    font-weight: 800;
    color: #00F2FE;
    margin: 6px 0;
    letter-spacing: -1px;
}

.kpi-metric-label {
    color: #9CA3AF;
    font-size: 13px;
    font-weight: 600;
    text-transform: uppercase;
}

.insight-card {
    background: rgba(17, 24, 39, 0.6);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    margin-top: 35px;
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
st.markdown("""
<div class="header-container">
    <h1 class="shimmer-header">📊 Sales Overview Dashboard</h1>
    <p style='margin:8px 0 0 0; color:#9CA3AF; font-size:16px;'>Business Intelligence | Sales Performance Analytics</p>
</div>
""", unsafe_allow_html=True)

# =============================
# LOAD DATA
# =============================
@st.cache_data
def load_data():
    df = pd.read_csv("train.csv", encoding="latin1")
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True, format="mixed")
    return df

df = load_data()

# =============================
# SIDEBAR FILTERS
# =============================
st.sidebar.header("🔍 Filters")

regions = st.sidebar.multiselect(
    "Select Region",
    df["Region"].unique(),
    default=df["Region"].unique()
)

categories = st.sidebar.multiselect(
    "Select Category",
    df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[
    (df["Region"].isin(regions)) &
    (df["Category"].isin(categories))
]

# =============================
# KPI CALCULATION
# =============================
total_sales = filtered_df["Sales"].sum()
orders = filtered_df["Order ID"].nunique()
customers = filtered_df["Customer ID"].nunique()
avg_sales = filtered_df["Sales"].mean()

# =============================
# KPI DISPLAY
# =============================
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="kpi-metric-card" style="animation-delay: 0.1s;">
        <div style="font-size:24px;">💰</div>
        <div class="kpi-metric-value">${total_sales:,.0f}</div>
        <div class="kpi-metric-label">Total Sales</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="kpi-metric-card" style="animation-delay: 0.2s;">
        <div style="font-size:24px;">🛒</div>
        <div class="kpi-metric-value">{orders:,}</div>
        <div class="kpi-metric-label">Total Orders</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="kpi-metric-card" style="animation-delay: 0.3s;">
        <div style="font-size:24px;">👤</div>
        <div class="kpi-metric-value">{customers:,}</div>
        <div class="kpi-metric-label">Customers</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="kpi-metric-card" style="animation-delay: 0.4s;">
        <div style="font-size:24px;">📦</div>
        <div class="kpi-metric-value">${avg_sales:,.2f}</div>
        <div class="kpi-metric-label">Avg Order Value</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# =============================
# SALES BY YEAR
# =============================
yearly = filtered_df.groupby(filtered_df["Order Date"].dt.year)["Sales"].sum().reset_index()
yearly.columns = ["Year", "Sales"]

fig1 = px.bar(
    yearly, x="Year", y="Sales", text_auto='.2s',
    color="Sales", color_continuous_scale="Viridis",
    title="📊 Sales by Year", template="plotly_dark"
)
fig1.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    title_font_size=18, title_font_color="#00F2FE",
    xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.05)")
)
st.plotly_chart(fig1, use_container_width=True)

# =============================
# MONTHLY TREND
# =============================
monthly = filtered_df.groupby(filtered_df["Order Date"].dt.to_period("M"))["Sales"].sum().reset_index()
monthly["Order Date"] = monthly["Order Date"].astype(str)

fig2 = px.line(
    monthly, x="Order Date", y="Sales", markers=True,
    title="📈 Monthly Sales Trend", template="plotly_dark"
)
fig2.update_traces(line_color="#00F2FE", line_width=3, marker=dict(size=8, color="#4FACFE"))
fig2.update_layout(
    paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
    title_font_size=18, title_font_color="#00F2FE",
    xaxis=dict(showgrid=False), yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.05)")
)
st.plotly_chart(fig2, use_container_width=True)

# =============================
# REGION & CATEGORY
# =============================
col1, col2 = st.columns(2)

with col1:
    region_sales = filtered_df.groupby("Region")["Sales"].sum().reset_index()
    fig3 = px.bar(region_sales, x="Region", y="Sales", color="Region", color_discrete_sequence=px.colors.qualitative.Pastel, title="🌍 Sales by Region", template="plotly_dark")
    fig3.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", title_font_size=16, title_font_color="#00F2FE")
    col1.plotly_chart(fig3, use_container_width=True)

with col2:
    category_sales = filtered_df.groupby("Category")["Sales"].sum().reset_index()
    fig4 = px.pie(category_sales, names="Category", values="Sales", hole=0.5, color_discrete_sequence=["#00F2FE", "#6366F1", "#EC4899"], title="🛍 Category Distribution", template="plotly_dark")
    fig4.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", title_font_size=16, title_font_color="#00F2FE")
    col2.plotly_chart(fig4, use_container_width=True)

# =============================
# INSIGHTS
# =============================
st.markdown("""
<div class="insight-card">
    <h3 style='margin-top:0; color:#00F2FE; font-weight:700;'>💡 Business Insights</h3>
    <ul style='color:#9CA3AF; line-height:1.7; font-size:15px; margin-bottom:0;'>
        <li>Technology and Furniture drive major revenue contribution</li>
        <li>Sales show seasonal peaks across months</li>
        <li>Certain regions outperform others significantly</li>
        <li>Focus inventory planning on high-demand categories</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# =============================
# TABLE
# =============================
st.markdown("### 📋 Filtered Data")
st.dataframe(filtered_df, use_container_width=True)

# ==========================================================
# FOOTER COMPONENT
# ==========================================================
st.markdown(
"""
<div class='footer-container'>
    Developed by <span style="color:#00F2FE; font-weight:600;">Vaishnavi Labhasetwar</span><br>
    <span style='font-size: 12px; color: #4B5563; margin-top: 5px; display: block;'>Business Intelligence Suite • All Rights Reserved © 2026</span>
</div>
""", unsafe_allow_html=True)