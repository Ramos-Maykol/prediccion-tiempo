import matplotlib.pyplot as plt

def guardar_grafico_pred_vs_real(y_real, y_pred, nombre_modelo, ruta_salida):
    plt.figure(figsize=(6, 4))
    plt.scatter(y_real, y_pred, alpha=0.6)
    plt.plot([min(y_real), max(y_real)], [min(y_real), max(y_real)], color='red', linestyle='--')
    plt.xlabel("Real")
    plt.ylabel("Predicho")
    plt.title(f"Predicho vs Real - {nombre_modelo}")
    plt.tight_layout()
    plt.savefig(ruta_salida)
    plt.close()
