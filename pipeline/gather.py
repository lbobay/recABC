

import os
import sys 

SP = sys.argv[-1]


# Pi and Theta are in "metrics"
# fitted LD is in "fit"
# h/m estimates are in "all"

simulations = os.listdir("" + SP + "/merged/simul/")


log = open("" + SP + "/merged/log.txt","w")


h=open("" + SP + "/merged/gather.txt","w")
h.write("coeff\tdelta\tRho_theta\tnu\trm\tPi\tTheta\tfit\thm\n")
for file in simulations:
	file = file.split(".fa")[0] + ".txt"
	try:
		f=open("" + SP + "/merged/metrics/" + file , "r")
		for l in f:
			a=l.strip("\n").split("\t")
			if a[1] == "Pi":
				pi = a[2]
			elif a[1] == "Theta":
				theta=a[2]
		f.close()
		try:
			f=open("" + SP + "/merged/fit/" + file , "r")
			l=f.readline()
			fit = l.strip("\n")
			f.close()
		except IOError:
			fit="1.0"
			#print("Empty fit file for " + SP)
		try:
			f=open("" + SP + "/merged/all/" + file , "r")
			l=f.readline()
			a=l.strip("\n").split("\t")
			f.close()
			hm = a[2]
			f=open("" + SP + "/merged/nu/" + file , "r")
			l=f.readline()
			nu = l.strip("\n")
			f.close()
			b = file.strip(".txt").split("_")
			rm = float(b[3]) * float(nu) * float(b[2])
			h.write(b[1] + "\t" + b[2] + "\t" + b[3] + "\t" + nu + "\t" + str(rm) + "\t" + pi + "\t" + theta + "\t" + fit + "\t" + hm + "\n")
		except IOError:
			print("File " + file + " missing in all or nu\n")
	except:
		print("File " + file + " missing in metrics.... skipping\n")
		pass

h.close()
log.close()










