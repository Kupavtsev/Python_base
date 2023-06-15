# for sms or email protection...
import random

def generate_secret_code():
    array_for_random = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    secret_array = random.sample(array_for_random, 5)
    secret_code = ""
    for number in secret_array:
        secret_code += str(number)
    return secret_code