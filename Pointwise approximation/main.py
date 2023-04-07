import numpy as np
import matplotlib.pyplot as plt
arguments = []
values = []
with open("data.txt", "r") as file:
    for line in file:
        arg, val = line.strip().split()
        arg1 = float(arg)
        val1 = float(val)
        arguments.append(arg1)
        values.append(val1)
def matrixA(arguments):
    matrix = []
    for x in range(100):
        temp = []
        temp.append(np.sin(2*arguments[x]))
        temp.append(np.sin(3*arguments[x]))
        temp.append(np.cos(5*arguments[x]))
        temp.append(np.exp(-arguments[x]))
        matrix.append(temp)
    return matrix
arr = []
def curve(factors):
    y = 0
    result = []
    for x in range(100):
        arr.append(y)
        result.append(factors[0]*np.sin(2*y) + factors[1]*np.sin(3*y) + factors[2]*np.cos(5*y) + factors[3]*np.exp(-y))
        y += 0.1
    return result
# podpunkt a
A = matrixA(arguments)
At = np.transpose(A)
a = np.dot(At,A)
b = np.dot(At,values)
c = np.linalg.solve(a,b)
print(c)
plt.scatter(arguments, values, c='#8a134e')
plt.plot(arr,curve(c))
plt.title("Podpunkt a")
plt.xlabel("arguments")
plt.ylabel("values")
plt.show()

#podpunkt b
argumentsB = []
valuesB = []
n = 100
def generateValues():
    y = 0.1
    for x in range(n):
        argumentsB.append(y)
        valuesB.append((1.3*np.log(y)) + (0.345*y) + (0.997*np.sin(11*y)) - (0.671*np.cos(9*y)) + np.random.randint(0,10))
        y+=0.1
def matrixB(argumentsB):
    matrix = []
    for x in range(n):
        temp = []
        temp.append(np.log(argumentsB[x]))
        temp.append(argumentsB[x])
        temp.append(np.sin(11*argumentsB[x]))
        temp.append(np.cos(9*argumentsB[x]))
        matrix.append(temp)
    return matrix
arrB = []
def curveB(factorsB):
    y = 0.1
    result = []
    for x in range(n):
        arrB.append(y)
        result.append(factorsB[0]*np.log(y) + factorsB[1]*y + factorsB[2]*np.sin(11*y) + factorsB[3]*np.cos(9*y))
        y += 0.1
    return result

generateValues()
B = matrixB(argumentsB)
Bt = np.transpose(B)
aB = np.dot(Bt,B)
bB = np.dot(Bt,valuesB)
cB = np.linalg.solve(aB,bB)
print(cB)
plt.scatter(argumentsB, valuesB, c='#8a134e')
plt.plot(arrB,curveB(cB))
plt.title("Podpunkt b")
plt.xlabel("arguments")
plt.ylabel("values")
plt.show()