# utils/lang/textos_comparacion_ui.py

"""
Módulo de internacionalización (i18n) para la interfaz de usuario de la página de comparación de modelos.

Este archivo contiene un diccionario `TEXTOS_COMPARACION_UI` con los textos utilizados
en la UI de Streamlit para la comparación de modelos, disponibles en varios idiomas.
"""

TEXTOS_COMPARACION_UI = {
    "titulo_app": {
        "es": "📊 Comparación de Modelos de Predicción",
        "en": "📊 Prediction Models Comparison",
        "pt": "📊 Comparação de Modelos de Previsão",
        "fr": "📊 Comparaison des Modèles de Prédiction",
        "it": "📊 Confronto Modelli di Previsione"
    },
    "intro_app": {
        "es": """
        Esta sección presenta una comparación detallada del rendimiento de los modelos individuales
        (Red Neuronal ANN, Random Forest, XGBoost) y el Modelo Híbrido. Podrá analizar métricas clave
        y pruebas estadísticas para entender cuál modelo ofrece el mejor desempeño.
        """,
        "en": """
        This section provides a detailed comparison of the performance of individual models
        (ANN, Random Forest, XGBoost) and the Hybrid Model. You can analyze key metrics
        and statistical tests to understand which model offers the best performance.
        """,
        "pt": """
        Esta seção apresenta uma comparação detalhada do desempenho dos modelos individuais
        (Rede Neural ANN, Random Forest, XGBoost) e do Modelo Híbrido. Você pode analisar métricas chave
        e testes estatísticos para entender qual modelo oferece o melhor desempenho.
        """,
        "fr": """
        Cette section présente une comparaison détaillée des performances des modèles individuels
        (Réseau de Neurones ANN, Random Forest, XGBoost) et du Modèle Hybride. Vous pourrez analyser les métriques clés
        et les tests statistiques pour comprendre quel modèle offre les meilleures performances.
        """,
        "it": """
        Questa sezione presenta un confronto dettagliato delle prestazioni dei singoli modelli
        (Rete Neurale ANN, Random Forest, XGBoost) e del Modello Ibrido. È possibile analizzare le metriche chiave
        e i test statistici per capire quale modello offre le migliori prestazioni.
        """
    },
    "error_carga_modelos": {
        "es": "Error al cargar los modelos o los datos de prueba. Asegúrese de que los archivos existan y estén accesibles:",
        "en": "Error loading models or test data. Make sure files exist and are accessible:",
        "pt": "Erro ao carregar modelos ou dados de teste. Certifique-se de que os arquivos existam e estejam acessíveis:",
        "fr": "Erreur lors du chargement des modèles ou des données de test. Assurez-vous que les fichiers existent et sont accessibles :",
        "it": "Errore durante il caricamento dei modelli o dei dati di test. Assicurati che i file esistano e siano accessibili:"
    },
    "error_carga_hibrido": {
        "es": "Advertencia: No se pudo cargar el Modelo Híbrido. Asegúrese de haberlo entrenado y guardado previamente en la página de 'Entrenamiento de Modelo Híbrido'.",
        "en": "Warning: Could not load the Hybrid Model. Make sure you have trained and saved it previously on the 'Hybrid Model Training' page.",
        "pt": "Aviso: Não foi possível carregar o Modelo Híbrido. Certifique-se de tê-lo treinado e salvo anteriormente na página 'Treinamento de Modelo Híbrido'.",
        "fr": "Avertissement : Impossible de charger le Modèle Hybride. Assurez-vous de l'avoir entraîné et enregistré précédemment sur la page 'Entraînement du Modèle Hybride'.",
        "it": "Avviso: Impossibile caricare il Modello Ibrido. Assicurati di averlo addestrato e salvato in precedenza nella pagina 'Addestramento Modello Ibrido'."
    },
    "metricas_rendimiento": {
        "es": "📐 Métricas de Rendimiento",
        "en": "📐 Performance Metrics",
        "pt": "📐 Métricas de Desempenho",
        "fr": "📐 Métriques de Performance",
        "it": "📐 Metriche di Prestazione"
    },
    "col_modelo": {
        "es": "Modelo",
        "en": "Model",
        "pt": "Modelo",
        "fr": "Modèle",
        "it": "Modello"
    },
    "col_mae": {
        "es": "MAE",
        "en": "MAE",
        "pt": "MAE",
        "fr": "MAE",
        "it": "MAE"
    },
    "col_mse": {
        "es": "MSE",
        "en": "MSE",
        "pt": "MSE",
        "fr": "MSE",
        "it": "MSE"
    },
    "col_r2": {
        "es": "R²",
        "en": "R²",
        "pt": "R²",
        "fr": "R²",
        "it": "R²"
    },
    "coeficiente_theil": {
        "es": "📉 Coeficiente U de Theil",
        "en": "📉 Theil's U Coefficient",
        "pt": "📉 Coeficiente U de Theil",
        "fr": "📉 Coefficient U de Theil",
        "it": "📉 Coefficiente U di Theil"
    },
    "info_theil": {
        "es": "El coeficiente U de Theil mide la precisión de la predicción. Valores más cercanos a 0 indican mayor precisión. Un valor de 0 indica una predicción perfecta, mientras que 1 indica que el modelo no es mejor que una predicción ingenua.",
        "en": "Theil's U coefficient measures prediction accuracy. Values closer to 0 indicate higher accuracy. A value of 0 indicates perfect prediction, while 1 indicates the model is no better than a naive forecast.",
        "pt": "O coeficiente U de Theil mede a precisão da previsão. Valores mais próximos de 0 indicam maior precisão. Um valor de 0 indica uma previsão perfeita, enquanto 1 indica que o modelo não é melhor que uma previsão ingênua.",
        "fr": "Le coefficient U de Theil mesure la précision de la prédiction. Des valores plus proches de 0 indiquent une plus grande précision. Une valeur de 0 indique une prédiction parfaite, tandis que 1 indique que le modèle n'est pas meilleur qu'une prévision naïve.",
        "it": "Il coefficiente U di Theil misura l'accuratezza della previsione. Valori più vicini a 0 indicano maggiore accuratezza. Un valore di 0 indica una previsione perfetta, mentre 1 indica che il modello non è migliore di una previsione ingenua."
    },
    "col_utheil": {
        "es": "U de Theil",
        "en": "Theil's U",
        "pt": "U de Theil",
        "fr": "U de Theil",
        "it": "U di Theil"
    },
    "prueba_dm": {
        "es": "📊 Prueba de Diebold-Mariano vs Híbrido",
        "en": "📊 Diebold-Mariano Test vs Hybrid",
        "pt": "📊 Teste de Diebold-Mariano vs Híbrido",
        "fr": "📊 Test de Diebold-Mariano vs Hybride",
        "it": "📊 Test di Diebold-Mariano vs Ibrido"
    },
    "info_dm": {
        "es": "La prueba de Diebold-Mariano evalúa si hay una diferencia estadísticamente significativa en la precisión de las predicciones entre dos modelos. Un valor *p* bajo (típicamente < 0.05) sugiere que la diferencia es significativa.",
        "en": "The Diebold-Mariano test evaluates whether there is a statistically significant difference in prediction accuracy between two models. A low *p*-value (typically < 0.05) suggests that the difference is significant.",
        "pt": "O teste de Diebold-Mariano avalia se há uma diferença estatisticamente significativa na precisão das previsões entre dois modelos. Um valor *p* baixo (tipicamente < 0.05) sugere que a diferença é significativa.",
        "fr": "Le test de Diebold-Mariano évalue s'il existe une différence statistiquement significative dans la précision des prédictions entre deux modèles. Une faible valeur *p* (généralement < 0.05) suggère que la différence est significative.",
        "it": "Il test di Diebold-Mariano valuta se esiste una differenza statisticamente significativa nell'accuratezza delle previsioni tra due modelli. Un valor *p* basso (tipicamente < 0.05) suggerisce que la differenza è significativa."
    },
    "col_comparacion": {
        "es": "Comparación",
        "en": "Comparison",
        "pt": "Comparação",
        "fr": "Comparaison",
        "it": "Confronto"
    },
    "col_estadistico_dm": {
        "es": "Estadístico DM",
        "en": "DM Statistic",
        "pt": "Estatística DM",
        "fr": "Statistique DM",
        "it": "Statistica DM"
    },
    "col_valor_p": {
        "es": "Valor p",
        "en": "p-value",
        "pt": "Valor p",
        "fr": "Valeur p",
        "it": "Valore p"
    },
    "dm_resultado_significativo": {
        "es": "    La diferencia en la precisión entre {nombre_modelo} y el modelo Híbrido es estadísticamente significativa (p < 0.05).",
        "en": "    The difference in accuracy between {nombre_modelo} and the Hybrid model is statistically significant (p < 0.05).",
        "pt": "    A diferença na precisão entre {nombre_modelo} e o modelo Híbrido é estatisticamente significativa (p < 0.05).",
        "fr": "    La différence de précision entre {nombre_modelo} et le modèle Hybride est statistiquement significative (p < 0.05).",
        "it": "    La differenza di accuratezza tra {nombre_modelo} e il modello Ibrido è statisticamente significativa (p < 0.05)."
    },
    "dm_resultado_no_significativo": {
        "es": "    No hay una diferencia estadísticamente significativa en la precisión entre {nombre_modelo} y el modelo Híbrido (p >= 0.05).",
        "en": "    There is no statistically significant difference in accuracy between {nombre_modelo} and the Hybrid model (p >= 0.05).",
        "pt": "    Não há uma diferença estadisticamente significativa na precisão entre {nombre_modelo} e o modelo Híbrido (p >= 0.05).",
        "fr": "    Il n'y a pas de différence statistiquement significative dans la précision entre {nombre_modelo} et le modèle Hybride (p >= 0.05).",
        "it": "    Non c'è una differenza statisticamente significativa nell'accuratezza tra {nombre_modelo} e il modello Ibrido (p >= 0.05)."
    },
    "dm_error": {
        "es": "    No se pudo realizar la prueba Diebold-Mariano para {nombre_modelo} vs Híbrido: {error}",
        "en": "    Could not perform Diebold-Mariano test for {nombre_modelo} vs Hybrid: {error}",
        "pt": "    Não foi possível realizar o teste Diebold-Mariano para {nombre_modelo} vs Híbrido: {error}",
        "fr": "    Impossible d'effectuer le test de Diebold-Mariano pour {nombre_modelo} vs Hybride : {error}",
        "it": "    Impossibile eseguire il test di Diebold-Mariano per {nombre_modelo} vs Ibrido: {error}"
    },
    "nota_informativa_p_value": {
        "es": "📌 Un valor *p* < 0.05 indica una diferencia estadísticamente significativa entre los modelos comparados.",
        "en": "📌 A *p*-value < 0.05 indicates a statistically significant difference between the compared models.",
        "pt": "📌 Um valor *p* < 0.05 indica uma diferença estatisticamente significativa entre os modelos comparados.",
        "fr": "📌 Une valeur *p* < 0.05 indica una diferencia estadísticamente significativa entre les modèles comparés.",
        "it": "📌 Un valor *p* < 0.05 indica una differenza statisticamente significativa entre i modelli confrontati."
    },
    "opciones_idioma": {
        "es": "⚙️ Opciones de Idioma",
        "en": "⚙️ Language Options",
        "pt": "⚙️ Opções de Idioma",
        "fr": "⚙️ Options de Langue",
        "it": "⚙️ Opzioni Lingua"
    },
    "seleccione_idioma_label": {
        "es": "Seleccione el idioma:",
        "en": "Select language:",
        "pt": "Selecione o idioma:",
        "fr": "Sélectionnez la langue :",
        "it": "Seleziona la lingua:"
    },
    # Nuevas claves para la sección de generación de PDF
    "generar_reporte_pdf_seccion_titulo": {
        "es": "📄 Generar Reporte PDF",
        "en": "📄 Generate PDF Report",
        "pt": "📄 Gerar Relatório PDF",
        "fr": "📄 Générer Rapport PDF",
        "it": "📄 Genera Report PDF"
    },
    "generar_reporte_pdf_info": {
        "es": "Haz clic en el botón para descargar un reporte PDF completo con todas las métricas y comparaciones.",
        "en": "Click the button to download a complete PDF report with all metrics and comparisons.",
        "pt": "Clique no botão para baixar um relatório PDF completo com todas as métricas e comparações.",
        "fr": "Cliquez sur le bouton pour télécharger un rapport PDF complet avec toutes les métriques et comparaisons.",
        "it": "Fai clic sul pulsante per scaricare un report PDF completo con tutte le metriche e i confronti."
    },
    "boton_descargar_reporte_comparacion_pdf": {
        "es": "⬇️ Descargar Reporte de Comparación (PDF)",
        "en": "⬇️ Download Comparison Report (PDF)",
        "pt": "⬇️ Baixar Relatório de Comparação (PDF)",
        "fr": "⬇️ Télécharger Rapport de Comparaison (PDF)",
        "it": "⬇️ Scarica Report di Confronto (PDF)"
    },
    "pdf_generado_exito": {
        "es": "✅ Reporte PDF generado y listo para descargar.",
        "en": "✅ PDF report generated and ready for download.",
        "pt": "✅ Relatório PDF gerado e pronto para download.",
        "fr": "✅ Rapport PDF généré et prêt à être téléchargé.",
        "it": "✅ Report PDF generato e pronto per il download."
    },
    "pdf_error_generacion": {
        "es": "❌ Error al generar el PDF: {error}. Por favor, intente de nuevo.",
        "en": "❌ Error generating PDF: {error}. Please try again.",
        "pt": "❌ Erro ao gerar o PDF: {error}. Por favor, tente novamente.",
        "fr": "❌ Erreur lors de la génération du PDF : {error}. Veuillez réessayer.",
        "it": "❌ Errore durante la generazione del PDF: {error}. Per favore, riprova."
    }
}
