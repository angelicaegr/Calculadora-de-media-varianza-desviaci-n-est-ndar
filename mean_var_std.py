import numpy as np

def calculate(list):

def calculate(List):
    Matrix = np.array([List[0:9]])
    Matrix = Matrix.reshape(3, 3)
    print('matrix', Matrix)
    meanax0 = np.array([np.mean(Matrix[0]), np.mean(Matrix[1]), np.mean(Matrix[2])])
    meanax1 = np.array([np.mean(Matrix[:, 0]), np.mean(Matrix[:, 1]), np.mean(Matrix[:, 2])])
    meanF = np.mean(List)
    varax0 = np.array([np.var(Matrix[0]), np.var(Matrix[1]), np.var(Matrix[2])])
    varax1 = np.array([np.var(Matrix[:, 0]), np.var(Matrix[:, 1]), np.var(Matrix[:, 2])])
    varF = np.var(List)
    stdax0 = np.array([np.std(Matrix[0]), np.std(Matrix[1]), np.std(Matrix[2])])
    stdax1 = np.array([np.std(Matrix[:, 0]), np.std(Matrix[:, 1]), np.std(Matrix[:, 2])])
    stdF = np.std(List)
    maxax0 = np.array([np.max(Matrix[0]), np.max(Matrix[1]), np.max(Matrix[2])])
    maxax1 = np.array([np.max(Matrix[:, 0]), np.max(Matrix[:, 1]), np.max(Matrix[:, 2])])
    maxF = np.max(List)
    minax0 = np.array([np.min(Matrix[0]), np.min(Matrix[1]), np.min(Matrix[2])])
    minax1 = np.array([np.min(Matrix[:, 0]), np.min(Matrix[:, 1]), np.min(Matrix[:, 2])])
    minF = np.min(List)
    sumax0 = np.array([np.sum(Matrix[0]), np.sum(Matrix[1]), np.sum(Matrix[2])])
    sumax1 = np.sum([np.sum(Matrix[:, 0]), np.sum(Matrix[:, 1]), np.sum(Matrix[:, 2])])
    sumF = np.sum(List)

    keys = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    values = ([meanax0, meanax1, meanF], [varax0, varax1, varF], [stdax0, stdax1, stdF], [maxax0, maxax1, maxF],
              [minax0, minax1, minF], [sumax0, sumax1, sumF])
    dictionary = dict(zip(keys, values))

    print('dictionary', dictionary)
    return calculate


calculate(List)


   
