import streamlit as st
import pandas as pd
from src.profiler import profile
import random

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
    st.write("Profiler page - coming soon")
elif page == "About":
    st.write("About page - coming soon")