

import os
import sys



SP = sys.argv[-2]
species=[SP]

name = sys.argv[-1] + ".fa"

files = [name]

try:
	os.mkdir("" + SP + "/merged/all")
except OSError:
	pass



# Load distances
for data in files:
	data = data.split(".fa")[0] + ".txt"
	strains=[]	
	dist={}
	f=open("" + SP + '/merged/distances/' + data ,"r")
	for l in f:
		a=l.strip("\n").split("\t")
		st1,st2 = a[0], a[1]
		if st1 not in strains:
			strains.append(st1)
		if st1 in dist:
			pass
		else:
			dist[st1] = {}
		if st2 in dist:
			pass
		else:
			dist[st2] = {}
		dist[st1][st2] = float(a[2])
		dist[st2][st1] = float(a[2])
	
	f.close()
	
	
	
	tmp={}
	f=open("" + SP + "/merged/simul/" +  data.split(".txt")[0] + '.fa',"r")
	for l in f:
		if l[0] == '>':
			nb=0
			tag=0
			sp = l.strip('>').strip('\n') 
			tmp[sp] = []
		else:
			nb += len(l.strip('\n'))
			tmp[sp].append(l.strip('\n'))
	
	
	f.close()
	
	
	seq = {}
	for sp in strains:
		seq[sp] = ''.join(tmp[sp])
	
	
	
	subsets=[";".join(strains)]
	
	
	
	
	alpha=['A','C','G','T']
	
	LONGUEUR=len(seq[sp])
	for truc in subsets:
		strains = truc.split(';')
		bip=[]
		singleton,more=0,0
		i = 0
		r,m=0,0
		while i < LONGUEUR: #LONGUEUR:
			tmp=[]
			memo=[]
			for sp in strains:
				N = seq[sp][i]
				if N in alpha:
					tmp.append(N)
					memo.append(sp)
			tot = len(tmp)
			all = list(set(tmp))
			unique,number=[],[]
			for N in all:
				number.append(tmp.count(N))
				if tmp.count(N) >1:
					unique.append(N)
			if len(number) > 1:
				while 1 in number:
					number.remove(1)
					singleton+=1
					m+=1
				if len(number) == 2:																		##### 2 #####
					more += 1
					N1,N2 = unique[0],unique[1]
					nt1,nt2 = tmp.count(N1),tmp.count(N2)
					if nt1 <= nt2:
						minor = N1
					elif nt1 > nt2:
						minor = N2
					sac,other=[],[]
					j=0
					while j < len(tmp):
						N,sp = tmp[j],memo[j]
						if N == minor:
							sac.append(sp)
						else:
							other.append(sp)
						j+=1
					INTRA,INTER=[],[]
					for st1 in sac:
						for st2 in sac:
							if st1 != st2:
								INTRA.append(dist[st1][st2])
						for st2 in other:
							INTER.append(dist[st1][st2])
					if max(INTRA) > min(INTER):
						r+=1
						toto='r'
					else:
						toto='m'
						m+=1
					#print i,' ',tot,' ',unique,' ',number,' ',minor,' ',min(INTRA),' ',min(INTER),' ',toto
					bip.append(toto)
				elif len(number) == 3:																		##### 3 #####
					N1,N2,N3 = unique[0],unique[1],unique[2]
					check,check2=0,0
					done=[]
					k=0
					while k < 3:
						N,nt = unique[k],number[k]
						if nt == min(number):
							if check == 0:
								minor1 =  N
								done.append(N)
								check=1
						elif nt == max(number):
							if check2==0:
								major = N
								done.append(N)
								check2=1
						k+=1
					for N in unique:
						if N not in done:
							minor2 = N
					sac1,sac2,other=[],[],[]
					j=0
					while j < len(tmp):
						N,sp = tmp[j],memo[j]
						if N == minor1:
							sac1.append(sp)
						elif N == minor2:
							sac2.append(sp)
						else:
							other.append(sp)
						j+=1
					INTRA,INTER=[],[]
					for st1 in sac1:
						for st2 in sac1:
							if st1 != st2:
								INTRA.append(dist[st1][st2])
						for st2 in other:
							INTER.append(dist[st1][st2])
					if max(INTRA) > min(INTER):
						r+=1
						toto='r'
					else:
						toto='m'
						m+=1	
					#print i,' ',tot,' ',unique,' ',number,' ',minor1,' ',min(INTRA),' ',min(INTER),' ',toto
					bip.append(toto)
					INTRA,INTER=[],[]
					for st1 in sac2:
						for st2 in sac2:
							if st1 != st2:
								INTRA.append(dist[st1][st2])
						for st2 in other:
							INTER.append(dist[st1][st2])
					if max(INTRA) > min(INTER):
						r+=1
						toto='r'
					else:
						toto='m'
						m+=1
					#print i,' ',tot,' ',unique,' ',number,' ',minor2,' ',min(INTRA),' ',min(INTER),' ',toto
					bip.append(toto)
				elif len(number) == 4:																		##### 4 #####
					N1,N2,N3,N4 = unique[0],unique[1],unique[2],unique[3]
					done=[]
					check,check2=0,0
					k=0
					while k < 4:
						N,nt = unique[k],number[k]
						if nt == min(number):
							if check==0:
								minor1 =  N
								done.append(N)
								check=1
						elif nt == max(number):
							if check2==0:
								major = N
								done.append(N)
								check2=1
						k+=1
					left=[]
					for N in unique:
						if N not in done:
							left.append(N)
					souvenir=[]
					k=0
					while k < 4:
						N,nt = unique[k],number[k]
						if N in left:
							souvenir.append(nt)
						k+=1
					if souvenir[0] <= souvenir[1]:
						minor2,minor3 = left[0],left[1]
					else:
						minor2,minor3 = left[1],left[0]
					sac1,sac2,sac3,other=[],[],[],[]
					j=0
					while j < len(tmp):
						N,sp = tmp[j],memo[j]
						if N == minor1:
							sac1.append(sp)
						elif N == minor2:
							sac2.append(sp)
						elif N == minor3:
							sac3.append(sp)
						else:
							other.append(sp)
						j+=1
					INTRA,INTER=[],[]
					for st1 in sac1:
						for st2 in sac1:
							if st1 != st2:
								INTRA.append(dist[st1][st2])
						for st2 in other:
							INTER.append(dist[st1][st2])
					if max(INTRA) > min(INTER):
						r+=1
						toto='r'
					else:
						toto='m'
						m+=1	
					#print i,' ',tot,' ',unique,' ',number,' ',minor1,' ',min(INTRA),' ',min(INTER),' ',toto
					bip.append(toto)
					INTRA,INTER=[],[]
					for st1 in sac2:
						for st2 in sac2:
							if st1 != st2:
								INTRA.append(dist[st1][st2])
						for st2 in other:
							INTER.append(dist[st1][st2])
					if max(INTRA) > min(INTER):
						r+=1
						toto='r'
					else:
						toto='m'
						m+=1
					#print i,' ',tot,' ',unique,' ',number,' ',minor2,' ',min(INTRA),' ',min(INTER),' ',toto
					bip.append(toto)
					INTRA,INTER=[],[]
					for st1 in sac3:
						for st2 in sac3:
							if st1 != st2:
								INTRA.append(dist[st1][st2])
						for st2 in other:
							INTER.append(dist[st1][st2])
					if max(INTRA) > min(INTER):
						r+=1
						toto='r'
					else:
						toto='m'
						m+=1
					#print i,' ',tot,' ',unique,' ',number,' ',minor3,' ',min(INTRA),' ',min(INTER),' ',toto
					bip.append(toto)
			i+=1
		try:
			rm = float(r)/m
		except ZeroDivisionError:
			rm = 'NA'
		print(len(strains),' h/m= ', rm)      #,' r= ',r,' m= ',m	, '   Bips:  r= ',bip.count('r'),'  m= ',bip.count('m'),' |  for ',singleton,' singleton'
		h=open("" + SP + "/merged/all/" + data ,"w")
		h.write(str(r) + '\t' + str(m) + '\t' + str(rm) + '\t' + str(len(bip)) + '\n'   )
		h.close()
	
	
	
	
	