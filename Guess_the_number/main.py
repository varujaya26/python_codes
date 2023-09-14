from art import logo
import random

global attempts

print(logo)
print("I am thinking of a number from 1 and 100")
number = random.randint(1, 100)
# print(number)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
  attempts = 10
elif difficulty == 'hard':
  attempts = 5


def guess_game(attempts):
  print(f" You have {attempts} remaining to guess the number.")
  while (attempts != 0):
    guess = int(input("Make a guess: "))
    if guess > number:
      attempts -= 1
      print(
          f"Too High \n Guess again. \n You have {attempts} attempts to guess the number"
      )
    elif guess < number:
      attempts -= 1
      print(
          f"Too Low \n Guess again. \n You have {attempts} attempts to guess the number"
      )
    elif guess == number:
      print(f"You have correctly guessed the number {number}")
      break
    if attempts == 0:
      print(f"you have lost and the correct number is {number}")


guess_game(attempts)
