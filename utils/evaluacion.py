# utils/evaluacion.py

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from scipy.stats import t

def calcular_metricas(y_true, y_pred):
    """Calcula MAE, MSE y R²."""
    return {
        "MAE": mean_absolute_error(y_true, y_pred),
        "MSE": mean_squared_error(y_true, y_pred),
        "R²": r2_score(y_true, y_pred)
    }

def theils_u(y_true, y_pred):
    """Calcula el coeficiente U de Theil."""
    num = np.sqrt(np.mean((y_pred - y_true) ** 2))
    den = np.sqrt(np.mean(y_pred ** 2)) + np.sqrt(np.mean(y_true ** 2))
    return num / den

def prueba_diebold_mariano(y, pred1, pred2):
    """Prueba Diebold-Mariano para comparar modelos."""
    e1 = y - pred1
    e2 = y - pred2
    d = (e2 ** 2) - (e1 ** 2)
    mean_d = np.mean(d)
    var_d = np.var(d, ddof=1)
    dm_stat = mean_d / np.sqrt(var_d / len(d))
    p_value = 2 * (1 - t.cdf(abs(dm_stat), df=len(d) - 1))
    return dm_stat, p_value
