import streamlit as st



st.title("Power Calculator")
st.write("Enter the number to calculate its power.")

n=st.number_input("Enter a number:", value=1,step=1)

square = n ** 2
cube = n ** 3
fourth_power = n ** 4
fifth_power = n ** 5

st.write(f"Square of {n} is {square}")
st.write(f"Cube of {n} is {cube}")
st.write(f"Fourth Power of {n} is {fourth_power}")
st.write(f"Fifth Power of {n} is {fifth_power}")




