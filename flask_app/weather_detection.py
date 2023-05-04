# import fetch_date_time 
# month = fetch_date_time.month

from datetime import datetime
from datetime import date

date_today=str(date.today())
split_date_array = date_today.split('-')
month = int(split_date_array[1])
# time_now = datetime.now().strftime("%H:%M:%S")
# hour = datetime.now().strftime("%H")

if month >=3 and month <=5:
    season = "summer"
elif month >=6 and month <=9:
    season = "rainy"
elif month >=10 and month <=2:
    season = "winter"

# print(f"The season is: {season}")

