import streamlit as st
import pandas as pd
from src.profiler import profile
import random
import altair as alt

st.set_page_config(page_title="AutoPilot ML X", page_icon="🤖", layout="wide")
st.markdown("""
<style>
.stApp {
    background-color: #0a0e27;
}
.gradient-title {
    background: linear-gradient(90deg, #fbbf24, #a855f7, #22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 3rem;
    font-weight: 800;
}
.star {
    position: absolute;
    width: 4px;
    height: 4px;
    border-radius: 50%;
    background: radial-gradient(circle, #ffffff, transparent);
    animation: twinkle 2s infinite;        
} 
@keyframes twinkle {
    0% { opacity: 0.2; }
    50% { opacity: 1; }
    100% { opacity: 0.2; }
}
[data-testid="stMetric"] {
    background: rgba(168, 85, 247, 0.08);
    border: 1px solid #a855f7;
    border-radius: 12px;
    padding: 16px;
    box-shadow: 0 0 12px rgba(34, 211, 238, 0.4);
}            
                                   
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="gradient-title">🤖 AutoPilot ML X</div>', unsafe_allow_html=True)
st.markdown("v1 of 6 · Self-Healing MLOps Platform")

stars_html = ""
for i in range(18):
    top = random.randint(0, 800)
    left = random.randint(0, 1800)
    delay = random.uniform(0, 2)
    stars_html += f'<div class="star" style="top:{top}px; left:{left}px; animation-delay:{delay}s;"></div>'

st.markdown(stars_html, unsafe_allow_html=True)
page = st.sidebar.radio("Navigate", ["Dashboard", "Profiler", "About"])

if page == "Dashboard":
    st.write("Dashboard page - coming soon")
elif page == "Profiler":
    st.markdown('<div class="gradient-title" style="font-size:2rem;">📊 Data Profiler</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload a dataset", type=["csv", "json", "xlsx"])

    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(".json"):
            df = pd.read_json(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.write(df.head())
        report = profile(df)
        total_missing = sum(report["missing_values"].values())

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Files Ingested", 1)
        with col2:
            st.metric("Rows Profiled", report["rows"])
        with col3:
            st.metric("Missing Values Found", total_missing)

        st.json(report)
        missing_df = pd.DataFrame({
            "column": list(report["missing_values"].keys()),
            "missing_count": list(report["missing_values"].values())
        })

        chart = alt.Chart(missing_df).mark_bar(color="#a855f7").encode(
            x="column",
            y="missing_count"
        )

        st.altair_chart(chart, use_container_width=True)
elif page == "About":
    st.write("About page - coming soon")