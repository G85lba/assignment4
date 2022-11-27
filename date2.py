import datetime

today = datetime.date.today()

x = datetime.timedelta(days = 1)

yesterday = today - x
tomorrow = today + x

print(today, yesterday, tomorrow)