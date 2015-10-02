# This script creates the starting values for the main figures
# These starting values are were run on the Collose cluster.


require(lhs)
set.seed(10)
starting_values_base = randomLHS(400,k=6)
max_value = 30
colnames(starting_values_base) = c("R1","R2","H1","H2","P1","P2")
starting_values = sweep(starting_values_base, MARGIN=2, 
                        STATS=rep(max_value,6),FUN="*")
dR = seq(0.01, 6, length=30)
dH = seq(0.01, 0.2, length=30)
dP = seq(0.01, 0.2, length=30)
beta = seq(0.05,0.5,length=30)
K= 1/beta

dR_dH_data = expand.grid(g = 1,aRH = 0.1, aHP = 0.1, hRH = 0, hHP = 10,
                            mH = 0.04, mP = 0.08,
                            dR = dR, dH = dH, dP = 0.1,
                            K=6)


dR_dP_data = expand.grid(g = 1,aRH = 0.1, aHP = 0.1, hRH = 0, hHP = 10,
                         mH = 0.04, mP = 0.08,
                         dR = dR, dH = 0.1, dP = dP,
                         K=6)

dH_dP_data = expand.grid(g = 1,aRH = 0.1, aHP = 0.1, hRH = 0, hHP = 10,
                         mH = 0.04, mP = 0.08,
                         dR = 5, dH = dH, dP = dP,
                         K=6)

K_dR_data = expand.grid(g = 1,aRH = 0.1, aHP = 0.1, hRH = 0, hHP = 10,
                         mH = 0.04, mP = 0.08,
                         dR = dR, dH = 0.1, dP = 0.1,
                         K=K)

K_dH_data = expand.grid(g = 1,aRH = 0.1, aHP = 0.1, hRH = 0, hHP = 10,
                        mH = 0.04, mP = 0.08,
                        dR = 5, dH = dH, dP = 0.1,
                        K=K)

K_dP_data = expand.grid(g = 1,aRH = 0.1, aHP = 0.1, hRH = 0, hHP = 10,
                        mH = 0.04, mP = 0.08,
                        dR = 5, dH = 0.1, dP = dP,
                        K=K)

write.csv(x= dR_dH_data, file="data/dR_dH_data.csv")
write.csv(x= dR_dP_data, file="data/dR_dP_data.csv")
write.csv(x= dH_dP_data, file="data/dH_dP_data.csv")
write.csv(x= K_dR_data, file="data/K_dR_data.csv")
write.csv(x= K_dH_data, file="data/K_dH_data.csv")
write.csv(x= K_dP_data, file="data/K_dP_data.csv")
write.csv(x= starting_values, file="data/starting_values.csv")
write.csv(x= starting_values_base, file="data/starting_values_base.csv")