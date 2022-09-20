import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("# SUP")

st.write("## Level Two Header")

st.write(("_italic text_"))

df = pd.read_csv("data/Austin_Animal_Center_intakes-091922.csv")

type_counts = df['Animal Type'].value_counts(normalize=True)

fig, ax = plt.subplots()

ax.bar(x=type_counts.index, height=type_counts)

st.dataframe(type_counts)

st.pyplot(fig)