from art import logo
from replit import clear
import random

print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
lives = 0
if difficulty == "easy":
  lives = 10
elif difficulty == "hard":
  lives = 5
else:
  print("INCORRECT INPUT")
  clear()

number = random.randint(1, 100)
guess = 0

while lives != 0:
  print(f"You have {lives} attempt to guess the number.")
  lives -= 1
  guess = int(input("Make a guess: "))
  if guess == number:
    print("You are correct!!! Congrats!")
    lives = 0
  elif guess > number:
    print("Too high.")
    print("Guess again")
  else:
    print("Too low.")
    print("Guess again")