# tritrophic-dispersal-model
This was the code used to create the figures for the paper "Non-hierarchical dispersal promotes stability and resilience in a tri-trophic metacommunity" upcoming in American Naturalist

## Running bifurcation analyses
To reproduce the bifurcation analyses from this paper, you have to have python 2.x (2.7+ recommended)
as well as the pandas, numpy and matplotlib packages for python installed. Further, you need to have [auto-07p](http://indy.cs.concordia.ca/auto/) installed somewhere on your system. 

To generate all of the nessecary files for the R-scripts that plot the bifurcation code, you need to run the file "Code/auto_code_for_bifurcation_diagram/execution_and_analysis.py". For further details, see the file "Code/auto_code_for_bifurcation_diagram/instructions for running bifurcations.txt"

## Running R for plotting and simulations
This code repository is set up to be run as a Rstudio project. After downloading the repository and installing Rstudio, you can open the project by running the file "tritrophic-dispersal-model.Rproj".

### Creating the R package "tritrophsim"
The core of these analyses are simulation code run using a custom-built package: "tritrophsim". This package consists of three R files found in "/Code/simulating_dynamics_in_R": "compiling_functions.R", "plotting_functions.R" and "testing_functions.R". These can all be compiled into a package by first running the script "compile_package.R" then using Rstudio's "build" tool, by clicking the *build* menu, then *build source package*. After this, you should install the source package into your local library in R. 



### Running R simulations for figures
This code is currently not set up to be simple to run on any computer; This is because the simulation runs for both figure 3 and 4 require a great deal of computation, longer than is feasible on a single desktop. I ran all the simulations for this project on the Collose server from Compute Canada; as such, the code is set up to construct scripts and code to be moved over to that server to run. To set it up for a different use, please contact me for help.

However, the current output folder in this repository holds all the simulation outputs for the figures in the main text. 

###Plotting R figures
To create figures 2, 3, and 4 from the paper, you need to run "Code/simulating_dynamics_in_R/plotting_tritroph_sims.R". To create the figures in appendix B, you need to run "Code/simulating_dynamics_in_R/plotting_tritroph_sims_sensitivity_test.R". Finally, to create the figure for Appendix C, you need to run "Code/simulating_dynamics_in_R/analyzing_bistability.R". 