#Creates the plots for the main figures. 
#Requires that there is files in the"Output/simulations/" folder

require(plyr)
require(reshape2)
require(ggplot2)
require(tritrophsim)
require(grid)
require(RColorBrewer)
source("Code/simulating_dynamics_in_R/loading_auto_line_data.R")

   
  
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




dH_dP_output <- SummarizeSims(CompileOutputFiles("Output/simulations/", "dH","dP"))
dR_dP_output <- SummarizeSims(CompileOutputFiles("Output/simulations/", "dR","dP"))
dR_dH_output <- SummarizeSims(CompileOutputFiles("Output/simulations/", "dR","dH"))
K_dR_output <- SummarizeSims(CompileOutputFiles("Output/simulations/", "K","dR"))
K_dH_output <- SummarizeSims(CompileOutputFiles("Output/simulations/", "K","dH"))
K_dP_output <- SummarizeSims(CompileOutputFiles("Output/simulations/", "K","dP"))


dR_dH_plot_data = CreatePlottingData(dR_dH_output, .(dR,dH))
dR_dP_plot_data = CreatePlottingData(dR_dP_output, .(dR,dP))
dH_dP_plot_data = CreatePlottingData(dH_dP_output, .(dH,dP))

K_dR_plot_data = CreatePlottingData(K_dR_output, .(dR,K))
K_dH_plot_data = CreatePlottingData(K_dH_output, .(K,dH))
K_dP_plot_data = CreatePlottingData(K_dP_output, .(K,dP))

K_dR_plot_data$beta = with(K_dR_plot_data, g/K)
K_dH_plot_data$beta = with(K_dH_plot_data, g/K)
K_dP_plot_data$beta = with(K_dP_plot_data, g/K)

bifurc_line_data$beta = with(bifurc_line_data,1/K)
bifurc_line_data = transform(bifurc_line_data,dP_pos = !is.na(dP), 
                             dH_pos = !is.na(dH),dR_pos = !is.na(dR), 
                             beta_pos = !is.na(beta))
bifurc_line_data$line_id_unique = with(bifurc_line_data,
                                       paste(line_id,dR_pos, dH_pos, dP_pos,beta_pos)) 
bifurc_line_data$line_id_unique = as.numeric(as.factor(bifurc_line_data$line_id_unique))
#included_lines = c(1,5,7,29, 9,15, 17,22,23,25,27,14,39,24,37,40,41,32,35,43)
#included_lines = c(3,5,7, 12,13,15,19,20,21,23,25,27,29,30,34, 36,39,40,41,42,44)
included_lines = c(1,5,7, 9,14, 15, 16,17,21, 22,23,5,27,29, 31,32,36,38,41, 42,44)


main_plot_line_data = bifurc_line_data
main_plot_line_data = ddply(main_plot_line_data, .(line_id_unique), 
                            function(x){
                              out_data =x
                              n_dat = nrow(x)
                              n_points  = min(n_dat, n_dat)
                              step_size = floor(n_dat/n_dat)
                              used_indexes = seq.int(from=1,to=n_dat, by=step_size)
                              if(!tail(used_indexes,n=1)==n_points) {
                                used_indexes = c(used_indexes, n_dat)
                              }
                              return(out_data[used_indexes,])
                            })
                              
plot_template = list(geom_tile(aes(fill = weighted_col,colour=weighted_col)),
                     geom_path(data=subset(main_plot_line_data,line_id_unique%in% included_lines),
                               aes(group=line_id_unique),
                               fill="black",color="black",size=1),
                     theme_bw(),
                     scale_alpha_identity(guide="none"),
                     scale_color_identity(),
                     scale_fill_identity()
                     #aes(alpha=weight,fill=attractor)
)

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


colour_table_plot = ggplot(aes(x=col_num, y=attractor_type,fill= colours),
                           data=colour_table_data)+
  geom_tile(colour="black",lwd=0.5)+
  scale_fill_identity()+coord_equal(ratio=1)+
  scale_y_discrete(labels =rev(c("Symmetric equilibrium", "asymmetric equilibrium",
                                 "symmetric limit cycle","asymmetric limit cycle","asynchronous limit cycle")))+ 
  labs(x="",y="")+theme_bw()+
  theme(axis.title=element_blank(), axis.text.x = element_blank(),
        plot.margin = unit(3*c(1,1,1,0),units="lines"),
        text= element_text(size=15),axis.ticks= element_blank(),
        panel.grid=element_blank(), panel.background=element_blank(),
        rect=element_blank())
  

dR_label   = expression('resource dispersal rate (d'['R']*')')
dH_label   = expression('herbivore dispersal rate (d'['H']*')')
dP_label   = expression('predator dispersal rate (d'['P']*')')
beta_label = expression(paste('resource self-regulation strength (', beta,')'))
h1_label   = expression('Herbivore density in patch 1 (H'['1']*')')

x_rel_pos = 0.9
y_rel_pos = 0.9
beta_scale = scale_y_continuous(breaks = c(0.05,0.15,0.25,0.35))

