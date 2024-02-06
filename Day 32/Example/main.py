import smtplib
import datetime as dt
import random


### Credentials
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

## Random Quote
line = random.choice(open('quotes.txt').readlines())
print(line)


## for the "if stateement"
now = dt.datetime.now()
year = now.year
#month = now.month
#day = now.day
#
if year == 2024:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()  # Secure connection to our email server
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="myemail@]mail.com",
            msg=f"Subject:Happy Birthday\n\n{line}")


#date_of_birth = dt.datetime(year=year, month=month, day=1)
#print(date_of_birth)

#dt.datetime.now()

