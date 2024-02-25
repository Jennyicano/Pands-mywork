# This program reads in a student percentage 
# and prints out the corresponding grade.
# Using if , elif and else

# Author Jennifer Ibanez Cano

percentage = float(input("Enter the percentage: "))

if percentage < 0 or percentage > 100:
    print("Please enter a number between 0 and 100: ")

elif percentage < 40:
    print("Fail")
# The perentage is under 40
elif percentage < 50:
    print("Pass")
# The percentage is between 40 and 49
elif percentage < 60:
    print("Merit1")
# The percentage is between 50 and 59
elif percentage < 70:
    print("Merit2")
# The percentage is between 60 and 69
else:
    print("Distinction")
# The percentage is over 70