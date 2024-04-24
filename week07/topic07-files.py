# practise with files

FILENAME= "data.txt"

with open(FILENAME, 'r') as f:
    for data in f:
        #print(data , end="")
        print(data.strip() )
        #print(data[:-1])

with open("data2.txt", "wt") as f:
    f.write("how now\n")
    f.write("brown cow")
    # Here will open and write a new file "data2.txt"

print("done")
