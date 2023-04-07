import numpy as np
#podpunkt a
arrayM = np.array([[3,6,6,9],
                   [1,4,0,9],
                   [0,0.2,6,12],
                   [0,0,0.1,6]])
def norm(arrayA):
    array = []
    array.append(arrayA[1][0])
    array.append(arrayA[2][0])
    array.append(arrayA[2][1])
    array.append(arrayA[3][0])
    array.append(arrayA[3][1])
    array.append(arrayA[3][2])
    max = np.max(array)
    return max

roznica = 0.1
x = 0
aktualnaNorma = norm(arrayM)
aktualnaNorma1 = norm(arrayM)
while(roznica>0.0000000000001):
    Q, R = np.linalg.qr(arrayM)
    arrayM = np.dot(R,Q)
    if (x % 2 == 0):
        roznica = norm(arrayM)
    elif (x % 2 == 1):
        roznica = norm(arrayM)
    x+=1
a = np.diag(arrayM)
print("Podpunkt a:")
print(a)
#podpunkt b
arrayB = np.array([[3,4,2,4],
                   [4,7,1,-3],
                   [2,1,3,2],
                   [4,-3,2,2]])

wektorPoczatkowy = [1,0,0,0]
for x in range(100):
    vectorPrzykladowyPrzyblizony = np.dot(arrayB,wektorPoczatkowy)
    #normaVactorPrzykladowyPrzyblizony = np.linalg.norm(vectorPrzykladowyPrzyblizony)
    normaVactorPrzykladowyPrzyblizony = np.max(vectorPrzykladowyPrzyblizony)
    wektorPoczatkowy = vectorPrzykladowyPrzyblizony/normaVactorPrzykladowyPrzyblizony
wynik = np.dot(arrayB,wektorPoczatkowy)
wartoscWlasna = wynik/wektorPoczatkowy
a = np.abs(wartoscWlasna[0])
print("Podpunkt b:")
print(a)
print(wektorPoczatkowy)