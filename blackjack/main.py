import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def play_game():
  print(logo)
  player_sum = 0
  com_sum = 0
  player_cards = []
  com_cards = []
  #first hand
  player_cards.append(random.choice(cards))
  player_cards.append(random.choice(cards))
  com_cards.append(random.choice(cards))

  player_sum = sum(player_cards)
  if player_sum > 21 and (11 in player_cards):
    player_sum -= 10
    player_cards.remove(11)
    player_cards.append(1)
  com_sum = sum(com_cards)
  
  while com_sum < 17:
    com_cards.append(random.choice(cards))
    com_sum = sum(com_cards)
    if com_sum > 21 and (11 in com_cards):
      com_sum -= 10
      com_cards.remove(11)
      com_cards.append(1)

  print(f"Your cards: {player_cards}, current score: {player_sum}")
  print(f"Computer's first card: {com_cards[0]}")

  while player_sum <= 21 and input("Type 'y' to get another card, type 'n' to pass: ").lower() == 'y':
    player_cards.append(random.choice(cards))
    player_sum = sum(player_cards)
    if player_sum > 21 and (11 in player_cards):
      player_sum -= 10
      player_cards.remove(11)
      player_cards.append(1)
    print(f"Your cards: {player_cards}, current score: {player_sum}")
    print(f"Computer's first card: {com_cards[0]}")

  if player_sum > 21:
    print("You go over. You lose. 😭")
    return
  print(f"Your final hand: {player_cards}, final score: {player_sum}")
  print(f"Computer's final hand: {com_cards}, final score: {com_sum}")

  if com_sum > 21:
    print("Computer goes over. You win. 🤯")
    return
  if player_sum > com_sum:
    print("You win. 😎") 
    return

  print("You lose. 😭")  

game_cont = True
while game_cont:
  game_begin = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if game_begin == 'y':
    clear()
    play_game()
  else:
    game_cont = False


