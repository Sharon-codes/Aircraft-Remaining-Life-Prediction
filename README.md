# ✈️ Aircraft Remaining Useful Life Prediction

### 🌐 Live Demo: [Deployed on Render](https://aircraft-remaining-life-prediction.onrender.com)

---

## 📖 Introduction

Turbofan engines are the "heart" of modern aircraft. Approximately 60% of all aircraft faults are related to turbofan engine issues. Predicting the **Remaining Useful Life (RUL)** of these engines is crucial for:

- ✅ **Predictive Maintenance** - Schedule maintenance before failures occur
- ✅ **Cost Reduction** - Minimize unplanned downtime and repair costs
- ✅ **Safety Enhancement** - Prevent catastrophic engine failures

This project uses **Machine Learning** to predict the RUL of turbofan engines based on sensor data from NASA's C-MAPSS (Commercial Modular Aero-Propulsion System Simulation) dataset.

![Turbofan Engine](https://evolution.skf.com/wp-content/uploads/sites/5/2016/11/16-4-aerospace-fig-5-en.jpg)

---

## 🚀 Quick Start

### Clone this repository:
```bash
git clone https://github.com/Sharon-codes/Aircraft-Remaining-Life-Prediction.git
cd Aircraft-Remaining-Life-Prediction
```

### Create virtual environment:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

### Run the application:
```bash
python app.py
```

### Open in browser:
```
http://localhost:5000
```

---

## 🎯 Features

| Feature | Description |
|---------|-------------|
| 🎨 **Aviation-Themed UI** | Modern, dark futuristic design with glassmorphism effects |
| 📊 **RUL Prediction** | Predict remaining operational cycles based on 14 sensor readings |
| 📈 **Health Status** | Visual indicators for engine health (Good/Monitor/Critical) |
| 📱 **Responsive Design** | Works on desktop, tablet, and mobile devices |
| ⚡ **Fast Predictions** | Sub-second response time |

---

## 📊 Dataset

This project uses NASA's **C-MAPSS Turbofan Engine Degradation Simulation Dataset**:

- **100+ engines** simulated from healthy to failure
- **21 sensor measurements** per engine cycle
- **14 key sensors** selected after feature engineering
- **Run-to-failure data** for training RUL prediction models

### Sensor Parameters:

| Sensor | Description | Typical Range |
|--------|-------------|---------------|
| sensor2 | LPC Outlet Temperature | 641 - 644 °R |
| sensor3 | HPC Outlet Temperature | 1580 - 1610 °R |
| sensor4 | LPT Outlet Temperature | 1390 - 1435 °R |
| sensor7 | HPC Outlet Pressure | 550 - 556 psia |
| sensor8 | Physical Fan Speed | 2387 - 2389 rpm |
| sensor9 | Physical Core Speed | 9033 - 9200 rpm |
| sensor11 | HPC Static Pressure | 46.9 - 48.5 psia |
| sensor12 | Fuel Flow Ratio | 519 - 523 pps/psi |
| sensor13 | Corrected Fan Speed | 2387 - 2389 rpm |
| sensor14 | Corrected Core Speed | 8110 - 8260 rpm |
| sensor15 | Bypass Ratio | 8.35 - 8.55 |
| sensor17 | Bleed Enthalpy | 389 - 400 |
| sensor20 | HPT Coolant Bleed | 38.3 - 39.3 lbm/s |
| sensor21 | LPT Coolant Bleed | 22.9 - 23.6 lbm/s |

---

## 🏗️ Tech Stack

| Category | Technology |
|----------|------------|
| **Backend** | Python, Flask |
| **ML/AI** | Scikit-Learn, Pandas, NumPy |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Fonts** | Google Fonts (Orbitron, Inter) |
| **Icons** | Font Awesome |
| **Deployment** | Render / Gunicorn |

---

## 📁 Project Structure

```
Aircraft-Remaining-Life-Prediction/
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
├── Procfile                  # Deployment configuration
├── runtime.txt               # Python version
├── setup.py                  # Package setup
│
├── templates/                # HTML templates
│   ├── header.html          # Base template with styling
│   ├── index.html           # Home page
│   └── predict.html         # Prediction page
│
├── saved_models/            # Trained ML models
│   └── [timestamp]/
│       └── model.pkl
│
├── Turbofan/                # ML Pipeline modules
│   ├── component/           # Pipeline components
│   ├── config/              # Configuration
│   ├── entity/              # Data entities
│   ├── exception/           # Custom exceptions
│   ├── logger/              # Logging
│   └── util/                # Utilities
│
└── config/                  # YAML configurations
    ├── config.yaml
    ├── model.yaml
    └── schema.yaml
```

---

## 🧪 Model Performance

| Model | Accuracy | R² Train | R² Test |
|-------|----------|----------|---------|
| Linear Regression | 79.80% | 82.82% | 76.99% |
| SVR (linear) | 79.62% | 82.74% | 76.73% |
| Random Forest | 84.06% | 98.79% | 73.15% |
| **KNN (Final)** | **81.94%** | **90.38%** | **74.93%** |
| XGBoost | 74.69% | 98.99% | 59.97% |

The **K-Nearest Neighbors Regressor** was selected as the final model due to its balance between accuracy and generalization.

---

## 🔗 Resources

- [NASA C-MAPSS Dataset](https://www.kaggle.com/datasets/behrad3d/nasa-cmaps)
- [Turbofan Engine - Wikipedia](https://en.wikipedia.org/wiki/Turbofan)
- [Scikit-Learn Documentation](https://scikit-learn.org/)

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Credits

- Original ML Pipeline: [Vinayakmane47](https://github.com/Vinayakmane47/NASA-turbofan-ML-Project-AIOPS)
- UI/UX Redesign & Deployment: Sharon

---

<p align="center">
  Made with ❤️ for Aviation Safety
</p>
