import streamlit as st
import seaborn as sns  # type: ignore
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import des datasets depuis seaborn
datasets = sns.get_dataset_names()
# title de la page
st.title("Manipulation de données et création de graphiques")
# selecbox pour choisir le dataset
choixdataset = st.selectbox("Quel dataset veux-tu utiliser", datasets)
# sauvegarde du dataset choisi et previsualisation du jeux de données
df_selected = sns.load_dataset(choixdataset)

st.write("Aperçu des données :")
st.write(df_selected.head())

# Sélection des colonnes X et Y
numeric_columns = df_selected.select_dtypes(include=[np.number]).columns.tolist()
x_column = st.selectbox("Choisissez la colonne X", numeric_columns)
y_column = st.selectbox("Choisissez la colonne Y", numeric_columns)

# Sélection du graphique
graph_type = st.selectbox("Quel graphique veux-tu utiliser", ["scatter_chart", "bar_chart", "line_chart"])

# Affichage du graphique en fonction du choix de l'utilisateur
if graph_type == "scatter_chart":
    st.subheader("Graphique en nuage de points")
    st.scatter_chart(df_selected[[x_column, y_column]])
elif graph_type == "bar_chart":
    st.subheader("Graphique en barres")
    st.bar_chart(df_selected[[x_column, y_column]])
elif graph_type == "line_chart":
    st.subheader("Graphique en courbes")
    st.line_chart(df_selected[[x_column, y_column]])

# Affichage de la matrice de corrélation (choix utilisateur)
if st.checkbox("Afficher la matrice de corrélation"):
    # pour selectionner que les colonnes numeriques
    numeric_df = df_selected.select_dtypes(include=[np.number])
    
    if numeric_df.shape[1] > 1:  # pour être sure qu'il y a plus d'une colonne numerique
        st.subheader("Ma matrice de corrélation")
        correlation_matrix = numeric_df.corr()

        # graph de la matrice
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
