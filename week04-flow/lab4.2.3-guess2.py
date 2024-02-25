# This program asks the user to guess a number. 
# The program tells the usesr if the guess is too higt or too low.
# The program will keep prompting the user to guess the number
# until the user gets the right number.

# Author Jennifer Ibanez Cano

numberToGuess = 76

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("too low")
    else: 
        print("too high")
    guess = int(input("Please guess again "))

print ("Well done! Yes the number was ", numberToGuess)