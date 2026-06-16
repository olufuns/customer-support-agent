def support_agent(user_message):

    user_message = user_message.lower()

    if "refund" in user_message:
        return "I can help with your refund request."

    elif "order" in user_message:
        return "Please provide your order number."

    elif "delivery" in user_message:
        return "Your delivery is currently being processed."

    return "How can I assist you today?"