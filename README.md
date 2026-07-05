
---

# Public Transport Analytics 

This data engineering and machine learning pipeline automates the ETL, preprocessing, and feature engineering of raw public transport ridership data, culminating in predictive modeling and an interactive Streamlit dashboard for data visualization.

##  Overview
This project is a **data engineering and machine learning pipeline** for analyzing public transport ridership. It includes:
- ETL pipeline for raw ridership data
- Preprocessing and feature engineering
- Model training and prediction
- Interactive dashboard built with **Streamlit**

---

##  Project Structure
```
Public_Transport_Analytics/
│
├── data/
│   ├── raw/                # raw input CSVs (ridership data)
│   └── processed/          # cleaned/processed outputs
│
├── docs/                   # documentation, design notes
│
├── models/                 # trained ML models
│   └── ridership_model.pkl
│
├── notebooks/              # Jupyter notebooks for exploration
│   └── exploration.ipynb
│
├── src/
│   ├── __init__.py
│   ├── dashboard.py        # Streamlit dashboard
│   ├── data_loader.py      # functions to load CSVs
│   ├── main.py             # pipeline entry point
│   ├── predict.py          # prediction logic
│   ├── preprocess.py       # preprocessing functions
│   ├── run_pipeline.py     # orchestrates ETL + training
│   └── train.py            # training script
│
├── tests/
│   ├── test_data_loader.py
│   ├── test_preprocess.py
│   └── test_train.py
│
├── .gitignore
├── README.md
└── requirements.txt

```

---

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Public_Transport_Analytics.git
   cd Public_Transport_Analytics
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### 1. Prepare Data
Place your raw ridership CSV in:
```
data/raw/ridership.csv
```
Required columns:
- `date`
- `line`
- `station`
- `delay_minutes`
- `passengers` (only for training)

---

### 2. Train Model
Run:
```bash
python -m src.train
```
This will generate:
```
models/ridership_model.pkl
```

---

### 3. Run Dashboard
Start Streamlit:
```bash
python -m streamlit run src/dashboard.py
```
Upload a CSV with:
- `date`
- `line`
- `station`
- `delay_minutes`

The dashboard will drop `passengers` automatically and show predictions.

---

## 📓 Exploration Notebook
Open:
```bash
jupyter notebook notebooks/exploration.ipynb
```
This notebook demonstrates:
- Data loading
- Preprocessing
- Exploratory plots
- Correlation analysis

---

## 🧪 Testing
Run unit tests:
```bash
pytest tests/
```

---


