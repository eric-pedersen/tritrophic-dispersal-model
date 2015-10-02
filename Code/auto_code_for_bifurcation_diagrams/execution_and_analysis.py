import sys
import os
#need to change this to where auto/07p/python is located on your directory
sys.path.append("/home/ericpedersen/auto/07p/python")
#sys.path.append("C:\\auto\\07p\\python") #Use this path for running in Windows. 
#Note that it can be very problematic getting Auto running in Windows, especially 
#for using Matplotlib


#need to change this to the path for the project location on your system
os.chdir("/home/ericpedersen/Documents/Research_files/" +
         "Spatial_IGP_Paper/Code/auto_code_for_bifurcation_diagrams")

#Use this style for running the code in Windows.		 
#os.chdir("c:\\Users\\ericj_000\\Documents\\Research_files\\Spatial_IGP_Paper\\"+
#		 "Code\\Equal_handling_dispersal_IGP_bifurcations")

import auto
from matplotlib.pyplot import show
import numpy as np
import pandas as pd

def GetBifOutputs(object_name, file_path,is_single_var=False):
    var_1 = []
    var_2 = []
    is_period = []
    branch_type = []
    for i in range(object_name.__len__()):
        var_1.append(object_name[i].coordnames[0])
        if object_name[i].coordnames[-1]=="PERIOD":
            is_period.append("T")
            if is_single_var:
                var_2.append("H_1")
            else:
                var_2.append(object_name[i].coordnames[-2])
        else:
            is_period.append("F")
            if is_single_var:
                var_2.append("H_1")
            else:
                var_2.append(object_name[i].coordnames[-1])
        branch_type.append(object_name[i]['TY'])
    data = pd.DataFrame({'var_1':var_1,'var_2':var_2,'is_periodic':is_period,
                         'branch_type':branch_type})
    data.to_csv(file_path)
    return None

def ExtractBranchStability(object_name, file_path):
    line_id = []
    stability = []
    for i in range(object_name.__len__()):
        for j in object_name[i].stability():
            stability.append(j)
            line_id.append(i+1)
    data = pd.DataFrame({'line_id':line_id,'stability':stability})
    data.to_csv(file_path)
    return None
    
    
    


calc_limit_cycles= True
plot_combined_analyses = True

#These vectors establish ranges for the bifurcation parameters over which
#Auto will run continuation analyses
range_K = [-0.05,0,20]  
#Note: has both -0.05 and 0 in the list, due to some numerical problems when 
#computing solutions to the all-zero family of equilibria, which tends to skip 
#K = 0, so just keeps computing negative results

range_IGP = [0,0.1]
range_dispersal = [-0.5,10]
range_weak_dispersal = [-0.01,0,0.015,0.02]
range_dispersal_2_par = [-0.01,0,6]
range_K_two_parameter = [0,20]  

dynamics_file = "dynamics_fixed_high_dH"
        



start_point_analysis=[]
equal_handle_IGP_FP =[]
equal_handle_IGP_Hopf =[]
equal_handle_IGP_Asym_Branch =[]




execfile("starting_fixed_points.py")
execfile("starting_limit_cycles.py")



equilibrium_start =  equal_handle_IGP_FP('UZ8')  
#need this to start the equilibrium analysis
limit_start = equal_handle_IGP_Limit_Cycle('UZ2') 
#need this to start the dispersal limit cycles 


start_point_analysis = (equal_handle_IGP_FP + 
                 equal_handle_IGP_Hopf + 
                 equal_handle_IGP_Limit_Cycle)
start_point_analysis = auto.rl(start_point_analysis)

execfile('dispersal_fixed_points.py')

# The limit cycle is nessecary to follow to find the point where bistability is
# lost at different dispersal parameters
execfile("dispersal_limit_cycles.py")

if low_herbivore_dispersal:
    asym_branch = equal_handle_IGP_FP("BP6")
    sym_hopf = equal_handle_IGP_FP("HB3")
    sym_disperse_hopf_dP = dispersal_fixed_points("HB6")
    sym_disperse_hopf_dR = dispersal_fixed_points("HB1")
    
    asym_hopf_dR = dispersal_fixed_points("HB2")
    asym_hopf_dH = dispersal_fixed_points("HB4")
    asym_hopf_dP = dispersal_fixed_points("HB9")
