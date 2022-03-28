from replit import clear
from art import logo

print(logo)
print("Welcome to the Secret Auction")
check = True
bidders = {}

while check:
  name = input("What is your name? ")
  bid = float(input("What's your bid? $"))
  bidders[name] = bid
  cont = input("Are there any other bidders? Type 'yes' or 'no'. ")
  cont = cont.lower()
  if cont == "no":
    check = False
  clear()

name = ""
bid = 0.0
for bidder in bidders:
  if bid < bidders[bidder]:
    bid = bidders[bidder]
    name = bidder

print(f"The winner is {name} with a bid of ${bid}")