import random

import pandas
import datetime as dt
import smtplib
import os
my_email = os.getenv("MY_EMAIL")
my_password = os.getenv("MY_PASSWORD")

now = dt.datetime.now()
data_birthday = pandas.read_csv("birthdays.csv")
days = data_birthday["day"]
months = data_birthday["month"]

for i, day in enumerate(days):
    if day == now.day and now.month == data_birthday["month"][i]:
        name_of_birthday_person = data_birthday["name"][i]
        email_of_birthday_person = data_birthday["email"][i]

        letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
        file_name = random.choice(letters)
        with open(file_name) as email_file:
            text = email_file.read()
            text = text.replace("[NAME]", name_of_birthday_person)
            print(text)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=email_of_birthday_person,
                                msg=f"Subject:Happy Birthday \n\n {text}")
