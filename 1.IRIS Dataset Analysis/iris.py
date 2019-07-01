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
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()

plt.scatter(df["Sepal-length"], df["Petal-length"])
plt.xlabel('Sepal Length')
plt.ylabel('Petal Width')


plt.show()

plt.scatter(df["Sepal-length"], df["Petal-width"])
plt.xlabel('Sepal Length')
plt.xlabel('Petal Width')
plt.show()

plt.scatter(df["Sepal-width"], df["Sepal-length"])
plt.xlabel('Sepal Width')
plt.ylabel('Sepal Length')
plt.show()

plt.scatter(df["Sepal-width"], df["Petal-length"])
plt.xlabel('Sepal Width')
plt.ylabel('Petal Length')
plt.show()

plt.scatter(df["Sepal-width"], df["Petal-width"])
plt.xlabel('Sepal Width')
plt.ylabel('Petal Width')
plt.show()

plt.scatter(df["Petal-length"], df["Sepal-length"])
plt.xlabel('Petal Length')
plt.ylabel('Sepal Length')
plt.show()

plt.scatter(df["Petal-length"], df["Sepal-width"])
plt.xlabel('Petal Length')
plt.ylabel('Sepal Width')
plt.show()

plt.scatter(df["Petal-length"], df["Petal-width"])
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()

plt.scatter(df["Petal-width"], df["Sepal-length"])
plt.xlabel('Petal Width')
plt.xlabel('Sepal Length')
plt.show()

plt.scatter(df["Petal-width"], df["Sepal-width"])
plt.xlabel('Petal Width')
plt.xlabel('Sepal Width')
plt.show()


plt.scatter(df["Petal-width"], df["Petal-length"])
plt.xlabel('Petal Width')
plt.yxlabel('Petal Length')
plt.show()
