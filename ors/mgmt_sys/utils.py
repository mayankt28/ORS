import string
import random


def get_booking_id():
    data = string.digits
    code=""

    for i in range(1,11):
        code += random.choice(data)


    return int(code)


def get_password():
    data = string.ascii_letters + string.digits
    code=""

    for i in range(1,7):
        code += random.choice(data)

    return code
