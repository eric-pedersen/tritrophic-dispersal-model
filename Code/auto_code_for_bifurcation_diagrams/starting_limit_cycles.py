

equal_handle_IGP_Limit_Cycle = auto.run(equal_handle_IGP_FP("HB3"), 
                            ISP =2,
                            IPS= 2,     #Specifies that I want to find periodic solutions
                            ICP=[2,11], #specifies that I want to continue in the second parameter (K), and periodicity
                            ILP =0,     #Tells it not to find folds.
                            NTST=100,   #increases the mesh size used
                            NMX = 2000, #increases the number of steps taken
                            UZSTOP={2:range_K, 11:10000}, #new bounds on the parameters: K has to be between 0 and 4, and the period has to be <1000
                            DS  =   0.1,#setting new step sizes   
                            STOP = "PD1",
                            DSMIN= 0.05, 
                            DSMAX=   0.8
                            )
equal_handle_IGP_Limit_Cycle = auto.rl(equal_handle_IGP_Limit_Cycle)

auto.cl()

equal_handle_IGP_Limit_Cycle = equal_handle_IGP_Limit_Cycle + auto.run(equal_handle_IGP_FP("HB4"), 
                            ISP =2,
                            IPS= 2,     #Specifies that I want to find periodic solutions
                            ICP=[2,11], #specifies that I want to continue in the second parameter (K), and periodicity
                            ILP =1,     #Tells it not to find folds.
                            NTST=100,   #increases the mesh size used
                            NMX = 200, #increases the number of steps taken
                            UZSTOP={2:range_K, 11:10000}, #new bounds on the parameters: K has to be between 0 and 4, and the period has to be <1000
                            DS  =   0.01,#setting new step sizes   
                            DSMIN= 0.005, 
                            DSMAX=   0.08
                            )
equal_handle_IGP_Limit_Cycle = auto.rl(equal_handle_IGP_Limit_Cycle)




equal_handle_IGP_Limit_Cycle = equal_handle_IGP_Limit_Cycle + auto.run(equal_handle_IGP_FP("HB7"), 
                            ISP =2, 
                            IPS= 2,     #Specifies that I want to find periodic solutions
                            ICP=[2,11], #specifies that I want to continue in the second parameter (K), and periodicity
                            ILP =1,     
                            NTST=100,   #increases the mesh size used
                            NMX = 90, #increases the number of steps taken
                            UZSTOP={2:range_K, 11:10000}, #new bounds on the parameters: K has to be between 0 and 4, and the period has to be <1000
                            DS  =   0.1,#setting new step sizes   
                            DSMIN= 0.05, 
                            DSMAX=   0.8
                            )
equal_handle_IGP_Limit_Cycle = auto.rl(equal_handle_IGP_Limit_Cycle)


#Note value of ILP here is set to 1. This indicates that I want to find folds, which seperate stable
#from unstable asymmetric limit cycles
equal_handle_IGP_Limit_Cycle = equal_handle_IGP_Limit_Cycle + auto.run(equal_handle_IGP_FP("HB5"), 
                            ISP =2,
                            IPS= 2,     #Specifies that I want to find periodic solutions
                            ICP=[2,11], #specifies that I want to continue in the second parameter (K), and periodicity
                            ILP =1,     #Tells it not to find folds.
                            NTST=100,   #increases the mesh size used
                            NMX = 70, #increases the number of steps taken
                            UZSTOP={2:range_K, 11:10000}, #new bounds on the parameters: K has to be between 0 and 4, and the period has to be <1000
                            DS  =   0.1,#setting new step sizes   
                            DSMIN= 0.05, 
                            DSMAX=   0.8
                            )
equal_handle_IGP_Limit_Cycle = auto.rl(equal_handle_IGP_Limit_Cycle)
auto.cl()
#
#equal_handle_bistable_Limit_Cycle = auto.run(equal_handle_bistable_FP("HB3"), 
#                            ISP =2,
#                            IPS= 2,     #Specifies that I want to find periodic solutions
#                            ICP=[2,11], #specifies that I want to continue in the second parameter (K), and periodicity
#                            ILP =0,     #Tells it not to find folds.
#                            NTST=100,   #increases the mesh size used
#                            NMX = 2000, #increases the number of steps taken
#                            UZSTOP={2:range_K, 11:10000}, #new bounds on the parameters: K has to be between 0 and 4, and the period has to be <1000
#                            DS  =   0.01,#setting new step sizes   
#                            DSMIN= 0.005, 
#                            DSMAX=   0.08
#                            )
#equal_handle_IGP_Limit_Cycle = auto.rl(equal_handle_IGP_Limit_Cycle)
#
#auto.cl()
#
#equal_handle_bistable_Limit_Cycle =equal_handle_bistable_Limit_Cycle+ auto.run(equal_handle_bistable_FP("HB4"), 
#                            ISP =2,
#                            IPS= 2,     #Specifies that I want to find periodic solutions
#                            ICP=[2,11], #specifies that I want to continue in the second parameter (K), and periodicity
#                            ILP =0,     #Tells it not to find folds.
#                            NTST=100,   #increases the mesh size used
#                            NMX = 200, #increases the number of steps taken
#                            UZSTOP={2:range_K, 11:10000}, #new bounds on the parameters: K has to be between 0 and 4, and the period has to be <1000
#                            DS  =   0.01,#setting new step sizes   
#                            DSMIN= 0.005, 
#                            DSMAX=   0.08
#                            )
#equal_handle_IGP_Limit_Cycle = auto.rl(equal_handle_IGP_Limit_Cycle)
#
#auto.cl()
#
#
#equal_handle_bistable_Limit_Cycle =equal_handle_bistable_Limit_Cycle+ auto.run(equal_handle_bistable_FP("HB5"), 
#                            ISP =2,
#                            IPS= 2,     #Specifies that I want to find periodic solutions
#                            ICP=[2,11], #specifies that I want to continue in the second parameter (K), and periodicity
#                            ILP =0,     #Tells it not to find folds.
#                            NTST=100,   #increases the mesh size used
#                            NMX = 200, #increases the number of steps taken
#                            UZSTOP={2:range_K, 11:10000}, #new bounds on the parameters: K has to be between 0 and 4, and the period has to be <1000
#                            DS  =   0.1,#setting new step sizes   
#                            DSMIN= 0.05, 
#                            DSMAX=   0.8
#                            )
#equal_handle_IGP_Limit_Cycle = auto.rl(equal_handle_IGP_Limit_Cycle)
#
#auto.cl()
#
#full_bistable_plot = auto.rl(equal_handle_bistable_FP+equal_handle_bistable_Limit_Cycle)
#auto.plot(full_bistable_plot,
#            stability=True,use_labels=False,
#            bifurcation_x= ['K'],bifurcation_y= ['MAX H_1'])