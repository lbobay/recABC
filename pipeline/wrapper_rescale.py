

######## Launch simulation with different parameters

### LIST of data-specific parameters:
# GC% (GC)
# Alignment length (L)
# transition/transversion ratio (kappa)
# Branch re-scaling coefficient (coeff)


# LIST of recombination parameters to test:
# Recombination tract length (DELTA)
# Recombination rate (COEFF)

import os
import sys

def toto(start, stop, step):
	i = start
	while i < stop:
		yield i
		i += step

def frange(start, stop, step):
	LIST=[]
	for i in toto(start, stop, step):
		LIST.append(i)
	return LIST



coefficients = frange(0,1,0.01)


SP = sys.argv[-1]
species=[SP]


nb=0
for sp in species:
	try:
		os.mkdir("" + sp + "/merged/rescale")
	except OSError:
		pass
	f=open("" + sp + "/merged/parameters.txt","r")
	l=f.readline()
	f.close()
	a=l.strip("\n").split("\t")
	L = a[0]
	GC = a[1]
	kappa = a[2]
	FILES=os.listdir("" + sp + "/merged/rescale")
	done_delta,done_R={},{}
	for file in FILES:
		file = file.split(".fa")[0]
		b = file.split("_")
	delta,R=0,0
	for coeff in coefficients:
		if 1==1:
			os.system("python pipeline/rescale.py " + sp + " " + L + " " + GC + " " + kappa + " " + str(round(coeff,2))) #added round to fix floating pt error -ET



#os.system("sbatch  simul.slurm " + sp + " " + L + " " + GC + " " + kappa + " " + str(delta) + " " + str(R))

