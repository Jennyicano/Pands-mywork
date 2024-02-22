# This program will reads to number.
# Also divides the first number by the second 
# and will outputs the integrer answer and remainder.
# Author Jennifer Ibanez Cano

a = int(input("Enter first number: "))
b = int(input("Enter the number you want to divide by: "))
answer= int(a//b)
remainder = a%b
print(" {} divided by {} is {} with remainder {} ".format(a, b, answer, remainder))