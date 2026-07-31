# Care-Path-AI

Care-Path-AI is a healthcare application that combines a **Node.js-based website** with a **Streamlit application** to provide disease prediction, prescription analysis, and generic medicine recommendations using machine learning.

---

## Features

- 🔍 Symptom-based disease prediction using Machine Learning
- 📄 Prescription analysis
- 💊 Generic medicine recommendations
- 🌐 Responsive website for navigation
- 🖥️ Interactive Streamlit interface for predictions
- 📊 User-friendly dashboard and healthcare tools

---

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript
- Node.js

### Machine Learning Application
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

---

## Project Structure

```
Care-Path-AI/
│
├── Frontend/
│   ├── website/
│   │   ├── server.js
│   │   ├── package.json
│   │   └── ...
│   ├── app.py
│   └── ...
│
├── Prescription/
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Pavan85Kumar/Care-Path-AI.git
cd Care-Path-AI
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Node.js dependencies

```bash
cd Frontend/website
npm install
```

---

## Running the Project

### Start the Website

```bash
cd Frontend/website
npm start
```

The website will be available at:

```
http://localhost:3000
```

### Start the Streamlit Application

Open a second terminal:

```bash
cd Frontend
python -m streamlit run app.py
```

The Streamlit application will be available at:

```
http://localhost:8501
```

> **Note:** Keep both the Node.js server and the Streamlit application running. The website connects to the Streamlit application to provide the complete user experience.

---

## Usage

1. Start both the Node.js website and the Streamlit application.
2. Open **http://localhost:3000**.
3. Navigate through the website.
4. Access the Streamlit application to:
   - Predict diseases based on symptoms.
   - Analyze prescriptions.
   - View generic medicine recommendations.

---

## Future Enhancements

- User authentication
- Expanded disease prediction models
- Larger medicine database
- Cloud deployment
- Appointment booking integration

---

## Author

*Poreddy Pavan Kumar**

GitHub: https://github.com/Pavan85Kumar
**Poreddy Pavan Kumar**

GitHub: https://github.com/Pavan85Kumar
