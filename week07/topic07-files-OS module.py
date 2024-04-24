# os modules

import os

FILENAME = "topic07-files"

if os.path.exists(FILENAME):
    with open(FILENAME, "r") as f:
        for line in f:
            print(line, end='')
else:
    print (FILENAME, "does not exist")

# to remove a file use os.remove()

