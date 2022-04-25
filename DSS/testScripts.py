
from datetime import datetime
fromDate='2008/2/12'
toDate= '2008/2/10'

date_format = "%Y/%m/%d"
date1 = datetime.strptime(fromDate, date_format)
date2 = datetime.strptime(toDate, date_format)
delta = date1 - date2
print(delta)
if (delta.days >= 0):
    fromDate= date1
    toDate= date2
else:
    fromDate= date2
    toDate= date1

print(date1)
print(date2)

#--------------------------------

