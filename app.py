import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("# Adoption Prediction for Austin Animal Center")

st.write("## Describe the new intake:")

col_names = ['Color_black', 'Fixed', 'Type_Cat', 'Type_Dog', 'Intake Condition_Not Normal', 'Female', 'Young']

color = st.checkbox(label="Is the animal black?")

st.write(color)