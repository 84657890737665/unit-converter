# Imports 
import streamlit as st 


# Set up the Application 
st.title("Unit Swap 🔁")
st.markdown("### A One Step Conversion Solution!")  
st.write(" Select a Category to get the real-time Result!!!")

    # Category Selection
category = st.selectbox("Choose One", [ "Height Converter", "Weight Converter" , "Temperature Converter"])


    # 1. Height Converter

def convert_height(value, from_unit, to_unit):
    conversion_factors = {
        "meter":0.001,
        "feet": 3.281,
        "inches": 39.37,
        "centimeters": 0.03281,
        "kilograms":1,
        "pounds": 2.20462,
        "ounces": 35.274,
        "celsius":1,
        "fahrenheit": 9/5 + 32,
        "kelvin": 273.15
    }    
    return value * conversion_factors[to_unit] / conversion_factors[from_unit]


value = st.number_input("Enter Value to Convert", min_value=0.0, format = "%.2f")
from_unit = st.selectbox("From", ["meter", "feet", "inches", "centimeters", "kilograms", "pounds", "ounces", "celsius", "fahrenheit", "kelvin"])
to_unit = st.selectbox("To", ["meter", "feet", "inches", "centimeters", "kilograms", "pounds", "ounces", "celsius", "fahrenheit", "kelvin"])


if st.button("Convert"):
    result = convert_height(value, from_unit, to_unit)
    st.success(f"Converted Result: {result:.2f} {to_unit}")



