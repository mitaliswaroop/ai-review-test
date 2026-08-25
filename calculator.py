# Testing the clean slate setup
def calculate_discount(price, discount_percent):
    unused_var = 100
    # Deliberate bug: dividing by 0
    return price - (price * (discount_percent / 0))
