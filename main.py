import streamlit as st
import pandas as pd
from datacleaning import clean_data
from model import train_model, calculate_metrics
from scaling import S_scaler

def main():
    st.title('Regression Model Trainer')
    
    uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])
    if uploaded_file is not None:
        input_df = pd.read_csv(uploaded_file)
        st.write(input_df.head())

        st.subheader('Data Cleaning')
        cleaned_df = clean_data(input_df)
        st.write(cleaned_df.head())
        
        st.subheader('Scaling')
        scaler_df = S_scaler(input_df)
        st.write(scaler_df.head())
        
        st.sidebar.subheader('Model Training')
        target = str(st.sidebar.text_input("Please enter the name of the target variable: "))
        st.sidebar.button("Generate")
        if target:
            if target=="sales":
                model = train_model(scaler_df)
                st.sidebar.subheader('Model Metrics')
                rmse, r2 = calculate_metrics(model, scaler_df)
                st.sidebar.write(f'RMSE: {rmse}')
                st.sidebar.write(f'R2: {r2}')
            else:
                st.sidebar.write("ERROR VALUE FOR TARGET VARIABLE")

if __name__ == "__main__":
    main()