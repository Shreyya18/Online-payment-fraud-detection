import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
df = pd.read_csv('data/transactions.csv')

# Convert 'Amount (INR)' to numerical value and handle missing values
df['Amount (INR)'] = pd.to_numeric(df['Amount (INR)'], errors='coerce').fillna(0)

# Convert 'Timestamp' to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'], format='%d-%m-%Y %H:%M')

# Create a 'fraudulent' column based on the Status
df['fraudulent'] = df['Status'].apply(lambda x: 1 if x == 'FAILED' else 0)

# Extract useful information from 'Timestamp'
df['Hour'] = df['Timestamp'].dt.hour
df['Day'] = df['Timestamp'].dt.day
df['Month'] = df['Timestamp'].dt.month
df['Year'] = df['Timestamp'].dt.year

# Drop the original 'Timestamp' column
df = df.drop(columns=['Timestamp'])

# Save the preprocessed data to 'processed_transactions.csv'
df.to_csv('data/processed_transactions.csv', index=False)

# Define features and target variable
features = ['Amount (INR)', 'Hour', 'Day', 'Month', 'Year']  # Using extracted features
X = df[features]
y = df['fraudulent']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
with open('model/fraud_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved successfully.")
