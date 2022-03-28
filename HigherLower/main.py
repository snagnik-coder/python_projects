from art import logo, vs
import random
from replit import clear
from game_data import data

def game_run(score):
  print(logo)
  if score != 0:
    print(f"You're right! Current score: {score}")
  account_1 = random.choice(data)
  account_2 = random.choice(data)
  while account_1 == account_2:
    account_2 = random.choice(data)
  print(f"Compare A: {account_1['name']}, a {account_1['description']}, from {account_1['country']}.")
  print(vs)
  print(f"Against B: {account_2['name']}, a {account_2['description']}, from {account_2['country']}.")
  choice = input("Who has more followers? Type A or B: ").lower()
  if choice == "a" and account_1['follower_count'] >= account_2['follower_count']:
    score += 1
    clear()
    game_run(score)
  elif choice == "b" and account_1['follower_count'] <= account_2['follower_count']:
    score += 1
    clear()
    game_run(score)
  else:
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")

game_run(0) 