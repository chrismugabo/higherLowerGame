from art import logo
from art import vs
print(logo)
import random
from game_data import data
 
# def compare(guess):

random1=random.choice(data)
print(f"Compare A: {random1['name']}, a {random1['description']} from {random1['country']} " )
print(vs)
random2=random.choice(data)
print(f"Against B: {random2['name']}, a {random2['description']} from {random2['country']} " )

choice=input("Who has more followers? Type 'A' or 'B':")





 