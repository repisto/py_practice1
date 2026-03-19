# random_pop2.py
import random

def random_pop(data):
    number = random.choice(data)
    data.remove(number)
    return number

a = [1,2,3,4,5]
while a:
    print(random_pop(a))
