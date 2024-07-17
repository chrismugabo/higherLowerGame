from art import logo, vs
import random
from game_data import data
import os

print(logo)
end_of_game = False
current_score = 0

def clear_screen():
    os.system('clear')
    print(logo)

def game_score():
    global current_score
    print(f"You are right! Current score: {current_score}")

def play(random1, random2):
    print(f"Compare A: {random1['name']}, a {random1['description']} from {random1['country']}")
    print(vs)
    print(f"Against B: {random2['name']}, a {random2['description']} from {random2['country']}")

def compare(random1, random2, guess):
    global current_score, end_of_game
    if (guess == "a" and random1['follower_count'] > random2['follower_count']) or \
       (guess == "b" and random2['follower_count'] > random1['follower_count']):
        current_score += 1
        clear_screen()
        game_score()
        return random2, random.choice(data)
    else:
        end_of_game = True
        clear_screen()
        print(f"Sorry, that's wrong. Final score: {current_score}")
        return None, None

random1, random2 = random.choice(data), random.choice(data)
while not end_of_game:
    play(random1, random2)
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    random1, random2 = compare(random1, random2, choice)
    if random1 is None or random2 is None:
        break
    while random2 == random1:
        random2 = random.choice(data)





 