orders = {
    "12345": "Your order is out for delivery and should arrive today.",
    "67890": "Your order has been shipped and will arrive in 2 working days.",
    "11111": "Your order is still being processed.",
    "22222": "Your order has been delivered."
}


def lookup_order(order_number):
    return orders.get(
        order_number,
        "Sorry, I could not find that order number. Please check and try again."
    )


def refund_policy():
    return "You can request a refund within 30 days if the item is unused and in its original packaging."