from datetime import datetime

now = datetime.now()

new_years_day = datetime(year=now.year + 1, month=1, day=1)

difference = new_years_day - now

days_left = difference.days

print(f"There are {days_left} days left until the next New Year's Day!")