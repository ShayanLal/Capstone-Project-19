import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title = 'Early Diabetes Prediction Web App',
                    page_icon = 'random',
                    layout = 'wide',
                    initial_sidebar_state = 'auto'
                    )

@st.cache()
def load_data():

    data_file = "diabetes_main.csv"
    df = pd.read_csv(data_file, header=None)
    df.head()

    df.rename(columns = {"BloodPressure": "Blood_Pressure",}, inplace = True)
    df.rename(columns = {"SkinThickness": "Skin_Thickness",}, inplace = True)
    df.rename(columns = {"DiabetesPedigreeFunction": "Pedigree_Function",}, inplace = True)

    df.head() 

    return df

diabetes_df = load_data()

import diabetes_predict
import diabetes_home
import diabetes_plots

pages_dict = {"Home": diabetes_home, 
        "Predict Diabetes": diabetes_predict, 
        "Visualise Decision Tree": diabetes_plots}
title = st.sidebar.title("Navigation")
user_choice = st.sidebar.radio("Go to", ("Home", "Predict Diabetes", "Visualise Decision Tree"))