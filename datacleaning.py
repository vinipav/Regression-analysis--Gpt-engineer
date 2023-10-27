import pandas as pd
import streamlit as st
def clean_data(df):
    loan_data = df
    missing_values = loan_data.isnull().sum()
    st.header("Missing_values")
    st.write(missing_values)

    loan_data.fillna(df.median(), inplace=True)
    st.write("Filled the missing values with median")
    # Remove outliers from continuous variables
    # Calculate IQR for all columns
    
    Q1_loan = loan_data.quantile(0.25)
    Q3_loan = loan_data.quantile(0.75)
    IQR_loan= Q3_loan - Q1_loan

    # Define bounds for outliers
    lower_bound_loan = Q1_loan- 1.5 * IQR_loan
    upper_bound_loan = Q3_loan + 1.5 * IQR_loan

    # Identify outliers for each column
    outliers_advertising = {}
    for column in loan_data.columns:
        outliers = loan_data[(loan_data[column] < lower_bound_loan[column]) | 
                                    (loan_data[column] > upper_bound_loan[column])]
        outliers_loan[column] = len(outliers)
    st.header("Outliers")
    st.write(outliers_loan)

    