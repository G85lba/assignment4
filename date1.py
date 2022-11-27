import datetime

today = datetime.date.today()

x = datetime.timedelta(days = 5)

y = today - x

print(y)