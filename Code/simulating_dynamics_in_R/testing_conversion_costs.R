require(plyr)
require(deSolve)
source("Code/simulating_dynamics_in_R/model_file.r")
#source("Code/simulating_dynamics_in_R/testing_functions.R")
#source("Code/simulating_dynamics_in_R/model_file.r")

calc_resp_rate = function(mass,sp_type){
  if(sp_type=="invert"){
    a_t = 0.5
  }
  if(sp_type=="ectotherm"){
    a_t = 2.3
  }
  if(sp_type=="endotherm"){
    a_t = 54.9
  }
  return(mass^(-0.25)*a_t/52)
}

calc_max_consump_rate = function(mass,sp_type){
  if(sp_type=="invert"){
    a_j = 9.7
  }
  if(sp_type=="ectotherm"){
    a_j = 8.9
  }
  if(sp_type=="endotherm"){
    a_j = 89.2
  }
  return(mass^(-0.25)*a_j/52)
}

current_parameters = read.csv("data/K_dP_data.csv")
current_parameters = current_parameters[1,-1]
prey_mass = 0.0025
pred_mass = 40*prey_mass
prey_type ="invert"
pred_type ="invert"
herb_effic = 1-0.55
carn_effic = 1-0.15




current_parameters$eRP = 1; 
current_parameters$eRH = 0.3#(1-0.55); 
current_parameters$eHP = 0.3#(1-0.15);
current_parameters$mH = calc_resp_rate(prey_mass,prey_type)
current_parameters$mP = calc_resp_rate(pred_mass,pred_type)

current_parameters$aRH = 0.1
current_parameters$aHP = 0.1


current_parameters$hRH = herb_effic/calc_max_consump_rate(prey_mass,prey_type)
current_parameters$hHP = carn_effic/calc_max_consump_rate(pred_mass,pred_type)
current_parameters$dR =5
current_parameters$dH = 0.001
current_parameters$dP =0.

current_parameters$g = 0.5
current_parameters$K =current_parameters$g*12


starting_values = read.csv("data/starting_values.csv")
starting_values = as.matrix(starting_values)[1,-1]
starting_values[] = c(current_parameters$K, current_parameters$K,
                        current_parameters$K*0.2,current_parameters$K*0.3,
                        current_parameters$K*0.01,current_parameters$K*0.01)


model_output = ode(y=starting_values,
                   times=seq(0,52*100,length=1000),
                   maxsteps=500000,
                   func=TriTrophDynamics,
                   parms=current_parameters,
                   rtol= 1e-5,
                   conversion_costs=T)

#plot(model_output)

par(mfrow=c(1,3))

plot(model_output[,1]/52, model_output[,2],type="l",ylim=range(model_output[,2:3]),
     col="blue")
points(model_output[,1]/52,model_output[,3],type="l",col="red")
points(model_output[,1]/52,(model_output[,2]+model_output[,3])/2,type="l")
           
plot(model_output[,1]/52, model_output[,4],type="l",ylim=range(model_output[,4:5]),
     col="blue")
points(model_output[,1]/52,model_output[,5],type="l",col="red")
points(model_output[,1]/52,(model_output[,4]+model_output[,5])/2,type="l")

plot(model_output[,1]/52, model_output[,6],type="l",ylim=range(model_output[,6:7]),
     col="blue")
points(model_output[,1]/52, model_output[,7],type="l",col="red")
points(model_output[,1]/52,(model_output[,6]+model_output[,7])/2,type="l")
