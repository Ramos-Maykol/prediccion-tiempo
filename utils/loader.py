import joblib
import numpy as np
from tensorflow.keras.models import load_model
from xgboost import XGBRegressor

def cargar_modelos():
    modelo_ann = load_model("modelos/modelo_produccion_ANN.h5")
    modelo_rf = joblib.load("modelos/modelo_random_forest.pkl")
    modelo_xgb = XGBRegressor()
    modelo_xgb.load_model("modelos/modelo_xgboost.json")
    return modelo_ann, modelo_rf, modelo_xgb

def cargar_scaler():
    return joblib.load("data/scaler.pkl")

def cargar_datos_test():
    X_test = np.load("data/X_test.npy")
    y_test = np.load("data/y_test.npy")
    return X_test, y_test

def cargar_modelo_hibrido():
    return joblib.load("modelos/modelo_hibrido.pkl")