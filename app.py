import streamlit as st
from main import get_answer

st.title('FAQ Q&A Bot')
st.subheader('Choose the Required FAQ service from the dropdown box')

options_dict = {
    "Aadhar": "data/Aadhar",
    "Ain India": "data/Airindia",
    "Amazon Sagemaker": "data/Amazon",
    "HDFC bank": "data/HDFC",
    "Seven HIlls Hospital": "data/Sevenhills",
    "TATA communications": "data/TATA"
}

# Sidebar for option selection
option = st.sidebar.selectbox(
    "Choose an option:",
    options=options_dict.keys()
)

question = st.text_input("Enter your question:")
selected_value = options_dict[option]

if st.button('Get Answer'):
    answer = get_answer(selected_value, question)
    st.write(f"**Question:** {question}")
    st.write(f"**Answer:** {answer}")
