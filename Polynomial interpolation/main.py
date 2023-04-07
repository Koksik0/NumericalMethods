import numpy as np
import matplotlib.pyplot as plt


def argumentsA(n):
    arrayOfArguments = []
    for i in range(n):
        argument = -1 + ((2*i)/(n+1))
        arrayOfArguments.append(argument)
    return arrayOfArguments

def argumentsB(n):
    arrayOfArguments = []
    for i in range(n):
        argument = np.cos(((2*i+1)*np.pi)/((2*n) + 2))
        arrayOfArguments.append(argument)
    return arrayOfArguments

def values(arrayOfArguments,n):
    arrayOfValues = []
    for x in range(n):
        value = 1/(1+(25*arrayOfArguments[x]*arrayOfArguments[x]))
        arrayOfValues.append(value)
    return arrayOfValues

def values2(arrayofArguments,n):
    arrayOfValues = []
    for x in range(n):
        value = arrayofArguments[x] * arrayofArguments[x]
        arrayOfValues.append(value)
    return arrayOfValues

def phi(arrayOfArguments,n,index,x):
    dividend = 1
    divisor = 1
    for i in range(index):
        dividend *= (x - arrayOfArguments[i])
        divisor *= (arrayOfArguments[index] - arrayOfArguments[i])
    for i in range(index+1,n):
        dividend *= (x - arrayOfArguments[i])
        divisor *= (arrayOfArguments[index] - arrayOfArguments[i])
    result = dividend/divisor
    return result

def valueOfPolynomial(arrayOfArguments,arrayofValues, n,x):
    result = 0
    for i in range(0,n):
        result += arrayofValues[i]*phi(arrayOfArguments,n,i,x)
    return result

def multiplyPolynominals(firstPylominal, secondPylominal):
    results = []
    for x in range(0,len(firstPylominal) + len(secondPylominal) -1):
        results.append(0)
    for x in range(0,len(secondPylominal)):
        for y in range(0,len(firstPylominal)):
            results[x+y] += secondPylominal[x] * firstPylominal[y]
    return results

def addPolynominals(firstPylominal, secondPylominal):
    results = []
    firstPylominal.reverse()
    secondPylominal.reverse()
    if(len(firstPylominal)>=len(secondPylominal)):
        size = len(secondPylominal)
        size1 = len(firstPylominal)
    else:
        size = len(firstPylominal)
        size1 = len(secondPylominal)
    for x in range(size):
        results.append(firstPylominal[x] + secondPylominal[x])
    for x in range(size,size1):
        if(len(firstPylominal)>len(secondPylominal)):
            results.append(firstPylominal[x])
        else:
            results.append(secondPylominal[x])
    results.reverse()
    return results

def patternPolynominal(index,arrayOfArguments,arrayOfValues):
    pattern = []
    divisor = 1
    for x in range(index):
        pattern.append(arrayOfArguments[x])
    for x in range(index+1,len(arrayOfArguments)):
        pattern.append(arrayOfArguments[x])
    for x in range(index):
        divisor *= (arrayOfArguments[index] - arrayOfArguments[x])
    for x in range(index+1,len(arrayOfArguments)):
        divisor *= (arrayOfArguments[index] - arrayOfArguments[x])
    temp = multiplyPolynominals([1,-pattern[0]], [1,-pattern[1]])
    temp1 = []
    for x in range(2,len(pattern)):
        temp1 = multiplyPolynominals(temp, [1,-pattern[x]])
        temp = temp1
    for x in range(len(arrayOfArguments)):
        a = arrayOfValues[index]/divisor
        temp1[x] *= a
    # print(temp1)
    return temp1

#Wyznaczanie wielomianu

n=100
arrayOfArguments = argumentsA(n)
arrayOfValues = values(arrayOfArguments,n)
array = []
for y in range(len(arrayOfArguments)):
    array.append(patternPolynominal(y,arrayOfArguments,arrayOfValues))
for x in range(len(array)):
    for y in range(1,len(array[x])):
        array[0][x] += array[y][x]
polynominal = array[0]

#Wypisanie wzoru wielomianu
power = len(polynominal)-1
string = ""
for x in range(power+1):
    number = str(polynominal[x])
    if(polynominal[x]>0 and x>0):
        string += "+ " + str(number) +  "x^" + str(power) + " "
    else:
        string += " " + str(number) +  "x^" + str(power) + " "

    power-=1

print("Dla podpunktu a:")
print(string)

arrayOfArguments = argumentsB(n)
arrayOfValues = values(arrayOfArguments,n)
array = []
for y in range(len(arrayOfArguments)):
    array.append(patternPolynominal(y,arrayOfArguments,arrayOfValues))
for x in range(len(array)):
    for y in range(1,len(array[x])):
        array[0][x] += array[y][x]
polynominal = array[0]

power = len(polynominal)-1
string1 = ""
for x in range(power+1):
    number = str(polynominal[x])
    if(polynominal[x]>0 and x>0):
        string1 += "+ " + str(number) +  "x^" + str(power) + " "
    else:
        string1 += " " + str(number) +  "x^" + str(power) + " "

    power-=1
print("Dla podpunktu b:")
print(string1)
#Rysowanie wykresu
arrayOfArguments = argumentsA(n)
arrayOfArguments1 = argumentsB(n)
arrayOfValues = values(arrayOfArguments,n)
arrayOfValues1 = values(arrayOfArguments1,n)
arguments = []
result = []
arguments1 = []
result1 = []
x = -1
while(x<=1):
     result.append(valueOfPolynomial(arrayOfArguments,arrayOfValues,n,x))
     arguments.append(x)
     result1.append(valueOfPolynomial(arrayOfArguments1, arrayOfValues1, n, x))
     arguments1.append(x)
     x+=0.01
plt.plot(arguments,result)
plt.plot(arguments1,result1)
plt.xlabel("arguments")
plt.ylabel("values")
plt.yscale("log")
plt.savefig('chart'+ str(n) +'.svg')
plt.show()
# print(arguments)
# print(result)

