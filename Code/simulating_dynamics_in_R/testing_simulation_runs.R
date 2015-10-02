#Code to test that simulations are running appropriately locally

require(plyr)
require(tritrophsim)
#source("Code/simulating_dynamics_in_R/testing_functions.R")
#source("Code/simulating_dynamics_in_R/model_file.r")
starting_values = read.csv("data/starting_values.csv")
starting_values = as.matrix(starting_values[,-1])
current_data = read.csv("data/K_dP_data.csv")
current_data = current_data[,-1]
current_data= subset(current_data,1<K&K<5&0.04<dP&dP<0.06)
run_time = system.time({
model_outputs = RunSims(starting_points=starting_values[1,],use_jacob=F,use_block_tests=T,
                        restart_at_non_const=T,
                        parameter_values=current_data[1:11,])
})
print(run_time)
