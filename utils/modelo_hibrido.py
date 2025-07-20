# utils/modelo_hibrido.py

class ModeloHibrido:
    def __init__(self, modelo_ann=None, modelo_rf=None, modelo_xgb=None, pesos=[1/3, 1/3, 1/3]):
        self.modelo_ann = modelo_ann
        self.modelo_rf = modelo_rf
        self.modelo_xgb = modelo_xgb
        self.pesos = pesos

    def predict(self, X):
        pred = 0
        if self.modelo_ann and self.pesos[0] > 0:
            pred += self.pesos[0] * self.modelo_ann.predict(X).flatten()
        if self.modelo_rf and self.pesos[1] > 0:
            pred += self.pesos[1] * self.modelo_rf.predict(X)
        if self.modelo_xgb and self.pesos[2] > 0:
            pred += self.pesos[2] * self.modelo_xgb.predict(X)
        return pred
