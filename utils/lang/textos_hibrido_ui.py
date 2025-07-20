# utils/lang/textos_hibrido_ui.py

"""
Módulo de internacionalización (i18n) para la interfaz de usuario de la página de entrenamiento híbrido.

Este archivo contiene un diccionario `TEXTOS_HIBRIDO_UI` con los textos utilizados
en la UI de Streamlit para el entrenamiento híbrido, disponibles en varios idiomas.
"""

TEXTOS_HIBRIDO_UI = {
    "titulo_app": {
        "es": "🔀 Entrenamiento de Modelo Híbrido con Promedio Ponderado",
        "en": "🔀 Hybrid Model Training with Weighted Average",
        "pt": "🔀 Treinamento de Modelo Híbrido com Média Ponderada",
        "fr": "🔀 Entraînement de Modèle Hybride avec Moyenne Pondérée",
        "it": "🔀 Addestramento Modello Ibrido con Media Ponderata"
    },
    "intro_app": {
        "es": """
        Esta sección permite entrenar un modelo híbrido combinando las predicciones de los modelos
        ANN, Random Forest y XGBoost mediante un promedio ponderado. Ajusta los pesos para cada
        modelo y evalúa el rendimiento del modelo híbrido.
        """,
        "en": """
        This section allows training a hybrid model by combining the predictions of ANN,
        Random Forest, and XGBoost models using a weighted average. Adjust the weights for each
        model and evaluate the performance of the hybrid model.
        """,
        "pt": """
        Esta seção permite treinar um modelo híbrido combinando as previsões dos modelos
        ANN, Random Forest e XGBoost por meio de uma média ponderada. Ajuste os pesos para cada
        modelo e avalie o desempenho do modelo híbrido.
        """,
        "fr": """
        Cette section permet d'entraîner un modèle hybride en combinant les prédictions des modèles
        ANN, Random Forest et XGBoost par une moyenne pondérée. Ajustez les poids pour chaque
        modèle et évaluez les performances du modèle hybride.
        """,
        "it": """
        Questa sezione consente di addestrare un modello ibrido combinando le previsioni dei modelli
        ANN, Random Forest e XGBoost tramite una media ponderata. Regola i pesi per ciascun
        modello e valuta le prestazioni del modello ibrido.
        """
    },
    "error_carga_modelos": {
        "es": "Error al cargar los modelos o los datos de prueba:",
        "en": "Error loading models or test data:",
        "pt": "Erro ao carregar modelos ou dados de teste:",
        "fr": "Erreur lors du chargement des modèles ou des données de test :",
        "it": "Errore durante il caricamento dei modelli o dei dati di test:"
    },
    "asignacion_pesos": {
        "es": "⚖️ Asignación de Pesos a Modelos",
        "en": "⚖️ Model Weight Assignment",
        "pt": "⚖️ Atribuição de Pesos aos Modelos",
        "fr": "⚖️ Attribution des Poids aux Modèles",
        "it": "⚖️ Assegnazione Pesi ai Modelli"
    },
    "ajusta_pesos_info": {
        "es": "Ajusta los pesos para cada modelo. La suma total de los pesos debe ser 1.0.",
        "en": "Adjust the weights for each model. The total sum of weights must be 1.0.",
        "pt": "Ajuste os pesos para cada modelo. A soma total dos pesos deve ser 1.0.",
        "fr": "Ajustez les poids pour chaque modèle. La somme totale des poids doit être 1.0.",
        "it": "Regola i pesi per ciascun modello. La somma totale dei pesi deve essere 1.0."
    },
    "peso_ann": {
        "es": "Peso ANN",
        "en": "ANN Weight",
        "pt": "Peso ANN",
        "fr": "Poids ANN",
        "it": "Peso ANN"
    },
    "help_peso_ann": {
        "es": "Peso para el modelo de Red Neuronal Artificial (ANN).",
        "en": "Weight for the Artificial Neural Network (ANN) model.",
        "pt": "Peso para o modelo de Rede Neural Artificial (ANN).",
        "fr": "Poids pour le modèle de Réseau de Neurones Artificiels (ANN).",
        "it": "Peso per il modello di Rete Neurale Artificiale (ANN)."
    },
    "peso_rf": {
        "es": "Peso RF",
        "en": "RF Weight",
        "pt": "Peso RF",
        "fr": "Poids RF",
        "it": "Peso RF"
    },
    "help_peso_rf": {
        "es": "Peso para el modelo Random Forest.",
        "en": "Weight for the Random Forest model.",
        "pt": "Peso para o modelo Random Forest.",
        "fr": "Poids pour le modèle Random Forest.",
        "it": "Peso per il modello Random Forest."
    },
    "peso_xgb": {
        "es": "Peso XGB",
        "en": "XGB Weight",
        "pt": "Peso XGB",
        "fr": "Poids XGB",
        "it": "Peso XGB"
    },
    "help_peso_xgb": {
        "es": "Peso para el modelo XGBoost.",
        "en": "Weight for the XGBoost model.",
        "pt": "Peso para o modelo XGBoost.",
        "fr": "Poids pour le modèle XGBoost.",
        "it": "Peso per il modello XGBoost."
    },
    "warning_suma_pesos": {
        "es": "⚠️ La suma de los pesos no es exactamente 1.0. Se ajustarán automáticamente al entrenar.",
        "en": "⚠️ The sum of weights is not exactly 1.0. They will be automatically adjusted during training.",
        "pt": "⚠️ A soma dos pesos não é exatamente 1.0. Eles serão ajustados automaticamente durante o treinamento.",
        "fr": "⚠️ La somme des poids n'est pas exactement 1.0. Ils seront ajustés automatiquement lors de l'entraînement.",
        "it": "⚠️ La somma dei pesi non è esattamente 1.0. Verranno regolati automaticamente durante l'addestramento."
    },
    "boton_entrenar": {
        "es": "✅ Entrenar y Evaluar Modelo Híbrido",
        "en": "✅ Train and Evaluate Hybrid Model",
        "pt": "✅ Treinar e Avaliar Modelo Híbrido",
        "fr": "✅ Entraîner et Évaluer le Modèle Hybride",
        "it": "✅ Addestra e Valuta Modello Ibrido"
    },
    "spinner_entrenamiento": {
        "es": "Entrenando y evaluando el modelo híbrido...",
        "en": "Training and evaluating the hybrid model...",
        "pt": "Treinando e avaliando o modelo híbrido...",
        "fr": "Entraînement et évaluation du modèle hybride...",
        "it": "Addestramento e valutazione del modello ibrido..."
    },
    "success_entrenamiento": {
        "es": "✅ Modelo híbrido entrenado y evaluado con éxito.",
        "en": "✅ Hybrid model successfully trained and evaluated.",
        "pt": "✅ Modelo híbrido treinado e avaliado com sucesso.",
        "fr": "✅ Modèle hybride entraîné et évalué avec succès.",
        "it": "✅ Modello ibrido addestrato e valutato con successo."
    },
    "comparacion_theil": {
        "es": "📊 Comparación de U de Theil",
        "en": "📊 Theil's U Comparison",
        "pt": "📊 Comparação do U de Theil",
        "fr": "📊 Comparaison du U de Theil",
        "it": "📊 Confronto del U di Theil"
    },
    "info_theil": {
        "es": "El coeficiente U de Theil mide la precisión de la predicción. Valores más cercanos a 0 indican mayor precisión.",
        "en": "Theil's U coefficient measures prediction accuracy. Values closer to 0 indicate higher accuracy.",
        "pt": "O coeficiente U de Theil mede a precisão da previsão. Valores mais próximos de 0 indicam maior precisão.",
        "fr": "Le coefficient U de Theil mesure la précision de la prédiction. Des valeurs plus proches de 0 indiquent une plus grande précision.",
        "it": "Il coefficiente U di Theil misura l'accuratezza della previsione. Valori più vicini a 0 indicano maggiore accuratezza."
    },
    "col_modelo": {
        "es": "Modelo",
        "en": "Model",
        "pt": "Modelo",
        "fr": "Modèle",
        "it": "Modello"
    },
    "col_utheil": {
        "es": "U de Theil",
        "en": "Theil's U",
        "pt": "U de Theil",
        "fr": "U de Theil",
        "it": "U di Theil"
    },
    "comparacion_metricas": {
        "es": "📈 Comparación de Métricas de Rendimiento",
        "en": "📈 Performance Metrics Comparison",
        "pt": "📈 Comparação de Métricas de Desempenho",
        "fr": "📈 Comparaison des Métriques de Performance",
        "it": "📈 Confronto delle Metriche di Prestazione"
    },
    "info_metricas": {
        "es": "Análisis de las métricas clave: Error Absoluto Medio (MAE), Error Cuadrático Medio (MSE) y Coeficiente de Determinación (R²).",
        "en": "Analysis of key metrics: Mean Absolute Error (MAE), Mean Squared Error (MSE), and Coefficient of Determination (R²).",
        "pt": "Análise das métricas-chave: Erro Absoluto Médio (MAE), Erro Quadrático Médio (MSE) e Coeficiente de Determinação (R²).",
        "fr": "Analyse des métriques clés : Erreur Absolue Moyenne (MAE), Erreur Quadratique Moyenne (MSE) et Coefficient de Détermination (R²).",
        "it": "Analisi delle metriche chiave: Errore Assoluto Medio (MAE), Errore Quadratico Medio (MSE) e Coefficiente di Determinazione (R²)."
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
    "prueba_dm": {
        "es": "📐 Prueba de Diebold-Mariano (DM)",
        "en": "📐 Diebold-Mariano (DM) Test",
        "pt": "📐 Teste de Diebold-Mariano (DM)",
        "fr": "📐 Test de Diebold-Mariano (DM)",
        "it": "📐 Test di Diebold-Mariano (DM)"
    },
    "info_dm": {
        "es": "La prueba de Diebold-Mariano evalúa si hay una diferencia estadísticamente significativa en la precisión de las predicciones entre dos modelos. Un valor p bajo (típicamente < 0.05) sugiere que la diferencia es significativa.",
        "en": "The Diebold-Mariano test evaluates whether there is a statistically significant difference in prediction accuracy between two models. A low p-value (typically < 0.05) suggests that the difference is significant.",
        "pt": "O teste de Diebold-Mariano avalia se há uma diferença estatisticamente significativa na precisão das previsões entre dois modelos. Um valor p baixo (tipicamente < 0.05) sugere que a diferença é significativa.",
        "fr": "Le test de Diebold-Mariano évalue s'il existe une différence statistiquement significative dans la précision des prédictions entre deux modèles. Une faible valeur p (généralement < 0.05) suggère que la différence est significative.",
        "it": "Il test di Diebold-Mariano valuta se esiste una differenza statisticamente significativa nell'accuratezza delle previsioni tra due modelli. Un valore p basso (tipicamente < 0.05) suggerisce che la differenza è significativa."
    },
    "dm_resultado_significativo": {
        "es": "    La diferencia en la precisión entre {nombre} y el modelo Híbrido es estadísticamente significativa (p < 0.05).",
        "en": "    The difference in accuracy between {nombre} and the Hybrid model is statistically significant (p < 0.05).",
        "pt": "    A diferença na precisão entre {nombre} e o modelo Híbrido é estatisticamente significativa (p < 0.05).",
        "fr": "    La différence de précision entre {nombre} et le modèle Hybride est statistiquement significative (p < 0.05).",
        "it": "    La differenza di accuratezza tra {nombre} e il modello Ibrido è statisticamente significativa (p < 0.05)."
    },
    "dm_resultado_no_significativo": {
        "es": "    No hay una diferencia estadísticamente significativa en la precisión entre {nombre} y el modelo Híbrido (p >= 0.05).",
        "en": "    There is no statistically significant difference in accuracy between {nombre} and the Hybrid model (p >= 0.05).",
        "pt": "    Não há uma diferença estatisticamente significativa na precisão entre {nombre} e o modelo Híbrido (p >= 0.05).",
        "fr": "    Il n'y a pas de différence statistiquement significative dans la précision entre {nombre} et le modèle Hybride (p >= 0.05).",
        "it": "    Non c'è una differenza statisticamente significativa nell'accuratezza tra {nombre} e il modello Ibrido (p >= 0.05)."
    },
    "dm_error": {
        "es": "    No se pudo realizar la prueba Diebold-Mariano para {nombre} vs Híbrido: {error}",
        "en": "    Could not perform Diebold-Mariano test for {nombre} vs Hybrid: {error}",
        "pt": "    Não foi possível realizar o teste Diebold-Mariano para {nombre} vs Híbrido: {error}",
        "fr": "    Impossible d'effectuer le test de Diebold-Mariano pour {nombre} vs Hybride : {error}",
        "it": "    Impossibile eseguire il test di Diebold-Mariano per {nombre} vs Ibrido: {error}"
    },
    "guardar_modelo": {
        "es": "💾 Guardar Modelo Híbrido",
        "en": "💾 Save Hybrid Model",
        "pt": "💾 Salvar Modelo Híbrido",
        "fr": "💾 Enregistrer le Modèle Hybride",
        "it": "💾 Salva Modello Ibrido"
    },
    "info_guardar_modelo": {
        "es": "Haz clic en el botón para descargar el modelo híbrido entrenado en tu máquina local.",
        "en": "Click the button to download the trained hybrid model to your local machine.",
        "pt": "Clique no botão para baixar o modelo híbrido treinado para sua máquina local.",
        "fr": "Cliquez sur le bouton pour télécharger le modèle hybride entraîné sur votre machine locale.",
        "it": "Fai clic sul pulsante per scaricare il modello ibrido addestrato sul tuo computer locale."
    },
    "boton_descargar_modelo": {
        "es": "⬇️ Descargar Modelo Híbrido (.pkl)",
        "en": "⬇️ Download Hybrid Model (.pkl)",
        "pt": "⬇️ Baixar Modelo Híbrido (.pkl)",
        "fr": "⬇️ Télécharger le Modèle Hybride (.pkl)",
        "it": "⬇️ Scarica Modello Ibrido (.pkl)"
    },
    "help_descargar_modelo": {
        "es": "Haz clic para descargar el modelo híbrido entrenado.",
        "en": "Click to download the trained hybrid model.",
        "pt": "Clique para baixar o modelo híbrido treinado.",
        "fr": "Cliquez pour télécharger le modèle hybride entraîné.",
        "it": "Fai clic per scaricare il modello ibrido addestrato."
    },
    "info_modelo_listo": {
        "es": "El modelo híbrido está listo para ser descargado.",
        "en": "The hybrid model is ready for download.",
        "pt": "O modelo híbrido está pronto para download.",
        "fr": "Le modèle hybride est prêt à être téléchargé.",
        "it": "Il modello ibrido è pronto per il download."
    },
    "error_preparar_descarga": {
        "es": "Error al preparar el modelo para descarga: {error}",
        "en": "Error preparing model for download: {error}",
        "pt": "Erro ao preparar o modelo para download: {error}",
        "fr": "Erreur lors de la préparation du modèle pour le téléchargement : {error}",
        "it": "Errore durante la preparazione del modello per il download: {error}"
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
    }
}
