import numpy as np
import time
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
arrayOfSize = []
arrayOfTime = []


def setArray(a, b,firstRow,secondRow):
    for x in range(0, sizeArray):
        firstRow.append(a)
        secondRow.append(b)

def setVector(vector,y):
    for x in range(0,sizeArray):
        vector.append(y)

def backSubctitution(array, vector,solution):
    solution.append(vector[sizeArray-1]/array[0][sizeArray-1])
    for x in range(0,sizeArray-1):
        solution.append((vector[sizeArray-2-x] - array[1][sizeArray-2-x]*solution[x])/array[0][sizeArray-2-x])

def sum(vector):
    sum = 0.0
    for x in range(0,sizeArray):
        sum += vector[x]
    return sum

def shermanMorisson(solution, vectorZ, vectorX,sumZ,sumX):
    for x in range(0,sizeArray):
        vectorX[x] *= (sumZ/(1+sumX))
        solution.append(vectorZ[x] - vectorX[x])



x = 1
while(x<10000):
    sizeArray = x
    array = []
    solution = []
    firstRow = []
    secondRow = []
    vectorB = []
    vectorU = []
    setArray(9, 7,firstRow,secondRow)
    array = np.array([firstRow,secondRow])
    setVector(vectorB,5)
    setVector(vectorU,1)
    vectorZ = []
    vectorX = []
    start = time.time()
    backSubctitution(array,vectorB,vectorZ)
    backSubctitution(array,vectorU,vectorX)
    vectorZ.reverse()
    vectorX.reverse()
    shermanMorisson(solution,vectorZ,vectorX,sum(vectorZ),sum(vectorX))
    finish = time.time() - start
    arrayOfSize.append(x)
    arrayOfTime.append(finish)
    x += 100
plt.title('NUM4')
plt.xlabel('Rozmiar macierzy')
plt.ylabel('Czas w sekundach')
plt.plot(arrayOfSize, arrayOfTime)
plt.show()

solution1 = []
firstRow1 = []
secondRow1 = []
vectorB1 = []
vectorU1 = []
sizeArray =  int(input("Wpisz rozmiar macierzy: "))
setArray(9,7,firstRow1,secondRow1)
array1 = np.array([firstRow1,secondRow1])
setVector(vectorB1,5)
setVector(vectorU1,1)
vectorZ1 = []
vectorX1 = []
backSubctitution(array1,vectorB1,vectorZ1)
backSubctitution(array1,vectorU1,vectorX1)
vectorZ1.reverse()
vectorX1.reverse()
shermanMorisson(solution1,vectorZ1,vectorX1,sum(vectorZ1),sum(vectorX1))
print(solution1)