


# abc(target, param, sumstat, tol, method, hcorr = TRUE, transf = 'none',
# logit.bounds, subset = NULL, kernel = 'epanechnikov', numnet = 10, sizenet = 5,
# lambda = c(0.0001,0.001,0.01), trace = FALSE, maxit = 500, ...)



# target = vector of summary statistics of observed data param = parameters of
# the simulation sumstat = vector of summary statistics of simulated data tol =
# tolerance, the required proportion of points accepted nearest the target
# values.  method = Possible values are 'rejection', 'loclinear', 'neuralnet' and
# 'ridge'

# the function cv4abc() can help chose the tolerance rate the function hist.abc()
# makes histograms of posterior samples from objects of class 'abc' the function
# plot.abc() to plot results for objects of class 'abc' generated with methods
# 'loclinear' or 'neuralnet'
options(digits = 15)
args = commandArgs(trailingOnly = TRUE)

SP = args[1]
pi = as.numeric(args[2])
self = as.numeric(args[3])
hm = as.numeric(args[4])


library(abc)


# target=c(0.0367814657582,0.0205615,1.31587297795) # vector: Pi , LD_fit, h/m
# tab=read.table(paste('gather.txt',sep=''),h=T)

target = c(pi, self, hm)
# param=c(100,1.0,0.2) # Data frame of parameters sumstat = c(0.02,0.3,1.3) #
# Data frame of simulations


#abc tolerance
tol = 1e-04


tab = read.table(paste('', SP, "/merged/gather.txt", sep = ""), h = T)
# param = data.frame(tab$coeff,tab$delta,tab$Rho_theta)
w = which(tab$hm != "NA" )


param = data.frame(tab$coeff[w], tab$rm[w], tab$hm[w], tab$Pi[w], tab$fit[w])
sumstat = data.frame(tab$Pi[w], tab$fit[w], tab$hm[w])

param <- param[complete.cases(param), ]
sumstat <- sumstat[complete.cases(sumstat), ]

toto = abc(target, param, sumstat, tol, method = "neuralnet")

# plot(toto,param)

# cv4abc(param,sumstat,toto,nval=100,tols=c(0.01,0.001,0.0001),method='loclinear')

#M = median(toto[2]$unadj.values[, 2])

#pdf(paste('', SP, "/merged/Test.pdf", sep = ""))
#par(mfrow = c(2, 2), bty = "n")
#hist(tab$rm, nclass = 100, col = "grey", xlim = c(0, 10), xlab = expression(italic("r/m")), 
# main = expression("Prior distribution"), las = 1, cex.axis = 0.8, cex.lab = 0.8)
#abline(v = M, lty = 2, col = "dark red")

#lines(density(toto[2]$unadj.values[, 2]), col = "red", xlim = c(0, 10))
#plot(density(toto[2]$unadj.values[, 2]), col = "red", xlim = c(0, 10))
#abline(v = M, lty = 2, col = "dark red")

#boxplot(toto[2]$unadj.values[, 2], -10, -10, -10, -10, col = "dark red", ylim = c(0, 
# 10), xaxt = "n", las = 1, cex.axis = 0.8, cex.lab = 0.8, ylab = expression(italic("r/m")), 
# main = expression(paste("Inferred ", italic("r/m"), "")))
#title(main = expression("Tolerance = 0.01%"), line = 0.5, cex.main = 0.8)
#hist(toto[2]$unadj.values[, 2], nclass = 5, col = "dark red", xlim = c(0, 10))
# hist(toto[1]$adj.values[,2],nclass=5,col='dark red',xlim=c(0,10))
#dev.off()

stuff = matrix(toto[2]$unadj.values, ncol = 5)
write.matrix(stuff, file = paste('', SP, "/merged/abc.txt", sep = ""))

quit(save = "no")
# write.matrix(stuff,file='abc.txt')
