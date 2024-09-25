import numpy as np

def calculate(lista):
    # Verificar se a lista contém exatamente 9 elementos
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")  # Mensagem que os testes esperam

    # Transformar a lista em um array NumPy de 3x3
    matriz = np.array(lista).reshape(3, 3)

    # Cálculos ao longo dos eixos e na matriz achatada
    calculations = {
        'mean': [matriz.mean(axis=0).tolist(), matriz.mean(axis=1).tolist(), matriz.mean().item()],
        'variance': [matriz.var(axis=0).tolist(), matriz.var(axis=1).tolist(), matriz.var().item()],
        'standard deviation': [matriz.std(axis=0).tolist(), matriz.std(axis=1).tolist(), matriz.std().item()],
        'max': [matriz.max(axis=0).tolist(), matriz.max(axis=1).tolist(), matriz.max().item()],
        'min': [matriz.min(axis=0).tolist(), matriz.min(axis=1).tolist(), matriz.min().item()],
        'sum': [matriz.sum(axis=0).tolist(), matriz.sum(axis=1).tolist(), matriz.sum().item()]
    }

    return calculations