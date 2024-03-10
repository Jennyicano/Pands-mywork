# In this progran we practice to read in two numbers
# and multiple them

def readNum():
    num = False
    while (num == False):
        try:
            num = int(input("enter a number"))
        except ValueError:
            print("that was not a number" , end="")
    return num

num1 = readNum()
num2 = readNum()

answer = num1 * num2

print(f"answer is {answer}")