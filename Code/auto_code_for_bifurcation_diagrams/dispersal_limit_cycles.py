dispersal_limit_cycles =   auto.run(limit_start, 
                            ISP =2,
                            IPS= 2,     #Specifies that I want to find periodic solutions
                            ICP=[15,11], #specifies that I want to continue in the second parameter (K), and periodicity
                            ILP =0,     #Tells it not to find folds.
                            NTST=100,   #increases the mesh size used
                            NMX = 6000, #increases the number of steps taken
                            UZSTOP={11:10000,
                                    15:[0,10]}, #new bounds on the parameters: K has to be between 0 and 4, and the period has to be <1000
                            DS  =   0.01,#setting new step sizes   
                            DSMIN= 0.005, 
                            DSMAX=   0.008
                            )
dispersal_limit_cycles = auto.rl(dispersal_limit_cycles)



dispersal_limit_cycles =  dispersal_limit_cycles+ auto.run(limit_start, 
                            ISP =2,
                            IPS= 2,     #Specifies that I want to find periodic solutions
                            ICP=[16,11], 
                            ILP =0,     #Tells it not to find folds.
                            NTST=100,   #increases the mesh size used
                            NMX = 2000, #increases the number of steps taken
                            ISW=1,
                            UZSTOP={11:10000,
                                    16:[0,0.2]}, 
                            DS  =   -0.0001,#setting new step sizes   
                            DSMIN= 0.0001, 
                            DSMAX=   0.005
                            )
dispersal_limit_cycles = auto.rl(dispersal_limit_cycles)



dispersal_limit_cycles =   dispersal_limit_cycles+ auto.run(limit_start, 
                            ISP =2,
                            IPS= 2,     #Specifies that I want to find periodic solutions
                            ICP=[17,11], #specifies that I want to continue in the second parameter (K), and periodicity
                            ILP =0,     #Tells it not to find folds.
                            NTST=100,   #increases the mesh size used
                            NMX = 2000, #increases the number of steps taken
                            UZSTOP={11:10000,
                                    17:[0,0.2]}, #new bounds on the parameters: K has to be between 0 and 4, and the period has to be <1000
                            DS  =   -0.0001,#setting new step sizes   
                            DSMIN= 0.000005, 
                            DSMAX=   0.0008
                            )
dispersal_limit_cycles = auto.rl(dispersal_limit_cycles)





auto.plot(dispersal_limit_cycles,stability=True,use_labels=False)
