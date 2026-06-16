import streamlit as st

st.title("Customer Support Agent")

if "customer_name" not in st.session_state:
    st.session_state.customer_name = None

message = st.text_input("Ask a question")

if st.button("Send"):
    user_message = message.lower()

    if "my name is" in user_message:
        name = message.lower().replace("my name is", "").strip()
        st.session_state.customer_name = name
        st.write(f"Nice to meet you, {name.title()}.")

    elif "what is my name" in user_message or "what's my name" in user_message:
        if st.session_state.customer_name:
            st.write(f"Your name is {st.session_state.customer_name.title()}.")
        else:
            st.write("I do not know your name yet.")

    elif "order" in user_message:
        st.write("Please provide your order number.")

    elif "refund" in user_message:
        st.write("I can help with your refund request.")

    else:
        st.write("How can I assist you today?")