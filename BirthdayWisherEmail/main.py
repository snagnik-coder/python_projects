import datetime as dt
import pandas
from random import choice
import smtplib

my_email = "snagnikdas2001@gmail.com"
my_pass = "tr01sd07"

letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
now = dt.datetime.now()
month = now.month
day = now.day
birthdays = pandas.read_csv("birthdays.csv")
birthdays = birthdays.to_dict("records")
for birth_dict in birthdays:
    if birth_dict["month"] == month and birth_dict["day"] == day:
        recipent_email = birth_dict["email"]
        recipent_name = birth_dict["name"]
        letter = choice(letters)
        with open(f"letter_templates/{letter}") as file:
            message = file.read()
            message = message.replace("[NAME]", recipent_name)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user = my_email, password = my_pass)
                connection.sendmail(from_addr = my_email, to_addrs = recipent_email, msg = f"Subject: HAPPY BIRTHDAY!!!\n\n{message}")

