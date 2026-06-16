from memory import save_memory, get_memory

def handle_user_input(user_input):

    # extract name (simple rule or LLM extraction)
    if "my name is" in user_input.lower():
        name = user_input.split("is")[-1].strip()
        save_memory("name", name)
        return f"Got it. I'll remember your name is {name}."

    # retrieval test
    if "what is my name" in user_input.lower():
        name = get_memory("name")
        if name:
            return f"Your name is {name}"
        return "I don't know your name yet."

    return "How can I help you?"