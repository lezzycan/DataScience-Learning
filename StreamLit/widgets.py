import streamlit as st

st.title("Streamlit Widgets innit?😂")

name = st.text_input("Enter your name:")

age = st.slider("Select your age:", 0,100,25)
st.write(age)

options = ['Python', "Java", "C++", "Javascript", "Flutter"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}.")
if name: 
    st.write(f"Hello, {name}")