dH_dP_plot = ggplot(data=dH_dP_plot_data, aes(x=dP,y=dH))+plot_template+
  coord_fixed(xlim=c(0.007,0.2),ylim=c(0.007,0.2), ratio = 1)+
  theme(plot.margin =  unit(c(1,1,1,0),units="lines"))+
  xlab(dP_label)+
  ylab("")
  #ylab(dH_label)
  #theme(axis.title.y = element_text(colour="white"))

dR_dP_plot = ggplot(data=dR_dP_plot_data,aes(x=dR,y=dP))+plot_template+
  coord_fixed(xlim=c(0.0,6),ylim=c(0.007,0.2),ratio = 6/(0.2-0.007))+
  theme(plot.margin =  unit(c(0,1,2,1),units="lines"))+
  xlab(dR_label)+
  ylab(dP_label)

dR_dH_plot = ggplot(data=dR_dH_plot_data,aes(x=dR,y=dH))+plot_template+
  coord_fixed(xlim=c(0.0,6),ylim=c(0.007,0.2),ratio = 6/(0.2-0.007))+
  theme(plot.margin =  unit(c(1,1,1,1),units="lines"))+
  ylab(dH_label)+
  xlab("")
  #xlab(dR_label)
  #theme(axis.title.x = element_text(colour="white"))

beta_dR_plot = ggplot(data=K_dR_plot_data,aes(x=dR,y=beta))+plot_template+
  coord_fixed(xlim=c(0.0,6),ylim=c(0.05,0.35),ratio = 6/(.35-0.05))+
  geom_hline(aes(yintercept = 0.089), linetype=3)+
  beta_scale+
  xlab(dR_label)+
  ylab(beta_label)

beta_dP_plot = ggplot(data=K_dP_plot_data,aes(x=dP,y=beta))+plot_template+
  coord_fixed(xlim=c(0.007,0.2),ylim=c(0.05,0.35), ratio = (0.2-0.007)/0.3)+
  geom_hline(aes(yintercept = 0.089), linetype=3)+
  theme(plot.margin =  unit(c(0,1,2,1),units="lines"))+
  beta_scale+
  xlab(dP_label)+
  ylab(beta_label)

beta_dH_plot = ggplot(data=K_dH_plot_data,aes(x=dH,y=beta))+plot_template+
  coord_fixed(xlim=c(0.007,0.2),ylim=c(0.05,0.35), ratio = (0.2-0.007)/0.3)+
  geom_hline(aes(yintercept = 0.089), linetype=3)+
  theme(plot.margin =  unit(c(1,1,1,0),units="lines"))+
  beta_scale+
  xlab(dH_label)+
  ylab("")
  #ylab(beta_label)

beta_bifurc_plot = ggplot(aes(x=1/K, y=H_1, group=stable_line_id, linetype=stability,
                           colour=is_periodic), 
                       data= k_bifurc_line_data,line_id==9)+
  geom_path(size=1)+
  coord_cartesian(xlim=c(0.05,0.35),ylim=c(0,22))+
  scale_colour_manual(values=c("black","darkgrey"))+
  scale_linetype_manual(values=c("1111","solid"))+
  labs(x = beta_label, y = h1_label)+
  theme_bw()+
  theme(legend.position="none", panel.grid=element_blank())

write_svg = F

if(write_svg){
  svg("Output/figures/dx_dy_sim_plot.svg",width=8,height=8) 
}else{
  pdf("Output/figures/dx_dy_sim_plot.pdf",width=8,height=8) 
}
{
  PlotMultipleGgplotObjs(
    dR_dH_plot+annotate("text",x=6.0*x_rel_pos,y=0.193*y_rel_pos+0.007,label ="A"),
    dR_dP_plot+annotate("text",x=6.0*x_rel_pos,y=0.193*y_rel_pos+0.007,label ="C"),
    dH_dP_plot+annotate("text",x=0.193*x_rel_pos+0.007,y=0.193*y_rel_pos+0.007,label ="B"),
    colour_table_plot,cols=2)
} 
dev.off()

if(write_svg){
  svg("Output/figures/beta_dx_sim_plot.svg",width=8,height=8) 
}else{
  pdf("Output/figures/beta_dx_sim_plot.pdf",width=8,height=8) 
}
{
  PlotMultipleGgplotObjs(
    beta_dR_plot+annotate("text",x=6*x_rel_pos,y=0.3*y_rel_pos+0.05,label ="A"),
    beta_dP_plot+annotate("text",x=0.193*x_rel_pos+0.007,y=0.3*y_rel_pos+0.05,label ="C"),
    beta_dH_plot+annotate("text",x=0.193*x_rel_pos+0.007,y=0.3*y_rel_pos+0.05,label ="B")
    ,colour_table_plot,cols=2)
} 
dev.off()

if(write_svg){
  svg("Output/figures/beta_bifurc_plot.svg",width=8,height=4.5) 
}else{
  pdf("Output/figures/beta_bifurc_plot.pdf",width=8,height=4.5) 
}
{
  print(beta_bifurc_plot)
} 
dev.off()
