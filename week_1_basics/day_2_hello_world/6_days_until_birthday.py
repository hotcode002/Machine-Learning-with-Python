# In this program we will calculate the number of days
# to the user entered birth date.
# 1. date object
# 2. 

import datetime
import time

birth_date = input ( "Enter your birthday (MM DD YYYY)- " )

# Convert the user entered string to datetime format
birth_date = time.strptime(birth_date, "%m %d %Y")

print ( birth_date.tm_year )

today = datetime.date.today()
birth_date = datetime.date(birth_date.tm_year,birth_date.tm_mon, birth_date.tm_mday)


print ( today)
print ( birth_date)

p