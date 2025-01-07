import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convertendo a lista em uma matriz 3x3
    arr = np.array(list).reshape(3, 3)
    
    # Calculando os valores requisitados
    calculations = {
        'mean': [
            arr.mean(axis=0).tolist(),  # média das colunas
            arr.mean(axis=1).tolist(),  # média das linhas
            arr.mean().tolist()         # média da matriz nivelada
        ],
        'variance': [
            arr.var(axis=0).tolist(),   # variância das colunas
            arr.var(axis=1).tolist(),   # variância das linhas
            arr.var().tolist()          # variância da matriz nivelada
        ],
        'standard deviation': [
            arr.std(axis=0).tolist(),   # desvio-padrão das colunas
            arr.std(axis=1).tolist(),   # desvio-padrão das linhas
            arr.std().tolist()          # desvio-padrão da matriz nivelada
        ],
        'max': [
            arr.max(axis=0).tolist(),   # máximo das colunas
            arr.max(axis=1).tolist(),   # máximo das linhas
            arr.max().tolist()          # máximo da matriz nivelada
        ],
        'min': [
            arr.min(axis=0).tolist(),   # mínimo das colunas
            arr.min(axis=1).tolist(),   # mínimo das linhas
            arr.min().tolist()          # mínimo da matriz nivelada
        ],
        'sum': [
            arr.sum(axis=0).tolist(),   # soma das colunas
            arr.sum(axis=1).tolist(),   # soma das linhas
            arr.sum().tolist()          # soma da matriz nivelada
        ]
    }
    
    return calculations



