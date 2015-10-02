

equal_handle_IGP_FP = auto.run(e=dynamics_file,
                      c='spatial_IGP.FP',
                      ICP = [2], JAC=1,
                      DS  =   -0.001, DSMIN= 0.001, DSMAX=   0.01,NMX=  5000,
                      UZR = {2:[6,8]},
                      UZSTOP={15:range_dispersal,16:range_dispersal,17:range_dispersal,2:range_K}) 
                                                      
auto.cl()
    
equal_handle_bistable_FP = auto.run(e='dynamics_fixed_bistability',
                      c='spatial_IGP.FP',
                      ICP = [2],
                      DS  =   -0.001, DSMIN= 0.001, DSMAX=   0.01,NMX=  5000,
                      UZR = {2:6},
                      UZSTOP={15:range_dispersal,16:range_dispersal,17:range_dispersal,2:range_K}) 
             
auto.cl()
    

