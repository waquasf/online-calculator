import streamlit as st

st.title("Online Calculator")

num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

operation = st.selectbox("Choose an operation", ["A", "S", "M", "D"])

if st.button("Calculate"):
    if operation == "A":
        result = num1 + num2
    elif operation == "S":
        result = num1 - num2
    elif operation == "M":
        result = num1 * num2
    elif operation == "D":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"

    st.success(f"Result: {result}")
