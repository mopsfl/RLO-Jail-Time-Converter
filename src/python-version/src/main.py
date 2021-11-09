import os

print("mopsfl - Real Life Online - Jail Time Convert - v.0.1\n")

try:
    months = int(input("Enter the months: "))
    method = input("Enter to what you want to convert it (hour, day): ")

    
    if method == "hour":
        print("\nResults: " + str(months/60) + " hour(s)")
        print("Results rounded: " + str(round(months/60)) + " hour(s)\n\n")
    elif method == "day":
        print("\nResults: " + str(months/1440) + " day(s)")
        print("Results rounded: " + str(round(months/1440)) + " day(s)\n\n")
    else:
        print("Invalid method")

    os.system('pause')
except:
    print("Invalid input")
    os.system('pause')

