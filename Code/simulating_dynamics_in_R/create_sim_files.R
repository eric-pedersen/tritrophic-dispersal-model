# Creates the simulation files for running the main simulations on a cluster.
# Basically, each of these files needs to be run (there are n_blocks of them for each figure)
# Assumes that you're running this on an 8-core machine. To change this, alter the value in
# getOption("cl.cores", 8) to however many cores you need.
# You'll need to move the output files (all in the form of something like "dR_dH_1_output.csv") to
# the folder output/simulations/senstivity_tests


n_blocks = 10

for(i in c("dR_dH","dR_dP","dH_dP","K_dR","K_dH","K_dP")){
  for(j in 1:n_blocks){
    sim_file_name = paste(i,j, "code.R",sep="_")
    sim_file_name = paste("code/",sim_file_name,sep="/")
    script_file_name = paste(i,j, "script.sh",sep="_")
    script_file_name = paste("scripts/",script_file_name,sep="/")
    sink(sim_file_name)
    cat('require(parallel)
require(plyr)
InitiateSims = function(...){
  require(tritrophsim)
  return(RunSims(...))
}
require(tritrophsim)
#source("code/testing_functions.R")
#source("code/model_file.r")
starting_values = read.csv("data/starting_values_base.csv")
starting_values = as.matrix(starting_values[,-1])
'
      )
    cat('current_data = read.csv("data/', i, 'data.csv")',sep=c('','_','_'))
    cat('\n')
    cat('current_data = current_data[,-1]
n_dat = nrow(starting_values)
')
cat('starting_values = starting_values[((',j,'-1)*(n_dat/',n_blocks,')+1):',
    '(',j,'*(n_dat/',n_blocks,')),]',sep="")
    
cat('
cl <- makeCluster(getOption("cl.cores", 8))

model_outputs = parApply(cl=cl,X=starting_values,MARGIN=1,FUN= InitiateSims, 
                         parameter_values =current_data, rescale_start=T)
model_outputs = ldply(model_outputs)

'
  )
    cat('write.csv(x =model_outputs, file="output/', i, j,'output.csv")',sep=c('','_','_')) 
    cat('\n')
    cat('stopCluster(cl)')
    sink()
  
    sink(script_file_name)
    cat(
'#!/bin/bash
#PBS -A uxb-461-aa
#PBS -l nodes=1:ppn=8
#PBS -l walltime=48:00:00
')
    cat(paste("#PBS -o ClusterOut_",i,"_",j,".txt",'\n',sep=""))
    cat(paste("#PBS -e ClusterError_",i,"_",j,".txt",sep=""))
    cat('
module load apps/r/3.0.3
cd ~/tri_trophic_model/
')
    cat(paste('Rscript code/',paste(i,j, "code.R",sep="_"),sep=""))
    sink()
  
}
}