import streamlit as st
import pandas as pd

st.write("# SUP")

st.write("## Level Two Header")

st.write(("_italic text_"))

df = pd.read_csv("data/Austin_Animal_Center_intakes-091922.csv")

type_counts = df['Animal Type'].value_counts(normalize=True)

st.datafram(type_counts)