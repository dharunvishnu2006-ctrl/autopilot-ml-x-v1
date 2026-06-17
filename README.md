# 🤖 AutoPilot ML X v1 — Async Data Ingestion & Profiling Engine

**The data engine of a self-healing MLOps platform.** Ingests CSV/JSON/Excel concurrently, auto-profiles any dataset, and exposes a Flask API — all wrapped in a clean `@pipeline` decorator.

![Python](https://img.shields.io/badge/Python-3.14-blue) ![asyncio](https://img.shields.io/badge/asyncio-concurrent-purple) ![Pandas](https://img.shields.io/badge/Pandas-data-orange) ![Flask](https://img.shields.io/badge/Flask-API-green) ![pytest](https://img.shields.io/badge/pytest-passing-brightgreen) ![Streamlit](https://img.shields.io/badge/Streamlit-deployed-red)

🔗 **Live demo:** https://autopilot-ml-x-v1-gprhnmfn2nhiemmsu8c6dp.streamlit.app/


## ✨ Features
- **Async Data Ingestion** — reads CSV/JSON/Excel files concurrently using `asyncio.gather`
- **Data Profiler** — auto-generates shape, dtypes, missing values, and statistical summary for any dataset
- **`@pipeline` Decorator** — clean, automatic START/DONE logging with timing for any function
- **Flask Upload API** — `/upload` endpoint validates files and returns the profile report as JSON
- **OOP Ingestor** — `AutoPilotIngestor` class ties ingestion + profiling into one clean, reusable interface

## 🚀 How to Run
```bash
git clone https://github.com/dharunvishnu2006-ctrl/autopilot-ml-x-v1.git
cd autopilot-ml-x-v1
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## 📚 What I Learned
*(Write this part yourself, in your own words — what genuinely felt new or tricky? Some ideas to draw from: asyncio.gather and concurrency, why @functools.wraps matters, debugging the `python -m` import path issue, building a decorator from scratch, connecting Flask to pandas, writing pytest tests for async code)*

## 🗺️ Roadmap
v1 of 6 — the data foundation of a self-healing MLOps platform.
Next: **v2** adds full Python ML mastery.

## 🔗 Links
- 💻 Code: https://github.com/dharunvishnu2006-ctrl/autopilot-ml-x-v1
- 🌐 Live App: https://autopilot-ml-x-v1-gprhnmfn2nhiemmsu8c6dp.streamlit.app/
