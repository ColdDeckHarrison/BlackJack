from replit import clear
import random
from art import logo
def play_game():
  print(logo)
  user_cards = []
  dealer_cards = []

  def deal_cards():
      cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
      card = random.choice(cards)
      return card

  def calculate_score(cards):
    return sum(cards)
    if sum(cards) == 21 and len(cards) == 2:
      return 0
    
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
          
  def compare(user_score, computer_score):
      if computer_score == 0:
        return "BlackJack, Dealer Wins"
      elif user_score > 21:
        return "You Bust, Dealer Wins"
      elif user_score == computer_score:
        return "It's a Draw"
      elif user_score == 0 and computer_score != 0:
        return "BlackJack, You Win!" 
      elif user_score > computer_score:
        return "You Win!"
      elif computer_score > 21:
        return "Dealer Busts, You Win"
      else:
        return "Dealer Wins"
      
  user_cards = []
  dealer_cards = []
  is_game_over = False


  for _ in range(2):
    user_cards.append(deal_cards())
    dealer_cards.append(deal_cards())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(dealer_cards)
    print(f" Your cards {user_cards}, current score {user_score}")
    print(f" Dealer's card {dealer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      draw_card = input("Draw another card? 'y' or 'n'")
      if draw_card == 'y':
        user_cards.append(deal_cards()) 
      else:
        is_game_over = True
  while computer_score != 0 and computer_score < 17:
    dealer_cards.append(deal_cards())
    computer_score = calculate_score(dealer_cards)
  print(f"{user_score} and {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play BlackJack? 'y' or 'n'") == 'y':
    clear()
    play_game()
