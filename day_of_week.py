# configuration section
Sunday = 0
Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6

# processing
day = int(input("Day (0-6?) "))

if day == 0:
    # print("Sunday")
    message = "Sunday"
elif day == 1:
    #print("Monday")
    message = "Monday"
elif day == 2:
    #print("Tuesday")
    message = "Tuesday"
elif day == 3:
    #print("Wednesday")
    message = "Wednesday"
elif day == 4:
    #print("Thursday")
    message = "Thursday"
elif day == 5:
    #print("Friday")
    message = "Friday"
elif day == 6:
    #print("Saturday")
    message = "Saturday"
else:
    #print("Try again.")
    message = "Try again."

print(message)