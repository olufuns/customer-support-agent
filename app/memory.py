import streamlit as st

def init_memory():
    if "memory_store" not in st.session_state:
        st.session_state.memory_store = {}

def save_memory(key, value):
    init_memory()
    st.session_state.memory_store[key] = value

def get_memory(key):
    init_memory()
    return st.session_state.memory_store.get(key)

def get_all_memory():
    init_memory()
    return st.session_state.memory_store