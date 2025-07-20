# utils/lang/textos_prediccion_ui.py

"""
Módulo de internacionalización (i18n) para la interfaz de usuario de la página de predicción.

Este archivo contiene un diccionario `TEXTOS_PREDICCION_UI` con los textos utilizados
en la UI de Streamlit para la predicción, disponibles en varios idiomas.
"""

TEXTOS_PREDICCION_UI = {
    "titulo_app": {
        "es": "🛠️ Predicción del Tiempo de Producción",
        "en": "🛠️ Production Time Prediction",
        "pt": "🛠️ Previsão do Tempo de Produção",
        "fr": "🛠️ Prédiction du Temps de Production",
        "it": "🛠️ Previsione del Tempo de Produzione"
    },
    "intro_app": {
        "es": """
        Bienvenido a la herramienta de predicción del tiempo de producción. Aquí podrá ingresar los parámetros clave
        de su proceso y obtener una estimación del tiempo de producción utilizando diferentes modelos de Machine Learning.
        Al finalizar, podrá descargar un reporte PDF con la predicción y una recomendación de recogida del producto.
        """,
        "en": """
        Welcome to the production time prediction tool. Here you can enter key parameters
        of your process and get an estimate of the production time using different Machine Learning models.
        Finally, you can download a PDF report with the prediction and a product collection recommendation.
        """,
        "pt": """
        Bem-vindo à ferramenta de previsão do tempo de produção. Aqui você pode inserir os parâmetros chave
        do seu processo e obter uma estimativa do tempo de produção usando diferentes modelos de Machine Learning.
        Finalmente, você pode baixar um relatório PDF com a previsão e uma recomendação de coleta do produto.
        """,
        "fr": """
        Bienvenue dans l'outil de prédiction du temps de production. Ici, vous pouvez entrer les paramètres clés
        de votre processus et obtenir une estimation du temps de production à l'aide de différents modèles d'apprentissage automatique.
        Enfin, vous pouvez télécharger un rapport PDF avec la prédiction et une recommandation de collecte du produit.
        """,
        "it": """
        Benvenuto nello strumento di previsione del tempo di produzione. Qui puoi inserire i parametri chiave
        del tuo processo e ottenere una stima del tempo di produzione utilizzando diversi modelli di Machine Learning.
        Infine, puoi scaricare un rapporto PDF con la previsione e una raccomandazione per il ritiro del prodotto.
        """
    },
    "error_carga_modelos": {
        "es": "Error al cargar los modelos o el escalador. Asegúrese de que los archivos existan y estén accesibles:",
        "en": "Error loading models or scaler. Make sure files exist and are accessible:",
        "pt": "Erro ao carregar modelos ou escalador. Certifique-se de que os arquivos existam e estejam acessíveis:",
        "fr": "Erreur lors du chargement des modèles ou du scaler. Assurez-vous que les fichiers existent et sont accessibles :",
        "it": "Errore durante il caricamento dei modelli o dello scaler. Assicurati che i file esistano e siano accessibili:"
    },
    "configuracion_prediccion": {
        "es": "⚙️ Configuración de la Predicción",
        "en": "⚙️ Prediction Configuration",
        "pt": "⚙️ Configuração da Previsão",
        "fr": "⚙️ Configuration de la Prédiction",
        "it": "⚙️ Configurazione della Previsione"
    },
    "seleccione_modelo": {
        "es": "**Seleccione el Modelo de Predicción:**",
        "en": "**Select Prediction Model:**",
        "pt": "**Selecione o Modelo de Previsão:**",
        "fr": "**Sélectionnez le Modèle de Prédiction :**",
        "it": "**Seleziona il Modello di Previsione:**"
    },
    "help_modelo": {
        "es": "Elija el modelo de Machine Learning que desea utilizar para la estimación del tiempo.",
        "en": "Choose the Machine Learning model you want to use for time estimation.",
        "pt": "Escolha o modelo de Machine Learning que deseja usar para a estimativa de tempo.",
        "fr": "Choisissez le modèle d'apprentissage automatique que vous souhaitez utiliser para l'estimation du temps.",
        "it": "Scegli il modello di Machine Learning che desideri utilizzare per la stima del tempo."
    },
    "ingrese_parametros": {
        "es": "✏️ Ingrese los Parámetros del Proceso",
        "en": "✏️ Enter Process Parameters",
        "pt": "✏️ Insira os Parâmetros do Processo",
        "fr": "✏️ Entrez les Paramètres du Processus",
        "it": "✏️ Inserisci i Parametri del Processo"
    },
    "ajuste_parametros": {
        "es": "Ajuste los valores de los parámetros que influyen en el tiempo de producción.",
        "en": "Adjust the values of the parameters that influence production time.",
        "pt": "Ajuste os valores dos parâmetros que influenciam o tempo de produção.",
        "fr": "Ajustez les valeurs des paramètres qui influencent le temps de production.",
        "it": "Regola i valori dei parametri che influenzano il tempo de produzione."
    },
    "parametros_produccion": {
        "es": "#### 🏭 Parámetros de Producción",
        "en": "#### 🏭 Production Parameters",
        "pt": "#### 🏭 Parâmetros de Produção",
        "fr": "#### 🏭 Paramètres de Production",
        "it": "#### 🏭 Parametri di Produzione"
    },
    "help_machine_id": {
        "es": "Identificador único de la máquina utilizada.",
        "en": "Unique identifier of the machine used.",
        "pt": "Identificador único da máquina utilizada.",
        "fr": "Identifiant unique de la machine utilisée.",
        "it": "Identificatore unico della macchina utilizzata."
    },
    "help_units_produced": {
        "es": "Número de unidades fabricadas en el ciclo de producción.",
        "en": "Number of units manufactured in the production cycle.",
        "pt": "Número de unidades fabricadas no ciclo de produção.",
        "fr": "Nombre d'unités fabriquées dans le cycle de production.",
        "it": "Numero di unità prodotte nel ciclo di produzione."
    },
    "help_operator_count": {
        "es": "Número de operarios asignados a la máquina.",
        "en": "Number of operators assigned to the machine.",
        "pt": "Número de operadores atribuídos à máquina.",
        "fr": "Nombre d'opérateurs affectés à la machine.",
        "it": "Numero di operatori assegnati alla macchina."
    },
    "parametros_calidad_ambiente": {
        "es": "#### 🌡️ Parámetros de Calidad y Ambiente",
        "en": "#### 🌡️ Quality and Environment Parameters",
        "pt": "#### 🌡️ Parâmetros de Qualidade e Ambiente",
        "fr": "#### 🌡️ Paramètres de Qualité et d'Environnement",
        "it": "#### 🌡️ Parametri di Qualità e Ambiente"
    },
    "help_scrap_rate": {
        "es": "Porcentaje de material desechado durante la producción (entre 0 y 1).",
        "en": "Percentage of material discarded during production (between 0 and 1).",
        "pt": "Porcentagem de material descartado durante a produção (entre 0 e 1).",
        "fr": "Pourcentage de matériau rejeté pendant la production (entre 0 et 1).",
        "it": "Percentuale di materiale scartato durante la produzione (tra 0 e 1)."
    },
    "help_quality_checks_failed": {
        "es": "Número de controles de calidad que no pasaron la inspección.",
        "en": "Number of quality checks that failed inspection.",
        "pt": "Número de verificações de qualidade que falharam na inspeção.",
        "fr": "Nombre de contrôles qualité ayant échoué à l'inspection.",
        "it": "Numero di controlli qualità falliti."
    },
    "help_avg_temp_c": {
        "es": "Temperatura promedio en el área de producción en grados Celsius.",
        "en": "Average temperature in the production area in Celsius degrees.",
        "pt": "Temperatura média na área de produção em graus Celsius.",
        "fr": "Température moyenne dans la zone de production en degrés Celsius.",
        "it": "Temperatura media nell'area di produzione in gradi Celsius."
    },
    "help_avg_humidity_percent": {
        "es": "Humedad promedio en el área de producción en porcentaje.",
        "en": "Average humidity in the production area in percentage.",
        "pt": "Umidade média na área de produção em porcentagem.",
        "fr": "Humidité moyenne dans la zone de production en pourcentage.",
        "it": "Umidità media nell'area di produzione in percentuale."
    },
    "help_labour_cost_per_hour": {
        "es": "Costo de la mano de obra por hora en la moneda local (S/.).",
        "en": "Labor cost per hour in local currency (S/.).",
        "pt": "Custo da mão de obra por hora na moeda local (S/.).",
        "fr": "Coût de la main-d'œuvre par heure en monnaie locale (S/.).",
        "it": "Costo del lavoro per ora in valuta locale (S/.)."
    },
    "tipo_producto_turno": {
        "es": "#### 📦 Tipo de Producto y Turno",
        "en": "#### 📦 Product Type and Shift",
        "pt": "#### 📦 Tipo de Produto e Turno",
        "fr": "#### 📦 Type de Produit et Quart",
        "it": "#### 📦 Tipo di Prodotto e Turno"
    },
    "tipo_producto_label": {
        "es": "**Tipo de Producto:**",
        "en": "**Product Type:**",
        "pt": "**Tipo de Produto:**",
        "fr": "**Type de Produit :**",
        "it": "**Tipo di Prodotto:**"
    },
    "help_tipo_producto": {
        "es": "Categoría del producto que se está fabricando.",
        "en": "Category of the product being manufactured.",
        "pt": "Categoria do produto que está sendo fabricado.",
        "fr": "Catégorie du produit en cours de fabrication.",
        "it": "Categoria del prodotto in fase di produzione."
    },
    "turno_label": {
        "es": "**Turno de Producción:**",
        "en": "**Production Shift:**",
        "pt": "**Turno de Produção:**",
        "fr": "**Quart de Production :**",
        "it": "**Turno di Produzione:**"
    },
    "help_turno": {
        "es": "Turno en el que se realiza la producción (Día, Tarde, Noche).",
        "en": "Shift in which production takes place (Day, Afternoon, Night).",
        "pt": "Turno em que a produção ocorre (Dia, Tarde, Noite).",
        "fr": "Quart pendant lequel la production a lieu (Jour, Après-midi, Nuit).",
        "it": "Turno in cui avviene la produzione (Giorno, Pomeriggio, Notte)."
    },
    "boton_predecir": {
        "es": "🔍 Predecir Tiempo de Producción",
        "en": "🔍 Predict Production Time",
        "pt": "🔍 Prever Tempo de Produção",
        "fr": "🔍 Prédire le Temps de Production",
        "it": "🔍 Prevedi il Tempo di Produzione"
    },
    "prediccion_exitosa": {
        "es": "✅ **Predicción Exitosa:** El tiempo estimado de producción con **{modelo}** es de **{tiempo:.2f} horas**.",
        "en": "✅ **Prediction Successful:** Estimated production time with **{modelo}** is **{tiempo:.2f} hours**.",
        "pt": "✅ **Previsão Bem-Sucedida:** O tempo estimado de produção com **{modelo}** é de **{tiempo:.2f} horas**.",
        "fr": "✅ **Prédiction Réussie :** Le temps de production estimé avec **{modelo}** est de **{tiempo:.2f} heures**.",
        "it": "✅ **Previsione Riuscita:** Il tempo di produzione stimato con **{modelo}** è de **{tiempo:.2f} ore**."
    },
    "reporte_pdf_titulo": {
        "es": "📄 Reporte de Predicción",
        "en": "📄 Prediction Report",
        "pt": "📄 Relatório de Previsão",
        "fr": "📄 Rapport de Prédiction",
        "it": "📄 Report di Previsione"
    },
    "info_descarga_pdf": {
        "es": "Haga clic en el botón para generar y descargar un reporte PDF detallado con la predicción y una recomendación de recogida.",
        "en": "Click the button to generate and download a detailed PDF report with the prediction and a collection recommendation.",
        "pt": "Clique no botão para gerar e baixar um relatório PDF detalhado com a previsão e uma recomendação de coleta.",
        "fr": "Cliquez sur le bouton pour générer et télécharger un rapport PDF détaillé avec la prédiction et une recommandation de collecte.",
        "it": "Fai clic sul pulsante per generare e scaricare un report PDF dettagliato con la previsione e una raccomandazione di ritiro."
    },
    "boton_descargar_pdf": {
        "es": "⬇️ Descargar Reporte de Predicción",
        "en": "⬇️ Download Prediction Report",
        "pt": "⬇️ Baixar Relatório de Previsão",
        "fr": "⬇️ Télécharger le Rapport de Prédiction",
        "it": "⬇️ Scarica Report di Previsione"
    },
    "error_generar_pdf": {
        "es": "❌ **Error al generar el PDF:** {error}. Por favor, intente de nuevo o contacte al soporte.",
        "en": "❌ **Error generating PDF:** {error}. Please try again or contact support.",
        "pt": "❌ **Erro ao gerar o PDF:** {error}. Por favor, tente novamente ou entre em contato com o suporte.",
        "fr": "❌ **Erreur lors de la génération du PDF :** {error}. Veuillez réessayer ou contacter le support.",
        "it": "❌ **Errore durante la generazione del PDF:** {error}. Per favore, riprova o contatta il supporto."
    },
    "seleccione_idioma": {
        "es": "Seleccione el idioma:",
        "en": "Select language:",
        "pt": "Selecione o idioma:",
        "fr": "Sélectionnez la langue :",
        "it": "Seleziona la lingua:"
    }
    # Las opciones de idioma como "es_option", "en_option" se eliminan de aquí
    # ya que no son textos que se traducen dinámicamente en el bucle T = {...}
}
