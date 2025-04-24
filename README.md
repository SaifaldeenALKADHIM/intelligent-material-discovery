# 🧠 Intelligent Material Discovery

This repository contains a full pipeline for discovering and evaluating materials for advanced applications using machine learning, explainable AI (SHAP), and real-world design constraints. It includes:

## 🔍 Features

- Multi-target property prediction (e.g. density, band gap, formation energy)
- SHAP-based feature importance visualization
- COMSOL/JSON export of top candidates
- Streamlit dashboard for real-time filtering and analysis

## 🚀 Streamlit App

You can deploy this app on [Streamlit Cloud](https://share.streamlit.io):

- Main file path: `streamlit_app.py`
- Requirements: see `requirements.txt`

## 📁 Structure

```
.
├── streamlit_app.py              # Streamlit dashboard
├── requirements.txt              # Required packages for app and model
├── README.md                     # This file
├── data/
│   └── materials_combined_dataset.csv   # Your input dataset
│   └── top_materials_export.csv         # Auto-generated predictions
└── notebooks/
    └── Intelligent_Material_Discovery_Engine.ipynb  # Full ML + SHAP workflow
```

## 🧪 Getting Started

Clone the repository and install dependencies:

```bash
pip install -r requirements.txt
```

Then run the Streamlit dashboard:

```bash
streamlit run streamlit_app.py
```

## 📬 Author

Saifaldeen ALKADHIM — [GitHub](https://github.com/SaifaldeenALKADHIM)
