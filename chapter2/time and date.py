from datetime import time
from datetime import date
from datetime import datetime

#today = datetime.today()
#print("Today date & Time is :", today)

d= date.today()
print("Today date :" , d)
t = datetime.now().time()
print("Current time:", t)
# diffrenet way to select time show

now= datetime.now()
t1 = now.time()
print("Current time:", t1)

d= datetime.today()
print(d)
