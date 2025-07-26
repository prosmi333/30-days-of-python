from datetime import datetime, date, time, timedelta

# Exercise 1
now = datetime.now()
print("Current date & time:", now)
print("Day:", now.day)
print("Month:", now.month)
print("Year:", now.year)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Timestamp:", now.timestamp())

# Exercise 2
formatted = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Formatted datetime:", formatted)

# Exercise 3
date_str = "5 December, 2019"
converted = datetime.strptime(date_str, "%d %B, %Y")
print("Converted datetime object:", converted)

# Exercise 4
new_year = datetime(now.year + 1, 1, 1)
time_until_ny = new_year - now
print("Time until New Year:", time_until_ny)

# Exercise 5
epoch = datetime(1970, 1, 1)
elapsed_since_epoch = now - epoch
print("Time since epoch:", elapsed_since_epoch)

# Exercise 6 (Creative prompt)
# Examples for using datetime module:
# · Logging time stamps in an application
# · Calculating age from a birthday
# · Scheduling events or reminders
# · Time-series data tracking
