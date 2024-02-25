# This program generated a random number between 0 and 100 to guess.
# This program asks the user to guess a number. 
# The program tells the usesr if the guess is too higt or too low.
# The program will keep prompting the user to guess the number
# until the user gets the right number.

# Author Jennifer Ibanez Cano

import random
numberToGuess = random.randint(1,100)

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else: 
        print("too high")
    guess = int(input("Please guess again "))

print ("Well done! Yes the number was ", numberToGuess)
