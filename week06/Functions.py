# Learning functions
# the defining and using functions

x , y , z = (1, 2, 3)
print (x, y, z)
print (f"{x} {y} {z}")
print (x, y, z, sep="", end="")

# Other way to print functions
print ("{} {}--{}".format(x, y, z))

# To define a function we'll use def

def cube(number):
    print(number)
    return (number ** 3)

ans = cube(23)
print(f"we got {ans}")

print(f"and 33 is {cube(33)}")