else:
    asym_branch = equal_handle_IGP_FP("BP4")
    sym_hopf = equal_handle_IGP_FP("HB3")
    sym_disperse_hopf_dP = dispersal_fixed_points("HB8")
    sym_disperse_hopf_dR = dispersal_fixed_points("HB1")
    
    asym_hopf_dR = dispersal_fixed_points("HB2")
    asym_hopf_dH = dispersal_fixed_points("HB6")
    asym_hopf_dH_low = dispersal_fixed_points("HB7")
    asym_hopf_dP = dispersal_fixed_points("HB9")

period_doubling_point = start_point_analysis("PD1")
limit_cycle_fold = equal_handle_IGP_Limit_Cycle(["LP1","LP5"])

dispersal_limit_branch_dH = dispersal_limit_cycles("BP1")
dispersal_limit_branch_dP = dispersal_limit_cycles("BP2")

asym_branch_dR = dispersal_fixed_points("BP1")
asym_branch_dH = dispersal_fixed_points("BP2")

tri_stable_branch_point = equal_handle_IGP_Limit_Cycle("BP6")

dX_K_hopf_bifurcations = equal_handle_IGP_FP(["HB4","HB5"])

execfile('dispersal_K_analyses.py')


limit_branch_points = {"dR":limit_branch_point("UZ5"),
                       "dH":limit_branch_point("UZ3"),
                       "dP":limit_branch_point("UZ8")
                       }

fold_points = {"dR":fold_plot("UZ2"),
                       "dH":fold_plot("UZ4"),
                       "dP":fold_plot("UZ5")
                       }


execfile('dispersal_two_parameter_analyses.py')


dX_K_plot =auto.merge(dX_K_plot)
dX_dY_plot =auto.merge(dX_dY_plot)
start_point_analysis = auto.merge(start_point_analysis)

auto.rl(start_point_analysis)

#Plots to look at the raw bifurcation diagrams in python. Comment out these 
#commands if you don't want plots. Not needed for making final diagrams
auto.plot(start_point_analysis, 
            stability=True,use_labels=False,
            bifurcation_x= ['K'],bifurcation_y= ['MAX H_1'],
            coloring_method = "type", use_symbols= False,
            grid = False)
auto.plot(dispersal_fixed_points, 
            stability=True,use_labels=False,
            bifurcation_x= ['dR'],bifurcation_y= ['H_1'],
            coloring_method = "type", use_symbols= False,
            grid = False)
auto.plot(dX_K_plot, 
            stability=False,use_labels=False,
            bifurcation_x= ['dP'],bifurcation_y= ['K'],
            minx=0,maxx = 0.2,
            miny=0, maxy =20,
            coloring_method = "type", use_symbols= False,
            grid = False)
auto.plot(dX_dY_plot, 
            stability=False,use_labels=False,
            bifurcation_x= ['dR'],bifurcation_y= ['dP'],
            coloring_method = "type", use_symbols= False,
            grid = False)

auto.cl()


#exports csv files for R to analyze
#If running in windows, change / to \\ for these parts. 
dX_dY_plot.writeRawFilename("../simulating_dynamics_in_R/dX_dY_line_data.csv")
GetBifOutputs(dX_dY_plot, "../simulating_dynamics_in_R/dX_dY_plot_ids.csv")

dX_K_plot.writeRawFilename("../simulating_dynamics_in_R/dX_K_line_data.csv")
GetBifOutputs(dX_K_plot, "../simulating_dynamics_in_R/dX_K_plot_ids.csv")

start_point_analysis.writeRawFilename("../simulating_dynamics_in_R/K_bifuc_line_data.csv")
GetBifOutputs(start_point_analysis, "../simulating_dynamics_in_R/K_bifurc_plot_ids.csv",is_single_var=True)
ExtractBranchStability(start_point_analysis,"../simulating_dynamics_in_R/K_bifurc_stability.csv")
                       
