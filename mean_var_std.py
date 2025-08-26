import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    m = np.array(numbers).reshape(3, 3)

    return {
        'mean': [
            m.mean(axis=0).tolist(),
            m.mean(axis=1).tolist(),
            m.mean().item()
        ],
        'variance': [
            m.var(axis=0).tolist(),
            m.var(axis=1).tolist(),
            m.var().item()
        ],
        'standard deviation': [
            m.std(axis=0).tolist(),
            m.std(axis=1).tolist(),
            m.std().item()
        ],
        'max': [
            m.max(axis=0).tolist(),
            m.max(axis=1).tolist(),
            m.max().item()
        ],
        'min': [
            m.min(axis=0).tolist(),
            m.min(axis=1).tolist(),
            m.min().item()
        ],
        'sum': [
            m.sum(axis=0).tolist(),
            m.sum(axis=1).tolist(),
            m.sum().item()
        ],
    }
