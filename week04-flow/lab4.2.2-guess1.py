# This program asks the user to guess a number. 
# The program will keep prompting the user to guess the number
# until the user gets the right number.

# Author Jennifer Ibanez Cano

numberToGuess = 27

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    print("Wrong")
    guess = int(input("Please guess again: "))

print ("Well done! Yes the number was ", numberToGuess)
