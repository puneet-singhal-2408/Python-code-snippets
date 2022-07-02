name = input("Enter your name :")
age = int(input ("Enter your age :"))
from datetime import datetime
date = datetime.now()
year = date.year
old = 100-age
year += old
print("hello " + name + " you will be 100 year old in " + str(year))
