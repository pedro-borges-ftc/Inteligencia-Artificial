from sklearn.datasets import load_iris
import pandas as pd

# Carrega o dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Mostra estatísticas básicas
print(df.describe())