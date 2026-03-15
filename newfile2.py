# newfile2.py
import os
path = os.path.expanduser("~/doit/newfile.txt")
f = open(path,"w")
f.close()
