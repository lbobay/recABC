
import sys
import os

SP = sys.argv[-1]




try:
	os.mkdir("" + SP + "/merged/real")
except OSError:
	pass



if 1==1:
	if 1==1:
		tmp={}
		f=open("" + SP + "/merged/merged_core.fa","r")
		for l in f:
			if l[0]==">":
				id = l.strip("\n").strip(">")
				tmp[id]=[]
			else:
				tmp[id].append(l.strip("\n"))
		
		f.close()
		
		seq={}
		for id in tmp:
			seq[id] = "".join(tmp[id])
			
		
		length=len(seq[id])
			
		print("LENGTH= ",length)


		tot=0.0
		nb=0
		i=0
		while i < length:
			tmp=[]
			for id in seq:
				N= seq[id][i]
				if N != "-" and N != "N":
					if N not in tmp:
						tmp.append(N)
			if len(tmp) > 0:
				tot+=1
			if len(tmp)>1:
				nb+=1
			i+=1
		
		
		h=open("" + SP + "/merged/real/metrics.txt","w")
		h.write(SP + "\tTheta\t" + str(nb/tot) + "\n")
		h.close()
		print("Theta= ",nb/tot)
		
		
		
		g=open("" + SP + "/merged/real/distances.txt","w")
		average=[]
		pie={}
		for id1 in seq:
			#print(id1)
			pie[id1]={}
			for id2 in seq:
				if id1 != id2:
					tot=0.0
					diff=0
					i=0
					while i < len(seq[id1]):
						N1,N2 = seq[id1][i],seq[id2][i]
						if N1 != "-" and N1 != "N" and N2 != "-" and N2 != "N":
							tot+=1
							if N1!=N2:
								diff+=1
						i+=1
					pie[id1][id2] = diff / tot
					g.write(id1 + "\t" + id2 + "\t" + str(diff / tot) + "\n")
					average.append(diff / tot)
		
		g.close()
		print("PI= ",sum(average)/len(average))
		
		h=open("" + SP + "/merged/real/metrics.txt","a")
		h.write(SP + "\tPi\t" + str(sum(average)/len(average)) + "\n")
		h.close()
		
		