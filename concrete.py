import streamlit as st
import pandas as pd
import numpy as np
import requests
import time
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Concrete Protocol Pulse",
    layout="wide",
    page_icon="📊"
)

# -----------------------------
# CUSTOM STYLING
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
    color: white;
}
.stMetric {
    background-color: #1f2937;
    padding: 15px;
    border-radius: 12px;
    border: 1px solid #374151;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("⚙️ Controls")

refresh_rate = st.sidebar.slider("Refresh Rate (sec)", 10, 120, 30)

vault_options = ["All Vaults", "USDT Vault", "ETH Vault", "BTC Vault"]
selected_vault = st.sidebar.selectbox("Select Vault", vault_options)

st.sidebar.markdown("---")
st.sidebar.caption("Concrete Analytics Engine")

# -----------------------------
# DATA FETCH (API + FALLBACK)
# -----------------------------
@st.cache_data(ttl=30)
def fetch_data():
    try:
        url = "https://api.concrete.xyz/v1/metrics"  # Replace with real endpoint
        res = requests.get(url, timeout=5)
        return res.json()
    except:
        # fallback mock data
        return {
            "tvp": round(np.random.uniform(10, 15), 2),
            "utilization": round(np.random.uniform(70, 95), 2),
            "peg": round(np.random.uniform(0.998, 1.002), 4),
            "buffer": round(np.random.uniform(10, 20), 2),
            "market_slippage": round(np.random.uniform(5, 15), 2),
            "historical": pd.DataFrame({
                "day": range(1, 31),
                "market_yield": np.random.uniform(5, 25, 30),
                "concrete_yield": np.full(30, 15)
            }).to_dict()
        }

# -----------------------------
# MAIN LOOP (AUTO REFRESH)
# -----------------------------
placeholder = st.empty()

while True:
    with placeholder.container():

        data = fetch_data()

        # -----------------------------
        # DERIVED METRICS
        # -----------------------------
        peg_deviation = abs(data["peg"] - 1)
        risk_score = (data["utilization"] * data["market_slippage"]) / max(data["buffer"], 1)
        slippage_protection = data["buffer"] / max(data["market_slippage"], 1)

        # -----------------------------
        # HEADER
        # -----------------------------
        st.title("📊 Concrete Protocol Pulse")
        st.caption("Real-time monitoring of automated vault infrastructure")

        # -----------------------------
        # METRICS
        # -----------------------------
        st.subheader("🏛️ Protocol Health")

        m1, m2, m3, m4 = st.columns(4)

        m1.metric("Total Value Protected", f"${data['tvp']}M")
        m2.metric("Utilization", f"{data['utilization']}%")
        m3.metric("Peg", f"${data['peg']}")
        m4.metric("Risk Score", f"{round(risk_score,2)}")

        st.divider()

        # -----------------------------
        # ALERT SYSTEM
        # -----------------------------
        if peg_deviation > 0.01:
            st.error("⚠️ Peg instability detected")

        if data["utilization"] > 90:
            st.warning("⚠️ High utilization risk")

        if risk_score > 80:
            st.error("🚨 Extreme risk level")

        # -----------------------------
        # TABS
        # -----------------------------
        tab1, tab2, tab3 = st.tabs(["📈 Overview", "🗿 Distribution", "⚙️ Risk Engine"])

        # -----------------------------
        # TAB 1: CHART
        # -----------------------------
        with tab1:
            df = pd.DataFrame(data["historical"])

            fig = px.line(
                df,
                x="day",
                y=["market_yield", "concrete_yield"],
                template="plotly_dark"
            )
            st.plotly_chart(fig, use_container_width=True)

        # -----------------------------
        # TAB 2: PIE
        # -----------------------------
        with tab2:
            dist_data = pd.DataFrame({
                "Category": ["Yield", "Buffer", "Liquidity", "Insurance"],
                "Value": [45, 25, 20, 10]
            })

            fig2 = px.pie(
                dist_data,
                values="Value",
                names="Category",
                hole=0.5,
                template="plotly_dark"
            )
            st.plotly_chart(fig2, use_container_width=True)

        # -----------------------------
        # TAB 3: RISK ENGINE
        # -----------------------------
        with tab3:
            st.subheader("Risk Analytics")

            st.metric("Slippage Protection", f"{round(slippage_protection,2)}x")
            st.metric("Buffer Strength", f"{data['buffer']}%")
            st.metric("Market Slippage", f"{data['market_slippage']}%")

            st.info(f"""
            System currently absorbing **{round(slippage_protection,2)}x**
            market volatility while maintaining peg stability.
            """)

        # -----------------------------
        # FOOTER
        # -----------------------------
        st.markdown("---")
        st.caption("Built for Concrete Protocol | DeFi Intelligence Layer")

    time.sleep(refresh_rate)
    st.experimental_rerun()
