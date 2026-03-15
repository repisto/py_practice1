# read_for.py
import os
path = os.path.expanduser("~/doit/newfile.txt")
f = open(path,'r')
for line in f:
    print(line)
f.close()
