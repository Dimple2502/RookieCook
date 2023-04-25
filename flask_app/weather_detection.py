import fetch_date_time 
month = fetch_date_time.month


if month >=3 and month <=5:
    season = "summer"
if month >=6 and month <=9:
    season = "rainy"
if month >=10 and month <=2:
    season = "winter"

print(f"The season is: {season}")

