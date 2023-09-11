args = commandArgs(trailingOnly=TRUE)

SP = args[1]

# 1 estimate parameters for real data
tab=read.table(paste("",SP,"/merged/real/LD.txt",sep=""))
x = tab$V1
y = tab$V2
trbFunb <- function(x,r0,r1){r0 *  x + r1}
Zfit <- nls(y~trbFunb(x,r0,r1),start=list(r0=0.2,r1=0.07),algorithm="port")



# 2 Compare to itself with RMSE
require(Metrics)
predictions <- predict(Zfit, y)
self = rmse(y, predictions)




write(self,file=paste("",SP,"/merged/real/self.txt",sep=""))
