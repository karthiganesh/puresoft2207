#kg220729 demo for date functions
from datetime import date, timedelta, datetime

dt_curr = date.today()
print(dt_curr)
print(dt_curr.strftime('%A'),dt_curr.strftime('%a'))

n_oldday = timedelta(minutes=30)

dt_lastmonth = dt_curr - n_oldday
print(dt_lastmonth, dt_lastmonth.strftime('%A'))

dt_invoice = datetime.fromisoformat('2021-07-22 15:11:23 +01:00')
print(dt_invoice,dt_invoice.strftime('%A'))