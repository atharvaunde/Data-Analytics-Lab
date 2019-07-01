import matplotlib.pyplot as plt
import pandas as pd

path = "iris.csv"

df = pd.read_csv(path, header=None)

headers = ["Sepal-length", "Sepal-width", "Petal-length", "Petal-width", "Species"]
df.columns = headers

print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
print(df.dtypes)
print(df.describe())

df.hist()
plt.show()

df.boxplot()
plt.show()

plt.scatter(df["Sepal-length"], df["Sepal-width"])
plt.show()

plt.scatter(df["Sepal-length"], df["Petal-length"])
plt.show()

plt.scatter(df["Sepal-length"], df["Petal-width"])
plt.show()

plt.scatter(df["Sepal-width"], df["Sepal-length"])
plt.show()

plt.scatter(df["Sepal-width"], df["Petal-length"])
plt.show()

plt.scatter(df["Sepal-width"], df["Petal-width"])
plt.show()

plt.scatter(df["Petal-length"], df["Sepal-length"])
plt.show()

plt.scatter(df["Petal-length"], df["Sepal-width"])
plt.show()

plt.scatter(df["Petal-length"], df["Petal-width"])
plt.show()

plt.scatter(df["Petal-width"], df["Sepal-length"])
plt.show()

plt.scatter(df["Petal-width"], df["Sepal-width"])
plt.show()

plt.scatter(df["Petal-width"], df["Petal-length"])
plt.show()
