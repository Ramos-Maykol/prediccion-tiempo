# utils/lang/textos_pdf.py

"""
Módulo de internacionalización (i18n) para el generador de reportes en PDF.

Este archivo contiene un diccionario `TRADUCCIONES` con los textos utilizados
en el reporte, disponibles en varios idiomas.

--- ESTRUCTURA DE CLAVES ---
- Claves en minúsculas y snake_case (ej: 'titulo', 'texto_conclusion').
- Las claves que corresponden a cabeceras de tablas en los DataFrames de entrada
  (ej: 'modelo', 'mae', 'estadistico_dm') son cruciales para que el sistema
  de renombrado automático de columnas funcione correctamente. Asegúrese de que
  estas claves existan en todas las traducciones.
"""

TRADUCCIONES = {
    "es": {
        # --- Secciones Generales ---
        "titulo": "📊 Reporte Comparativo de Modelos de Predicción",
        "intro": "Este informe presenta un análisis comparativo de varios modelos predictivos entrenados para estimar el tiempo de producción.",
        "detalles_maquina": "🖥️ Especificaciones de la Máquina",
        "visualizaciones": "📈 Visualizaciones del Análisis Exploratorio (EDA)",
        "preprocesamiento": "⚙️ Preprocesamiento de Datos",
        "descripcion_preprocesamiento": "Se aplicaron técnicas de limpieza, codificación de variables categóricas (One-Hot Encoding) y escalado de características (StandardScaler) para preparar los datos antes del entrenamiento.",
        "conclusion": "📌 Conclusión",
        "texto_conclusion": "Tras analizar las métricas de rendimiento, los tests estadísticos y los tiempos de entrenamiento, el modelo con el mejor desempeño general, considerando el balance entre precisión y eficiencia, fue: {modelo}.",
        
        # --- Métricas y Tablas ---
        "metricas": "📏 Métricas de Evaluación de Modelos",
        "modelo": "Modelo",
        "mae": "MAE",
        "mse": "MSE",
        "r2": "R²",
        "tiempo": "⏱️ Tiempo (s)",
        
        # --- Gráficos ---
        "graficos_pred_vs_real": "📉 Predicciones vs. Valores Reales",
        "pred_vs_real_titulo": "Predicho vs. Real",
        "valor_real": "Valor Real",
        "valor_predicho": "Valor Predicho",

        # --- Tests Estadísticos ---
        "theil": "📐 Coeficiente U de Theil",
        "diebold": "🧪 Prueba de Diebold-Mariano",
        "comparacion": "Comparación",
        "estadistico_dm": "Estadístico DM",
        "valor_p": "Valor p",
    },
    "en": {
        # --- General Sections ---
        "titulo": "📊 Predictive Model Comparison Report",
        "intro": "This report presents a comparative analysis of several predictive models trained to estimate production time.",
        "detalles_maquina": "🖥️ Machine Specifications",
        "visualizaciones": "📈 Exploratory Data Analysis (EDA) Visualizations",
        "preprocesamiento": "⚙️ Data Preprocessing",
        "descripcion_preprocesamiento": "Cleaning, categorical variable encoding (One-Hot Encoding), and feature scaling (StandardScaler) techniques were applied to prepare the data before model training.",
        "conclusion": "📌 Conclusion",
        "texto_conclusion": "After analyzing performance metrics, statistical tests, and training times, the model with the best overall performance, considering the balance between accuracy and efficiency, was: {modelo}.",

        # --- Metrics & Tables ---
        "metricas": "📏 Model Evaluation Metrics",
        "modelo": "Model",
        "mae": "MAE",
        "mse": "MSE",
        "r2": "R²",
        "tiempo": "⏱️ Time (s)",

        # --- Plots ---
        "graficos_pred_vs_real": "📉 Predictions vs. Real Values",
        "pred_vs_real_titulo": "Predicted vs. Real",
        "valor_real": "Real Value",
        "valor_predicho": "Predicted Value",

        # --- Statistical Tests ---
        "theil": "📐 Theil's U Coefficient",
        "diebold": "🧪 Diebold-Mariano Test",
        "comparacion": "Comparison",
        "estadistico_dm": "DM Statistic",
        "valor_p": "p-value",
    },
    "pt": {
        # --- Seções Gerais ---
        "titulo": "📊 Relatório Comparativo de Modelos Preditivos",
        "intro": "Este relatório apresenta uma análise comparativa de vários modelos preditivos treinados para estimar o tempo de produção.",
        "detalles_maquina": "🖥️ Especificações da Máquina",
        "visualizaciones": "📈 Visualizações da Análise Exploratória de Dados (EDA)",
        "preprocesamiento": "⚙️ Pré-processamento de Dados",
        "descripcion_preprocesamiento": "Técnicas de limpeza, codificação de variáveis categóricas (One-Hot Encoding) e escalonamento de características (StandardScaler) foram aplicadas para preparar os dados antes do treinamento.",
        "conclusion": "📌 Conclusão",
        "texto_conclusion": "Após analisar as métricas de desempenho, testes estatísticos e tempos de treinamento, o modelo com o melhor desempenho geral, considerando o equilíbrio entre precisão e eficiência, foi: {modelo}.",

        # --- Métricas e Tabelas ---
        "metricas": "📏 Métricas de Avaliação de Modelos",
        "modelo": "Modelo",
        "mae": "MAE",
        "mse": "MSE",
        "r2": "R²",
        "tiempo": "⏱️ Tempo (s)",

        # --- Gráficos ---
        "graficos_pred_vs_real": "📉 Previsões vs. Valores Reais",
        "pred_vs_real_titulo": "Previsto vs. Real",
        "valor_real": "Valor Real",
        "valor_predicho": "Valor Previsto",

        # --- Testes Estatísticos ---
        "theil": "📐 Coeficiente U de Theil",
        "diebold": "🧪 Teste de Diebold-Mariano",
        "comparacion": "Comparação",
        "estadistico_dm": "Estatística DM",
        "valor_p": "Valor-p",
    },
    "fr": {
        # --- Sections Générales ---
        "titulo": "📊 Rapport Comparatif des Modèles Prédictifs",
        "intro": "Ce rapport présente une analyse comparative de plusieurs modèles prédictifs entraînés pour estimer le temps de production.",
        "detalles_maquina": "🖥️ Spécifications de la Machine",
        "visualizaciones": "📈 Visualisations de l'Analyse Exploratoire des Données (EDA)",
        "preprocesamiento": "⚙️ Prétraitement des Données",
        "descripcion_preprocesamiento": "Des techniques de nettoyage, d'encodage de variables catégorielles (One-Hot Encoding) et de mise à l'échelle des caractéristiques (StandardScaler) ont été appliquées pour préparer les données avant l'entraînement.",
        "conclusion": "📌 Conclusion",
        "texto_conclusion": "Après analyse des métriques de performance, des tests statistiques et des temps d'entraînement, le modèle avec la meilleure performance globale, en considérant l'équilibre entre précision et efficacité, était : {modelo}.",
        
        # --- Métriques et Tableaux ---
        "metricas": "📏 Métriques d'Évaluation des Modèles",
        "modelo": "Modèle",
        "mae": "MAE",
        "mse": "MSE",
        "r2": "R²",
        "tiempo": "⏱️ Temps (s)",

        # --- Graphiques ---
        "graficos_pred_vs_real": "📉 Prédictions vs. Valeurs Réelles",
        "pred_vs_real_titulo": "Prédit vs. Réel",
        "valor_real": "Valeur Réelle",
        "valor_predicho": "Valeur Prédite",

        # --- Tests Statistiques ---
        "theil": "📐 Coefficient U de Theil",
        "diebold": "🧪 Test de Diebold-Mariano",
        "comparacion": "Comparaison",
        "estadistico_dm": "Statistique DM",
        "valor_p": "Valeur p",
    },
    "it": {
        # --- Sezioni Generali ---
        "titulo": "📊 Rapporto Comparativo dei Modelli Predittivi",
        "intro": "Questo rapporto presenta un'analisi comparativa di vari modelli predittivi addestrati per stimare il tempo di produzione.",
        "detalles_maquina": "🖥️ Specifiche del Computer",
        "visualizaciones": "📈 Visualizzazioni dell'Analisi Esplorativa dei Dati (EDA)",
        "preprocesamiento": "⚙️ Pre-elaborazione dei Dati",
        "descripcion_preprocesamiento": "Sono state applicate tecniche di pulizia, codifica di variabili categoriali (One-Hot Encoding) e scalatura delle caratteristiche (StandardScaler) per preparare i dati prima dell'addestramento.",
        "conclusion": "📌 Conclusione",
        "texto_conclusion": "Dopo aver analizzato le metriche di performance, i test statistici e i tempi di addestramento, il modello con le migliori prestazioni complessive, considerando l'equilibrio tra accuratezza ed efficienza, è stato: {modelo}.",

        # --- Metriche e Tabelle ---
        "metricas": "📏 Metriche di Valutazione dei Modelli",
        "modelo": "Modello",
        "mae": "MAE",
        "mse": "MSE",
        "r2": "R²",
        "tiempo": "⏱️ Tempo (s)",

        # --- Grafici ---
        "graficos_pred_vs_real": "📉 Previsioni vs. Valori Reali",
        "pred_vs_real_titulo": "Previsto vs. Reale",
        "valor_real": "Valore Reale",
        "valor_predicho": "Valore Previsto",

        # --- Test Statistici ---
        "theil": "📐 Coefficiente U di Theil",
        "diebold": "🧪 Test di Diebold-Mariano",
        "comparacion": "Confronto",
        "estadistico_dm": "Statistica DM",
        "valor_p": "Valore p",
    },
}