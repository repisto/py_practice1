# readline_test.py
import os
path = os.path.expanduser("~/doit/newfile.txt")
f = open(path,'r')
line = f.readline()
print(line)
f.close()
