library('ggplot2')
rmsd <- read.csv("C:/Users/Administrator/Desktop/rmsd.csv", row.names=NULL, quote="\"", comment.char="")
qplot(Time,RMSD,data = rmsd,geom = 'line',xlab = 'Time(ns)',ylab = 'RMSD(nm)',main = 'JZ4_Heavy after lsq fit to Backbone')