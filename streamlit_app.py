import streamlit as st
import pandas as pd

st.title("Welcome to TriniLand")
st.header("it's like Amazon, but just bettter")
st.text("TriniLand is a non-profit organization which focuses on the easy distribution of goods")
df = pd.DataFrame({
    '2023' [1],
    '2024' [2]
})
st.table(df)
if st.button("click me please"):
    st.write("thanks")
if st.checkbox("Early access"):
    st.write("It has been added to your list")

uChoice = st.radio("Choose one" ,["box", "cutter", "amazon"])
st.write("you selected" + " " + uChoice)

options = st.selectbox("Which model", ["x", "y", "z"])
st.write(f"thank you for chosing the model {options}")
ms = st.multiselect("color", ["red", "blue", "black", "yellow"])
st.write(f"Great choice, {ms} is a beautiful color")
slide = st.slider("Level of satisfaction", 0, 100)
st.write(f"Thank you for being {slide} satisfied with our service")
txt_input = st.text_input("write a bit")
st.write(f"that was {txt_input} right?")
txt_area = st.text_area ("write your sorrows here") 
st.write(f"your sorrows are {len(txt_area)} characters long, be happy now")
date_for_report = st.date_input("What is the date of your complaint bitch?")
st.write(f"so its {date_for_report} bitch")
uploaded_file = st.file_uploader('Upload a file')
if uploaded_file is not None:
    st.write('File uploaded successfully!')

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

col1, col2 = st.columns(2)
with col1:
    st.write("This is column 1")
with col2:
    st.write("This is column 2")

with st.expander("Expand for more"):
    st.write("Hidden content!")
