from numpy import Inf, trapz
import matplotlib.pyplot as plt
from random import random
from statistics import median
import requests
from datetime import datetime
import math


def prog1():   
    x = 5 >= 2
    A = {1, 3, 7, 8}
    B = {2, 4, 5, 10, "apple"}
    C = A & B
    df = "Antony Antonov", 34, "MAN"
    z = "type"
    D = [1, "tittle", 2, "content"]
    arr = [x, A, B, C, df, z, D]
    for elem in arr:
        print(f"{elem}: {type(elem)}")
def prog2():
    x = 98
    if x > -Inf and x < -5:
        print("x in (-infinity, -5)")
    elif x >= -5 and x <= 5:
        print("x in [-5, 5]")
    elif x > 5 and x < Inf:
        print("x in (5, +infinity)")
def prog3():
    for x in range(1, 10+1, 3)[::-1]:
        print(x)
def prog4():
    arr = ["White", "Slav", "Tall", "Swole"]
    for i in arr:
        print(i)
def prog5():
    arr = range(2, 15)
def prog6():
    for i in range(5, 105+1, 25)[::-1]:
        print(i)
def prog7():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = []
    for i in x:
        y.append(i)
    arr = []
    k = 0
    for i in x:
        if i%2 == 0:
            arr.append(k)
        k-=-1
    arrRev = arr[::-1]
    for i in range(0, len(arr)):
        x[arr[i]] = y[arrRev[i]]
def  prog4_1():
    x = []
    for i in range(0, 101):
        x.append(round(random(), 2))
    print(sum(x)/len(x))
    print(median(x))
    y = []
    for i in x:
        y.append(x.count(i))
    plt.scatter(x, y)
    plt.show()
def prog4_2():
    def func4_2(x):
        return (math.sqrt( 1 + math.exp(math.sqrt(x)) + math.cos( math.pow( x, 2 ) ) ) / abs( 1 - math.pow( math.sin(x), 3 ) ) + math.log( abs( 2 * x ) ) )
    arr = []
    for i in range(1, 10 + 1):
        arr.append(func4_2(i))
    arrHalf = arr[0:len(arr)//2]
    plt.plot(range(1, len(arr) + 1), arr, label = "Linear")
    plt.scatter(range(1, len(arrHalf) + 1), arrHalf, label = "Pointed")
    plt.legend()
    plt.show()
def prog4_3():
    def func4_3(x):
        return abs( math.cos( x * math.exp( ( math.cos( x ) + math.log( x + 1 ) ) ) ) )
    arr = []
    for i in range(0, 10 + 1):
        arr.append(func4_3(i))
    xArr = range(0, 10 + 1)
    print(trapz(arr, xArr))
    plt.plot(xArr, arr)
    plt.fill_between(xArr, arr)
    plt.show()
def prog4_4():
    companies = ["GOOG", "AAPL", "MSFT"]
    for i in companies:
        r = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{i}?region=US&lang=en-US&includePrePost=false&interval=1d&useYfid=true&range=1y&corsDomain=finance.yahoo.com&.tsrc=finance",
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36"})
        result = r.json()
        xRaw = result['chart']['result'][0]['timestamp']
        x = []
        for j in xRaw:
            x.append(datetime.fromtimestamp(j))
        y = result['chart']['result'][0]['indicators']['quote'][0]['close']
        plt.plot(x, y, label = i)
    plt.legend()
    plt.show()
def prog4_5():
    try:
        temp = input("Input your option:\n1 - calculate '+', '-', '*', '/' operations\n2 - calculate e^x+y, sin(x+y) and cos(x+y), x^y\n")
        if (temp == "1"):
                print("Answer: " + eval(input("Input calculation as '5 + 4':\n")))
        elif (temp == "2"):
            nums = input("Input arguments divided by space as '5 4':\n").split(" ")
            x = float(nums[0])
            y = float(nums[1])
            print(f"e^x+y: {math.exp(x + y)}\nsin(x+y): {math.sin(x+y)}\ncos(x+y): {math.cos(x+y)}\nx^y: {x**y}")
        else:
            print("Please provide 1 or 2 next time")
    except Exception as e:
        print("bruh")