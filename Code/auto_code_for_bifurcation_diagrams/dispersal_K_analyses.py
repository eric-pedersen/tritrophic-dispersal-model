##################################################
##################################################
####### Two-dimensional bifurcations with ########
########### respect to dispersal and K ###########
##################################################
##################################################



###########################
####### #1: dR ############
###########################


# Following the branch point for the asymetric equm
dX_K_plot = auto.run(asym_branch,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','K'],
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
dX_K_plot = auto.rl(dX_K_plot) 
dX_K_plot = dX_K_plot + auto.run(asym_branch,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','K'],
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
dX_K_plot = auto.rl(dX_K_plot) 


                         
#following the symmetric Hopf bifurcation                       
dX_K_plot  = dX_K_plot  + auto.run(sym_hopf,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','K'],
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
dX_K_plot = auto.rl(dX_K_plot) 
dX_K_plot  = dX_K_plot  + auto.run(sym_hopf,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','K'],
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
dX_K_plot = auto.rl(dX_K_plot) 


                            
#following the asymmetric Hopf bifurcation                                            
dX_K_plot  = dX_K_plot + auto.run(asym_hopf_dR,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','K'],
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
dX_K_plot = auto.rl(dX_K_plot) 
dX_K_plot  = dX_K_plot + auto.run(asym_hopf_dR,
                                  c='spatial_IGP.FP',
                                  ICP = ['dR','K'],
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
dX_K_plot = auto.rl(dX_K_plot)                                                                      
                         

auto.cl()



###########################
####### #2: dH ############
###########################


# Following the branch point for the asymetric equm
dX_K_plot = dX_K_plot+ auto.run(asym_branch,
                                  c='spatial_IGP.FP',
                                  ICP = ['dH','K'],
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
dX_K_plot = auto.rl(dX_K_plot) 
dX_K_plot = dX_K_plot + auto.run(asym_branch,
                                  c='spatial_IGP.FP',
                                  ICP = ['dH','K'],
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
dX_K_plot = auto.rl(dX_K_plot) 


                         
#following the symmetric Hopf bifurcation                       
dX_K_plot  = dX_K_plot  + auto.run(sym_hopf,
                                  c='spatial_IGP.FP',
                                  ICP = ['dH','K'],
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
dX_K_plot = auto.rl(dX_K_plot) 
dX_K_plot  = dX_K_plot  + auto.run(sym_hopf,
                                  c='spatial_IGP.FP',
                                  ICP = ['dH','K'],
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
dX_K_plot = auto.rl(dX_K_plot) 


                            
#following the asymmetric Hopf bifurcation                                            
dX_K_plot  = dX_K_plot + auto.run(asym_hopf_dH,
                                  c='spatial_IGP.FP',
                                  ICP = ['dH','K'],
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
dX_K_plot = auto.rl(dX_K_plot) 
dX_K_plot  = dX_K_plot + auto.run(asym_hopf_dH,
                                  c='spatial_IGP.FP',
                                  ICP = ['dH','K'],
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
dX_K_plot = auto.rl(dX_K_plot)           

auto.cl()


dX_K_plot  = dX_K_plot + auto.run(asym_hopf_dH_low,
                                  c='spatial_IGP.FP',
                                  ICP = ['dH','K'],
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
dX_K_plot = auto.rl(dX_K_plot) 




dX_K_plot  = dX_K_plot + auto.run(asym_hopf_dH_low,
                                  c='spatial_IGP.FP',
                                  ICP = ['dH','K'],
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
dX_K_plot = auto.rl(dX_K_plot)           



    
##Trying to calculate the period-doubling bifurcation location   
#dX_K_plot  =  dX_K_plot +  auto.run(start_point_analysis("PD1"),
#                            c='spatial_IGP.FP',
#                                  ICP = ['dH','K',11],
#                                  IPS=2,JAC=0,
#                                  ISW = 2,
#                                  ISP=1,
#                                  ILP=0,      #tells auto not to find folds;
#                                  DS  =   -0.0005, 
#                                  DSMIN= 0.0001, 
#                                  DSMAX=   0.0005,
#                                  NMX=  7000,
#                                  UZSTOP={'dH':range_dispersal_2_par,
#                                         'dH':range_dispersal_2_par,
#                                         'dP':range_dispersal_2_par,
#                                         'K':range_K_two_parameter,
#                                         'aRP':range_IGP})         
#dX_K_plot = auto.rl(dX_K_plot)          

auto.cl()






###########################
####### #3: dP ############
###########################


# Following the branch point for the asymetric equm
dX_K_plot = dX_K_plot+ auto.run(asym_branch,
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','K'],
                                  IPS = 1,
                                  ISW=2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  70000,
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_K_plot = auto.rl(dX_K_plot) 
dX_K_plot = dX_K_plot + auto.run(asym_branch,
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','K'],
                                  IPS = 1,
                                  ISW=2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  70000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_K_plot = auto.rl(dX_K_plot) 


                         
#following the symmetric Hopf bifurcation                       
dX_K_plot  = dX_K_plot  + auto.run(sym_hopf,
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','K'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  70000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_K_plot = auto.rl(dX_K_plot) 
dX_K_plot  = dX_K_plot  + auto.run(sym_hopf,
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','K'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  70000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})       
dX_K_plot = auto.rl(dX_K_plot) 


                            
#following the asymmetric Hopf bifurcation                                            
dX_K_plot  = dX_K_plot + auto.run(asym_hopf_dP,
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','K'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.0005, 
                                  DSMIN= 0.00005, 
                                  DSMAX=   0.001,
                                  NMX=  70000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
dX_K_plot = auto.rl(dX_K_plot) 
dX_K_plot  = dX_K_plot + auto.run(asym_hopf_dP,
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','K'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  70000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
dX_K_plot = auto.rl(dX_K_plot)   


# Following asynchronous hopf bifurcation
dX_K_plot = dX_K_plot + auto.run(sym_disperse_hopf_dP,
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','K'],
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
dX_K_plot = auto.rl(dX_K_plot) 
dX_K_plot = dX_K_plot + auto.run(sym_disperse_hopf_dP,
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','K'],
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
dX_K_plot = auto.rl(dX_K_plot) 
################################################
####### Following branches and folds of ########
########## limit-cycle based points ############

#This is to follow the two sets of fold points that occur that allow for
#stable asymmetric limit cycles
fold_plot = []
for j in ['dR','dH','dP']:
    for i in limit_cycle_fold: 
        fold_start  =    auto.run(i,
                            c='spatial_IGP.FP',
                                  ICP = [j,'K',11],
                                  IPS=2,
                                  ITMX =20,
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.05, 
                                  DSMIN= 0.005, 
                                  DSMAX=   0.1,
                                  NMX=  70000,
                                  UZR={'K':6},
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
        fold_plot  =   fold_plot+  auto.run(fold_start("EP1"),
                            c='spatial_IGP.FP',
                                  ICP = [j,'K',11],
                                  IPS=2, JAC=-1,
                                  ISW = 2,
                                  ITMX =20,
                                  ISP=1,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.05, 
                                  DSMIN= 0.01, 
                                  DSMAX=   0.05,
                                  NMX=  70000,
                                  UZR={'K':6},                                  
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
        fold_plot  =  fold_plot +  auto.run(fold_start("EP1"),
                            c='spatial_IGP.FP',
                                  ICP = [j,'K',11],
                                  IPS=2,JAC=-1,
                                  ISW = 2,
                                  ITMX =20,
                                  ISP=1,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.05, 
                                  DSMIN= 0.01, 
                                  DSMAX=   0.05,
                                  NMX=  70000,
                                  UZR={'K':6},                                  
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})         
        fold_plot = auto.rl(fold_plot)       


auto.cl()




##following the branch point for stability of the symmetric limit cycle
start_1 =auto.run(dispersal_limit_branch_dH,
                                  c='spatial_IGP.FP',
                                  IPS=2,JAC=1,
                                  ISP=2,
                                  ICP = ['dH','K'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.05, 
                                  DSMIN= 0.05, 
                                  DSMAX=   0.1,
                                  NMX=  7000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
#
##Note: it looks like it has to generate a new start point,thus this rigamarole
limit_branch_point = auto.run(start_1("EP1") ,
                                  c='spatial_IGP.FP',
                                  IPS=2,JAC=0,
                                  ISP=0,
                                  ICP = ['dH','K'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.008, 
                                  DSMIN= 0.005, 
                                  DSMAX=   0.01,
                                  NMX=  15000,
                                  UZR ={'dH':0.1, 'K':6},
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
   
limit_branch_point = limit_branch_point+ auto.run(start_1("EP1") ,
                                  c='spatial_IGP.FP',
                                  IPS=2,
                                  ISP=0,
                                  ICP = ['dH','K'],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.005, 
                                  DSMAX=   0.01,
                                  NMX=  15000,
                                  UZR ={'dH':0.1, 'K':6},
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
limit_branch_point = auto.rl(limit_branch_point)

dispersal_limit_branch = limit_branch_point("UZ1")

for i in ["dR","dP"]:
    if i == "dP":
        DS = 0.1
        DSMIN = 0.1
        DSMAX = 1
    else:
        DS = 0.001
        DSMIN = 0.001
        DSMAX = 0.05
    limit_branch_point = limit_branch_point + auto.run(dispersal_limit_branch,
                                  c='spatial_IGP.FP',
                                  IPS=2,
                                  ISP=1,
                                  ICP = ['K',i,11],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   DS, 
                                  DSMIN= DSMIN, 
                                  DSMAX=   DSMAX,
                                  NMX=  7000,
                                  NTST = 200,

                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
    limit_branch_point =  limit_branch_point+auto.run(dispersal_limit_branch,
                                  c='spatial_IGP.FP',
                                  IPS=2,JAC=1,
                                  ISP=1,
                                  ICP = ['K',i,11],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -1*DS,
                                  DSMIN= DSMIN, 
                                  DSMAX=   DSMAX,
                                  NMX=  7000,
                                  NTST=200,
                                  UZR={'K':6},
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  


tri_stable_branch = []

for i in ["dR","dH","dP"]:
    start_point = auto.run(tri_stable_branch_point,
                                  c='spatial_IGP.FP',
                                  IPS=2,JAC=0,
                                  ISP=1,
                                  ICP = ['K','dH',11],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -10, 
                                  DSMIN= 10, 
                                  DSMAX=   20,
                                  NMX=  7000,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
    tri_stable_branch = tri_stable_branch + auto.run(start_point("EP1"),
                                  c='spatial_IGP.FP',
                                  IPS=2,JAC=0,
                                  ISP=1,
                                  ICP = ['K',i,11],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   -0.5, 
                                  DSMIN= 0.5, 
                                  DSMAX=   1,
                                  NMX=  200,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
    tri_stable_branch = tri_stable_branch + auto.run(start_point("EP1"),
                                  c='spatial_IGP.FP',
                                  IPS=2,JAC=0,
                                  ISP=1,
                                  ICP = ['K',i,11],
                                  ISW = 2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.5, 
                                  DSMIN= 0.5, 
                                  DSMAX=   1,
                                  NMX=  200,
                                  UZSTOP={'dH':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})  
    tri_stable_branch = auto.rl(tri_stable_branch)


dX_K_plot = limit_branch_point + fold_plot + dX_K_plot + tri_stable_branch 
dX_K_plot = auto.rl(dX_K_plot)   



## This is the bifurcation of the branch point found by reducing predator 
## dispersal. This may lead to stabilizing the asynchronous limit cycle 
## need to look at it further
#start_point2 =  auto.run(dispersal_limit_branch_dP,
#                                  c='spatial_IGP.FP',
#                                  IPS=2,JAC=1,
#                                  ISP=1,
#                                  ICP = [i,'K'],
#                                  ISW = 2,
#                                  ILP=0,      #tells auto not to find folds;
#                                  DS  =   -0.0005, 
#                                  DSMIN= 0.0005, 
#                                  DSMAX=   0.001,
#                                  NMX=  7000,
#                                  UZSTOP={'dR':range_dispersal_2_par,
#                                         'dH':range_dispersal_2_par,
#                                         'dP':range_dispersal_2_par,
#                                         'K':range_K_two_parameter,
#                                         'aRP':range_IGP}) 
#limit_branch_point =  limit_branch_point+auto.run(start_point2("EP1"),
#                                  c='spatial_IGP.FP',
#                                  IPS=2,JAC=1,
#                                  ISP=1,
#                                  ICP = [i,'K'],
#                                  ISW = 2,
#                                  ILP=0,      #tells auto not to find folds;
#                                  DS  =   0.01, 
#                                  DSMIN= 0.01, 
#                                  DSMAX=   0.05,
#                                  NMX=  7000,
#                                  UZSTOP={'dR':range_dispersal_2_par,
#                                         'dH':range_dispersal_2_par,
#                                         'dP':range_dispersal_2_par,
#                                         'K':range_K_two_parameter,
#                                         'aRP':range_IGP}) 
#limit_branch_point =  limit_branch_point+auto.run(start_point2("EP1"),
#                                  c='spatial_IGP.FP',
#                                  IPS=2,JAC=1,
#                                  ISP=1,
#                                  ICP = [i,'K'],
#                                  ISW = 2,
#                                  ILP=0,      #tells auto not to find folds;
#                                  DS  =   -0.01, 
#                                  DSMIN= 0.01, 
#                                  DSMAX=   0.05,
#                                  NMX=  7000,
#                                  UZSTOP={'dR':range_dispersal_2_par,
#                                         'dH':range_dispersal_2_par,
#                                         'dP':range_dispersal_2_par,
#                                         'K':range_K_two_parameter,
#                                         'aRP':range_IGP}) 
   
