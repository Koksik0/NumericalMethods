import matplotlib.pyplot as plt
import numpy as np

firstDiagonal = 0.2
secondDiagonal = 1
thirdDiagonal = 3
fourthDiagonal = 1
fifthDiagonal = 0.2
matrixSize = 100

def setVector(vector, number, matrixSize):
    for x in range(matrixSize):
        vector.append(number)

def GaussaSeidlaMethod():
    for x in range(0, matrixSize + 1):
        if (x == 0):
            startValues[x] = (1 - (secondDiagonal * startValues[x + 1]) - (
                    fifthDiagonal * startValues[x + 2])) / thirdDiagonal
        elif (x == 1):
            startValues[x] = (2 - (fourthDiagonal * startValues[x - 1]) - (secondDiagonal * startValues[x + 1]) - (
                    fifthDiagonal * startValues[x + 2])) / thirdDiagonal
        elif (x >= 2 and x <= matrixSize - 3):
            startValues[x] = (x + 1 - (fifthDiagonal * startValues[x - 2]) - (fourthDiagonal * startValues[x - 1]) - (
                    secondDiagonal * startValues[x + 1]) - firstDiagonal * startValues[x + 2]) / thirdDiagonal
        elif (x == matrixSize - 2):
            startValues[x] = (x + 1 - (fifthDiagonal * startValues[x - 2]) - (fourthDiagonal * startValues[x - 1]) - (
                    secondDiagonal * startValues[x + 1])) / thirdDiagonal
        elif (x == matrixSize - 1):
            startValues[x] = (x + 1 - (fifthDiagonal * startValues[x - 2]) - (
                    fourthDiagonal * startValues[x - 1])) / thirdDiagonal


def JacobiMethod(vector, vector1, startValues):
    for x in range(matrixSize):
        if (x == 0):
            vector1[x] = (1 - (secondDiagonal * vector[x + 1]) - (
                    fifthDiagonal * vector[x + 2])) / thirdDiagonal
        elif (x == 1):
            vector1[x] = (2 - (fourthDiagonal * vector[x - 1]) - (secondDiagonal * vector[x + 1]) - (
                    fifthDiagonal * startValues[x + 2])) / thirdDiagonal
        elif (x >= 2 and x <= matrixSize - 3):
            vector1[x] = (x + 1 - (fifthDiagonal * vector[x - 2]) - (fourthDiagonal * vector[x - 1]) - (
                    secondDiagonal * vector[x + 1]) - firstDiagonal * startValues[x + 2]) / thirdDiagonal
        elif (x == matrixSize - 2):
            vector1[x] = (x + 1 - (fifthDiagonal * vector[x - 2]) - (fourthDiagonal * vector[x - 1]) - (
                    secondDiagonal * vector[x + 1])) / thirdDiagonal
        elif (x == matrixSize - 1):
            vector1[x] = (x + 1 - (fifthDiagonal * vector[x - 2]) - (
                    fourthDiagonal * vector[x - 1])) / thirdDiagonal


def subtraction(lista1, lista2):
    wynik = []
    for x in range(matrixSize):
        wynik.append(lista1[x] - lista2[x])
    return wynik


def rewrite(lista1, lista2, matrixSize):
    for x in range(matrixSize):
        lista1.append(lista2[x])


howManyTimes = int(input("Ile razy chcesz podawać wartość startową?"))
for y in range(howManyTimes):
    delta = 1
    x = 0
    startValues = []
    startValues2 = []
    startValuesJacobi2 = []
    startValuesJacobi = []
    numberOfOperation = []
    deltaJacobi = []
    deltaGaussSeidel = []
    initialValue = int(input("Podaj wartość startową: "))
    setVector(startValues, initialValue, matrixSize)
    setVector(startValuesJacobi,initialValue, matrixSize)
    setVector(startValuesJacobi2, initialValue, matrixSize)
    while(delta>0.0000000000001 and x<1000):
        if (x >= 1):
            numberOfOperation.append(x)
        startValues2 = []
        rewrite(startValues2, startValues, matrixSize)
        GaussaSeidlaMethod()
        if (x >= 1):
            if(np.linalg.norm(subtraction(startValues2, startValues))>0.0000000000001):
                deltaGaussSeidel.append(np.linalg.norm(subtraction(startValues2, startValues)))
            else:
                deltaGaussSeidel.append(0.0000000000001)
        if (x % 2 == 0):
            JacobiMethod(startValuesJacobi, startValuesJacobi2, startValues)
        else:
            JacobiMethod(startValuesJacobi2, startValuesJacobi, startValues)
        if (x >= 1 and x % 2 == 1):
            deltaJacobi.append(np.linalg.norm(subtraction(startValuesJacobi, startValuesJacobi2)))
            delta = np.linalg.norm(subtraction(startValuesJacobi, startValuesJacobi2))
        elif (x >= 2 and x % 2 == 0):
            deltaJacobi.append(np.linalg.norm(subtraction(startValuesJacobi2, startValuesJacobi)))
            delta = np.linalg.norm(subtraction(startValuesJacobi2, startValuesJacobi))
        x+=1
    print(startValuesJacobi)
    print(startValues)
    plt.xlabel("Ilość operacji")
    plt.ylabel("Różnica norm pomiędzy iteracjami(log)")
    string = "Wartość startowa: " + str(initialValue)
    plt.title(string)
    plt.plot(numberOfOperation, deltaJacobi)
    plt.plot(numberOfOperation, deltaGaussSeidel)
    plt.yscale("log")
    plt.savefig('chart' + str(y) + '.svg')
    plt.show()



