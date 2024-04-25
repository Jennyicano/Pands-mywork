# Learning numpy
# Following lesson 8 

import numpy as np

list_numbers= [1,2,3,"asdf"]
print (list_numbers)

numbers = np.array([1,2,3,4])
# here you can give the number sum, multiplication, etc
numbers = numbers + 3

print(numbers)


rando = np.random.randint(100,200,30)
print(rando)

normalrando = np.random.normal(size=100)
print (normalrando)


