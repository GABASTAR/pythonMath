import numpy as np
import pandas as pd
from sklearn import preprocessing

def prog1():
    arr = []
    for i in range(0, 8):
        arr.append([])
        for j in range(0, 8):
            if j%2 == i%2:
                arr[i].append(1)
            else:
                arr[i].append(0)
    nArr = np.array(arr)
    print(nArr)
def prog2():
    arr = []
    for i in range(0, 5):
        arr.append(np.arange(0, 5))
    arr = np.array(arr)
    print(arr)
def prog3():
    arr = np.random.random((3, 3, 3))
    print(arr)
def prog4():
    arr = np.full((5, 5), 1)
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if (i != 0 and i != len(arr)-1) and (j != 0 and j != len(arr[i])-1):
                arr[i][j] = 0
    print(arr)
def prog5():
    arr = np.arange(0, 9)
    print(np.sort(arr)[::-1])
def prog6():
    arr = np.random.random((3, 4))
    print(f"Size: {arr.size}\nDimension size: {arr.ndim}\nShape: {arr.shape}")


def pand1():
    s1 = pd.Series([1, 2, 3])
    s2 = pd.Series([5, 3, 6])
    print(np.sqrt(sum(pow(a-b, 2) for a, b in zip(s1, s2))))
def pand2():
    url = "https://raw.githubusercontent.com/akmand/datasets/main/airline_passenger_satisfaction.csv"
    dataframe = pd.read_csv(url)
    print(dataframe.head(5))
    print(dataframe.tail(5))
    print(dataframe.shape)
    print(dataframe.describe(), "\n40-44:")
    print(dataframe.iloc[40:45], "\nEco:")
    print(dataframe[dataframe["customer_class"] == "Eco"].head(5))
def panda3():
    url = "https://raw.githubusercontent.com/akmand/datasets/master/iris.csv"
    dataframe = pd.read_csv(url)
    print(dataframe)
    minMaxScale = preprocessing.MinMaxScaler()
    zScale = preprocessing.StandardScaler()
    dataframe[["sepal_length_cm"]] = minMaxScale.fit_transform(dataframe[["sepal_length_cm"]])
    dataframe[["sepal_width_cm"]] = zScale.fit_transform(dataframe[["sepal_width_cm"]])
    print(dataframe)
panda3()