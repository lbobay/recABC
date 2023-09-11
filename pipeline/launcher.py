
import numpy
import sys
import os


#print sys.argv

SP = sys.argv[-7].split("-")
coeff = sys.argv[-6].split("-")
DELTA = sys.argv[-2].split("-")
COEFF = sys.argv[-1].split("-")
L = 22000
GC = sys.argv[-4].split("-")
kappa = sys.argv[-3].split("-")



i=0
while i < len(SP):
	sp,c,delta,R,gc,k= SP[i],coeff[i],DELTA[i],COEFF[i],GC[i],kappa[i]
	print("File= " ,"data_" + str(c) + "_" + str(delta) + "_" + str(R))
	os.system("python pipeline/pipeline.py  " + sp + " " + c + " " + str(L) + " " + gc  + " " + k + " " + delta + " " + R )
	i+=1







