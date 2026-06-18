import streamlit as st

from app.database import create_table, save_memory, get_memory
from app.tools import lookup_order, refund_policy
from app.bedrock_client import ask_bedrock

st.set_page_config(
    page_title="Customer Support Agent",
    page_icon="🤖"
)

create_table()

st.title("🤖 Customer Support Agent")
st.caption("AI-powered customer support assistant with memory, order lookup tools, and Amazon Bedrock.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask a question...")

if user_input:

    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.write(user_input)

    user_message = user_input.lower()

    if "my name is" in user_message:
        name = user_message.replace("my name is", "").strip()
        save_memory("customer_name", name)
        response = f"Nice to meet you, {name.title()}."

    elif "what is my name" in user_message or "what's my name" in user_message:
        name = get_memory("customer_name")

        if name:
            response = f"Your name is {name.title()}."
        else:
            response = "I do not know your name yet."

    elif "12345" in user_message:
        response = lookup_order("12345")

    elif "67890" in user_message:
        response = lookup_order("67890")

    elif "11111" in user_message:
        response = lookup_order("11111")

    elif "22222" in user_message:
        response = lookup_order("22222")

    elif "refund policy" in user_message:
        response = refund_policy()

    elif "order" in user_message:
        response = "Please provide your order number."

    elif "refund" in user_message:
        response = "I can help with your refund request. Please provide your order number."

    else:
        try:
            bedrock_response = ask_bedrock(user_input)

            if "Too many tokens per day" in bedrock_response:
                response = (
                    "Amazon Bedrock is currently unavailable because the daily token quota "
                    "has been reached. The agent can still help with customer memory, "
                    "order tracking, and refund enquiries."
                )
            else:
                response = bedrock_response

        except Exception as e:
            response = f"Bedrock connection error: {str(e)}"

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.write(response)