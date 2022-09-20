import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("# Adoption Prediction for Austin Animal Center")

st.write("## Describe the new intake:")

col_names = ['Color_black', 'Fixed', 'Type_Cat', 'Type_Dog', 'Intake Condition_Not Normal', 'Female', 'Young']

color = st.checkbox(label="Is the animal black?")

fixed = st.checkbox(label="Is the animal fixed?")

type = st.radio(label='What type of animal?', options=['Dog', 'Cat', 'Other'])

if type == 'Dog':
    dog_type = True
    cat_type = False
elif type == 'Cat':
    cat_type = True
    dog_type = False
else:
    cat_type = False
    dog_type = False

condition = st.checkbox(label="Is the intake condition not normal")

female = st.checkbox(label="Is the animal female?")

young = st.checkbox(label="Is the animal young?")

input_row = [color, fixed, cat_type, dog_type, condition, female, young]

input = pd.DataFrame(dict(zip(used_cols, input_row)), index=[0])
st.write(input)