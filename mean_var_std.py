import numpy as np

def calculate(input_list):
    if len(input_list)<9:
        raise ValueError( "List must contain nine numbers.")
    reshaped=np.reshape(input_list,(3,3))
    result={
        'mean': [
            np.mean(reshaped,axis=0).tolist(),
            np.mean(reshaped,axis=1).tolist(),
            np.mean(reshaped).item()
        ],
        'variance': [
            np.var(reshaped,axis=0).tolist(),
            np.var(reshaped,axis=1).tolist(),
            np.var(reshaped).item()
        ],
    'standard deviation': [
            np.std(reshaped,axis=0).tolist(),
            np.std(reshaped,axis=1).tolist(),
            np.std(reshaped).item()
        ],
    'max': [
            np.max(reshaped,axis=0).tolist(),
            np.max(reshaped,axis=1).tolist(),
            np.max(reshaped).item()
        ],
    'min': [
            np.min(reshaped, axis=0).tolist(),
            np.min(reshaped, axis=1).tolist(),
            np.min(reshaped).item()
        ],
        'sum': [
            np.sum(reshaped, axis=0).tolist(),
            np.sum(reshaped, axis=1).tolist(),
            np.sum(reshaped).item()
        ]
    }

        
    return result
