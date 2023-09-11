import os
import sys

sp = sys.argv[-1]

path = ''

file = open(path + sp + '/merged/gather.txt', 'r')
out = open(path + sp + '/merged/gather2.txt', 'w')
length = 9
for line in file:
    if len(line.split())!=length:
        pass
    else:
        out.write(line)
file.close()
out.close()


