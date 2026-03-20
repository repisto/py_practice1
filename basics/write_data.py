# write_data.py
import os
path = os.path.expanduser("~/doit/newfile.txt")
f = open(path,'w')
for i in range(1,11):
    data = "%d's line\n"%i
    f.write(data)

f.close()
