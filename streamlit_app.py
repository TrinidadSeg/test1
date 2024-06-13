import streamlit as st
import pandas as pd

# Title
st.title("Simple Streamlit App")

# Text
st.header("Welcome to my app!")
st.text("This is a simple Streamlit app to demonstrate the basics.")

# DataFrame
df = pd.DataFrame({
    'Name': ['John', 'Paul', 'George', 'Ringo'],
    'Instrument': ['Guitar', 'Bass', 'Guitar', 'Drums']
})
st.dataframe(df)

# Widgets
name = st.text_input("Enter your name:")
if st.button("Submit"):
    st.write(f"Hello, {name}!")

# Sidebar
with st.sidebar:
    st.header("Sidebar")
    option = st.selectbox('Choose a number', [1, 2, 3, 4])
    st.write(f"You selected: {option}")

# Media
st.image('path/to/image.jpg', caption='Sample Image', use_column_width=True)

# Layout
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1 content")
with col2:
    st.write("Column 2 content")

st.markdown("### Thank you for using this app!")
