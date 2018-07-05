import datetime as dt
import time as t

print(t.time())

dtnow = dt.datetime.utcfromtimestamp(t.time())
print(dtnow)

delta = dt.timedelta(days=100)
delta
today = dt.date.today()
print(today - delta)
