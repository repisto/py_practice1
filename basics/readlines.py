# readlines.py
import os
path = os.path.expanduser("~/doit/newfile.txt")
f = open(path,'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)

f.close()
