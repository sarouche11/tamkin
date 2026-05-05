import random
import string

def numeric_challenge():
    print("CAPTCHA LOADED")
    value = ''.join(random.choices(string.digits, k=6))
    return value, value