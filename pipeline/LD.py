
import os
import sys






SP = sys.argv[-2]
species=[SP]

name = sys.argv[-1] + ".fa"

files = [name]

try:
	os.mkdir("" + SP + "/merged/LD")
except OSError:
	pass


distrib=[]

for data in files:
	dico={}
	h=open("" + SP + "/merged/LD/" + data.split(".fa")[0] + ".txt" ,"w")
	ordered=[]
	seq={}
	f=open("" + SP  + "/merged/simul/" + data ,"r")
	for l in f:
		if l[0] == ">":
			st = l.strip(">").strip("\n")
			ordered.append(st)
		else:
			seq[st] = l.strip("\n")
	f.close()
	sorted(ordered)
	nb = float(len(ordered))
	L = len(seq[st])
	i=0
	while i < L:
		tmp1=[]
		for st in ordered:
			N=seq[st][i]
			tmp1.append(N)
		unique1 = list(set(tmp1))
		if len(unique1) == 2:
			j= i -1000
			if j < 0:
				j=0
			limit = i+1000
			if limit > 10000:
				limit=10000
			while j < limit:
				if j > i:
					pairs=[]
					tmp2=[]
					k=0
					while k < nb:
						st = ordered[k]
						N=seq[st][j]
						tmp2.append(N)
						resu = tmp1[k] + "-" + N
						pairs.append(resu)
						k+=1
					unique2 = list(set(tmp2))
					if len(unique2) ==  2:
						distance = abs(i-j)
						A1,B1 = unique1[0],unique1[1]
						A2,B2 = unique2[0],unique2[1]
						resuA = A1 + "-" + A2
						freq = pairs.count(resuA)/nb
						fA1,fB1 = tmp1.count(A1) / nb , tmp1.count(B1) / nb 
						fA2,fB2 = tmp2.count(A2) / nb , tmp2.count(B2) / nb 
						r2 = ((freq - fA1 * fA2)**2) / (fA1 * fB1 * fA2  * fB2  )
						#print i," ",j," ",distance," ",fA1," ",fB1," ",fA2," ",fB2," ",A1," ",B1," ",A2," ",B2,"  freq= ",freq," ",r2
						distrib.append(r2)
						#h.write(str(distance) + "\t" + str(r2) + "\n")
						if distance in dico:
							dico[distance].append(r2)
						else:
							dico[distance]=[r2]
				j+=1
		i+=1
		toto = dico.keys()
		sorted(toto)
	for dist in dico:
		sorted(dico[dist])
		mid = float(len(dico[dist])) / 2
		if len(dico[dist])%2 == 0:
			median = dico[dist][int(mid)]
			h.write(str(dist) + "\t" + str(sum(dico[dist]) / len(dico[dist])) +  "\t" + str(median)  + "\n")
		else:
			if len(dico[dist]) >= 2:
				mid1,mid2 = int(mid),int(mid) + 1
				median = (dico[dist][mid1] + dico[dist][mid2]) / 2
				h.write(str(dist) + "\t" + str(sum(dico[dist]) / len(dico[dist])) +  "\t" + str(median)  + "\n")
	h.close()




print(min(distrib)," ",max(distrib))

