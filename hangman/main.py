import random
from symbols import stages
# Number of lives
lives = 6
from symbols import logo
print(logo)
# word_list
from words import word_list
#word_list = ["aardvark", "baboon", "camel"]
# Randomly choose a word from the word_list and assign it to a variable called chosen_word
chosen_word = random.choice(word_list)
print(chosen_word)
# Create a list with underscore based on the chosen word
value = len(chosen_word)
l = []
m = []
i = 0
while (i < value):
    l.append("_")
    i += 1
display = ' '.join(str(item) for item in l )
print(display)
bool = True
#Loop the guessing of letters
while (bool == True):
    #Ask the user to guess a letter and assign their answer     to a variable called guess. Make guess lowercase.
    letter = input("Guess the letter? ")
    guess = letter.lower()
    if guess in m:
       print(f"You have already guessed the letter {guess}")
    #Check if the letter the user guessed (guess) is one of     the letters in the chosen_word.
    count = 0
    for i in chosen_word:
        if count < value:
            if i == guess:
                l[count] = guess
            count += 1
    # to check for "_" in l 
    result = ' '.join(str(k) for k in l)
    print(result)
    #check for values not in chosen_word
    if not guess in chosen_word:
      lives -= 1
      m.append(guess)
      print("You have lost one life")
    # Track lives 
    if lives == 0:
      print("Game over You lost")
      print(chosen_word)
      bool = False
    #check for "_"
    if "_" not in l:
        bool = True
        print("You win.")
        break
    print(stages[lives])
