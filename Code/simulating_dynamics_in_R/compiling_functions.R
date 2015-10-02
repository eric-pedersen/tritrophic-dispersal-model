#Functions for tritrophsim package to summarize and compile output files
CalcStateTypes = function(x){
  output = transform(x, sym_equib = !is_asym&!is_cyclic, asym_equib = is_asym&!is_cyclic,
                     sym_cyclic = !is_asym&is_cyclic, asym_cyclic = is_asym&is_cyclic, 
                     async_cyclic = is_cyclic&is_async&!is_asym)
  return(output)
}

CompileOutputFiles = function(path, first_var, second_var){
  pattern = paste(first_var, second_var, "[0-9]+_output.csv",sep="_")
  output_files = list.files(path,pattern=pattern,include.dirs=F,full.names=T)
  output_data = llply(output_files,.fun=read.csv)
  output_data = ldply(output_data)
  return(output_data)
}

SummarizeSimOutput = function(x){
  output_data = x[1,]
  output_data$sym_equib = sum(x$sym_equib,na.rm=T)/sum(!is.na(x$sym_equib))
  output_data$asym_equib = sum(x$asym_equib,na.rm=T)/sum(!is.na(x$asym_equib))
  output_data$sym_cyclic = sum(x$sym_cyclic,na.rm=T)/sum(!is.na(x$sym_cyclic))
  output_data$asym_cyclic = sum(x$asym_cyclic,na.rm=T)/sum(!is.na(x$asym_cyclic))
  output_data$async_cyclic = sum(x$async_cyclic,na.rm=T)/sum(!is.na(x$async_cyclic))
  output_data$class_color = with(output_data,
                                 ifelse(asym_equib>0&sym_cyclic>0,
                                        "yellow", 
                                        ifelse(sym_cyclic>0,
                                               "green",
                                               ifelse(asym_equib>0,
                                                      "red",
                                                      ifelse(async_cyclic>0,
                                                             "orange","blue")))))
  return(output_data)
}

SplitDataAtBlanks = function(x) {
  out_data = list()
  data_blanks = which(is.na(x[,1]))
  data_blanks = c(0,data_blanks)
  for(i in 1:(length(data_blanks)-1)){
    out_data[[i]] = x[(data_blanks[i]+1):(data_blanks[i+1]-1),]
  }
  return(out_data)
}