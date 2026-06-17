import streamlit as st
from app.database import create_table, save_memory, get_memory
from app.tools import lookup_order, refund_policy

create_table()

st.title("Customer Support Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

message = st.text_input("Ask a question")

if st.button("Send"):

    st.session_state.messages.append(
        {"role": "user", "content": message}
    )

    user_message = message.lower()

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
        response = "I can help with your refund request."

    else:
        response = "How can I assist you today?"

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write(f"👤 You: {msg['content']}")
    else:
        st.write(f"🤖 Agent: {msg['content']}")