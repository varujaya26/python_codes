## Import
from game_data import data
from art import logo
from art import vs
import random
import os

def get_random_dict(data):
  """Gets a random dictionary from the data and return it as a list"""
  random_dictionary = random.choice(data)
  list = []
  # Print the randomly selected dictionary
  for values in random_dictionary.values():
      list.append(values)
  return list

def question_func_a(data):
  """Create a question A function"""
  question_a = get_random_dict(data)
  name_a = question_a[0]
  followers_a = int(question_a[1])
  description_a = question_a[2]
  country_a = question_a[3]
  print(f"Compare A: {name_a}, {description_a}, {country_a}")
  return followers_a, question_a

def question_func_b(data):
  """Create a question B function"""
  question_b = get_random_dict(data)
  name_b = question_b[0]
  followers_b = int(question_b[1])
  description_b = question_b[2]
  country_b = question_b[3]
  print(f"Against Compare B: {name_b}, {description_b}, {country_b}")
  return followers_b, question_b
# variables    
score = 0
turn = 0
game_continue = True
# while loop to repeat the game on user victory
while game_continue == True:
  print(logo)
  if turn == 0:
     followers_a, question_a = question_func_a(data)
  else:
      print(f"You have got it right Your current Score: {score}")
      print(f"Compare A: {question_a[0]}, {question_a[2]}, {question_a[3]}")
      followers_a = question_a[1]
  
  print(vs)
  
  followers_b, question_b = question_func_b(data)
  if question_a == question_b:
     followers_b, question_b = question_func_b(data)

  
  # choose one option
  
  user_choice = input("Who has more followers? type A or B ")
  
  # compare the followers
  if followers_a > followers_b:
     correct_choice = 'A'
  else:
     correct_choice = 'B'
  print(correct_choice)
  
  ## Keep track of the score
  if user_choice == correct_choice:
      score += 1
      turn += 1
      os.system('clear')
      if correct_choice == 'B':
        question_a = question_b
        followers_a = followers_b
  else:
     print("Sorry! you have lost the game")
     game_continue = False
