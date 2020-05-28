from datetime import date
my_day = date(1998, 6, 5)
print(my_day)
print(my_day.weekday())
print(my_day.isoweekday())
from datetime import timedelta
party_day = my_day + timedelta(days=10000)
print(party_day)