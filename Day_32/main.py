import datetime as dt
import pandas
import random
import smtplib
import os

today = dt.datetime.today()
today_month = today.month
today_day = today.day

try:
    birthday_df = pandas.read_csv("birthdays.csv")
except FileNotFoundError:
    print("Birthday's file not found.")
    birthday_df = pandas.DataFrame(columns=["name", "email", "year", "month", "day"])

matches = birthday_df[
    (birthday_df["month"] == today_month) &
    (birthday_df["day"] == today_day)
]

if not matches.empty:
    print("Birthday's found:", len(matches))
    print(matches.name)

    for _, person in matches.iterrows():

        name = person["name"]
        to_email = person["email"]

        template_number = random.randint(1, 3)
        template_path = f"letter_templates/letter_{template_number}.txt"

        with open(template_path, "r") as file:
            letter_contents = file.read()

        personalized_letter = letter_contents.replace("[NAME]", name)

        MY_EMAIL = os.getenv("MY_EMAIL")
        SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

        if not MY_EMAIL or not SMTP_PASSWORD:
            raise ValueError("Set MY_EMAIL and SMTP_PASSWORD as environment variables!")

        msg = (
            f"Subject: Happy Birthday!\n\n"
            f"{personalized_letter}\n"
        )

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, SMTP_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=to_email,
                msg=msg
            )

else:
    print("No birthdays today.")
