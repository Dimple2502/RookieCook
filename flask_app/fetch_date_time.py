#----------------------------------------------------------#
#importing modules
from datetime import datetime
from datetime import date


#----------------------------------------------------------#
#fetching date
#storing date in the variable 'date'
date_today=str(date.today())
print(date_today)
print(type(date_today))

#----------------------------------------------------------#
#splitting date to get month
split_date_array = date_today.split('-')
print(split_date_array)
month = int(split_date_array[1])

#----------------------------------------------------------#
#Getting temperature from the user's location



#----------------------------------------------------------#
#storing current time in variable 'time_now'
time_now = datetime.now().strftime("%H:%M:%S")

print(f"Current time: {time_now}")

#----------------------------------------------------------#
# storing hour, minute and second in respective variables.
hour = datetime.now().strftime("%H")
print(hour)
# minute = datetime.now().strftime("%M")
# print(minute)
# second = datetime.now().strftime("%S")
# print(second)