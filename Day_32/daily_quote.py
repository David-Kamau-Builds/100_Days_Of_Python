import random
import smtplib
import datetime as dt

days = ["Monday's", "Tuesday's", "Wednesday's", "Thursday's",
        "Friday's", "Saturday's", "Sunday's"]

MY_EMAIL = "your_email@gmail.com"
SMTP_PASSWORD = "your_app_password"

TO_EMAIL = "recipient@gmail.com"
EMAIL_SUBJECT = "Subject: " + days[dt.datetime.now().weekday()] + " quote"


try:
    with open("quotes.txt") as f:
        quotes_list = [line.strip() for line in f]
except FileNotFoundError:
    print("Quotes file not found")
    quotes_list = []


def date_picker():
    return random.choice(quotes_list)


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=SMTP_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL,msg=EMAIL_SUBJECT + "\n\n" + date_picker())
