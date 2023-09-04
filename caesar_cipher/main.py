from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    new_code = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position < len(alphabet):
             new = alphabet[new_position]
             new_code += new
        else:
             new_position -= len(alphabet)
             new = alphabet[new_position]
             new_code += new
    print(f"The encoded text is {new_code}")


def decrypt(code_text, shift_amt):
  decode = ""
  for item in code_text:
      position = alphabet.index(item)
      if position >= shift_amt:
         new_position = position - shift_amt
         # print(new_position)
         old = alphabet[new_position]
         decode += old
      elif position < shift_amt:
         new_position = (len(alphabet) + position) - shift_amt
         old = alphabet[new_position]
         decode += old
  print(f"The decoded text is {decode}")

if direction == "encode":
   encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
   decrypt(code_text=text, shift_amt=shift)
