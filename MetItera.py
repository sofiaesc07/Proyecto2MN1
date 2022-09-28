#Ana Sofía Escobar - 20489

#librerias a importar
import numpy as np

def calc(A, b, relaj, xi, conv):
    #plantear las matrices y los procedimientos
  final = xi[:]
  mtrz = np.linalg.norm(np.matmul(A, final) - b) #planteamos los residuos
  while mtrz > conv:
    for i in range(A.shape[0]):
      sigma = 0
      for j in range(A.shape[1]):
        if j != i:
          sigma += A[i][j] * final[j]
      final[i] = (1 - relaj) * final[i] + (relaj / A[i][i]) * (b[i] - sigma)
    mtrz = np.linalg.norm(np.matmul(A, final) - b)
    print(xi, 'Error: {0:10.6g}'.format(mtrz))
  return final

#elegimos la cantidad de error que queremos y cual va a ser nuestro lambda
error = 1.e-10
relaj = 0.9301823921679299 #factor lambda  

#PLANTEAMOS LA MATRIZ
A = np.ones((3, 3))#podemos colocar de que tamaño sera nuestra matriz
#linea 1
A[0][0] = 0.268 
A[0][1] = 0.079 
A[0][2] = 0.005
#linea 2
A[1][0] = 0.122 
A[1][1] = 0.371
A[1][2] = 0.216
#linea 3
A[2][0] = 0.122
A[2][1] = 0.154 
A[2][2] = 0.200
#nuestra matriz b
b = np.ones(3)
b[0] = 25
b[1] = 201
b[2] = 145
#colocamos con cuantos 0 empezamos
xi = np.zeros(3)

final = calc(A, b, relaj, xi, error)
print('')
print('Solucion final:', final)
print('')