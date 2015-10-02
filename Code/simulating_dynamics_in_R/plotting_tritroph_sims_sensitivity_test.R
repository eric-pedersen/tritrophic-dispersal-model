# This plots the output of the sensitivity test simulations. 
# Requires that there are files in the "Output/simulations/sensitivity_test_results/" folder

require(plyr)
require(reshape2)
require(ggplot2)
require(tritrophsim)
require(grid)
require(RColorBrewer)
library(dplyr)

RelabelScenarios = function(x){
  x_out = as.character(x)
  x_out = ifelse(x_out=="base_w_conversion","1. Conversion efficiencies",x_out)
  x_out = ifelse(x_out=="base_w_handling","2. Type II herbivore \n functional response",x_out)
  x_out = ifelse(x_out=="invert_invert","3. Invertebrate predator \n invertebrate prey",x_out)
  x_out = ifelse(x_out=="ectotherm_ecotherm_large","4. Large ectothermic predator\n ectothermic prey",x_out)
  x_out = factor(x_out, levels = c("1. Conversion efficiencies","2. Type II herbivore \n functional response",
                                   "3. Invertebrate predator \n invertebrate prey",
                                   "4. Large ectothermic predator\n ectothermic prey"))
  return(x_out)
}   
  
PlotMultipleGgplotObjs <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  require(grid)
  
  # Make a list from the ... arguments and plotlist
  plots <- c(list(...), plotlist)
  
  numPlots = length(plots)
  
  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                     ncol = cols, nrow = ceiling(numPlots/cols))
  }
  
  if (numPlots==1) {
    print(plots[[1]])
    
  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))
    
    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))
      
      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}

colour_table_data = data.frame(attractor_type = factor(c("sym_equib", "asym_equib",
                                                         "sym_cycle","asym_cycle","async_cycle"),
                                                       levels=rev(c("sym_equib", "asym_equib",
                                                                    "sym_cycle","asym_cycle","async_cycle"))),
                               col_num =rep(1,times= 5),
                               colours = CalculateColourWeights(data.frame(sym_equib=c(1,0,0,0,0),
                                                                           asym_equib=c(0,1,0,0,0),
                                                                           sym_cycle=c(0,0,1,0,0), 
                                                                           asym_cycle=c(0,0,0,1,0), 
                                                                           async_cycle=c(0,0,0,0,1))))

colour_table_plot = ggplot(aes(y=col_num, x=attractor_type,fill= colours),
                           data=colour_table_data)+
  geom_tile(colour="black",lwd=0.5)+
  scale_fill_identity()+coord_equal(ratio=1)+
  scale_x_discrete(labels =rev(c("Symmetric equilibrium", "asymmetric equilibrium",
                                 "symmetric limit cycle","asymmetric limit cycle","asynchronous limit cycle")))+ 
  labs(x="",y="")+theme_bw()+
  theme(axis.title=element_blank(), axis.text.y = element_blank(),
        plot.margin = unit(3*c(1,1,1,0),units="lines"),
        text= element_text(size=15),axis.ticks= element_blank(),
        panel.grid=element_blank(), panel.background=element_blank(),
        rect=element_blank())



dH_dP_output <- SummarizeSims(CompileOutputFiles("Output/simulations/sensitivity_test_results/",
                                                 "dH","dP"))
dR_dP_output <- SummarizeSims(CompileOutputFiles("Output/simulations/sensitivity_test_results/",
                                                 "dR","dP"))
dR_dH_output <- SummarizeSims(CompileOutputFiles("Output/simulations/sensitivity_test_results/",
                                                 "dR","dH"))


standarize_values = function(x) mean(x,na.rm = T)

dR_dH_plot_data = dR_dH_output %>%
  group_by(dR, dH, scenarios) %>%
  summarise_each(funs(standarize_values), -pred_type, -prey_type)%>%
  ungroup()%>%
  mutate(weighted_col = CalculateColourWeights(.),
         scenarios = RelabelScenarios(scenarios))

