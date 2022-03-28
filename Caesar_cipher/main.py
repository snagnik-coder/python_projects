from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
  encrypted_text = ""
  for letter in range(len(text)):
    if text[letter] in alphabet:
      index = alphabet.index(text[letter])
      index = (index + shift) % 26
      encrypted_text += alphabet[index]
    else:
      encrypted_text += text[letter]
  print(f"The encoded text is {encrypted_text}")

if direction.lower() == "encode":
  encrypt(text, shift)
elif direction.lower() == "decode":
  encrypt(text, -shift)
    