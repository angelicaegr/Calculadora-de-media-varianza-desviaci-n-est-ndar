import numpy as np

def calculate(list):

ls = np.array(list)
print(ls)

mean_rows = [ls[[0,1,2]].mean(), ls[[3,4,5]].mean(), ls[[6,7,8]].mean()]
mean_colums =  [ls[[0,3,6]].mean(), ls[[1,4,7]].mean(), ls[[2,5,8]].mean()]

var_rows = [ls[[0,1,2]].var(), ls[[3,4,5]].var(), ls[[6,7,8]].var()]
mean_colums =  [ls[[0,3,6]].var(), ls[[1,4,7]].var(), ls[[2,5,8]].var.()]

return(  
  'mean': [mean_colums, mean_arrowa, ls.mean()],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]

)
