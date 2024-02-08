import requests
from datetime import datetime
import smtplib

### GET DATA FROM ISS
response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
response1.raise_for_status()

data = response1.json()

longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']

### GET DATA FROM SUNSET SUNRISE
requests1 = requests.get(f"https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}&date=today&formatted=0")
data1 = requests1.json()
sunrise = data1['results']['sunrise']
sunset = data1['results']['sunset']
sunrise1 = int(sunrise.split("T")[1].split(":")[0])
sunset2 = int(sunset.split("T")[1].split(":")[0])
print(int(sunrise1))
print(int(sunset2))

time_now = datetime.now()

### MY LOCATION
my_latitude = -40.966530
my_longitude = 47.298550

### IF THE ISS IS CURRENTLY TO MY CURRENT POSITION - send me mail to look  up
if my_longitude-5 < float(longitude) < my_longitude+5 and my_latitude-5 < float(latitude) < my_latitude+5:
    if time_now.hour <= sunrise1 or time_now.hour >= sunset2:

        MY_EMAIL = "YOUR EMAIL"
        MY_PASSWORD = "YOUR PASSWORD"
        TO_EMAIL = "WHO EMAIL"

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg=f"Subject:ISS ABOVE YOU!\n\nGo look at the sky ISS is above your desired location"
            )

