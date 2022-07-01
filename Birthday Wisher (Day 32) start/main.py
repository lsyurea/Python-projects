import smtplib
import datetime
import random

# relevant set up
my_email, password = 'insert email here', 'insert your password here'
to_email = 'insert recipient email here'

# set up random quotes here if it is monday

time = datetime.datetime.now() # can be modified to use select dates to write message
if time.weekday() == 0:
    with open('quotes.txt') as file:
        quotes = file.readlines()
        msg = f'Subject: Monday quotes here\n\n{random.choice(quotes)}'

    # set up connection here using context manager
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()  # secure connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs= to_email, msg=msg)


