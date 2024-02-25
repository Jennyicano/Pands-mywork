# This program reads in numbers until the user enters 0.
# The program will show the numbers in a list.
# The program will print out each of the numbers entered
# and the average of them

# Author Jennifer Ibanez Cano

numbers = []
number = int(input("Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)
    number = int(input("enter another (0 to quit): "))
    
for value in numbers:
    print (value)

average = float(sum(numbers)) / len(numbers)

print(f"The average is {average}")