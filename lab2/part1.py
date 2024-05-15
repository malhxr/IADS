from datetime import timedelta, datetime

#1 Create a basic ‘timedelta’
time = timedelta(days=365, hours=5, minutes=1)
print(time)

#2 Print today’s date and current time
current = datetime.now()
print(current)

#3 Print today’s date and time two years from now
after_two_years = datetime.now() + timedelta(days=365*2)
print(after_two_years)

#3.1  Create and print a timedelta with two arguments. E.g., In 2 weeks and 3 days
res = timedelta(weeks=2, days=3)
after_given_days = datetime.now() + res
print(after_given_days)

#4 5.	Calculate the date three weeks ago and print it like a string
before = datetime.now() - timedelta(weeks=3)
print("Three weeks ago it was", before.strftime("%A %B %d, %Y"))


#5 Here you need to find the number of days till next Christmas

# today's date
today = datetime.today()

# current year
current_year = today.year

# Get the date for Christmas in the current year
christmas_2024 = datetime(current_year, 12, 25)
# Check if Christmas has already passed this year
if today > christmas_2024:
    #  remaining  for Christmas next year
    remaining_days = datetime(current_year + 1, 12, 25)
    #  timedelta till next Christmas
    res = (remaining_days - today).days
else:
    res = (christmas_2024 - today).days

print(" {} days left till next Christmas.".format(res))
