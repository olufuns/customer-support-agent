import streamlit as st
from app.agent import support_agent

st.set_page_config(page_title="Customer Support Agent")

st.title("Customer Support Agent")

message = st.text_input("Ask a question")

if st.button("Send"):

    response = support_agent(message)

    st.write(response)