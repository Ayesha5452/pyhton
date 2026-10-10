"""Exercise for calculating a discounted price."""


def calculate_discount(price, discount):
    """Return the final price after applying a percentage discount."""
    discount_amount = (price * discount) / 100
    final_price = price - discount_amount
    return final_price

