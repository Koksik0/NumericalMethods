import numpy as np

sizeArray = int(input("Wpisz rozmiar macierzy: "))
firstRow = []
secondRow = []
thirdRow = []
fourthRow = []

def setArray():
    for x in range(1, sizeArray+1):
        firstRow.append(0.2)
        secondRow.append(1.2)
        thirdRow.append(0.1/x)
        fourthRow.append(0.4 / (x * x))

def decompositionLU(array):
    array[0][0] /= array[1][0]
    for x in range(1, sizeArray):
        array[1][x] -= (array[0][x-1]*array[2][x-1])
        array[2][x] -= (array[0][x-1]*array[3][x-1])
        array[0][x] /= array[1][x]

vectorX = []
for x in range(1,sizeArray+1):
    vectorX.append(x)

solutionForwardSubstitution = []
def forwardSubstitution(array):
    solutionForwardSubstitution.append(vectorX[0])
    for x in range(1,sizeArray):
        solutionForwardSubstitution.append(vectorX[x] - array[0][x-1]*solutionForwardSubstitution[x-1])


solutionBackSubstitution = []
def backSubstituition(array):
    solutionBackSubstitution.append(solutionForwardSubstitution[sizeArray-1]/array[1][sizeArray-1])
    solutionBackSubstitution.append((solutionForwardSubstitution[sizeArray - 2] - array[2][sizeArray - 2]*solutionBackSubstitution[0]) / array[1][sizeArray - 2])
    for x in range(0,sizeArray-2):
        temp = (array[2][sizeArray-3-x]*solutionBackSubstitution[x+1] + array[3][sizeArray-3-x]*solutionBackSubstitution[x])
        solutionBackSubstitution.append((solutionForwardSubstitution[sizeArray-x-3] - temp)/array[1][sizeArray-3-x])


def det(array):
    valueOfDet = 1.0
    for x in range(0,sizeArray):
        valueOfDet *= array[1][x]
    return valueOfDet


setArray()
array = np.array([firstRow,secondRow,thirdRow,fourthRow])
decompositionLU(array)
forwardSubstitution(array)
print("Rozwiązanie układu równań")
backSubstituition(array)
solutionBackSubstitution.reverse()
print(solutionBackSubstitution)
print("\n\n\n")
print("Wyznacznik macierzy")
print(det(array))
