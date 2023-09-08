import os
from art import logo


# CALCULATOR

#Addition
def add(n1, n2):
    return n1 + n2

#Subtraction
def sub(n1, n2):
    return n1 - n2

#Multiplication
def multiply(n1, n2):
    return n1 * n2

#Division
def divide(n1, n2):
    return n1 / n2

def calculator():
  print(logo)
  #Read number 1
  num1 = float(input("Enter the number: "))
  #create a dictionary
  operations = {
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide
  }
  
  num2 = float(input("Enter the next number: "))
  for item in operations:  
       print(item)
  operation = input("what kind of operations you wish to carry on?: ") 
  function = operations[operation]
  first_answer = function(num1, num2)
  print(f"{num1} {operation} {num2} = {first_answer}")
  continued = True
  while continued:
    loop = input(f"Type 'y' if you wish to continue operations on the {first_answer} or type 'n' to start a new calculation or type 'e' to exit ")
    if loop == "y":
      operation = input(f"what kind of operations you wish to carry on with the {first_answer}: ")
      num3 = float(input("Enter the next number: "))
          
      function = operations[operation]
      second_answer = function(first_answer, num3)
          
      print(f"{first_answer} {operation} {num3} = {second_answer}")
    elif loop == "n":
      continued = False
      os.system('clear')
      calculator()
    else: 
      continued = False


calculator()
