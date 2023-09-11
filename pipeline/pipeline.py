

import os
import sys


#print sys.argv

SP = sys.argv[-7]
coeff = float(sys.argv[-6])
DELTA = float(sys.argv[-2])
R = float(sys.argv[-1])
L = 22000
GC = float(sys.argv[-4])
kappa = float(sys.argv[-3])


name = "data_" + str(coeff) + "_" + str(float(DELTA)) + "_" + str(R)

print(name)

print("1. Launch simulation.py")
os.system("python pipeline/simulation.py "  + SP + " " + str(coeff) + " " + str(L) + " " + str(GC) + " " + str(kappa) + " " + str(DELTA) + " " + str(R))

print("2. Launch poly.py")
os.system("python pipeline/poly.py " + SP + " " + name)

print("3. Launch LD.py")
os.system("python pipeline/LD.py " + SP + " " + name)
#
print("4. fit.py")
os.system("python pipeline/fit.py " + SP + " " + name)
#
print("5. all.py")
os.system("python pipeline/all.py " + SP + " " + name)












