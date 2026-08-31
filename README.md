🏥 Care-Path-AI

Care-Path-AI is a healthcare application that combines a Node.js-based web application with a Streamlit machine learning application to provide disease prediction, prescription analysis, and generic medicine recommendations.

🚀 Features
🔍 Symptom-based disease prediction using Machine Learning
📄 Prescription analysis
💊 Generic medicine recommendations
🧠 Multiple machine learning disease prediction models
🌐 Node.js healthcare and medicine website
🖥️ Interactive Streamlit interface
📊 User-friendly healthcare dashboard
☁️ Cloud deployment using Streamlit Cloud and Render
🛠️ Tech Stack
Web Application
HTML
CSS
JavaScript
Node.js
Express.js
Machine Learning Application
Python
Streamlit
Scikit-learn
XGBoost
Pandas
NumPy
Joblib
Deployment
Streamlit Cloud
Render
GitHub
📁 Project Structure
Care-Path-AI/
│
├── Frontend/
│   │
│   ├── app.py                 # Streamlit application
│   │
│   ├── code/
│   │   ├── DiseaseModel.py
│   │   └── helper.py
│   │
│   ├── data/
│   │   └── Healthcare datasets
│   │
│   ├── models/
│   │   └── Machine learning models
│   │
│   └── website/
│       ├── frontend/
│       │   ├── assets/
│       │   ├── css/
│       │   ├── js/
│       │   └── HTML pages
│       │
│       ├── server.js
│       ├── package.json
│       └── data.json
│
├── Prescription/
├── requirements.txt
└── README.md
⚙️ Installation
1. Clone the repository
git clone <repository-url>
cd Care-Path-AI
2. Install Python dependencies
pip install -r requirements.txt
3. Install Node.js dependencies
cd Frontend/website
npm install
▶️ Running the Project Locally
Start the Node.js Website
cd Frontend/website
npm start

The website runs locally on port:
3000

Start the Streamlit Application

Open another terminal:

cd Frontend
python -m streamlit run app.py

The Streamlit application runs locally on port:
8501

🌐 Live Deployment: https://care-path-ai-cjjbzufu3es5twjitugrrh.streamlit.app/
💊 Medicine Website: https://care-path-ai.onrender.com/

The Node.js and Express medicine website is deployed using Render.

Open Live Medicine Website

🧠 Streamlit Application

The Streamlit application is deployed separately using Streamlit Cloud.

Streamlit deployment link here:
🔗 https://care-path-ai-cjjbzufu3es5twjitugrrh.streamlit.app/

The Streamlit application is connected to the deployed medicine website.

When users click:

Get Affordable Medicine

they are redirected from the Streamlit application to the live Node.js medicine website deployed on Render.

This allows the project to provide a complete healthcare workflow using:

Streamlit Machine Learning Application
              ↓
      Disease Prediction
              ↓
   Get Affordable Medicine
              ↓
Node.js / Express Medicine Website
📌 Usage
Open the Streamlit application.
Select healthcare prediction features.
Enter symptoms or required patient information.
Get machine learning-based predictions.
Analyze prescriptions when applicable.
Click Get Affordable Medicine.
Access the deployed medicine website.
Submit medicine-related information and track requests.
☁️ Deployment Architecture
GitHub Repository
       │
       ├──────────────► Streamlit Cloud
       │                    │
       │                    ▼
       │              ML Application
       │
       └──────────────► Render
                            │
                            ▼
                    Node.js / Express Website
🔮 Future Enhancements
🔐 User authentication and authorization
🗄️ Database integration
🤖 Improved machine learning models
💊 Larger generic medicine database
📅 Doctor appointment booking
📱 Improved mobile responsiveness
🔔 Notifications and request tracking
☁️ Full cloud-based architecture
👨‍💻 Author

Poreddy Pavan Kumar

GitHub: Pavan85Kumar on GitHub
