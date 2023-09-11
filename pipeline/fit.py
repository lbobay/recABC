
import os
import sys

SP = sys.argv[-2]


species=[SP]
name = sys.argv[-1] + ".txt"

try:
	os.mkdir("" + SP + "/merged/fit/")
except OSError:
	pass

simulations = [name]


for file in simulations:
	os.system("Rscript --vanilla pipeline/fit.R " + SP + " " + file)


