# practise with files

FILENAME= "test.txt"

with open(FILENAME, 'r') as f:
    data = f.read()
    print(data[0])
