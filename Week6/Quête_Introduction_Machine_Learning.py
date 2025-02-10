import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVR
from sklearn.linear_model import SGDRegressor, LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



# URL del archivo CSV
url_main = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather_main_2018.csv"
url_opinion = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather_opinion_2018.csv"
# Crear el DataFrame
df_main= pd.read_csv(url_main)
df_opinion = pd.read_csv(url_opinion)

# Mostrar las primeras filas del DataFrame
df_main.head()
df_opinion.head()
df_main = df_main.rename(columns={'DATE': 'date'})


df_merge = pd.merge(df_opinion, df_main, on="date", how= 'right')

df_manquants = df_merge[df_merge.isnull().any(axis=1)]

numeric_df = df_merge.select_dtypes(include=[np.number])
correlation = numeric_df.corr()['SUNHOUR'].abs()
correlation_filtered = correlation[correlation >= 0.5]

# Exclure la colonne cible 'SUNHOUR' elle-même
correlation_filtered.drop('SUNHOUR')

# Séparer les données en X (features) et y (target)
X = numeric_df[correlation_filtered]
y = numeric_df['SUNHOUR']

# Diviser les données en train et test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
