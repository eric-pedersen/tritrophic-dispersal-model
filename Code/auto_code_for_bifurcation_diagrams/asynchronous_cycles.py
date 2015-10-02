

asynchronous_plot =  auto.run(dispersal_fixed_points("HB6"), 
                            ISP =1,
			    JAC=1,
                            IPS= 2,     #Specifies that I want to find periodic solutions
                            ICP=[2,11], #specifies that I want to continue in the second parameter (K), and periodicity
                            ILP =0,     #Tells it not to find folds.
                            NTST=100,   #increases the mesh size used
                            NMX = 3000, #increases the number of steps taken
                            UZSTOP={2:[0.0,8], 11:10000}, #new bounds on the parameters: K has to be between 0 and 4, and the period has to be <1000
                            DS  =   0.005,#setting new step sizes   
                            STOP="PD1",
                            DSMIN= 0.005, 
                            DSMAX=   0.01
                            )



asynchronous_plot = auto.rl(asynchronous_plot)

auto.plot(asynchronous_plot, stability=True,use_labels=False,bifurcation_y= ['MAX H_1'])


asynchronous_plot = asynchronous_plot+ auto.run(dispersal_fixed_points("HB6"),
                                  c='spatial_IGP.FP',
                                  ICP = ['dP','K'],
                                  IPS = 1,
                                  ISW=2,
                                  ILP=0,      #tells auto not to find folds;
                                  DS  =   0.005, 
                                  DSMIN= 0.0005, 
                                  DSMAX=   0.01,
                                  NMX=  7000,
                                  UZR={'dP':0.1},
                                  UZSTOP={'dR':range_dispersal_2_par,
                                         'dH':range_dispersal_2_par,
                                         'dP':range_dispersal_2_par,
                                         'K':range_K_two_parameter,
                                         'aRP':range_IGP})
asynchronous_plot = auto.rl(asynchronous_plot)



