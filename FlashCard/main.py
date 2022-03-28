BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
from random import choice, random

window = Tk()
window.title("Flash Cards")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

try:
    french_data = pandas.read_csv("data/to_learn.csv")
    french_dict_list = french_data.to_dict(orient = "records")
    card = None
except FileNotFoundError:
    french_data = pandas.read_csv("data/french_words.csv")
    french_dict_list = french_data.to_dict(orient = "records")
    card = None

def new_card():
    global card, timer
    window.after_cancel(timer)
    card = choice(french_dict_list)
    canvas.itemconfig(card_title, text = "French", fill = "Black")
    canvas.itemconfig(card_word, text = card["French"], fill = "Black")
    canvas.itemconfig(card_background, image = card_front)
    timer = window.after(3000, func = flip)

def flip():
    global card
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_word, text = card["English"], fill = "White")
    canvas.itemconfig(card_background, image = card_back)

def known_card():
    global card
    french_dict_list.remove(card)
    df = pandas.DataFrame(french_dict_list)
    df.to_csv("data/to_learn.csv", index = False)
    new_card()

timer = window.after(3000, func = flip)

canvas = Canvas(width = 800, height = 526)
card_front = PhotoImage(file = "images/card_front.png")
card_back = PhotoImage(file = "images/card_back.png")
card_background = canvas.create_image(400, 263, image = card_front)
card_title = canvas.create_text(400, 150, text = "Title", font = ("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "Word", font = ("Ariel", 60, "bold"))
canvas.grid(row = 0, column = 0, columnspan = 2)
canvas.config(bg = BACKGROUND_COLOR, highlightthickness = 0)

cross_image = PhotoImage(file = "images/wrong.png")
wrong_button = Button(image = cross_image, command = new_card)
wrong_button.grid(row = 1, column = 0)
wrong_button.config(highlightthickness = 0)

check_image = PhotoImage(file = "images/right.png")
right_button = Button(image = check_image, command = known_card)
right_button.grid(row = 1, column = 1)
right_button.config(highlightthickness = 0)

new_card()
    
window.mainloop()