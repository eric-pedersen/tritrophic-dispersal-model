#This file creates figures for Appendix C: analyzing bistablity. Requires the tritrophsim packag
#to be installed prior

library(plyr)
library(ggplot2)
library(dplyr)
library(mgcv)
library(tritrophsim)
bistability_data = CompileOutputFiles(path="Output/simulations",first_var="K",second_var="dH")%>%
  CalcStateTypes(.)%>%
  mutate(beta = 1/K)%>%
  filter(between(dH, 0.05,0.11), between(beta, 0.09, 0.15))%>%
  mutate(R1 = R1*K, R2 = R2*K, H1=H1*K,H2=H2*K, P1=P1*K, P2=P2*K,
         avg_pop = (R1 +R2 + H1 + H2 + P1+P2)/2 -45, 
         avg_r = (R1+R2)/2,
         avg_h = (H1+H2)/2,
         avg_p = (P1+P2)/2,
         diff_r = abs(R1-R2),
         diff_h = abs(H1-H2),
         diff_p = abs(P1-P2),
         sym_equm_state = as.numeric(sym_cyclic),
         R1_s = R1 - K/2,R2_s = R2 - K/2,
         H1_s = H1 - K/2,H2_s = H2 - K/2,
         P1_s = P1 - K/2,P2_s = P2 - K/2,
         dH_round = round(dH, 2),
         state_val = ifelse(sym_cyclic, "Symmetric limit cycles","Asymmetric equilibrium")
  )

labeller_func = function(variable, value){
  if(variable=="K"){
    output_val = paste("beta==", round(1/value,3),"")
  }else{
    output_val = paste("d[H]==",round(value,2), "")
  }
  return(label_parsed(variable, output_val))
}

model_1 = gam(sym_equm_state~s(avg_r)+ diff_r +s(avg_h)+diff_h + s(avg_p)+diff_p,
              family=binomial,data=bistability_data)

model_2 = gam(sym_equm_state~s(R1, R2)+ s(H1,H2)+s(P1,P2),
              family=binomial,data=bistability_data)

model_3 = gam(sym_equm_state~R1_s*R2_s+ H1_s*H2_s+P1_s*P2_s,
              family=binomial,data=bistability_data)

bistable_plot = qplot(P1, P2, colour=state_val, data=bistability_data) +
  facet_grid(facets=K~dH_round, labeller = labeller_func)+
  scale_color_grey()+
  scale_x_continuous(breaks=seq(0,10, by=2.5), labels=c("0","2.5","5","7.5","10"))+
  scale_y_continuous(breaks=seq(0,10, by=2.5), labels=c("0","2.5","5","7.5","10"))+
  coord_equal()+theme_bw()+
  labs(x=expression(paste("Initial density of ", P[1])),
       y = expression(paste("Initial density of ", P[2])),
       color = "Final state")+
  theme(legend.position="bottom")

ggsave("Output/figures/bistable_plot.pdf",bistable_plot, width = 10 ,height=8)
