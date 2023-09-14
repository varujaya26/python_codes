from art import logo
import random
import os
def play_blackjack():
  """This play_blackjack is a function to play BlackJack"""
  # prints the logo backjavk
  print(logo)
  
  def deal_card():
    """Randomly selecting new cards"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    ace = cards[0]
    card = random.choice(cards)
    return card
  
  def calculate_score(cards):
    """This calculate score calculates the user cards and computer cards drawn"""
      # Checks for sum of black jack 
      if sum(cards) == 21 and len(cards) == 2:
         return 0
      # checks the score if sum of cards in the list is greater than 27 and also has an Ace
      if cards == 11 and sum(cards) > 21:
         cards.remove(11)
         cards.append(1)
      return sum(cards)
  
  def compare(current_score, computer_score):
    """This function is used to compare the user cards and computer cards"""
      if current_score == computer_score:
         print(f" The score is same {current_score} It is a Draw!")
      elif computer_score == 0:
         print(f" The computer has blackjack, The Computer Wins!")
      elif current_score == 0:
         print(f" The user has blackjack, The User Wins!")
      elif computer_score > 21:
         print(f" The computer score is {computer_score}, The User Wins!")
      elif current_score > 21:
         print(f" The user score is {current_score}, The Computer Wins!")
      else:
          if current_score > computer_score:
             print(f"The user wins with score of {current_score}, while computer score is {computer_score}")
          else:
             print(f"The computer wins with score of {computer_score}, while computer score is {current_score}")
  
#Draw user cards and computer cards and save it in a list
  user_cards = []
  computer_cards = []
  for _ in range(2):
     user_cards.append(deal_card())
     computer_cards.append(deal_card())
  game_ends = False
  #Calculates the score of user and print the cards
  while(game_ends == False):
    current_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards {user_cards} and current score is {current_score}")
    print(f"Computer's first card is {computer_cards[0]}")
    #Check for blackjack or score greater than 21 to end game, if not continue the game
    if current_score == 0 or computer_score == 0 or current_score > 21:
       game_ends = True
    else:
       game_continue = input("Type 'y' if you want to continue to draw a card or type 'n' to pass ")
       if game_continue == 'y':
           user_cards.append(deal_card())
           print(user_cards)
       else:
          game_ends = True
# check if computer has blackJack and draw cards until score less than 17
  while computer_score != 0 and computer_score < 17:
     computer_cards.append(deal_card())
     computer_score = calculate_score(computer_cards)
  print(f" The final hand of User is {user_cards} and score is {current_score}")
  print(f" The final hand of Computer is {computer_cards} and score is {computer_score}")
  print(compare(current_score, computer_score))
# To play a new game of blackjack
  while input("Do you want to play another game of BlackJack type 'y' or 'n' for no ") == 'y':
      os.system('clear')
      play_blackjack()

play_blackjack()
