# Learning functions
# flexible arguments

print (1, 2, 3, end="\t", sep="")
# adding the 'end=' and 'sep=' will make the hi is in the same line as the number
print("hi")

def fun1(*args):
    print(type(args))
    print(args)

fun1("a", "b", "c")

# We can see is a tuple

# adding the val, will print the letters in differents lines
def fun1(*args):
    print(type(args))
    for val in args:
        print(val)

fun1("a", "b", "c")

# keyword arguments
def fun2(**kwargs): 
    print(type(kwargs))
    print(kwargs)
    
fun2(name="joe", age=21, gender="M")

# it can be use to get average numbers
# sample code

def ave(*values):
    number_of_values = len(values)
    sum= 0
    for value in values:
        sum+= value
    
    average = sum / number_of_values
    return average , sum

print(ave(1,2,3,4,5,6,7))

av1, sum_of_numbers = ave(1,2,3,4,5,6,7)
print(f"{av1} and sum is {sum_of_numbers}")