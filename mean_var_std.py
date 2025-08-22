import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")

    array = np.array(lista).reshape(3, 3)

    calculations = {
        'mean': [
            array.mean(axis=0).tolist(),
            array.mean(axis=1).tolist(),
            array.mean().item()
        ],
        'variance': [
            array.var(axis=0).tolist(),
            array.var(axis=1).tolist(),
            array.var().item()
        ],
        'standard deviation': [
            array.std(axis=0).tolist(),
            array.std(axis=1).tolist(),
            array.std().item()
        ],
        'max': [
            array.max(axis=0).tolist(),
            array.max(axis=1).tolist(),
            array.max().item()
        ],
        'min': [
            array.min(axis=0).tolist(),
            array.min(axis=1).tolist(),
            array.min().item()
        ],
        'sum': [
            array.sum(axis=0).tolist(),
            array.sum(axis=1).tolist(),
            array.sum().item()
        ]
    }

    return calculations

# lista = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# calculate(lista)