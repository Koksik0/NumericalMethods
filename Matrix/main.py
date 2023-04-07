from array import array
import numpy as np

arrA1 = np.array([[2.34332898, -0.11253278, -0.01485349, 0.33316649, 0.71319625],
                  [-0.11253278, 1.67773628, -0.32678856, -0.31118836, -0.43342631],
                  [-0.01485349, -0.32678856, 2.66011353, 0.85462464, 0.16698798],
                  [0.33316649, -0.31118836, 0.85462464, 1.54788582, 0.32269197],
                  [0.71319625, -0.43342631, 0.16698798, 0.32269197, 3.27093538]])
arrB = np.array([[3.55652063354463],
                 [-1.86337418741501],
                 [5.84125684808554],
                 [-1.74587299057388],
                 [0.84299677124244]])
arrA1y1 = np.linalg.solve(arrA1, arrB)

arrA2 = np.array([[2.34065520, -0.05353743, 0.00237792, 0.32944082, 0.72776588],
                  [-0.05353743, 0.37604149, -0.70698859, -0.22898376, -0.75489595],
                  [0.00237792, -0.70698859, 2.54906441, 0.87863502, 0.07309288],
                  [0.32944082, -0.22898376, 0.87863502, 1.54269444, 0.34299341],
                  [0.72776588, -0.75489595, 0.07309288, 0.34299341, 3.19154447]])

arrA2y2 = np.linalg.solve(arrA2, arrB)

arrBprim = np.array([[3.55653063354463],
                     [-1.86337418741501],
                     [5.84125684808554],
                     [-1.74587299057388],
                     [0.84299677124244]])

arrA1y1prim = np.linalg.solve(arrA1, arrBprim)
arrA2y2prim = np.linalg.solve(arrA2, arrBprim)

delta1 = np.linalg.norm(arrA1y1 - arrA1y1prim)
delta2 = np.linalg.norm(arrA2y2 - arrA2y2prim)
wartosciWlaseA1max = np.linalg.eigvals(arrA1).max()
wartosciWlaseA1min = np.linalg.eigvals(arrA1).min()
wartosciWlaseA2max = np.linalg.eigvals(arrA2).max()
wartosciWlaseA2min = np.linalg.eigvals(arrA2).min()

wspolczynnikUwarunkowaniaMacierzy1 = np.linalg.cond(arrA1)
wspolczynnikUwarunkowaniaMacierzy2 = np.linalg.cond(arrA2)

print ("Rozwiązanie układu równań A1y1 = b:")
print (arrA1y1)
print ("\nRozwiązanie układu równań A1y1' = b:'")
print (arrA1y1prim)
print ("\nDelta1:")
print (delta1)
print("\nWspółczynnik uwarunkowania macierzy A1:")
print (wspolczynnikUwarunkowaniaMacierzy1)

print ("\n\n\n")
print ("Rozwiązanie układu równań A2y2 = b:")
print (arrA2y2)
print ("\nRozwiązanie układu równań A1y1' = b:")
print (arrA2y2prim)
print ("\nDelta2:")
print (delta2)
print("\nWspółczynnik uwarunkowania macierzy A1:")
print (wspolczynnikUwarunkowaniaMacierzy2)