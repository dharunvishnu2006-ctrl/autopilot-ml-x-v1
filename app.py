import streamlit as st
import pandas as pd
from src.profiler import profile
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
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="gradient-title">🤖 AutoPilot ML X</div>', unsafe_allow_html=True)
st.markdown("v1 of 6 · Self-Healing MLOps Platform")