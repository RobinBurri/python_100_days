# SMTP simple mail transfet protocol
import smtplib
import datetime as dt
import random

my_email = "my email@gmail.com"
# gmail SMTP Ports 25, 465 ou 587
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(my_email, "your password")
    connection.sendmail(
        my_email, to_addrs="your email", msg="Subject:Hello\n\nThe body of the email"
    )


# You have to security in your email account and turn on 2-step verification
# create an app password and create a new app

# MY_EMAIL = "appbreweryinfo@gmail.com"
# MY_PASSWORD = "abcd1234()"

# now = dt.datetime.now()
# weekday = now.weekday()
# if weekday == 1:
#     with open("quotes.txt") as quote_file:
#         all_quotes = quote_file.readlines()
#         quote = random.choice(all_quotes)

#     print(quote)
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(MY_EMAIL, MY_PASSWORD)
#         connection.sendmail(
#             from_addr=MY_EMAIL,
#             to_addrs=MY_EMAIL,
#             msg=f"Subject:Monday Motivation\n\n{quote}"
#         )
