
##############################################
recABC Tested with Python v3.11.4 and R v4.3.1
   - requires Python libraries: NumPy
   - requires R libraries: abc, Metrics
##############################################

to run (*):
   from:
   
      python recABC_master.py Bacillus_safensis

      (*) Currently there is no way to specify the number of simulations you want to run in recABC. 	Please see "Option for Test Run" for options on exiting the program early.


Runtime Information:
   Test run of serialized 35k simulations required ~24 hours on Apple M1 Pro with 32GB 
   available RAM (ram requirements were not computed but would estimate about 5G needed 
   to run) and required ~7GB storage. Full run would take ~15 days and require ~140GB 
   Storage.

   
Option for Test Run: 
   To run a smaller number of simulations(*) you can run the pipeline for a set amount of time, 
   end the run, and then create the abc.txt output file with:
      
      python recABC_terminate.py Bacillus_safensis

      (*)NOTE: If running fewer than 100k simulations, you may need to increase the ABC 
      tolerance (line 41 of abc.R in /pipeline) from 1e-4 (Chooses 0.0001% of best fitting 
      simulations which must result in a nonzero number to be successful). 
      Receiving either of the below two error messages after running recABC_terminate.py 
      will indicate the need to change line 41 of abc.R:
                     1) Loading required package: locfit
                        locfit 1.5-9.8 	 2023-06-11
                        Error in lsfit(scaled.sumstat[wt1, ], log(residuals^2), wt = weights) : 
                          NA/NaN/Inf in 'y'
                        Calls: abc -> lsfit
                        In addition: Warning message:
                        All parameters are "none" transformed. 
                        Execution halted
                     2) Loading required package: locfit
                        locfit 1.5-9.8 	 2023-06-11
                        Error in lsfit(scaled.sumstat[wt1, ], param[wt1, ], wt = weights) : 
                        only 3 cases, but 4 variables
                        Calls: abc -> lsfit
                        In addition: Warning message:
                        All parameters are "none" transformed. 
                        Execution halted

Reading output:
   Results of the recABC analysis can be found in Bacillus_safensis/merged/abc.txt 
   and represent the data from the 0.0001% (unless the tolerance has been changed) of simulations 
   which best match real species data according to comparisons between summary statistics (LD_fit, h/m, pi):
      col1: branch length rescaling coefficient of simulation
      col2: r/m of simulation
      col3: h/m of simulation
      col4: pi of simulation 
      col5: LD_fit of simulation
   The parameters from all simulations can be found in Bacillus_safensis/merged/gather.txt
   You should expect r/m values to be between r/m=0-3 with values converging toward an 
   average of 2.5 as the simulation number approaches 500k. 


