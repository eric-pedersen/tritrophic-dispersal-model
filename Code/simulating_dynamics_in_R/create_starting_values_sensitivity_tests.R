# This script creates the starting values for running sensitivity tests (appendix B)
# These starting values are were run on the Collose cluster.

require(lhs)
require(dplyr)

calc_resp_rate = function(mass,sp_type){
  stopifnot(all(sp_type%in%c("invert","ectotherm","endotherm")))
  a_t = ifelse(sp_type=="invert", 0.5,
               ifelse(sp_type=="ectotherm", 2.3,54.9))
  return(mass^(-0.25)*a_t/52)
}

calc_max_consump_rate = function(mass,sp_type){
  stopifnot(all(sp_type%in%c("invert","ectotherm","endotherm")))
  a_j = ifelse(sp_type=="invert", 9.7,
               ifelse(sp_type=="ectotherm", 8.9,89.2))
  return(mass^(-0.25)*a_j/52)
}

set.seed(10)
starting_values_base = randomLHS(400,k=6)
colnames(starting_values_base) = c("R1","R2","H1","H2","P1","P2")

dR = 10^seq(-2, 1, length=30)
dH = 10^seq(-4, -1, length=30)
dP = 10^seq(-4, -1, length=30)

herb_effic = 1-0.55
carn_effic = 1-0.15
scenarios =1:4#c("base_w_conversion","base_w_handling",
           #"invert_invert", "ectotherm_ecotherm_large")

sensitivity_scenarios = data_frame(scenarios =scenarios,
                                   pred_type = c("ectotherm","ectotherm","invert","ectotherm"),
                                   prey_type= c("invert","invert","invert","ectotherm"),
                                   mass_ratio = 40, 
                                   prey_mass = c(0.0025,0.0025,0.0025, 0.025),
                                   g = c(2,2,0.5,2),
                                   herb_effic = c(0,herb_effic, herb_effic,herb_effic))

sensitivity_scenarios = sensitivity_scenarios %>% 
  mutate(pred_mass = prey_mass*mass_ratio, 
         K = g*c(6,6,12,6),
         mH = calc_resp_rate(prey_mass,prey_type),
         mP = calc_resp_rate(pred_mass,pred_type),
         hRH = herb_effic/calc_max_consump_rate(prey_mass,prey_type),
         hHP = carn_effic/calc_max_consump_rate(pred_mass,pred_type))

dR_dH_data = expand.grid(aRH = 0.1, aHP = 0.1, 
                         eRH=0.3,eRP=0.3,eHP=0.3,
                         scenarios = scenarios,
                         dR = dR, dH = dH, dP = 0.1)%>%
  as.data.frame(.)%>%
  left_join(sensitivity_scenarios) %>%
  select(-pred_type, -prey_type)


dR_dP_data = expand.grid(aRH = 0.1, aHP = 0.1, 
                         eRH=0.3,eRP=0.3,eHP=0.3,
                         scenarios = scenarios,
                         dR = dR, dH = 0.01, dP = dP)%>%
  as.data.frame(.)%>%
  mutate(dH = ifelse(scenarios%in%c("invert_invert", "ectotherm_ecotherm_large"),
                     0.001,dH)) %>%
  left_join(sensitivity_scenarios)%>%
  select(-pred_type, -prey_type)

dH_dP_data = expand.grid(aRH = 0.1, aHP = 0.1, 
                         eRH=0.3,eRP=0.3,eHP=0.3,
                         scenarios = scenarios,
                         dR = 5, dH = dH, dP = dP)%>%
  as.data.frame(.)%>%
  left_join(sensitivity_scenarios)%>%
  select(-pred_type, -prey_type)


write.csv(x= dR_dH_data, file="data/dR_dH_data.csv",row.names = F)
write.csv(x= dR_dP_data, file="data/dR_dP_data.csv",row.names = F)
write.csv(x= dH_dP_data, file="data/dH_dP_data.csv",row.names = F)
write.csv(x= starting_values_base, file="data/starting_values.csv",row.names = F)
