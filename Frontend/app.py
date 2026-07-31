import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pandas as pd
from streamlit_option_menu import option_menu
import pickle
from PIL import Image
import numpy as np
import plotly.figure_factory as ff
import streamlit as st
from code.DiseaseModel import DiseaseModel
from code.helper import prepare_symptoms_array
import seaborn as sns
import matplotlib.pyplot as plt
import joblib
import warnings
from sklearn.exceptions import InconsistentVersionWarning
import os
import streamlit.components.v1 as components
warnings.filterwarnings("ignore", category=InconsistentVersionWarning)


# loading the models
diabetes_model = joblib.load("models/diabetes_model.sav")
heart_model = joblib.load("models/heart_disease_model.sav")
parkinson_model = joblib.load("models/parkinsons_model.sav")
# Load the lung cancer prediction model
lung_cancer_model = joblib.load('models/lung_cancer_model.sav')


# Load the pre-trained model
chronic_disease_model = joblib.load('models/chronic_model.sav')

# Load the hepatitis prediction model
hepatitis_model = joblib.load('models/hepititisc_model.sav')


liver_model = joblib.load('models/liver_model.sav')# Load the lung cancer prediction model
lung_cancer_model = joblib.load('models/lung_cancer_model.sav')


# sidebar
from streamlit_option_menu import option_menu
import streamlit as st

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction', [
        'Disease Prediction',
        'Diabetes Prediction',
        'Heart disease Prediction',
        'Parkison Prediction',
        'Liver prediction',
        'Hepatitis prediction',
        'Lung Cancer Prediction',
        'Chronic Kidney prediction',
        'Get Affordable Medicine'  
    ],
    icons=['', 'activity', 'heart', 'person', 'person', 'person', 'person', 'bar-chart-fill','person' ,'cart'],
    default_index=0)


if selected == 'Get Affordable Medicine':
    st.title("🛒 Get Affordable Medicine")
    st.markdown(
        '[🛒 Click here to open Get Affordable Medicine Page](http://localhost:3000/home.html)',
        unsafe_allow_html=True
    )



# multiple disease prediction
if selected == 'Disease Prediction': 
    # Create disease class and load ML model
    disease_model = DiseaseModel()
    disease_model.load_xgboost('model/xgboost_model.json')

    # Title
    st.write('# Disease Prediction using Machine Learning')

    symptoms = st.multiselect('What are your symptoms?', options=disease_model.all_symptoms)

    X = prepare_symptoms_array(symptoms)

    # Trigger XGBoost model
    if st.button('Predict'): 
        # Run the model with the python script
        
        prediction, prob = disease_model.predict(X)
        st.write(f'## Disease: {prediction} with {prob*100:.2f}% probability')


        tab1, tab2= st.tabs(["Description", "Precautions"])

        with tab1:
            st.write(disease_model.describe_predicted_disease())

        with tab2:
            precautions = disease_model.predicted_disease_precautions()
            for i in range(4):
                st.write(f'{i+1}. {precautions[i]}')




