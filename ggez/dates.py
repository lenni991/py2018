from datetime import datetime
date_format = "%m/%d/%Y"
print("Format Must Be ~month/day/year~")
d1=input("First Date: ")
d2=input("Second date: ")
a = datetime.strptime(d1, date_format)
b = datetime.strptime(d2, date_format)
delta = b - a
print (delta.days)
print (delta.months)

