from replit import clear
from art import logo 
import random


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards."""
  if sum(cards) == 21 and len(cards) == 2:
    print("Black jack")
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.append(1)
    cards.remove(11)
  return sum(cards)

def compare(user_score, computer_score): 
  if user_score > 21 and computer_score > 21:
    return "You went over. You Lose!"
  
  if user_score == computer_score:
    return "DRAW"
  elif computer_score == 0: 
    return "You LOSE!, Opponent has BlackJack!"
  elif user_score == 0: 
    return "You Win with a BlackJack!"
  elif user_score > 21:
    return "YOU WENT OVER! You Lose!"
  elif computer_score > 21:
    return "Opponent went over. You Win!"
  else: 
    return "You Lose!"


def play_game():

  print(logo)

  user_cards = []
  computer_cards = []
  
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not is_game_over: 
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards is: {user_cards}, score is: {user_score}.")
    print(f" Computer first card is: {computer_cards[0]}.")
  
    if user_score == 0 or computer_score == 0 or user_score > 21: 
      is_game_over = True
    else:
      should_deal = input("Type 'Y' to draw a card, Type 'N' to pass: ").lower()
      if should_deal == "y":
        user_cards.append(deal_card())
      else: 
        is_game_over = True 
  
    while computer_score != 0  and computer_score <= 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)
  
    print(f" Your final hands: {user_cards}, final score: {user_score}.")
    print(f" Computer's final hand: {computer_cards}, final score: {computer_score}.")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'Y' or 'N': ").lower() == "y":
  clear()
  play_game()
    