# Diabetes prediction page
if selected == 'Diabetes Prediction':
    st.title("Diabetes disease prediction")
    image = Image.open('d3.jpg')
    st.image(image, caption='diabetes disease prediction')

    name = st.text_input("Name:")

    # MODE SELECT
    mode = st.radio("Select Input Mode:", ["Medical Values", "Symptoms (Recommended)"])

    # ------------------ MEDICAL MODE ------------------
    if mode == "Medical Values":
        col1, col2, col3 = st.columns(3)

        with col1:
            Pregnancies = st.number_input("Number of Pregnancies")
        with col2:
            Glucose = st.number_input("Glucose level")
        with col3:
            BloodPressure = st.number_input("Blood pressure value")

        with col1:
            SkinThickness = st.number_input("Skin thickness value")
        with col2:
            Insulin = st.number_input("Insulin value")
        with col3:
            BMI = st.number_input("BMI value")

        with col1:
            DiabetesPedigreefunction = st.number_input("Diabetes pedigree function")
        with col2:
            Age = st.number_input("Age")

        if st.button("Diabetes test result"):
            prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreefunction, Age]])

            if prediction[0] == 1:
                st.image(Image.open('positive.jpg'))
                st.error(name + ", High risk of Diabetes. Please consult a doctor.")
            else:
                st.image(Image.open('negative.jpg'))
                st.success(name + ", Low risk of Diabetes.")

    # ------------------ SYMPTOM MODE ------------------
    else:
        st.subheader("Answer simple questions")

        col1, col2 = st.columns(2)

        with col1:
            frequent_urination = st.checkbox("Frequent urination")
            excessive_thirst = st.checkbox("Excessive thirst")
            fatigue = st.checkbox("Fatigue")

        with col2:
            blurred_vision = st.checkbox("Blurred vision")
            weight_loss = st.checkbox("Sudden weight loss")
            slow_healing = st.checkbox("Slow healing wounds")

        Age = st.number_input("Age")

        if st.button("Check Diabetes Risk"):
            # DEFAULT VALUES
            glucose = 100
            bmi = 22
            insulin = 80
            skin = 20
            bp = 70
            dpf = 0.5
            preg = 0

            # MAPPING LOGIC
            if frequent_urination and excessive_thirst:
                glucose = 160

            if fatigue or weight_loss:
                bmi = 28

            if slow_healing:
                insulin = 150

            if blurred_vision:
                glucose += 20

            prediction = diabetes_model.predict([[preg, glucose, bp, skin, insulin, bmi, dpf, Age]])

            if prediction[0] == 1:
                st.image(Image.open('positive.jpg'))
                st.error(name + ", High risk based on symptoms. Get tested.")
            else:
                st.image(Image.open('negative.jpg'))
                st.success(name + ", Low risk based on symptoms.")
        
        



# Heart prediction page
if selected == 'Heart disease Prediction':
    st.title("Heart disease prediction")
    image = Image.open('heart2.jpg')
    st.image(image, caption='heart failure')

    name = st.text_input("Name:")

    # MODE SELECT
    mode = st.radio("Select Input Mode:", ["Medical Values", "Symptoms (Recommended)"])

    # ------------------ MEDICAL MODE ------------------
    if mode == "Medical Values":
        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.number_input("Age")
        with col2:
            sex = 0
            display = ("male", "female")
            options = list(range(len(display)))
            value = st.selectbox("Gender", options, format_func=lambda x: display[x])
            if value == "male":
                sex = 1
            else:
                sex = 0
        with col3:
            cp = 0
            display = ("typical angina","atypical angina","non-anginal pain","asymptomatic")
            options = list(range(len(display)))
            value = st.selectbox("Chest Pain Type", options, format_func=lambda x: display[x])
            cp = value

        with col1:
            trestbps = st.number_input("Resting Blood Pressure")
        with col2:
            chol = st.number_input("Serum Cholesterol")
        with col3:
            restecg = 0
            display = ("normal","ST-T abnormality","left ventricular hypertrophy")
            options = list(range(len(display)))
            value = st.selectbox("Resting ECG", options, format_func=lambda x: display[x])
            restecg = value

        with col1:
            thalach = st.number_input("Max Heart Rate Achieved")
        with col2:
            oldpeak = st.number_input("ST depression")
        with col3:
            slope = st.selectbox("Slope", [0,1,2])

        with col1:
            ca = st.number_input("Major vessels (0–3)")
        with col2:
            thal = st.selectbox("Thal", [0,1,2])
        with col3:
            exang = 1 if st.checkbox('Exercise induced angina') else 0

        fbs = 1 if st.checkbox('Fasting blood sugar > 120') else 0

        if st.button("Heart test result"):
            prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

            if prediction[0] == 1:
                st.image(Image.open('positive.jpg'))
                st.error(name + ", High risk of Heart Disease.")
            else:
                st.image(Image.open('negative.jpg'))
                st.success(name + ", Low risk of Heart Disease.")

    # ------------------ SYMPTOM MODE ------------------
    else:
        st.subheader("Answer simple questions")

        col1, col2 = st.columns(2)

        with col1:
            chest_pain = st.checkbox("Chest pain")
            breath_short = st.checkbox("Shortness of breath")
            fatigue = st.checkbox("Fatigue")

        with col2:
            dizziness = st.checkbox("Dizziness")
            sweating = st.checkbox("Excess sweating")
            nausea = st.checkbox("Nausea")

        age = st.number_input("Age")

        if st.button("Check Heart Risk"):
            # DEFAULT VALUES
            sex = 1
            cp = 0
            trestbps = 120
            chol = 200
            fbs = 0
            restecg = 0
            thalach = 150
            exang = 0
            oldpeak = 1
            slope = 1
            ca = 0
            thal = 1

            # MAPPING LOGIC
            if chest_pain:
                cp = 2
                exang = 1

            if breath_short:
                thalach = 120

            if fatigue:
                oldpeak = 2

            if dizziness or sweating:
                trestbps = 140

            if nausea:
                chol = 240

            prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

            if prediction[0] == 1:
                st.image(Image.open('positive.jpg'))
                st.error(name + ", High risk based on symptoms. Get checked.")
            else:
                st.image(Image.open('negative.jpg'))
                st.success(name + ", Low risk based on symptoms.")









