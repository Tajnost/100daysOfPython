from datetime import datetime

time_now = datetime.now()

latitude = 9.23
longitude = 50.343

my_longitude = 50.966530
my_latitude = 9.298550


if my_longitude-5 < float(longitude) < my_longitude+5 and my_latitude-5 < float(latitude) < my_latitude+5:
        print("hellow")


