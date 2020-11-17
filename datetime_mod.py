import datetime
import time
from datetime import date


mytime = datetime.time(2,20)
print(mytime)

today = datetime.date.today()
print(today)

# Date
date1 = date(2021,11,3)
date2 = date(2020,11,3)

print(date1 - date2)


# datetime1 = datetime(2021,11,3,22,0)
# datetime2 = datetime(2020,11,3,12,0)
# print(datetime1 - datetime2)