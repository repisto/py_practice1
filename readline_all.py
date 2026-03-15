# readline_all.py
import os
path = os.path.expanduser("~/doit/newfile.txt")
f = open(path,'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
