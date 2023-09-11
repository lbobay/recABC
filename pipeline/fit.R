
args = commandArgs(trailingOnly=TRUE)

SP = args[1]
file = args[2]



new = as.character(paste("",SP,"/merged/LD/",file,sep=""))
out = as.character(paste("",SP,"/merged/fit/",file,sep=""))



# 1 estimate parameters for real data
tab=read.table(paste("",SP,"/merged/real/LD.txt",sep=""))
x = tab$V1
y = tab$V2
trbFunb <- function(x,k,r0,r1){(r0 * exp(-k * x)) + r1}
Zfit <- nls(y~trbFunb(x,k,r0,r1),start=list(k=0.0025,r0=0.2,r1=0.07),algorithm="port")

# 2 Compare simulations to the model with RMSE
require(Metrics)
test = read.table(new)
Y = test$V2
predictions <- predict(Zfit, y)
estimate = rmse(Y, predictions)
self = rmse(y, predictions)


print(estimate)


write(estimate,file=out)
