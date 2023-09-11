
# Define GC% and Kappa

import sys

SP = sys.argv[-1]
species = [SP]


for sp in species:
	tmp={}
	f=open("" + sp + "/merged/merged_core.fa","r")
	for l in f:
		if l[0] == ">":
			id = l.strip("\n").strip(">")
			tmp[id]=[]
		else:
			tmp[id].append(l.strip("\n"))
	f.close()
	
	average=[]
	seq={}
	for id in tmp:
		seq[id] = "".join(tmp[id])
		L=len(seq[id])
		G = seq[id].count("G")
		C = seq[id].count("C")
		A = seq[id].count("A")
		T = seq[id].count("T")
		nb = (G + C) / float(A+T+G+C)
		average.append(nb)
	
	del tmp
	
	GC = 100 * sum(average) / len(average)
	
	
	
	kind={}
	kind["C"] = "pyrimidine"
	kind["G"] = "purine"
	kind["T"] = "pyrimidine"
	kind["A"] = "purine"
	
	alpha={}
	alpha["C"] = "C"
	alpha["G"] = "G"
	alpha["T"] = "T"
	alpha["A"] = "A"
	
	
	transitions,transversions=0,0
	i = 0
	while i < L:
		tmp=[]
		for id in seq:
			N = seq[id][i]
			try:
				tmp.append(alpha[N])
			except KeyError:
				pass
		unique = list(set(tmp))
		if len(unique) > 1:
			for N1 in unique:
				for N2 in unique:
					if N1 != N2:
						if kind[N1] == kind[N2]:
							transitions+=1
						else:
							transversions+=1
							
		i+=1
	
	
	kappa=transitions / float(transversions)
	
	print("Kappa= ",kappa)
	print("GC%= ",GC," %")
	print("L= ",L)
	
	h=open("" + sp + "/merged/parameters.txt","w")
	h.write(str(L) + "\t" + str(GC)  + "\t" + str(kappa) + "\n")
	h.close()
	
	
	
	
	
	
	
	
	
	
	
	
	
	