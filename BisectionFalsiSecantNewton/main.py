import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
precision = 0.00000000001
limit = 100
def function(x, n):
    #Pierwsza funkcja
    return (np.exp(x) -2)**n

    #Druga funkcja
    # return (1/2) - (1/np.exp(x))

    #Trzeciafunkcja
    # return (1/3) - (2/(3*np.exp(x)))

errorInBisectionMethod = []
def bisection(a, b, n):
    if(function(a,n)*function(b,n)>0):
        print("Metoda bisekcji nie działa dla (e^x -2)^" + str(n))
        return -10000000000
    c = (a+b)/2
    numberOfIterations = 0
    while(np.abs(function(c,n))>precision and numberOfIterations<=limit):
        c = (a+b)/2
        errorInBisectionMethod.append(c)
        numberOfIterations += 1
        if(function(c,n)*function(a,n)<0):
            b = c
        else:
            a = c
    return c

errorInFalsiMethod = []
def falsi(a,b,n):
    if (function(a, n) * function(b, n) > 0):
        print("Metoda falsi nie działa dla (e^x -2)^" + str(n))
        return -10000000000
    c = (function(b, n) * a - function(a, n) * b) / (function(b, n) - function(a, n))
    numberOfIterations = 0
    while(np.abs(function(c,n))>precision and numberOfIterations<=limit):
        c = (function(b, n) * a - function(a, n) * b) / (function(b, n) - function(a, n))
        errorInFalsiMethod.append(c)
        numberOfIterations+=1
        if (function(c, n) * function(a, n) < 0):
            b = c
        else:
            a = c
    return c

errorInSecantMethod = []
def secant(a,b,n):
    c = b - (function(b,n)*(b - a))/(function(b,n) - function(a,n))
    errorInSecantMethod.append(c)
    numberOfIterations = 0
    while(np.abs(function(c,n))>precision and numberOfIterations<=limit):
        a = b
        b = c
        c = b - (function(b, n) * (b - a)) / (function(b, n) - function(a, n))
        errorInSecantMethod.append(c)
        numberOfIterations +=1
    return c

errorInNewtonMethod = []
def Newton(a,n):
    #Pierwsza funkcja
    b = a - (function(a,n)/(np.exp(a)))

    #Druga funkcja
    # b = a - (function(a,n)/(1/np.exp(a)))

    #Trzecia funkcja
    # b = a - (function(a,n)/(2/(3*np.exp(a))))
    errorInNewtonMethod.append(b)
    numberOfIterations = 0
    while(np.abs(function(b,n))>precision and numberOfIterations<=limit):
        a = b
        #Pierwsza funkcja
        b = a - (function(a,n)/(np.exp(a)))

        # Druga funkcja
        # b = a - (function(a, n) / (1 / np.exp(a)))

        # Trzecia funkcja
        # b = a - (function(a, n) / (2 / (3 * np.exp(a))))

        errorInNewtonMethod.append(b)
        numberOfIterations += 1
    return b

def approximation(errorsInIterations, root):
    list = []
    for x in range(len(errorsInIterations)):
        list.append(np.abs(errorsInIterations[x] - root))
    return list

#Obliczenia
n = 1
rootBisection = bisection(0,1,n)
rootFalsi = falsi(0,1,n)
rootSecant= secant(0,1,n)
rootNewton = Newton(1,n)
print("Pierwiastek obliczony za pomocą metody bisekcji: " + str(rootBisection))
print("Pierwiastek obliczony za pomocą metody falsi: " + str(rootFalsi))
print("Pierwiastek obliczony za pomocą metody siecznych: " + str(rootSecant))
print("Pierwiastek obliczony za pomocą metody Newtona: " + str(rootNewton))
errorBisection = approximation(errorInBisectionMethod,rootBisection)
errorFalsi = approximation(errorInFalsiMethod,rootFalsi)
errorSecant = approximation(errorInSecantMethod, rootSecant)
errorNewton = approximation(errorInNewtonMethod,rootNewton)

#Wykres
fig, ax = plt.subplots()
ax.set_title("Porównanie metod z dla funkcji g(x)")
ax.set_xlabel("iteracje")
ax.set_ylabel("|błąd w iteracji - wartość dokłada|")
ax.set_yscale("log")
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.plot(errorBisection, color = 'red', label = "Bisekcja")
ax.plot(errorFalsi, color = 'blue', label = "Falsi")
ax.plot(errorSecant, color = 'yellow', label = "Sieczne")
ax.plot(errorNewton, color = 'green', label = "Newton")
ax.legend()
plt.show()
