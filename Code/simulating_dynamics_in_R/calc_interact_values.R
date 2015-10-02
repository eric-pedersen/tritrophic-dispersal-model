kg_to_j = 7e6
temp_level = 290
mass_pred = (5*kg_to_j)
mass_herb = mass_pred/2


intercept = 8.416
temp_effect = -2780.516
sessile = 0.011
swimming = 0.157
carn = -0.032
vision = 0.081
non_starved = 0.024
depth = 1
log_term = 10
days_to_weeks = 28
herb_r_log = intercept+ temp_effect/temp_level+sessile-carn-vision+
  non_starved -0.03*log(depth, log_term)-0.2*log(mass_herb,log_term)

pred_r_log = intercept+ temp_effect/temp_level +swimming +carn+vision+
  non_starved  -0.03*log(depth, log_term)-0.2*log(mass_pred,log_term)


herb_r = log_term^herb_r_log*days_to_weeks
pred_r = log_term^pred_r_log*days_to_weeks


print(c(herb_r,pred_r))
