# note to self version control: retired: .sort() .has_key()


#Tested with Python 3.11.4 and R 4.3.1
#requires Python: NumPy
#requires R: abc, Metrics

import os
import sys
import time

#start = time.perf_counter()

import os

#print('Number of CPUs in the system: {}'.format(os.cpu_count()))

#one = os.cpu_count()

#print(one)


SP = sys.argv[-1]

#print("0. Launch codons.py")
#os.system("python  pipeline/codons.py " + SP) #ok

print("0.1 Launch extract_names.py")
f = ''+ SP+'/merged/old.fa'
if os.path.isfile(f)==True: #fix to avoid overwrite of name key
    pass
else:
   os.system("python  pipeline/extract_names.py " + SP) #ok


print("1. Launch branch_length.py")
os.system("python  pipeline/branch_length.py " + SP) #ok

print("2. Launch parameters.py")
os.system("python pipeline/parameters.py " + SP) #ok

print("3. Launch real scripts")
os.system("python pipeline/real_poly.py " + SP) #ok
os.system("python pipeline/real_all.py " + SP) #ok
os.system("python pipeline/real_LD.py " + SP) #ok
#
#
print("4. Launch rescale.py")
os.system("python pipeline/wrapper_rescale.py " + SP) #ok
   ###calls rescale.py requires numpy #ok

#
print("5. Launch poly_rescale.py")
os.system("python pipeline/poly_rescale.py " + SP) #ok


print("6. Launch  assess.py")
os.system("python  pipeline/assess_genes.py " + SP) #ok
  ##requires numpy

print("Step2 0 launch big_wrapper.py")
os.system("python  pipeline/big_wrapper.py " + SP) #ok
   #calls launcher.py #ok
       #calls pipeline.py #ok
           #calls simulation.py #ok
           #calls poly.py #ok
           #calls LD.py #ok
           #calls fit.py #ok
               #calls fit.R #ok
           #calls all.py #ok
print("Step3 0 Launch terminate.py")
os.system("python  pipeline/terminate.py " + SP)
   #calls gather.py
   #calls rm.py #ok
   #calls self.R #ok requires Metrics
   #calls abc.R #ok requires abc

#end = time.perf_counter()
#times = (((end-start)/60)/60)
#print("runtime: ",times, " hours")
