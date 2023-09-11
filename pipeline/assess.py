
import os
import sys


# Compare Pi and Theta to real values 
# Can we estimate how to re-scale the trees?

SP = sys.argv[-1]

species=[SP]



real={}
f=open("" + SP + "/merged/real/metrics.txt","r")
for l in f:
	a=l.strip("\n").split("\t")
	real[a[1]]=float(a[2])

f.close()


files=os.listdir("" + SP + "/merged/poly_rescale/")

print(len(files)," files")


theta,pi={},{}
for data in files:
	if data.startswith("data"):
		a = data.split(".txt")[0].split("_")
		coeff=float(a[1])
		dico={}
		f=open("" + SP + "/merged/poly_rescale/" + data ,"r")
		for l in f:
			a=l.strip("\n").split("\t")
			dico[a[1]]=float(a[2])
		f.close()
		theta[coeff] = dico["Theta"]
		pi[coeff] = dico["Pi"]
		
coefficients = theta.keys()
coefficients.sort()



memo=""
MIN=1
for coeff in coefficients:
	dist = abs(theta[coeff] - real["Theta"])
	if dist < MIN:
		MIN = dist
		memo=coeff


MEMO1=memo
print("Closest Theta for ", memo," Theta= ",theta[memo]," Real=",real["Theta"])


memo=""
MIN=1
for coeff in coefficients:
	dist = abs(pi[coeff] - real["Pi"])
	if dist < MIN:
		MIN = dist
		memo=coeff

MEMO2=memo
print("Closest Pi for ", memo," Pi= ",pi[memo]," Real=",real["Pi"])

MIN,MAX= min([MEMO1,MEMO2]),max([MEMO1,MEMO2])
print("rescale coefficients from ", MIN," to ",MAX)



h=open("" + SP + "/merged/coefficients.txt","w")
i = MIN - 0.05
if i <= 0:
	i=0.01
j = MAX +0.05
if j > 1:
	j=1

while i <= j:
	h.write(str(i) + "\n")
	i+=0.01




















	


