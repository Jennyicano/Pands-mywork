# learning functions
#variable scope

x = 999

def fun(num):
    print(num)

def fun2(x):
    print(f"in fun2 x {x}")
    x= 21
    print(f"in fun2 x {x}")

fun2(x)
print(f"after fun2 x is {x}")