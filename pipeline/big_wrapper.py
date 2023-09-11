

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

#os.system('module load python/2.7.12')

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

inputs = sys.argv
SP = sys.argv[-1]

species=[SP]

coefficients=[]
f=open("" + SP + "/merged/coefficients.txt","r")
for l in f:
	coeff = l.strip("\n")
	coefficients.append(coeff)

f.close()

delta_distrib = range(5,1000,20) #start, end, increments # original 
#delta1 = range(0,100,20)
#delta2 = range(100,1000,100)
#delta_distrib = []
#delta_distrib.extend(delta1)
#delta_distrib.extend(delta2)
#R_distrib= frange(0,30,0.1)
R_distrib= frange(0,20,0.2) #start,end,increments # original 

#alt way to change number of simulations must call as:
#big_wrapper.py -num <#> <species>
NUMBER= len(coefficients) * len(delta_distrib) * len(R_distrib)
if "-test" in inputs:
	delta_distrib = range(5,25,20)
	R_distrib= frange(0,1,0.2)

else:
	pass

print(NUMBER," parameters to test")
print("coeff " + str(len(coefficients)))
print("delta " + str(len(delta_distrib))) 
print("R " + str(len(R_distrib)))

BATCH = 1000
print("This wrapper should submit ",1 + NUMBER/BATCH, " jobs, each running " , BATCH , " simulations")

nb=0
un,deux,trois,quatre,cinq,six,sept=[],[],[],[],[],[],[]
j=0
for sp in species:
	try:
		os.mkdir("" + sp + "/merged/simul")
	except OSError:
		pass
	try:
		os.mkdir("" + sp + "/merged/estimates")
	except OSError:
		pass
	f=open("" + sp + "/merged/parameters.txt","r")
	l=f.readline()
	f.close()
	a=l.strip("\n").split("\t")
	L = a[0]
	GC = a[1]
	kappa = a[2]
	FILES=os.listdir("" + sp + "/merged/simul")
	done_delta,done_R,done_coeff={},{},{}
	done={}
	for file in FILES:
		file = file.split(".fa")[0]
		b = file.split("_")
		done_coeff[b[1]] = "y"
		done_delta[b[2]] = "y"
		done_R[b[3]] = "y"
		done[file]="y"
	#if NUMBER > 300000:
		#BATCH = 1 + NUMBER / 30000
	print("BATCH SIZE= ",BATCH)
	for coeff in coefficients:
		for delta in delta_distrib:
			for R in R_distrib:
				#print "Launching ",sp,str(delta) + " " + str(R)
				#print coeff," ",delta," ",R
				name = "data_" + str(coeff) + "_" + str(float(delta)) + "_" + str(float(R))
				#if done_delta.has_key(str(delta)) and done_R.has_key(str(R)) and done_coeff.has_key(str(coeff)):
				if name in done:
					print("simulation with coeff= " ,coeff ," ,delta= ",delta," and R= ",R," already done. Skipping...")
				else:
					j+=1
					un.append(sp)
					deux.append(str(coeff))
					trois.append(str(L))
					quatre.append(str(GC))
					cinq.append(str(kappa))
					six.append(str(delta))
					sept.append(str(R))
					if j==BATCH:
						un = "-".join(un)
						deux = "-".join(deux)
						trois = "-".join(trois)
						quatre = "-".join(quatre)
						cinq = "-".join(cinq)
						six = "-".join(six)
						sept = "-".join(sept)
						#os.system("sbatch  launcher.slurm "   + str(un) + " " + str(deux) + " " + str(trois) + " " + str(quatre) + " " + str(cinq) + " " + str(six) + " " + str(sept))
						os.system("python  pipeline/launcher.py "   + str(un) + " " + str(deux) + " " + str(trois) + " " + str(quatre) + " " + str(cinq) + " " + str(six) + " " + str(sept))

						j=0
						un,deux,trois,quatre,cinq,six,sept=[],[],[],[],[],[],[]
						#os.system("sbatch  pipeline.slurm "   + sp + " " + coeff + " " + L + " " + GC + " " + kappa + " " + str(delta) + " " + str(R))
						nb+=1
	if j < BATCH:
		un = "-".join(un)
		deux = "-".join(deux)
		trois = "-".join(trois)
		quatre = "-".join(quatre)
		cinq = "-".join(cinq)
		six = "-".join(six)
		sept = "-".join(sept)
		#os.system("sbatch  launcher.slurm "   + str(un) + " " + str(deux) + " " + str(trois) + " " + str(quatre) + " " + str(cinq) + " " + str(six) + " " + str(sept))
		os.system("python  pipeline/launcher.py "   + str(un) + " " + str(deux) + " " + str(trois) + " " + str(quatre) + " " + str(cinq) + " " + str(six) + " " + str(sept))



print("Jobs launched= ",nb)
