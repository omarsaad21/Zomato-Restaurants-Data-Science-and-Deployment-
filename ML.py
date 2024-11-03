import streamlit as st 
import pandas as pd
import plotly.express as px
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import plotly.graph_objects as go


# Title of the ML page
st.title("Machine Learning Models for Car Price Prediction")



# Overview paragraph
st.write("""
## Machine Learning Models for Restaurant Rating Prediction

In this section, we explore several machine learning classification algorithms to predict whether a restaurant is considered "good" based on its rating. The target variable is defined as `rate_flag`, where a rating greater than 3.75 is classified as "good" (1), and a rating of 3.75 or below is classified as "not good" (0).

The models used include Logistic Regression, Random Forest, and K-Nearest Neighbors. Each model has been trained on the available restaurant data and evaluated based on its accuracy. The goal is to find the most effective model for predicting restaurant quality, helping stakeholders make data-driven decisions regarding restaurant performance.

Below, you can explore the performance of each model, including their respective accuracies and classification reports.
""")



# Define a function to display model accuracies
def show_model_accuracies():
    # Example accuracies (replace with actual model accuracy results)
    accuracies = {
        "Logistic Regression": "81%",
        "Random forest classifer": "97%",
        "KNN":'91%',
        "Support Vector Machine": "50.5%",
        "Gradient Boosting":'84.5%'
    }
    
    st.write("### Model Accuracies")
    for model, accuracy in accuracies.items():
        st.write(f"{model}: {accuracy}")

# Button to show model accuracies
if st.button("Show Model Accuracies"):
    show_model_accuracies()