if selected == 'Parkison Prediction':
    st.title("Parkison prediction")
    image = Image.open('p1.jpg')
    st.image(image, caption='parkinsons disease')
  # parameters
#    name	MDVP:Fo(Hz)	MDVP:Fhi(Hz)	MDVP:Flo(Hz)	MDVP:Jitter(%)	MDVP:Jitter(Abs)	MDVP:RAP	MDVP:PPQ	Jitter:DDP	MDVP:Shimmer	MDVP:Shimmer(dB)	Shimmer:APQ3	Shimmer:APQ5	MDVP:APQ	Shimmer:DDA	NHR	HNR	status	RPDE	DFA	spread1	spread2	D2	PPE
   # change the variables according to the dataset used in the model
    name = st.text_input("Name:")
    col1, col2, col3 = st.columns(3)
    with col1:
        MDVP = st.number_input("MDVP:Fo(Hz)")
    with col2:
        MDVPFIZ = st.number_input("MDVP:Fhi(Hz)")
    with col3:
        MDVPFLO = st.number_input("MDVP:Flo(Hz)")
    with col1:
        MDVPJITTER = st.number_input("MDVP:Jitter(%)")
    with col2:
        MDVPJitterAbs = st.number_input("MDVP:Jitter(Abs)")
    with col3:
        MDVPRAP = st.number_input("MDVP:RAP")

    with col2:

        MDVPPPQ = st.number_input("MDVP:PPQ ")
    with col3:
        JitterDDP = st.number_input("Jitter:DDP")
    with col1:
        MDVPShimmer = st.number_input("MDVP:Shimmer")
    with col2:
        MDVPShimmer_dB = st.number_input("MDVP:Shimmer(dB)")
    with col3:
        Shimmer_APQ3 = st.number_input("Shimmer:APQ3")
    with col1:
        ShimmerAPQ5 = st.number_input("Shimmer:APQ5")
    with col2:
        MDVP_APQ = st.number_input("MDVP:APQ")
    with col3:
        ShimmerDDA = st.number_input("Shimmer:DDA")
    with col1:
        NHR = st.number_input("NHR")
    with col2:
        HNR = st.number_input("HNR")
  
    with col2:
        RPDE = st.number_input("RPDE")
    with col3:
        DFA = st.number_input("DFA")
    with col1:
        spread1 = st.number_input("spread1")
    with col1:
        spread2 = st.number_input("spread2")
    with col3:
        D2 = st.number_input("D2")
    with col1:
        PPE = st.number_input("PPE")

    # code for prediction
    parkinson_dig = ''
    
    # button
    if st.button("Parkinson test result"):
        parkinson_prediction=[[]]
        # change the parameters according to the model
        parkinson_prediction = parkinson_model.predict([[MDVP, MDVPFIZ, MDVPFLO, MDVPJITTER, MDVPJitterAbs, MDVPRAP, MDVPPPQ, JitterDDP, MDVPShimmer,MDVPShimmer_dB, Shimmer_APQ3, ShimmerAPQ5, MDVP_APQ, ShimmerDDA, NHR, HNR,  RPDE, DFA, spread1, spread2, D2, PPE]])

        if parkinson_prediction[0] == 1:
            parkinson_dig = 'we are really sorry to say but it seems like you have Parkinson disease'
            image = Image.open('positive.jpg')
            st.image(image, caption='')
        else:
            parkinson_dig = "Congratulation , You don't have Parkinson disease"
            image = Image.open('negative.jpg')
            st.image(image, caption='')
        st.success(name+' , ' + parkinson_dig)



