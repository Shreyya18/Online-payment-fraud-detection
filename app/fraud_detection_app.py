import streamlit as st
import pickle
from utils import check_fraudulent_upi, add_fraudulent_upi

# Load model
model = pickle.load(open('model/fraud_model.pkl', 'rb'))

st.title("Online Payment Fraud Detection")

# Input for UPI ID or Phone Number
upi_id = st.text_input("Enter Receiver's UPI ID or Phone Number")

# Button to check if the UPI ID is fraudulent
check_button = st.button("Check")

if check_button:
    if check_fraudulent_upi(upi_id):
        st.error("Fraudulent UPI ID!")
    else:
        st.success("Safe Transaction")

# Button to flag a UPI ID as fraudulent
flag_button = st.button("Flag as Fraudulent")

if flag_button:
    add_fraudulent_upi(upi_id)
    st.warning("UPI ID flagged as fraudulent and updated in the dataset.")
