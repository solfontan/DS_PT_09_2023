#crear un modelo KNN con los datos de iris
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pickle

# Cargar el dataset Iris
iris = load_iris()

# Contar las instancias de cada clase en el target
print("Clases tamaños:\n", pd.Series(iris.target).value_counts())

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

print("\nXtrain", X_train.shape)
print("Xtest", X_test.shape)
print("ytrain", y_train.shape)
print("ytest", y_test.shape)

# Crear el modelo KNN
knn = KNeighborsClassifier(n_neighbors=3)  # Selecciona el número de vecinos que desees

# Entrenar el modelo
knn.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba
predictions = knn.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, predictions)
print("\nPrecisión del modelo KNN:", accuracy)

with open('flask\App\model_knn.pkl', 'wb') as f:
    pickle.dump(knn, f)