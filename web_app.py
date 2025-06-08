import streamlit as st
st.title("Hello Arya!")
st.header("Header")
st.subheader("Sub Header")

check_on = st.checkbox("Check Me!")
if(check_on):
    st.write("Checkbox is checked")

name = st.text_input("Enter Your Name")
if(name) :
    st.write(f"hello {name}")

import pandas as pd
data = pd.read_csv("iris_data.csv")
#print(data)
import plotly.express as px
fig = px.scatter(data, x="SepalLengthCm", y="SepalWidthCm", color="Species")
st.plotly_chart(fig, use_container_width=True)