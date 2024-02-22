# This program will print out a random fruit.
# Author Jennifer Ibanez Cano
# In this program I'll use a list []

import random
fruits = ['Apple', 'Pear', 'Orange', 'Banana', 'Peach']

# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print("A Random Fruit: {}". format(fruit))