# Load the dataset
lung_cancer_data = pd.read_csv('data/lung_cancer.csv')

# Convert 'M' to 0 and 'F' to 1 in the 'GENDER' column
lung_cancer_data['GENDER'] = lung_cancer_data['GENDER'].map({'M': 'Male', 'F': 'Female'})

# Lung Cancer prediction page
if selected == 'Lung Cancer Prediction':
    st.title("Lung Cancer Prediction")
    image = Image.open('h.png')
    st.image(image, caption='Lung Cancer Prediction')

    # Columns
    # No inputs from the user
    name = st.text_input("Name:")
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender:", lung_cancer_data['GENDER'].unique())
    with col2:
        age = st.number_input("Age")
    with col3:
        smoking = st.selectbox("Smoking:", ['NO', 'YES'])
    with col1:
        yellow_fingers = st.selectbox("Yellow Fingers:", ['NO', 'YES'])

    with col2:
        anxiety = st.selectbox("Anxiety:", ['NO', 'YES'])
    with col3:
        peer_pressure = st.selectbox("Peer Pressure:", ['NO', 'YES'])
    with col1:
        chronic_disease = st.selectbox("Chronic Disease:", ['NO', 'YES'])

    with col2:
        fatigue = st.selectbox("Fatigue:", ['NO', 'YES'])
    with col3:
        allergy = st.selectbox("Allergy:", ['NO', 'YES'])
    with col1:
        wheezing = st.selectbox("Wheezing:", ['NO', 'YES'])

    with col2:
        alcohol_consuming = st.selectbox("Alcohol Consuming:", ['NO', 'YES'])
    with col3:
        coughing = st.selectbox("Coughing:", ['NO', 'YES'])
    with col1:
        shortness_of_breath = st.selectbox("Shortness of Breath:", ['NO', 'YES'])

    with col2:
        swallowing_difficulty = st.selectbox("Swallowing Difficulty:", ['NO', 'YES'])
    with col3:
        chest_pain = st.selectbox("Chest Pain:", ['NO', 'YES'])

    # Code for prediction
    cancer_result = ''

    # Button
    if st.button("Predict Lung Cancer"):
        # Create a DataFrame with user inputs
        user_data = pd.DataFrame({
            'GENDER': [gender],
            'AGE': [age],
            'SMOKING': [smoking],
            'YELLOW_FINGERS': [yellow_fingers],
            'ANXIETY': [anxiety],
            'PEER_PRESSURE': [peer_pressure],
            'CHRONICDISEASE': [chronic_disease],
            'FATIGUE': [fatigue],
            'ALLERGY': [allergy],
            'WHEEZING': [wheezing],
            'ALCOHOLCONSUMING': [alcohol_consuming],
            'COUGHING': [coughing],
            'SHORTNESSOFBREATH': [shortness_of_breath],
            'SWALLOWINGDIFFICULTY': [swallowing_difficulty],
            'CHESTPAIN': [chest_pain]
        })

        # Map string values to numeric
        user_data.replace({'NO': 1, 'YES': 2}, inplace=True)

        # Strip leading and trailing whitespaces from column names
        user_data.columns = user_data.columns.str.strip()

        # Convert columns to numeric where necessary
        numeric_columns = ['AGE', 'FATIGUE', 'ALLERGY', 'ALCOHOLCONSUMING', 'COUGHING', 'SHORTNESSOFBREATH']
        user_data[numeric_columns] = user_data[numeric_columns].apply(pd.to_numeric, errors='coerce')

        # Perform prediction
        cancer_prediction = lung_cancer_model.predict(user_data)

        # Display result
        if cancer_prediction[0] == 'YES':
            cancer_result = "The model predicts that there is a risk of Lung Cancer."
            image = Image.open('positive.jpg')
            st.image(image, caption='')
        else:
            cancer_result = "The model predicts no significant risk of Lung Cancer."
            image = Image.open('negative.jpg')
            st.image(image, caption='')

        st.success(name + ', ' + cancer_result)




