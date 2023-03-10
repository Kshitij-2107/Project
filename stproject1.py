# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 22:44:48 2023

@author: kshitij
"""
import numpy as np
import pickle
import streamlit as st

#Loading the saved model
loaded_model = pickle.load(open('C:/Users/sakshi/Desktop/Project/trained_model1.pkl', 'rb'))

def customer_churn(input_data):


    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)

    if (prediction[0] == 0):
        return 'The customer will not churn'
    else:
        return 'The customer will churn'
    

def main():
    
    #title
    st.title('Customer Churn Prediction')
    
    #getting input data from user
    
    
    voice_plan = st.selectbox('Voice Plan', ['1', '0'])
    intl_plan = st.selectbox('International Plan', ['1', '0'])
    customer_calls = st.text_input('Customer calls')
    total_charge = st.text_input('Total Charges')
    
    
    #code for prediction
    telecom = ''
    
    #creating a button for prediction
    
    if st.button('Predict'):
        telecom = customer_churn([voice_plan, intl_plan, customer_calls, total_charge])
        
        
    st.success(telecom)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    