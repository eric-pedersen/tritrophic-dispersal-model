dispersal_fixed_points =auto.run(equilibrium_start,
                      c='spatial_IGP.FP',
                      ICP = [15],MXBF =5,
                      DS  =   0.01, DSMIN= 0.01, DSMAX=   0.016,
                      NMX=  4500,UZSTOP={15:range_dispersal,
                                          16:range_dispersal,
                                          17:range_dispersal,
                                          2:range_K}) 
dispersal_fixed_points = auto.rl(dispersal_fixed_points) 

dispersal_fixed_points =dispersal_fixed_points + auto.run(equilibrium_start,
                      c='spatial_IGP.FP',
                      ICP = [15],MXBF =5,
                      DS  =   -0.005, DSMIN= 0.005, DSMAX=   0.008,
                      NMX=  4500,UZSTOP={15:range_dispersal,
                                          16:range_dispersal,
                                          17:range_dispersal,
                                          2:range_K}) 
dispersal_fixed_points = auto.rl(dispersal_fixed_points) 

dispersal_fixed_points =dispersal_fixed_points + auto.run(equilibrium_start,
                      c='spatial_IGP.FP',
                      ICP = [16],MXBF =5,
                      DS  =   0.0005, DSMIN= 0.0005, DSMAX=   0.0008,
                      NMX=  40500,UZSTOP={15:range_dispersal,
                                          16:[0,0.2],
                                          17:range_dispersal,
                                          2:range_K}) 
dispersal_fixed_points = auto.rl(dispersal_fixed_points) 

dispersal_fixed_points =dispersal_fixed_points + auto.run(equilibrium_start,
                      c='spatial_IGP.FP',
                      ICP = [16],MXBF =5,
                      DS  =   -0.0005, DSMIN= 0.0005, DSMAX=   0.0008,
                      NMX=  10500,UZSTOP={15:range_dispersal,
                                          16:range_dispersal,
                                          17:range_dispersal,
                                          2:range_K}) 
dispersal_fixed_points = auto.rl(dispersal_fixed_points) 

dispersal_fixed_points =dispersal_fixed_points + auto.run(equilibrium_start,
                      c='spatial_IGP.FP',
                      ICP = [17],MXBF =5,
                      DS  =   0.005, DSMIN= 0.005, DSMAX=   0.008,
                      NMX=  4500,UZSTOP={15:range_dispersal,
                                          16:range_dispersal,
                                          17:range_dispersal,
                                          2:range_K}) 
dispersal_fixed_points = auto.rl(dispersal_fixed_points) 


dispersal_fixed_points =dispersal_fixed_points + auto.run(equilibrium_start,
                      c='spatial_IGP.FP',
                      ICP = [17],MXBF =5,
                      DS  =   -0.005, DSMIN= 0.005, DSMAX=   0.008,
                      NMX=  4500,UZSTOP={15:range_dispersal,
                                          16:range_dispersal,
                                          17:range_dispersal,
                                          2:range_K}) 
dispersal_fixed_points = auto.rl(dispersal_fixed_points) 




