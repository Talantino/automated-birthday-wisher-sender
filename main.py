##################### Normal Starting Project ######################
import datetime as dt
import smtplib

import pandas
import random
now = dt.datetime.now()
today = (now.month, now.day)

data = pandas.read_csv("birthdays.csv")
b_day = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in b_day:
    bd_person = b_day[today]
    num = random.randint(1, 3)
    with open(f"./letter_templates/letter_{num}.txt", "r") as file:
        letter = file.read()
        ready_letter = letter.replace("[NAME]", bd_person["name"])
        print(ready_letter)
    with smtplib.SMTP("smpt@gmail.com") as connection:
        connection.starttls()
        connection.login(user="user@gmail.com", password="")
        connection.sendmail(
            from_addr="user@gmail.com",
            to_addrs=bd_person["email"],
            msg=f"Subject: Happy Birthday \n\n{ready_letter}"
            )


