import streamlit as st

st.title("web app")
x = st.slider("x")
st.title("{} squared is {}".format(x, x*x))