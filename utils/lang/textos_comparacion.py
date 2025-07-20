# utils/lang/textos_comparacion.py

TEXTOS_COMPARACION = {
    "titulo": {
        "es": "📊 Comparación de Modelos de Predicción",
        "en": "📊 Prediction Model Comparison",
        "pt": "📊 Comparação de Modelos de Previsão",
        "fr": "📊 Comparaison des Modèles de Prédiction",
        "it": "📊 Confronto dei Modelli di Previsione"
    },
    "introduccion": {
        "es": """
        Esta aplicación interactiva permite comparar el rendimiento de diferentes modelos de aprendizaje automático 
        para la predicción. Podrás visualizar métricas clave, evaluar la significancia estadística de las diferencias 
        entre modelos y generar un reporte PDF detallado con todos los resultados.
        """,
        "en": """
        This interactive application allows you to compare the performance of different machine learning models 
        for prediction. You will be able to visualize key metrics, evaluate the statistical significance of differences 
        between models, and generate a detailed PDF report with all the results.
        """,
        "pt": """
        Este aplicativo interativo permite comparar o desempenho de diferentes modelos de aprendizado de máquina 
        para previsão. Você poderá visualizar métricas chave, avaliar a significância estatística das diferenças 
        entre os modelos e gerar um relatório PDF detalhado com todos os resultados.
        """,
        "fr": """
        Cette application interactive permet de comparer les performances de différents modèles d'apprentissage automatique 
        pour la prédiction. Vous pourrez visualiser les métriques clés, évaluer la signification statistique des différences 
        entre les modèles et générer un rapport PDF détaillé avec tous les résultats.
        """,
        "it": """
        Questa applicazione interattiva consente di confrontare le prestazioni di diversi modelli di machine learning 
        per la previsione. Sarai in grado di visualizzare le metriche chiave, valutare la significatività statistica delle differenze 
        tra i modelli e generare un rapporto PDF dettagliato con tutti i risultati.
        """
    },
    "subtitulo_metricas": {
        "es": "Métricas de Rendimiento del Modelo",
        "en": "Model Performance Metrics",
        "pt": "Métricas de Desempenho do Modelo",
        "fr": "Métriques de Performance du Modèle",
        "it": "Metriche di Prestazione del Modello"
    },
    "subtitulo_theils_u": {
        "es": "Coeficiente U de Theil",
        "en": "Theil's U Coefficient",
        "pt": "Coeficiente U de Theil",
        "fr": "Coefficient U de Theil",
        "it": "Coefficiente U di Theil"
    },
    "subtitulo_dm": {
        "es": "Prueba de Diebold-Mariano",
        "en": "Diebold-Mariano Test",
        "pt": "Teste de Diebold-Mariano",
        "fr": "Test de Diebold-Mariano",
        "it": "Test di Diebold-Mariano"
    },
    "dm_info": {
        "es": """
        La prueba de Diebold-Mariano evalúa si hay una diferencia estadísticamente significativa en la precisión de 
        las predicciones entre dos modelos. Un valor p bajo (típicamente < 0.05) sugiere que la diferencia es significativa.
        """,
        "en": """
        The Diebold-Mariano test assesses whether there is a statistically significant difference in prediction accuracy 
        between two models. A low p-value (typically < 0.05) suggests that the difference is significant.
        """,
        "pt": """
        O teste de Diebold-Mariano avalia se existe uma diferença estatisticamente significativa na precisão das 
        previsões entre dois modelos. Um valor p baixo (tipicamente < 0.05) sugere que a diferença é significativa.
        """,
        "fr": """
        Le test de Diebold-Mariano évalue s'il existe une différence statistiquement significative dans la précision 
        des prédictions entre deux modèles. Une faible valeur p (généralement < 0.05) suggère que la différence est significative.
        """,
        "it": """
        Il test di Diebold-Mariano valuta se esiste una differenza statisticamente significativa nell'accuratezza 
        delle previsioni tra due modelli. Un valore p basso (tipicamente < 0.05) suggerisce che la differenza è significativa.
        """
    },
    "generar_pdf": {
        "es": "Generar Reporte PDF",
        "en": "Generate PDF Report",
        "pt": "Gerar Relatório PDF",
        "fr": "Générer un Rapport PDF",
        "it": "Genera Report PDF"
    },
    "pdf_desc": {
        "es": "Haz clic en el botón para generar un reporte PDF completo con todos los resultados de la comparación.",
        "en": "Click the button to generate a comprehensive PDF report with all comparison results.",
        "pt": "Clique no botão para gerar um relatório PDF completo com todos os resultados da comparação.",
        "fr": "Cliquez sur le bouton pour générer un rapport PDF complet avec tous les résultats de la comparaison.",
        "it": "Fai clic sul pulsante per generare un report PDF completo con tutti i risultati del confronto."
    },
    "boton_generar": {
        "es": "Generar PDF",
        "en": "Generate PDF",
        "pt": "Gerar PDF",
        "fr": "Générer PDF",
        "it": "Genera PDF"
    },
    "generando": {
        "es": "Generando reporte PDF...",
        "en": "Generating PDF report...",
        "pt": "Gerando relatório PDF...",
        "fr": "Génération du rapport PDF...",
        "it": "Generazione report PDF..."
    },
    "exito": {
        "es": "¡Reporte PDF generado exitosamente!",
        "en": "PDF report generated successfully!",
        "pt": "Relatório PDF gerado com sucesso!",
        "fr": "Rapport PDF généré avec succès !",
        "it": "Report PDF generato con successo!"
    },
    "descargar": {
        "es": "Descargar Reporte PDF",
        "en": "Download PDF Report",
        "pt": "Baixar Relatório PDF",
        "fr": "Télécharger le Rapport PDF",
        "it": "Scarica Report PDF"
    },
    "error": {
        "es": "Ocurrió un error al generar el PDF",
        "en": "An error occurred while generating the PDF",
        "pt": "Ocorreu um erro ao gerar o PDF",
        "fr": "Une erreur est survenue lors de la génération du PDF",
        "it": "Si è verificato un errore durante la generazione del PDF"
    },
    "modelo_col": {
        "es": "Modelo",
        "en": "Model",
        "pt": "Modelo",
        "fr": "Modèle",
        "it": "Modello"
    },
    "comparacion_col": {
        "es": "Comparación",
        "en": "Comparison",
        "pt": "Comparação",
        "fr": "Comparaison",
        "it": "Confronto"
    },
    "estadistico_col": {
        "es": "Estadístico DM",
        "en": "DM Statistic",
        "pt": "Estatística DM",
        "fr": "Statistique DM",
        "it": "Statistica DM"
    },
    "p_valor_col": {
        "es": "Valor p",
        "en": "p-value",
        "pt": "Valor p",
        "fr": "Valeur p",
        "it": "Valore p"
    }
}
