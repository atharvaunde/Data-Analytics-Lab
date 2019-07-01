import pandas as pd
import matplotlib.pyplot as plt

path="iris.csv"

df=pd.read_csv(path,header=None)
headers=["Sepal-length","Sepal-width","Petal-length","Petal-width","Species"]
df.columns=headers
print(df.head(5)) #first 5 records when parameter is gives 
print(df.tail(5)) #last 5 records when parameter is gives
print(df.info())  #total records when parameter is gives
print(df.dtypes)  #features 
print(df.shape)
 
print(df.describe()) #gives mean, min, max of feaures
#print(df.describe(include = 'all')) #gives mean, min, max of ALL features
d=df.drop(['Species'],axis=1)

d.hist()
plt.show()
plt.scatter('Sepal-length', 'Sepal-width', 'Petal-length', 'Petal-width', 'Species') #drawing the scattered graph
plt.title('LAB 1')
plt.xlabel('x') #defining the X axis for graph
plt.ylabel('y') #defining the Y axis for graph
plt.show()
plt.scatter (df ['Sepal-length'],df['Sepal-width'])
plt.show()
