

import os
import sys



SP = sys.argv[-1]


os.system("python pipeline/rm.py " + SP)

os.system("python pipeline/gather.py " + SP)

os.system("Rscript --vanilla pipeline/self.R " + SP)

# Grab real values

f=open("" + SP + "/merged/real/all.txt","r")
l=f.readline()
a=l.strip("\n").split("\t")
hm = a[2]
f.close()


f=open("" + SP + "/merged/real/metrics.txt","r")
l=f.readline()
l=f.readline()
a=l.strip("\n").split("\t")
pi = a[2]
f.close()

try:
    f=open("" + SP + "/merged/real/self.txt","r")
    l=f.readline()
    a=l.strip("\n").split("\t")
    itself = a[0]
    f.close()
except:
    os.system("Rscript --vanilla pipeline/linear_self.R " + SP)
    f=open("" + SP + "/merged/real/self.txt","r")
    l=f.readline()
    a=l.strip("\n").split("\t")
    itself = a[0]
    f.close()



os.system("Rscript --vanilla pipeline/abc.R " + SP + " " + pi + " " + itself + " " + hm)



