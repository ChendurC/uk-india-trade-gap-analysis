"""
app.py - The Interactive Dashboard
====================================
Run this with: streamlit run dashboard/app.py
It turns your CSV data into a visual, interactive web app.
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Page setup ───────────────────────────────────────────────────────
st.set_page_config(
    page_title="UK–India Trade Gap Analysis",
    page_icon="🇬🇧",
    layout="wide"
)

# ── Load the data ─────────────────────────────────────────────────────
@st.cache_data
def load_data():
    return pd.read_csv("data/uk_india_trade_gap.csv")

df = load_data()

# ── Header ────────────────────────────────────────────────────────────
st.title("🇬🇧 UK–India Trade Gap Analysis")
st.markdown(
    "**What does the UK buy from the world that India isn't supplying enough of?**  "
    "This dashboard analyses $400B+ of UK imports to find where India's market share is smallest."
)
st.divider()

# ── Top metrics row ──────────────────────────────────────────────────
col1, col2, col3 = st.columns(3)
total_uk_imports = df["uk_imports_world_usd_billion"].sum()
total_india_supply = df["india_exports_to_uk_usd_billion"].sum()
total_gap = df["gap_usd_billion"].sum()

col1.metric("🌍 Total UK Imports Analysed", f"${total_uk_imports:.1f}B")
col2.metric("🇮🇳 India's Total Supply",      f"${total_india_supply:.1f}B")
col3.metric("📉 Total Gap (Opportunity)",    f"${total_gap:.1f}B")

st.divider()

# ── Chart 1: Gap by Category ──────────────────────────────────────────
st.subheader("📊 Biggest Gaps — Where India is Under-Represented")

fig1 = px.bar(
    df.sort_values("gap_usd_billion", ascending=True),
    x="gap_usd_billion",
    y="category",
    orientation="h",
    color="gap_usd_billion",
    color_continuous_scale="Reds",
    labels={"gap_usd_billion": "Gap (USD Billion)", "category": "Product Category"},
    title="UK Import Gap — What India Could Supply But Doesn't (Yet)"
)
fig1.update_layout(height=500, showlegend=False)
st.plotly_chart(fig1, use_container_width=True)

# ── Chart 2: India's market share ────────────────────────────────────
st.subheader("🥧 India's Market Share in UK Imports (by Category)")

fig2 = px.bar(
    df.sort_values("india_market_share_pct", ascending=True),
    x="india_market_share_pct",
    y="category",
    orientation="h",
    color="india_market_share_pct",
    color_continuous_scale="Greens",
    labels={"india_market_share_pct": "India's Market Share (%)", "category": "Product Category"},
    title="India's % Share of What the UK Imports"
)
fig2.update_layout(height=500, showlegend=False)
st.plotly_chart(fig2, use_container_width=True)

# ── Interactive table ─────────────────────────────────────────────────
st.subheader("🔍 Explore the Data")

selected = st.selectbox("Filter by category:", ["All"] + list(df["category"]))
if selected != "All":
    display_df = df[df["category"] == selected]
else:
    display_df = df

st.dataframe(
    display_df[[
        "category",
        "uk_imports_world_usd_billion",
        "india_exports_to_uk_usd_billion",
        "india_market_share_pct",
        "gap_usd_billion"
    ]].rename(columns={
        "category": "Category",
        "uk_imports_world_usd_billion": "UK Total Imports ($B)",
        "india_exports_to_uk_usd_billion": "India Supplies ($B)",
        "india_market_share_pct": "India Share (%)",
        "gap_usd_billion": "Gap ($B)"
    }),
    use_container_width=True,
    hide_index=True
)

st.caption("Data source: UN Comtrade & UK ONS Trade Statistics (2023)")