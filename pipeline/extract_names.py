#create new concat and tree file where long names are abbreviated

import os
import sys


SP = sys.argv[-1]
species = [SP]


TREE = SP + ".tree"


path = "" + SP + "/merged/"


#os.system('cp ' + '' + SP + '/concat.fa ' + path + '/merged_core.fa')
#os.system('cp ' + '' + SP + '/' + TREE + ' ' + path)



f=open(path + TREE,"r")
l=f.readline()
f.close()#



os.system("cp " + path + TREE + " " + path + "old.tree")#

symbols=[",","(",")",":",";"]#


link={}
bag=[]
tag=0
l=l.strip("\n")
i=1
while i < len(l):
	j=i-1
	if l[i] in symbols:
		if tag == 1:
			bag.append(taxa)
			link[taxa] = souvenir + taxa
			tag=0
	else:
		if l[j] == "(" or l[j] == ",":
			souvenir=l[j]
			taxa = l[i]
			tag=1
		else:
			taxa+=l[i]
	i+=1#

print(bag)#

memo=l#


NAME={}
h=open(path + "names.txt","w")
nb=0
for stuff in bag:
	if 1==1:
		if 2==2:
			taxa = stuff
			#print(taxa)
			nb+=1
			if nb < 10:
				new = "BOZO000" + str(nb) + ":"
			elif nb < 100:
				new = "BOZO00" + str(nb)  + ":"
			elif nb < 1000:
				new = "BOZO0" + str(nb)  + ":"
			elif nb < 10000:
				new = "BOZO" + str(nb)  + ":"
			h.write(new.strip(":") + "\t" + taxa + "\n")
			NAME[taxa] = new.strip(":")
			taxa = taxa + ":"
			new = link[taxa.strip(":")][0] + new
			thingy = link[taxa.strip(":")] + ":"
			memo = memo.replace(thingy,new)#

h.close()#




print("Found ",nb,"taxa in the tree")#

new=""
tmp=""
tag=0
for L in memo:
	if L == ")":
		tag=1
		tmp+=L
	if tag==0:
		new+=L
	elif tag==1:
		if L==":":
			tmp+=L
			new+=tmp
			tag=0
			tmp=""#
new += tmp
new+=";"#
h=open(path + SP + ".tree","w")
h.write(new)
h.close()#

f=open(path + "merged_core.fa","r")
h=open(path + "tmp","w")
for l in f:
	if l[0]==">":
		st = l.strip("\n").strip(">")
		h.write(">" + NAME[st] + "\n")
	else:
		h.write(l)#
f.close()
h.close()#
os.system("mv  " +  path + "merged_core.fa " + path  + "old.fa" )
os.system("mv  " +  path + "tmp " + path  + "merged_core.fa" )
