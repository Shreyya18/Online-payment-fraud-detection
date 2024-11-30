import pandas as pd

# Load data
df = pd.read_csv('data/processed_transactions.csv')
print("Data loaded:")
print(df.head())  # Print the first few rows of the dataframe

def check_fraudulent_upi(upi_id):
    print(f"Checking UPI ID: {upi_id}")  # Debug print statement
    if upi_id in df['Receiver UPI ID'].values:
        is_fraudulent = df[df['Receiver UPI ID'] == upi_id]['fraudulent'].values[0] == 1
        print(f"Is fraudulent: {is_fraudulent}")  # Debug print statement
        return is_fraudulent
    else:
        print(f"UPI ID: {upi_id} not found in the dataset.")  # Debug print statement
    return False

def add_fraudulent_upi(upi_id):
    print(f"Adding fraudulent UPI ID: {upi_id}")  # Debug print statement
    global df
    # Check if UPI ID already exists
    if upi_id in df['Receiver UPI ID'].values:
        df.loc[df['Receiver UPI ID'] == upi_id, 'fraudulent'] = 1
    else:
        new_data = {'Receiver UPI ID': upi_id, 'fraudulent': 1}
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
    
    df.to_csv('data/processed_transactions.csv', index=False)
    print(f"UPI ID {upi_id} flagged as fraudulent and updated in the dataset.")  # Debug print statement
    # Reload the data to ensure it's updated
    df = pd.read_csv('data/processed_transactions.csv')
