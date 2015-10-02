#This script will load the auto plot data

require(plyr)
require(ggplot2)
require(scales)
require(tritrophsim)

  
dxk_line_data <- read.table("Code/simulating_dynamics_in_R/dX_K_line_data.csv",blank.lines.skip=F, quote="\"")
dxk_line_data = SplitDataAtBlanks(dxk_line_data)

dxdy_line_data <- read.table("Code/simulating_dynamics_in_R/dX_dY_line_data.csv",blank.lines.skip=F, quote="\"")
dxdy_line_data = SplitDataAtBlanks(dxdy_line_data)



dxk_line_ids = read.table("Code/simulating_dynamics_in_R/dX_K_plot_ids.csv",sep=",",header=T,stringsAsFactors=F)
dxdy_line_ids = read.table("Code/simulating_dynamics_in_R/dX_dY_plot_ids.csv",sep=",",header=T,stringsAsFactors=F)

for(i in 1:nrow(dxk_line_ids)){
  if(dxk_line_ids$is_periodic[i]==T){
    dxk_line_data[[i]] = dxk_line_data[[i]][,c(1,7)]
  }else{
    dxk_line_data[[i]] = dxk_line_data[[i]][,c(1,8)]
  }
  names(dxk_line_data[[i]]) = c(dxk_line_ids$var_1[i],dxk_line_ids$var_2[i])
  dxk_line_data[[i]]$branch_type = dxk_line_ids$branch_type[i]
  dxk_line_data[[i]]$line_id = i
}


for(i in 1:nrow(dxdy_line_ids)){
  if(dxdy_line_ids$is_periodic[i]==T){
    dxdy_line_data[[i]] = dxdy_line_data[[i]][,c(1,7)]
  }else{
    dxdy_line_data[[i]] = dxdy_line_data[[i]][,c(1,8)]
  }
  names(dxdy_line_data[[i]]) = c(dxdy_line_ids$var_1[i],dxdy_line_ids$var_2[i])
  dxdy_line_data[[i]]$branch_type = dxdy_line_ids$branch_type[i]
  dxdy_line_data[[i]]$line_id = i
}
dxdy_line_data= ldply(dxdy_line_data)

dxk_line_data= ldply(dxk_line_data)
dxdy_line_data$K = NA

bifurc_line_data= rbind(dxdy_line_data,dxk_line_data)


k_bifurc_line_data = read.table("Code/simulating_dynamics_in_R/K_bifuc_line_data.csv",blank.lines.skip=F, quote="\"")
k_bifurc_line_data = SplitDataAtBlanks(k_bifurc_line_data)
k_bifurc_line_ids = read.table("Code/simulating_dynamics_in_R/K_bifurc_plot_ids.csv",sep=",",header=T,stringsAsFactors=F)
k_bifurc_stability = read.table("Code/simulating_dynamics_in_R/K_bifurc_stability.csv",sep=",",header=T,stringsAsFactors=F)


for(i in 1:nrow(k_bifurc_line_ids)){
  k_bifurc_line_data[[i]] = k_bifurc_line_data[[i]][,c(1,5)]
  names(k_bifurc_line_data[[i]]) = c(k_bifurc_line_ids$var_1[i],k_bifurc_line_ids$var_2[i])
  k_bifurc_line_data[[i]]$line_id = i
  k_bifurc_line_data[[i]]$is_periodic = k_bifurc_line_ids$is_periodic[i]
}

d_ply(k_bifurc_stability,.variables=.(line_id),.fun=function(x){
  current_line_id = x$line_id[1]
  n_points = nrow(k_bifurc_line_data[[current_line_id]])
  is_stable = rep(TRUE,times=n_points)
  stable_line_id = rep(0, times= n_points)
  for(i in 1:nrow(x)){
    current_index = abs(x$stability[i])
    current_stab = x$stability[i]<0
    if(i ==1){
      previous_index =1
    }else{
      previous_index = abs(x$stability[i-1])
    }
    is_stable[previous_index:(current_index-1)] = current_stab
    stable_line_id[previous_index:(current_index-1)] = paste(current_line_id,i,sep="_")
    if(i ==nrow(x)){
      is_stable[current_index:n_points] = !current_stab
      stable_line_id[current_index:n_points] = paste(current_line_id,i+1,sep="_")
    }
  }
  k_bifurc_line_data[[current_line_id]]$stability <<- is_stable
  k_bifurc_line_data[[current_line_id]]$stable_line_id <<- stable_line_id
  return(NULL)
})

k_bifurc_line_data = ldply(k_bifurc_line_data)
#removing extraneous lines
k_bifurc_line_data = subset(k_bifurc_line_data,
                            !line_id%in%c(1,2,3)&!stable_line_id%in%c("7_5","8_3","9_2"))


k_bifurc_line_data[with(k_bifurc_line_data,(1/K)<0.1&stable_line_id=="4_1"),"K"] = 20
k_bifurc_line_data[with(k_bifurc_line_data,(1/K)>0.3&stable_line_id=="4_2"),"K"] = 1/0.35

