import numpy as np

def calculate(list):

ls = np.array(list)
print(ls)

mean_rows = [ls[[0,1,2]].mean(), ls[[3,4,5]].mean(), ls[[6,7,8]].mean()]
mean_colums =  [ls[[0,3,6]].mean(), ls[[1,4,7]].mean(), ls[[2,5,8]].mean()]

var_rows = [ls[[0,1,2]].var(), ls[[3,4,5]].var(), ls[[6,7,8]].var()]
var_colums =  [ls[[0,3,6]].var(), ls[[1,4,7]].var(), ls[[2,5,8]].var.()]

std_rows = [ls[[0,1,2]].std(), ls[[3,4,5]].std(), ls[[6,7,8]].std()]
std_colums =  [ls[[0,3,6]].std(), ls[[1,4,7]].std(), ls[[2,5,8]].std.()]

max_rows = [ls[[0,1,2]].max(), ls[[3,4,5]].max(), ls[[6,7,8]].max()]
max_colums =  [ls[[0,3,6]].max(), ls[[1,4,7]].max(), ls[[2,5,8]].max.()]

min_rows = [ls[[0,1,2]].min(), ls[[3,4,5]].min(), ls[[6,7,8]].min()]
min_colums =  [ls[[0,3,6]].min(), ls[[1,4,7]].min(), ls[[2,5,8]].min.()]

return(  
  'mean': [mean_colums, mean_arrowa, ls.mean()],
  'variance': [var_colums, var_rows, ls.var()],
  'standard deviation':[std_colums, std_rows, ls.var()],
  'max': [max_colums, max_rows, ls.max()],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]

)
