import os
from art import logo
print(logo)
# Get inputs
name = input("what is your name: ")
bit_amt = int(input("what's your bid: $"))

def create_dict(name, bit_amt):
    max = 0
    # Creating a dictonary called auction
    auction = {name:bit_amt}
    # continue bidding
    bidding = input("Are there any other bidders? Type yes or no ")
    if bidding == "yes":
       os.system('clear')
       name = input("what is your name: ")
       bit_amt = int(input("what's your bid: $"))
       auction[name] = bit_amt
       create_dict(name, bit_amt)
    else:
       for item in auction:
          if auction[item] > max:
             max = auction[item]
             os.system('clear')
             print(f"The winner of the bid is {item} with ${max} value")
          
         
create_dict(name, bit_amt)
