import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    else:
        l = np.array(list).reshape(3,3)
        calculations = {
            'mean': [np.mean(l, axis = 0), np.mean(l, axis = 1), np.mean(l)],
            'variance': [np.var(l, axis = 0), np.var(l, axis = 1), np.var(l)],
            'standard deviation': [np.std(l, axis = 0), np.std(l, axis = 1), np.std(l)],
            'max': [np.max(l, axis = 0), np.max(l, axis = 1), np.max(l)],
            'min': [np.min(l, axis = 0), np.min(l, axis = 1), np.min(l)],
            'sum': [np.sum(l, axis = 0), np.sum(l, axis = 1), np.sum(l)]
                    }
    for chave, valor in calculations.items():
        for k in range(len(valor)):
            # Verify is valor is a np.array
            if isinstance(valor[k], np.ndarray):
                # transform ndarray into list
                valor[k] = valor[k].tolist()

    return calculations