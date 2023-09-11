
import os
import sys

SP = sys.argv[-1]


files = os.listdir("" + SP + "/merged/nu/")

h=open("" + SP + "/merged/rm.txt","w")
for truc in files:
	a = truc.strip(".txt").split("_")
	delta = float(a[2])
	R = float(a[3])
	f=open("" + SP + "/merged/nu/" + truc ,"r")
	l=f.readline()
	f.close()
	nu = float(l.strip("\n"))
	rm = R * delta * nu
	h.write(truc + "\t" + str(rm) + "\n")

h.close()







