# import random


# today = datetime.date.today()
# print(random.randint(1,200))

from datetime import datetime

now = datetime.now()
current_time = now.strftime('%H:%M:%S')

print(current_time)