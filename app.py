import streamlit as st
import joblib

model = joblib.load("D:/Project/Supermarket-Profit-Prediction/Models/logistic_model.pkl")
scaler = joblib.load("D:/Project/Supermarket-Profit-Prediction/Models/scaler.pkl")

st.title("Retail Profitability Predictor")

sales = st.number_input("Sales", min_value=0.0)
discount = st.number_input("Discount", min_value=0.0, max_value=1.0)

if st.button("Predict"):

    input_data = [[sales, discount]]

    # Scale before prediction
    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)
    probabilities = model.predict_proba(input_scaled)
    
    prob_dict = {
    "Not Profitable": f"{probabilities[0][0] * 100:.2f}%",
    "Profitable": f"{probabilities[0][1] * 100:.2f}%"
}

    st.write(prob_dict)

    if prediction[0] == 1:
        st.success("Order is likely to be Profitable")
    else:
        st.error("Order is likely to be Not Profitable")