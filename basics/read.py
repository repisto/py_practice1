# read.py
import os
path = os.path.expanduser("~/doit/newfile.txt")
f = open(path,'r')
data = f.read()
print(data)
f.close()
