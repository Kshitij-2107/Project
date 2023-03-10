# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 14:18:43 2023

@author: Avanti
"""

import numpy as np
import pickle
import streamlit as st

#loading the model
loaded_model=pickle.load(open('C:/Users/sakshi/Desktop/Project/Telecommunication_churn.sav','rb'))

#creating a function for prediction
def churn_predict(input_data):
    
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print (prediction)
    if (prediction[0]==0):
        return 'Customer will not churn'
    else:
        return 'Customer will churn'
    
    
def main():
    #giving a title
    st.title('Telecom Customer Churn')
    #getting the input data from the user
    voice_plan=st.selectbox('Voice Plan (Yes/No)', ['1', '0'])
    intl_plan=st.selectbox('International plan (Yes/No)', ['1', '0'])
    customer_calls=st.text_input('Number of calls made to customer care')
    total_charge=st.text_input('Total Charge')
    
    #code for prediction
    Prediction=''
    #creating a button for prediction
    if st.button('PREDICT'):
        Prediction=churn_predict([voice_plan, intl_plan, customer_calls, total_charge])
    st.success(Prediction)


if __name__=='__main__':
    main()