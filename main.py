import pandas
import datetime as dt
import random
import smtplib

sender = "youremail@email.com"
password = "yourpassword"
date_now = dt.datetime.now()
month = date_now.month
day = date_now.day

birthdays = pandas.read_csv("birthdays.csv")
birthdays_dict = birthdays.to_dict("records")
birthdays_today = [record for record in birthdays_dict if record["month"] == month and record["day"] == day]

letter_num = random.randint(1, 3)
if len(birthdays_today) > 0:
    with open(f"letter_templates/letter_{letter_num}.txt") as file:
        data = file.read()
        for celebrant in birthdays_today:
            name_celebrant = celebrant["name"]
            email_celebrant = celebrant["email"]
            new_data = data.replace("[NAME]", name_celebrant)

            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=sender, password=password)
                connection.sendmail(from_addr=sender, to_addrs=email_celebrant, msg=f"Subject: Happy Birthday {name_celebrant}!\n\n{new_data}")
                print(f'A birthday greeting to {name_celebrant} has been sent')

