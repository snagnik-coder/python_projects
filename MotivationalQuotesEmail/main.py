import smtplib
# import datetime as dt
# from random import choice

my_email = "snagnikdas2001@gmail.com"
password = "tr01sd07"
quote_for_today = "Visit: https://drive.google.com/file/d/1uXQvJvot32uUNTAvrTLgznLoAiIWewSe/view?usp=sharing"

# weekdays = ["Monday", "Tuesday", "wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# now = dt.datetime.now()
# day_name = weekdays[now.weekday()]
# with open("quotes.txt") as file:
#     quotes = file.read().split("\n")
# quote_for_today = choice(quotes)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user = my_email, password = password)
    connection.sendmail(
        from_addr = my_email, 
        to_addrs = "1929251@kiit.ac.in", 
        msg = f"Subject: Dekho goo, naile kutu demu\n\n{quote_for_today}")


