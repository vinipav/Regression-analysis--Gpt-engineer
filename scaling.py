import pandas as pd
from sklearn.preprocessing import StandardScaler

def S_scaler(df):
    loan_data = df
# Initialize the standard scaler
    scaler = StandardScaler()

    # Apply standard scaling to the dataset
    sales_scaled = scaler.fit_transform(loan_data)

    # Convert the scaled data back to a DataFrame for better visualization
    sales_scaled_df = pd.DataFrame(sales_scaled, columns=loan_data.columns)


    scaler_df = sales_scaled_df  

    return scaler_df