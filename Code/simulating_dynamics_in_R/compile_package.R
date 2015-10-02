#Code for building the pacakge tritrophsim. After running this file, 
# run rstudio's "Build source package" or "build binary package" commands
unlink("Code/simulating_dynamics_in_R/tritrophsim",recursive=T)
unlink("Code/simulating_dynamics_in_R/tritrophsim_1.0.tar.gz")
unlink("Code/simulating_dynamics_in_R/tritrophsim_1.0.zip")
package.skeleton(name="tritrophsim", code_files=c("Code/simulating_dynamics_in_R/testing_functions.R",
                                                  "Code/simulating_dynamics_in_R/compiling_functions.R",
                                                  "Code/simulating_dynamics_in_R/model_file.r",
                                                  "Code/simulating_dynamics_in_R/plotting_functions.R"),
                 path = "Code/simulating_dynamics_in_R/",force=T)

unlink("Code/simulating_dynamics_in_R/tritrophsim/man/*",recursive=F)
