#plotting functions. Incorporated into the Tritrophsim package

SummarizeSims = function(x) {
  x$is_asym = x$asym_val>0.05
  x$is_async = x$async_val<0.95
  x$sym_equib = with(x, !is_cyclic&!is_asym)
  x$asym_equib = with(x, !is_cyclic&is_asym)
  x$sym_cycle = with(x, is_cyclic&!is_asym&!is_async)
  x$asym_cycle = with(x, is_cyclic&is_asym)
  x$async_cycle = with(x, is_cyclic&!is_asym&is_async)
  
  return(x)
}

CalculateColourWeights = function(x){
  reduced_matrix =subset(x, select = c(sym_equib ,asym_equib,sym_cycle, asym_cycle, async_cycle))
  #red_weights = c(sym_equib = 0, asym_equib = 0,sym_cycle = 210, asym_cycle=210, async_cycle=200)
  red_weights = c(sym_equib = 0, asym_equib = 0,sym_cycle = 255, asym_cycle=205, async_cycle=140)
  green_weights = c(sym_equib = 200, asym_equib = 128,sym_cycle = 255, asym_cycle=133, async_cycle=72)
  blue_weights = c(sym_equib = 0, asym_equib = 0,sym_cycle = 255, asym_cycle=63, async_cycle=35)
  red_channel = format(as.hexmode(round(rowSums(sweep(reduced_matrix,MARGIN=2,STATS=red_weights, FUN ="*")))),upper.case=T)
  green_channel = format(as.hexmode(round(rowSums(sweep(reduced_matrix,MARGIN=2,STATS=green_weights, FUN ="*")))),upper.case=T)
  blue_channel = format(as.hexmode(round(rowSums(sweep(reduced_matrix,MARGIN=2,STATS=blue_weights, FUN ="*")))),upper.case=T)
  col_out = paste("#",red_channel,green_channel,blue_channel,sep="")
  return(col_out)
}

CreatePlottingData = function(x,vars){
  out_data = ddply(x,vars,
                   function(y) colSums(y,na.rm=T)/colSums(!is.na(y)))
  out_data$weighted_col = CalculateColourWeights(out_data)
  return(out_data)
}