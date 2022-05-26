from replit import clear
from art import logo 

print(logo)
print("Welcome to the secert auction program!")

bids = {}

bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder 
  print(f"The winnder is {winner} with a bid of ${highest_bid}.")
  
  
while not bidding_finished:
  name = input("What is your name? ").lower()
  price = int(input("What is your bidding price?$ "))
  bids[name] = price
  should_continue = input("Are there any bidders? Type 'Yes' or 'No': ")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
    

  
