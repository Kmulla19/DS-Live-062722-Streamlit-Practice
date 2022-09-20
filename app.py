import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("# SUP")

st.write("## Level Two Header")

st.write(("_italic text_"))

df = pd.read_csv("data/Austin_Animal_Center_intakes-091922.csv")

intake = st.radio(label="What intake type?", options=df['Intake Type'].unique())

segment_df = df.loc[df['Intake Type'] == intake]

type_counts = segment_df['Animal Type'].value_counts(normalize=True)

st.dataframe(sement_df)

# Version 1
fig, ax = plt.subplots()

ax.bar(x=type_counts.index, height=type_counts)

st.pyplot(fig)

# Version 2
st.bar_chart(type_counts)