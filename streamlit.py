import streamlit as st
import joblib
import pandas as pd


st.title('Prediction of Credit Card Upgrade')
st.text('This app was created by Ashwin Philip George for the module CET023.')
st.text('4 models are used in this app.')
 
GB_model = joblib.load("./models/gradient_boost_model")
DT_model = joblib.load("./models/decision_tree_model")
RFR_model = joblib.load("./models/random_forest_model")
LR_model = joblib.load("./models/linear_regression_model")

models = {'Gradient Boost Model': GB_model,
          'Decision Tree Model': DT_model,
          'Random Forest Model': RFR_model,
          'Logistic Regression Model': LR_model}

st.subheader("View Dataset here")
data_load_state = st.text('Loading data...')
data = pd.read_csv("./credit_card.csv")
data_load_state.text("Data has been loaded! Click the checkbox to see the data example.")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)



purchases = st.text_input('How many purchases has the user made?')

option = st.selectbox( 'Does the Person have a Supplementary Card?', ['Yes','No'])



def predictor(model,value,option):
    if option == 'Yes':
        option_value = 1
    else:
        option_value = 0
    prediction = model.predict([[value,option_value]])
    integer_value = int(prediction)
    if integer_value == 1:
        response = 'will be upgraded'
    else:
        response = 'will NOT be upgraded'
    return response

if st.button('Predict'):
    for key,item in models.items():
        answer = predictor(item,purchases,option)
        st.write('The ' + key+ ' predicts that the credit card of the user ' + answer)
    
    
    

