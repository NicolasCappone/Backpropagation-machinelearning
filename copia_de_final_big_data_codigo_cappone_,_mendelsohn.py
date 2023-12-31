# -*- coding: utf-8 -*-
"""Copia de Final Big data codigo - Cappone , Mendelsohn

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NasQUFT9YWOXbiI3X1jAMqu9tsTw_Dnv
"""

import pandas as pd
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD
from scipy.stats import ks_2samp
from scipy.stats import gamma
from numpy.random import seed
from numpy.random import poisson
from scipy.stats import kstest
import sklearn.metrics as metrics



# imporatmos dataset
sheet_url = 'https://docs.google.com/spreadsheets/d/1oxOrLEIBqxR8dKASYirv_xWBfImnHSlF/edit#gid=1922845540'
url_1 = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')

# dataset entero
dataset = pd.read_csv(url_1,decimal=',')



nuevodata = dataset

print(nuevodata)

# FILTRAMOS

from sklearn.model_selection import train_test_split

# Dividir los datos en un conjunto de aprendizaje (80%) y un conjunto de testeo (20%)
A_train, A_test, Z_train, Z_test = train_test_split(nuevodata.drop('Z', axis=1), nuevodata['Z'], train_size=0.7, test_size=0.3)

print(A_train)
print(A_test)

print(Z_train)
print(Z_test)

model = Sequential()
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='mse', optimizer=SGD(), metrics=['accuracy'])
model.fit(A_train, Z_train, epochs=10000, batch_size=200, verbose=1)

y_pred_probs = model.predict(A_test)
y_pred_probs = y_pred_probs.flatten()
y_test_array = Z_test.values

print(y_pred_probs)

print(y_test_array)

    # Metricass
accuracy = metrics.accuracy_score(Z_test, (y_pred_probs >= 0.5).astype(int))
mse = metrics.mean_squared_error(Z_test, y_pred_probs)
roc = metrics.roc_auc_score(Z_test, y_pred_probs)
ks, p_value = ks_2samp(y_pred_probs, y_test_array)
#revisar KS si lo podemos calcular de otra manera
0
#Ver tema de los weights, o separar los casos buenos de los malos.

# Calcular accuracy
accuracy = metrics.accuracy_score(Z_test, (y_pred_probs >= 0.5).astype(int))

# Calcular MSE
mse = metrics.mean_squared_error(Z_test, y_pred_probs)

# Calcular ROC AUC
roc = metrics.roc_auc_score(Z_test, y_pred_probs)

# Calcular KS
ks, p_value = ks_2samp(y_pred_probs, y_test_array)

# Crear una lista para almacenar los resultados
results = []

# Agregar los resultados a la lista
results.append({
    'Accuracy': accuracy,
    'MSE': mse,
    'ROC': roc,
    'KS': ks
})

# Imprimir los resultados
print(results)

import pandas as pd
from google.colab import files

# Crear un DataFrame de Pandas con las predicciones
df_results = pd.DataFrame({'y_pred_probs': y_pred_probs, 'y_test_array': y_test_array})

# Exportar el DataFrame a un archivo Excel
df_results.to_excel('resultados_predicciones.xlsx', index=False)

files.download('resultados_predicciones.xlsx')

import numpy as np
from sklearn.metrics import confusion_matrix

# Ejemplo de etiquetas reales y predicciones
etiquetas_reales = np.array([1, 0, 0, 1, 1, 1, 0, 0, 1, 0])
predicciones = np.array([1, 0, 1, 1, 0, 1, 0, 1, 0, 0])

# Definir un valor de corte
valor_corte = 0.5

# Aplicar el valor de corte a las predicciones
predicciones_binarias = (predicciones >= valor_corte).astype(int)

# Construir la matriz de confusión
matriz_confusion = confusion_matrix(etiquetas_reales, predicciones_binarias)

# Obtener los valores de la matriz de confusión
verdaderos_positivos = matriz_confusion[1, 1]
falsos_positivos = matriz_confusion[0, 1]
verdaderos_negativos = matriz_confusion[0, 0]
falsos_negativos = matriz_confusion[1, 0]

# Calcular el accuracy
accuracy = (verdaderos_positivos + verdaderos_negativos) / len(etiquetas_reales)

# Imprimir la matriz de confusión y el accuracy
print("Matriz de Confusión:")
print(matriz_confusion)
print("Accuracy:", accuracy)