# This program reads in a string and strips any leading or trailing spaces.
# The program also converts the string to lower case.
# The program will also output the lenght of the input and output strings. 

# Author Jennifer Ibanez cano

rawString = input("please enter a string: ")
normalisedString =  rawString.strip().lower()

lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)

print(f"That string normalised is: {normalisedString}")
print(f"we reduces the input string from {lenghtOfRawString} to {lenghtOfNormalised} characters")