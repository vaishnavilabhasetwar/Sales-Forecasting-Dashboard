import streamlit as st

# ==========================================================
# PAGE CONFIG
# ==========================================================
st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📈",
    layout="wide"
)

# ==========================================================
# PREMIUM ULTRA-MODERN GLASSMORPHIC CSS WITH ANIMATIONS
# ==========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Plus Jakarta Sans', sans-serif;
    background-color: #060913 !important;
    color: #F3F4F6 !important;
}

.stApp {
    background: #060913 !important;
}

/* 🌀 KEYFRAME ANIMATIONS */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(25px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes textShimmer {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes breathingGlow {
    0% { border-color: rgba(59, 130, 246, 0.2); box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4); }
    50% { border-color: rgba(0, 242, 254, 0.5); box-shadow: 0 20px 50px rgba(0, 242, 254, 0.15); }
    100% { border-color: rgba(59, 130, 246, 0.2); box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4); }
}

/* Glassmorphic Hero Banner with Breathing Animation */
.hero-container {
    background: linear-gradient(135deg, rgba(37, 99, 235, 0.15) 0%, rgba(6, 182, 212, 0.03) 100%);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(59, 130, 246, 0.2);
    padding: 50px 40px;
    border-radius: 24px;
    margin-bottom: 35px;
    animation: breathingGlow 6s ease-in-out infinite, fadeInUp 1s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Shimmering Animated Title */
.big-title {
    font-size: 44px;
    font-weight: 800;
    letter-spacing: -1.5px;
    background: linear-gradient(90deg, #00F2FE, #4FACFE, #6366F1, #00F2FE);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: textShimmer 4s linear infinite;
    margin-bottom: 12px;
}

.sub-title {
    font-size: 19px;
    color: #9CA3AF;
    font-weight: 400;
    animation: fadeInUp 1.2s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Premium Glass Container Cards */
.card {
    background: rgba(17, 24, 39, 0.7);
    backdrop-filter: blur(10px);
    padding: 35px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.06);
    color: #E5E7EB;
    box-shadow: 0 15px 35px rgba(0,0,0,0.3);
    margin-bottom: 30px;
    animation: fadeInUp 1.2s cubic-bezier(0.16, 1, 0.3, 1) backwards;
}

/* Feature Grid Cards With Smooth Hover Float Mechanics */
.feature-card {
    background: rgba(17, 24, 39, 0.6);
    backdrop-filter: blur(8px);
    padding: 30px 25px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    text-align: center;
    color: #E5E7EB;
    min-height: 250px;
    transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
    animation: fadeInUp 1.4s cubic-bezier(0.16, 1, 0.3, 1) backwards;
}

.feature-card:hover {
    transform: translateY(-10px) scale(1.03);
    border-color: rgba(0, 242, 254, 0.6);
    background: rgba(22, 32, 53, 0.85);
    box-shadow: 0 25px 45px rgba(0, 242, 254, 0.2);
}

.feature-icon {
    font-size: 44px;
    margin-bottom: 15px;
    display: inline-block;
    transition: transform 0.3s ease;
}
.feature-card:hover .feature-icon {
    transform: scale(1.2) rotate(5deg);
}

/* Sidebar styling overrides */
[data-testid="stSidebar"] {
    background-color: #04060E !important;
    border-right: 1px solid rgba(255, 255, 255, 0.06);
}

/* Premium Footer */
.footer-container {
    text-align: center;
    color: #6B7280;
    font-size: 14px;
    margin-top: 70px;
    padding: 30px 0;
    border-top: 1px solid rgba(255, 255, 255, 0.06);
}
.footer-accent {
    font-weight: 600;
    color: #00F2FE;
}
</style>
""", unsafe_allow_html=True)

# ==========================================================
# SIDEBAR NAVIGATION
# ==========================================================
st.sidebar.markdown("<h2 style='color:#00F2FE; font-weight:800; margin-bottom:0; letter-spacing:-1px;'>📈 SALES INTELLIGENCE</h2>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='color:#4B5563; font-size:12px; font-weight:500; text-transform:uppercase; letter-spacing:1px;'>Predictive Analytics Suite</p>", unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.write("### 📂 Dashboard Pages")
st.sidebar.write("📊 Sales Overview")
st.sidebar.write("📈 Forecast Explorer")
st.sidebar.write("🚨 Anomaly Report")
st.sidebar.write("📦 Demand Segments")

st.sidebar.markdown("---")
st.sidebar.write("Developed By")
st.sidebar.success("Vaishnavi Labhasetwar")

# ==========================================================
# HERO SECTION
# ==========================================================
st.markdown(
"""
<div class='hero-container'>
    <div class='big-title'>Sales Forecasting & Business Intelligence Dashboard</div>
    <div class='sub-title'>
        Machine Learning based Sales Forecasting using 
        <span style='color:#00F2FE; font-weight:600;'>XGBoost, Prophet, SARIMA, Isolation Forest and K-Means Clustering</span>
    </div>
</div>
""",
unsafe_allow_html=True
)

# ==========================================================
# PROJECT OBJECTIVE
# ==========================================================
st.markdown("""
<div class='card'>
    <h2 style='color:#00F2FE; font-weight:700; margin-top:0; font-size:24px;'>🎯 Project Objective</h2>
    <p style='font-size:17px; color:#9CA3AF; line-height:1.6;'>
        This dashboard helps organizations make better business decisions using Machine Learning and Time Series Forecasting.
    </p>
    <ul style='font-size:16px; color:#E5E7EB; line-height:1.8;'>
        <li>📈 Forecast Future Sales</li>
        <li>🚨 Detect Sales Anomalies</li>
        <li>🌍 Analyze Regional & Category Performance</li>
        <li>📦 Segment Products using K-Means Clustering</li>
        <li>📊 Improve Inventory Planning</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.write("")

# ==========================================================
# FEATURES
# ==========================================================
st.markdown("<h2 style='font-weight:700; color:#F3F4F6; margin-bottom:25px; font-size:24px; letter-spacing:-0.5px;'>🚀 Dashboard Features</h2>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='feature-card' style='animation-delay: 0.1s;'>
        <div class='feature-icon'>📊</div>
        <h3 style='color:#00F2FE; margin:10px 0; font-weight:700; font-size:18px;'>Sales Overview</h3>
        <p style='font-size:14px; color:#9CA3AF; line-height:1.5;'>Analyze yearly and monthly sales trends with interactive filters.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='feature-card' style='animation-delay: 0.2s;'>
        <div class='feature-icon'>📈</div>
        <h3 style='color:#4FACFE; margin:10px 0; font-weight:700; font-size:18px;'>Forecast Explorer</h3>
        <p style='font-size:14px; color:#9CA3AF; line-height:1.5;'>Predict future sales using the trained XGBoost forecasting model.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='feature-card' style='animation-delay: 0.3s;'>
        <div class='feature-icon'>🚨</div>
        <h3 style='color:#6366F1; margin:10px 0; font-weight:700; font-size:18px;'>Anomaly Detection</h3>
        <p style='font-size:14px; color:#9CA3AF; line-height:1.5;'>Detect unusual sales patterns using Isolation Forest.</p>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='feature-card' style='animation-delay: 0.4s;'>
        <div class='feature-icon'>📦</div>
        <h3 style='color:#EC4899; margin:10px 0; font-weight:700; font-size:18px;'>Demand Segmentation</h3>
        <p style='font-size:14px; color:#9CA3AF; line-height:1.5;'>Segment products into demand groups using K-Means Clustering.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ==========================================================
# TECHNOLOGY STACK
# ==========================================================
st.markdown("<h2 style='font-weight:700; color:#F3F4F6; margin:35px 0 20px 0; font-size:24px; letter-spacing:-0.5px;'>⚙️ Technology Stack</h2>", unsafe_allow_html=True)

t1, t2, t3, t4 = st.columns(4)
t1.info("🐍 Python")
t2.info("📈 Streamlit")
t3.info("🤖 XGBoost")
t4.info("📊 Plotly")

t5, t6, t7, t8 = st.columns(4)
t5.success("📚 Pandas")
t6.success("🧠 Scikit-Learn")
t7.success("📉 Prophet")
t8.success("📦 K-Means")

st.write("")

# ==========================================================
# PROJECT WORKFLOW
# ==========================================================
st.markdown("<h2 style='font-weight:700; color:#F3F4F6; margin:35px 0 20px 0; font-size:24px; letter-spacing:-0.5px;'>🔄 Project Workflow</h2>", unsafe_allow_html=True)

st.success("""
Raw Sales Data  ➡  Data Cleaning  ➡  Exploratory Data Analysis  ➡  Forecasting Models  ➡  Anomaly Detection  ➡  Product Segmentation  ➡  Interactive Dashboard
""")

# ==========================================================
# FOOTER COMPONENT
# ==========================================================
st.markdown(
"""
<div class='footer-container'>
    Developed with ❤️ by <span class='footer-accent'>Vaishnavi Labhasetwar</span><br>
    <span style='font-size: 12px; color: #4B5563; margin-top: 5px; display: block;'>Machine Learning Sales Forecasting Dashboard • All Rights Reserved © 2026</span>
</div>
""", unsafe_allow_html=True)