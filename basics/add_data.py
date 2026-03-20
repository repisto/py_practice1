# add_data.py
import os
path = os.path.expanduser("~/doit/newfile.txt")
f = open(path,'a')
for i in range(11,20):
    data = "%d's line\n"%i
    f.write(data)
f.close()
