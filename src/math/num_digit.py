import random
"""
get digit length of a number.
"""

def get_digit(num: int):
    digit = 0
    while num > 0:
        digit += 1
        num = num // 10
    return digit

if __name__ == "__main__":
    num = 100#random.randint(10, 6000)
    print(f'{num} has {get_digit(num)} digits!')