##################################################
##################################################
####### Two-dimensional bifurcations with ########
## respect to two separate dispersal parameters ##
##################################################
##################################################

###########################
###### #1: dR / dH ########
###########################


# Following the branch point for the asymmetric equm
dX_dY_plot = auto.run(asym_branch_dH,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','dH'],
                                  IPS = 1,
                                  ISW=2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_dY_plot = auto.rl(dX_dY_plot) 
dX_dY_plot = dX_dY_plot + auto.run(asym_branch_dH,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','dH'],
                                  IPS = 1,
                                  ISW=2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})

dX_dY_plot = auto.rl(dX_dY_plot) 


                         

                            
#following the asymmetric Hopf bifurcations                                          
dX_dY_plot  = dX_dY_plot + auto.run(asym_hopf_dR,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','dH'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_dY_plot = auto.rl(dX_dY_plot) 
dX_dY_plot  = dX_dY_plot + auto.run(asym_hopf_dR,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','dH'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
dX_dY_plot = auto.rl(dX_dY_plot)                                                                      
dX_dY_plot  = dX_dY_plot + auto.run(asym_hopf_dH,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','dH'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_dY_plot = auto.rl(dX_dY_plot) 

dX_dY_plot  = dX_dY_plot + auto.run(asym_hopf_dH,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','dH'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
dX_dY_plot = auto.rl(dX_dY_plot)                                                              

auto.cl()

#following the Hopf Bifurcation induced by dispersal - Asymmetric Tritrophic
dX_dY_plot  = dX_dY_plot + auto.run(sym_disperse_hopf_dR,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','dH'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_dY_plot = auto.rl(dX_dY_plot) 
dX_dY_plot  = dX_dY_plot + auto.run(sym_disperse_hopf_dR,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','dH'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
dX_dY_plot = auto.rl(dX_dY_plot)






###########################
###### #2: dH / dP ########
###########################


# Following the branch point for the asymetric equm
dX_dY_plot = dX_dY_plot+ auto.run(asym_branch_dH,
                                  c='spatial_IGP.FP',
                                  ICP = ['dH','dP'],
                                  IPS = 1,
                                  ISW=2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_dY_plot = auto.rl(dX_dY_plot) 
dX_dY_plot = dX_dY_plot + auto.run(asym_branch_dH,
                                  c='spatial_IGP.FP',
                                  ICP = ['dH','dP'],
                                  IPS = 1,
                                  ISW=2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_dY_plot = auto.rl(dX_dY_plot) 


                         

                            
#following the asymmetric Hopf bifurcation                                            
dX_dY_plot  = dX_dY_plot + auto.run(asym_hopf_dH,
                                  c='spatial_IGP.FP',
                                  ICP = ['dH','dP'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_dY_plot = auto.rl(dX_dY_plot) 
dX_dY_plot  = dX_dY_plot + auto.run(asym_hopf_dH,
                                  c='spatial_IGP.FP',
                                  ICP = ['dH','dP'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
dX_dY_plot = auto.rl(dX_dY_plot)           
dX_dY_plot  = dX_dY_plot + auto.run(asym_hopf_dP,
                                  c='spatial_IGP.FP',
                                  ICP = ['dH','dP'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_dY_plot = auto.rl(dX_dY_plot) 
dX_dY_plot  = dX_dY_plot + auto.run(asym_hopf_dP,
                                  c='spatial_IGP.FP',
                                  ICP = ['dH','dP'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
dX_dY_plot = auto.rl(dX_dY_plot)           

auto.cl()

dX_dY_plot  = dX_dY_plot + auto.run(asym_hopf_dH_low,
                                  c='spatial_IGP.FP',
                                  ICP = ['dH','dP'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_dY_plot = auto.rl(dX_dY_plot) 
dX_dY_plot  = dX_dY_plot + auto.run(asym_hopf_dH_low,
                                  c='spatial_IGP.FP',
                                  ICP = ['dH','dP'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
dX_dY_plot = auto.rl(dX_dY_plot)           

auto.cl()



#following the Hopf Bifurcation induced by dispersal - Asymmetric Tritrophic

dX_dY_plot  = dX_dY_plot + auto.run(sym_disperse_hopf_dP,
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','dH'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_dY_plot = auto.rl(dX_dY_plot) 
dX_dY_plot  = dX_dY_plot + auto.run(sym_disperse_hopf_dP,
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','dH'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
dX_dY_plot = auto.rl(dX_dY_plot)



###########################
##### #3: dR / dP #########
###########################


# Following the branch point for the asymmetric equm
dX_dY_plot = dX_dY_plot+ auto.run(asym_branch_dR,
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','dR'],
                                  IPS = 1,
                                  ISW=2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_dY_plot = auto.rl(dX_dY_plot) 
dX_dY_plot = dX_dY_plot + auto.run(asym_branch_dR,
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','dR'],
                                  IPS = 1,
                                  ISW=2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.05, 
                                  DSMIN= 0.005, 
                                  DSMAX=   0.01,
                                  NMX=  2000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_dY_plot = auto.rl(dX_dY_plot) 


                         
                            
#following the asymmetric Hopf bifurcation                                            
dX_dY_plot  = dX_dY_plot + auto.run(asym_hopf_dP,
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','dR'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.0005, 
                                  DSMIN= 0.00005, 
                                  DSMAX=   0.001,
                                  NMX=  50000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_dY_plot = auto.rl(dX_dY_plot) 
dX_dY_plot  = dX_dY_plot + auto.run(asym_hopf_dP,
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','dR'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.001,
                                  NMX=  7000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
dX_dY_plot = auto.rl(dX_dY_plot) 
  
dX_dY_plot  = dX_dY_plot + auto.run(asym_hopf_dR,
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','dR'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  8000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_dY_plot = auto.rl(dX_dY_plot) 
dX_dY_plot  = dX_dY_plot + auto.run(asym_hopf_dR,
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','dR'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.001,
                                  NMX=  8000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
dX_dY_plot = auto.rl(dX_dY_plot)   


#following the Hopf Bifurcation induced by dispersal - Asymmetric Tritrophic

dX_dY_plot  = dX_dY_plot + auto.run(sym_disperse_hopf_dP,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','dP'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_dY_plot = auto.rl(dX_dY_plot) 
dX_dY_plot  = dX_dY_plot + auto.run(sym_disperse_hopf_dP,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','dP'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
dX_dY_plot = auto.rl(dX_dY_plot)


dX_dY_plot  = dX_dY_plot + auto.run(sym_disperse_hopf_dR,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','dP'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_dY_plot = auto.rl(dX_dY_plot) 
dX_dY_plot  = dX_dY_plot + auto.run(sym_disperse_hopf_dR,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','dP'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
dX_dY_plot = auto.rl(dX_dY_plot)


###############################################
#### Following the limit cycle branch that ####
### leads to bistability, and the bistability##
### inducing fold in limit cycles #############
###############################################

plot_pairs = [("dR","dP"),("dR","dH"),("dH","dP")]

for i in plot_pairs:
    first_parameter = i[0]
    second_parameter = i[1]
    
    dX_dY_plot  = dX_dY_plot + auto.run(limit_branch_points[first_parameter], 
                                  c='spatial_IGP.FP',
                                  ICP = [first_parameter,second_parameter,11],
                                  IPS=2,
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.005, 
                                  DSMAX=   0.01,
                                  NMX=  70000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
    
    dX_dY_plot  = dX_dY_plot + auto.run(limit_branch_points[first_parameter], 
                                  c='spatial_IGP.FP',
                                  ICP = [first_parameter,second_parameter,11],
                                  IPS=2,
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.005, 
                                  DSMAX=   0.01,
                                  NMX=  70000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})    
    
    
    
    
    dX_dY_plot  = dX_dY_plot + auto.run(fold_points[first_parameter], 
                                  c='spatial_IGP.FP',
                                  ICP = [first_parameter,second_parameter,11],
                                  IPS=2,
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.005, 
                                  DSMAX=   0.01,
                                  NMX=  70000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
    
    dX_dY_plot  = dX_dY_plot + auto.run(fold_points[first_parameter], 
                                  c='spatial_IGP.FP',
                                  ICP = [first_parameter,second_parameter,11],
                                  IPS=2,
                                  ISP=1,
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.005, 
                                  DSMAX=   0.01,
                                  NMX=  70000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})     
    
dX_dY_plot = auto.rl(dX_dY_plot)   
auto.cl()
    
