import random


def generate_random_float():
    # Random.random generates a number between 0 and 1.0
    # Multiply by 100 to get a value between 0 and 100
    number = random.random() * 100
    number = "%.2f" % number
    return float(number)