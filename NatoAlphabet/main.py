
import pandas

#TODO 1. Create a dictionary in this format:
df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Enter your word: ").upper()
try:
    nato_list = [nato_dict[letter] for letter in input_word]
except KeyError:
    print("Sorry, only letters in the alphabet please")
else:
    print(nato_list)