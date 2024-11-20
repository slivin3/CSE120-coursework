##Created by SAL on 11/18/2024

#Import datetime module from datetime library
from datetime import datetime as dt

#This allows manual time entry for testing
User_time = input("Enter time (or press Enter):")

if User_time == "":
    User_time = int(f"{dt.now():%H%M}")
else:
    User_time = int(User_time)
print("The time is: ",User_time)
    
if User_time < 0 or User_time >= 2400 or User_time % 100 > 60:
    print("Negative time doesn't exist! Nor does more than 60 minutes in an hour! \nAre you trying to time travel or create a tear in the space time continuum?")
elif User_time > 0 and User_time <= 1159:
    print("Good mornin'!")
elif User_time > 1200 and User_time <= 1659:
    print("Good afternoon!")
elif User_time > 1700 and User_time <= 1959:
    print("Good evenin'!")
elif User_time >2000 and User_time <= 2359:
    print("Good night!")
