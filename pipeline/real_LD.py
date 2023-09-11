#calculate LDfit
import os
import sys






SP = sys.argv[-1]
species=[SP]



alpha={}
alpha["A"]="yes"
alpha["C"]="yes"
alpha["G"]="yes"
alpha["T"]="yes"

distrib=[]

if 1==1:
	dico={}
	h=open("" + SP + "/merged/real/LD.txt" ,"w")
	ordered=[]
	tmp={}
	f=open("" + SP  + "/merged/merged_core.fa" ,"r")
	for l in f:
		if l[0] == ">":
			st = l.strip(">").strip("\n")
			tmp[st] = []
			ordered.append(st)
		else:
			tmp[st].append(l.strip("\n"))
	f.close()
	seq={}
	for st in tmp:
		seq[st] = "".join(tmp[st])
	del tmp
	sorted(ordered)
	nb = float(len(ordered))
	L = len(seq[st])
	i=0
	while i < L:
		tmp1=[]
		ref={}
		for st in ordered:
			N=seq[st][i]
			if N in alpha:
				ref[st] = N
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
					tmp2,tmp1=[],[]
					for st in ordered:
						N=seq[st][j]
						if N in alpha and st in ref:
							tmp2.append(N)
							resu = ref[st] + "-" + N
							tmp1.append(ref[st])
							pairs.append(resu)
					unique2 = list(set(tmp2))
					unique1 = list(set(tmp1))
					nb = float(len(tmp1))
					if len(unique2) ==  2 and len(unique1) == 2 and nb/len(ordered)>=0.75:
						distance = abs(i-j)
						A1,B1 = unique1[0],unique1[1]
						A2,B2 = unique2[0],unique2[1]
						resuA = A1 + "-" + A2
						freq = pairs.count(resuA)/nb
						#print i," ",j," ",nb," ",unique1," ",unique2, " ",  freq," ",pairs," ",resuA
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
	for dist in sorted(dico):
		dico[dist]
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

