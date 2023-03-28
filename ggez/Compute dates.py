from datetime import datetime
date_format = "%m/%d/%Y"
a = datetime.strptime('9/5/1998', date_format)
b = datetime.strptime('1/29/2001', date_format)
delta = b - a
print (delta.days)