dR_dP_plot_data = dR_dP_output %>%
  group_by(dR, dP, scenarios) %>%
  summarise_each(funs(standarize_values), -pred_type, -prey_type)%>%
  ungroup()%>%
  mutate(weighted_col = CalculateColourWeights(.),
         scenarios = RelabelScenarios(scenarios))

dH_dP_plot_data = dH_dP_output %>%
  group_by(dH, dP, scenarios) %>%
  summarise_each(funs(standarize_values), -pred_type, -prey_type)%>%
  ungroup()%>%
  mutate(weighted_col = CalculateColourWeights(.),
         scenarios = RelabelScenarios(scenarios))


plot_template = list(geom_tile(aes(fill = weighted_col,colour=weighted_col)),
                     coord_equal(ratio=1),
                     facet_grid(.~scenarios),
                     theme_bw(),
                     scale_y_log10(),
                     scale_x_log10(),
                     scale_alpha_identity(guide="none"),
                     scale_color_identity(),
                     scale_fill_identity()
)


dR_label   = expression('resource dispersal rate (d'['R']*')')
dH_label   = expression('herbivore dispersal rate (d'['H']*')')
dP_label   = expression('predator dispersal rate (d'['P']*')')
beta_label = expression(paste('resource self-regulation strength (', beta,')'))
h1_label   = expression('Herbivore density in patch 1 (H'['1']*')')

x_rel_pos = 0.9
y_rel_pos = 0.9
beta_scale = scale_y_continuous(breaks = c(0.05,0.15,0.25,0.35))

dH_dP_plot = ggplot(data=dH_dP_plot_data, aes(x=dP,y=dH))+plot_template+
  coord_fixed(xlim=c(1e-04,1e-01),ylim=c(1e-04,1e-01), ratio = 1)+
  theme(plot.margin =  unit(c(1,1,1,0),units="lines"))+
  geom_abline(slope=1, intercept=0,linetype=2)+
  xlab(dP_label)+
  ylab(dH_label)+ 
  theme(panel.margin = unit(2, "lines"))

dR_dP_plot = ggplot(data=dR_dP_plot_data,aes(x=dR,y=dP))+plot_template+
  coord_fixed(xlim=c(0.01,10.00),ylim=c(1e-04,1e-01), ratio = 1)+
  geom_hline(aes(yintercept=dH),linetype=2)+
  theme(plot.margin =  unit(c(0,1,2,1),units="lines"))+
  #geom_abline(slope=1, intercept=0,linetype=2)+
  xlab(dR_label)+
  ylab(dP_label)+ 
  theme(panel.margin = unit(2, "lines"))

dR_dH_plot = ggplot(data=dR_dH_plot_data,aes(x=dR,y=dH))+plot_template+
  coord_fixed(xlim=c(0.01,10),ylim=c(1e-04,1e-01))+
  geom_abline(slope=1, intercept=0,linetype=2)+
  #geom_hline(aes(yintercept=dP),linetype=2)+
  theme(plot.margin =  unit(c(1,1,1,1),units="lines"))+
  ylab(dH_label)+
  xlab(dR_label)+ 
  theme(panel.margin = unit(2, "lines"))


write_svg = F

if(write_svg){
  svg("Output/figures/sensitivity_sim_plot.svg",width=12,height=14) 
}else{
  pdf("Output/figures/sensitivity_sim_plot.pdf",width=12,height=14) 
}
{
  PlotMultipleGgplotObjs(
    dR_dH_plot,#+annotate("text",x=6.0*x_rel_pos,y=0.193*y_rel_pos+0.007,label ="A"),
    dR_dP_plot,#annotate("text",x=1,y=0.193*y_rel_pos+0.007,label ="C"),
    dH_dP_plot,#+annotate("text",x=0.193*x_rel_pos+0.007,y=0.193*y_rel_pos+0.007,label ="B"),
    colour_table_plot,
    cols=1)
} 
dev.off()