# Liver prediction page
if selected == 'Liver prediction':  # pagetitle
    st.title("Liver disease prediction")
    image = Image.open('liver.jpg')
    st.image(image, caption='Liver disease prediction.')
    # columns
    # no inputs from the user
# st.write(info.astype(int).info())
    name = st.text_input("Name:")
    col1, col2, col3 = st.columns(3)

    with col1:
        Sex=0
        display = ("male", "female")
        options = list(range(len(display)))
        value = st.selectbox("Gender", options, format_func=lambda x: display[x])
        if value == "male":
            Sex = 0
        elif value == "female":
            Sex = 1
    with col2:
        age = st.number_input("Entre your age") # 2 
    with col3:
        Total_Bilirubin = st.number_input("Entre your Total_Bilirubin") # 3
    with col1:
        Direct_Bilirubin = st.number_input("Entre your Direct_Bilirubin")# 4

    with col2:
        Alkaline_Phosphotase = st.number_input("Entre your Alkaline_Phosphotase") # 5
    with col3:
        Alamine_Aminotransferase = st.number_input("Entre your Alamine_Aminotransferase") # 6
    with col1:
        Aspartate_Aminotransferase = st.number_input("Entre your Aspartate_Aminotransferase") # 7
    with col2:
        Total_Protiens = st.number_input("Entre your Total_Protiens")# 8
    with col3:
        Albumin = st.number_input("Entre your Albumin") # 9
    with col1:
        Albumin_and_Globulin_Ratio = st.number_input("Entre your Albumin_and_Globulin_Ratio") # 10 
    # code for prediction
    liver_dig = ''

    # button
    if st.button("Liver test result"):
        liver_prediction=[[]]
        liver_prediction = liver_model.predict([[Sex,age,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])

        # after the prediction is done if the value in the list at index is 0 is 1 then the person is diabetic
        if liver_prediction[0] == 1:
            image = Image.open('positive.jpg')
            st.image(image, caption='')
            liver_dig = "we are really sorry to say but it seems like you have liver disease."
        else:
            image = Image.open('negative.jpg')
            st.image(image, caption='')
            liver_dig = "Congratulation , You don't have liver disease."
        st.success(name+' , ' + liver_dig)






# Hepatitis prediction page
if selected == 'Hepatitis prediction':
    st.title("Hepatitis Prediction")
    image = Image.open('h.png')
    st.image(image, caption='Hepatitis Prediction')

    st.info("This prediction requires lab test values. Please enter values from your medical report.")

    name = st.text_input("Name:")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age")
        sex = st.selectbox("Gender", ["Male", "Female"])
        sex = 1 if sex == "Male" else 2
        alb = st.number_input("Albumin (ALB)")

    with col2:
        alp = st.number_input("Alkaline Phosphatase (ALP)")
        alt = st.number_input("Alanine Aminotransferase (ALT)")
        ast = st.number_input("Aspartate Aminotransferase (AST)")

    with col3:
        bil = st.number_input("Bilirubin (BIL)")
        che = st.number_input("Cholinesterase (CHE)")
        chol = st.number_input("Cholesterol (CHOL)")

    crea = st.number_input("Creatinine (CREA)")
    ggt = st.number_input("GGT")
    prot = st.number_input("Protein (PROT)")

    if st.button("Predict Hepatitis"):
        user_data = pd.DataFrame({
            'Age': [age],
            'Sex': [sex],
            'ALB': [alb],
            'ALP': [alp],
            'ALT': [alt],
            'AST': [ast],
            'BIL': [bil],
            'CHE': [che],
            'CHOL': [chol],
            'CREA': [crea],
            'GGT': [ggt],
            'PROT': [prot]
        })

        prediction = hepatitis_model.predict(user_data)

        if prediction[0] == 1:
            st.image(Image.open('positive.jpg'))
            st.error(name + ", High risk of Hepatitis. Please consult a doctor.")
        else:
            st.image(Image.open('negative.jpg'))
            st.success(name + ", Low risk of Hepatitis.")








from sklearn.preprocessing import LabelEncoder
import joblib


# Chronic Kidney Disease Prediction Page
if selected == 'Chronic Kidney prediction':
    st.title("Chronic Kidney Disease Prediction")

    name = st.text_input("Name:")

    mode = st.radio("Select Mode:", ["Medical Values", "Symptoms (Basic Screening)"])

    # ------------------ MEDICAL MODE ------------------
    if mode == "Medical Values":
        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.slider("Age", 1, 100, 25)
            al = st.slider("Albumin", 0, 5, 0)
            bgr = st.slider("Blood Glucose", 50, 200, 120)

        with col2:
            bp = st.slider("Blood Pressure", 50, 200, 120)
            su = st.slider("Sugar", 0, 5, 0)
            bu = st.slider("Blood Urea", 10, 200, 60)

        with col3:
            sg = st.slider("Specific Gravity", 1.0, 1.05, 1.02)
            sc = st.slider("Creatinine", 0, 10, 3)
            hemo = st.slider("Hemoglobin", 3, 17, 12)

        htn = 1 if st.selectbox("Hypertension", ["No","Yes"])=="Yes" else 0
        dm = 1 if st.selectbox("Diabetes", ["No","Yes"])=="Yes" else 0

        if st.button("Predict Kidney Disease"):
            df = pd.DataFrame({
                'age':[age],'bp':[bp],'sg':[sg],'al':[al],'su':[su],
                'rbc':[1],'pc':[1],'pcc':[0],'ba':[0],
                'bgr':[bgr],'bu':[bu],'sc':[sc],
                'sod':[140],'pot':[4],'hemo':[hemo],
                'pcv':[40],'wc':[10000],'rc':[4],
                'htn':[htn],'dm':[dm],'cad':[0],
                'appet':[1],'pe':[0],'ane':[0]
            })

            pred = chronic_disease_model.predict(df)

            if pred[0] == 1:
                st.image(Image.open('positive.jpg'))
                st.error(name + ", High risk of Kidney Disease.")
            else:
                st.image(Image.open('negative.jpg'))
                st.success(name + ", Low risk of Kidney Disease.")

    # ------------------ SYMPTOM MODE (NO ML) ------------------
    else:
        st.subheader("Basic Symptom Check (Not a medical diagnosis)")

        swelling = st.checkbox("Swelling in legs/feet")
        fatigue = st.checkbox("Fatigue")
        urination = st.checkbox("Changes in urination")
        nausea = st.checkbox("Nausea/Vomiting")
        appetite = st.checkbox("Loss of appetite")

        score = sum([swelling, fatigue, urination, nausea, appetite])

        if st.button("Check Risk"):
            if score >= 3:
                st.image(Image.open('positive.jpg'))
                st.warning(name + ", Possible risk. Please consult doctor.")
            else:
                st.image(Image.open('negative.jpg'))
                st.success(name + ", Low symptom-based risk.")


