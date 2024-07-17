from art import logo, vs
import random
from game_data import data
import os


def clear():
    os.system('clear' if os.name == 'posix' else 'cls')
counter=0

random1=random.choice(data)
random2=random.choice(data)

def format(account):
    return (f"{account['name']}, a {account['description']}, from {account['country']}")


print(logo)
print(f"Compare A: {format(random1)}")
print(vs)
print(f"Compare B: {format(random2)}")




 
