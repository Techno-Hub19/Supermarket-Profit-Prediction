import streamlit as st

st.title("Retail Profitability Prediction")

sales = st.number_input("Enter Sales")
discount = st.number_input("Enter Discount")

if st.button("Predict"):
    st.write("Prediction goes here")
