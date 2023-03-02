import streamlit as st

st.header("BMI Calculator")
height = st.slider('What is your height in inches?', 58,76)
weight = st.slider('What is your weight in lbs?', 98,500)
BMI = (weight/(height**2))*703

st.write('Your BMI is ',BMI)

if BMI<18.5:
    st.write('You are underweight')
elif 18.5<=BMI<=24.9:
    st.write('You are normal')
elif 25<=BMI<=29.9:
    st.write('You are overweight')
else:
    st.write('You are obese. Take Care!')
