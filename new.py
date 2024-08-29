import streamlit as st
import joblib
import numpy as np

# Load the trained model from the local directory
model = joblib.load('linear_regression_model.pkl')

# Define the function to make predictions
def predict_price(engine_size):
    # Ensure the output is a scalar, not an array
    prediction = model.predict(np.array([[engine_size]]))
    return prediction.item()

# Streamlit app
def main():
    st.title("Car Price Prediction")

    st.write("Enter the engine size to predict the car price:")

    # Input from user
    engine_size = st.number_input("Engine Size (in liters)", min_value=0.0, step=0.1)

    # Predict button
    if st.button("Predict Price"):
        if engine_size > 0:
            price = predict_price(engine_size)
            st.write(f"The predicted price of the car is: ${price:,.2f}")
        else:
            st.write("Please enter a valid engine size.")

if __name__ == "__main__":
    main()
