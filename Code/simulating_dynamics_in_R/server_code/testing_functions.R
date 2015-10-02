require(deSolve)

TestModelTypes = function(data,start_time=4000, use_block_tests=F,
                          error_tols = c(var_tol =0.01, diff_tol =0.01,cor_tol =0.9)){
  max_time = nrow(data)
  indexes =start_time:max_time
  n_points = length(indexes)

  H1 = data[,'H1']
  H2 = data[,'H2']
  cyclic_val = (var(H1[indexes])/mean(H1[indexes]) + var(H2[indexes])/mean(H2[indexes]))/2
  is_cyclic = cyclic_val>error_tols['var_tol']
  asym_val = abs(mean(H1[indexes]) - mean(H2[indexes]))/max(mean(H1[indexes]), mean(H2[indexes]))
  is_asym = asym_val>error_tols['diff_tol']
  async_val = ifelse(is_cyclic, cor(H1[indexes], H2[indexes]), 1)
  is_async = async_val < error_tols['cor_tol']
  if(use_block_tests){
    test_1 = TestModelTypes(data[1:round(n_points/2),],
                            start_time = 0, use_block_tests=F,
                            error_tols= error_tols)
    test_2 = TestModelTypes(data[(round(n_points/2)+1):max_time,],
                            start_time = 0, use_block_tests=F,
                            error_tols= error_tols)
    const_cyclic = abs(test_1$cyclic_val-test_2$cyclic_val)<=error_tols['var_tol']
    const_asym = abs(test_1$asym_val-test_2$asym_val)<=error_tols['diff_tol']
    const_async = abs(test_1$async_val-test_2$async_val)<=(1-error_tols['cor_tol'])
  }else{
    const_cyclic = NA
    const_asym = NA
    const_async = NA
  }
  return(data.frame(is_cyclic=is_cyclic,is_asym =is_asym, is_async= is_async,
                    const_cyclic=const_cyclic, const_asym= const_asym, const_async= const_async,
                    cyclic_val = cyclic_val, asym_val = asym_val, async_val =async_val)
                    )
}
  

RunSims = function(starting_points, parameter_values, run_length=10000,
                   measure_length = 5000,handle_errors=T, use_block_tests=T,
                   restart_at_non_const =T, n_extra_steps = 5, 
                   testing_function = TestModelTypes, use_jacob=F){
  #source("code/model_file.r",local=T)
  #source("code/testing_functions.R",local=T)
  require(deSolve)
  output_data = as.data.frame(parameter_values)
  output_data$is_cyclic = T
  output_data$is_asym= T
  output_data$is_async= T
  output_data$const_cyclic=NA 
  output_data$const_asym= NA 
  output_data$const_async=NA
  output_data$cyclic_val = T
  output_data$asym_val= T
  output_data$async_val= T
  output_data$R1 = starting_points['R1']
  output_data$R2 = starting_points['R2']
  output_data$H1 = starting_points['H1']
  output_data$H2 = starting_points['H2']
  output_data$P1 = starting_points['P1']
  output_data$P2 = starting_points['P2']
  output_data$run_time = 0

  if(use_jacob){
    jacfunc = TriTrophJacob
    jactype = "fullusr"
  }else{
    jacfunc = NULL
    jactype = "fullint"
  }
  
  for(i in 1:nrow(parameter_values)){
    current_parameters = parameter_values[i,]
    current_starting_point = starting_points
    current_run_length = run_length
    start_measuring = run_length - measure_length
    total_run_time = 0
    restart_sample = T
    while(restart_sample){
      total_run_time = total_run_time + current_run_length
    model_output = tryCatch(ode(y=current_starting_point,times=seq(0,current_run_length,
                                                                   length=current_run_length),
                                maxsteps=run_length*2,
                                func=TriTrophDynamics,parms=current_parameters),
                                jacfunc=jacfunc,jactype=jactype,
                                error=function(cond){
                                  if(handle_errors) {
                                      return (matrix(NA))
                                    }else stop(cond)
                                  }, 
                                warning=function(cond) matrix(NA)
    )
    if(is.na(model_output[1,1])){
      model_summary = data.frame(is_cyclic=NA,is_asym = NA, is_async=NA,
                                        cyclic_val= NA,  asym_val =NA, async_val =NA)
    }else{
      model_summary = testing_function(model_output,start_time=start_measuring, 
                                       use_block_tests=use_block_tests )
    }
    restart_run_test = restart_at_non_const&(!(model_summary$const_cyclic&model_summary$const_asym&model_summary$const_async))
    if(is.na(restart_run_test)){
      restart_run_test = F
    }
    if(restart_run_test){
      current_starting_point = model_output[nrow(model_output),-1]
      current_run_length = measure_length
      start_measuring = 0
      if(((total_run_time - run_length)/n_extra_steps) >= measure_length){
        restart_sample = F
      }
    }else{
      restart_sample=F
    }
    }
    output_data[i,12:20] = model_summary 
    output_data[i,'run_time'] = total_run_time
    restart_sample=T
  }

  return(output_data)
 } 