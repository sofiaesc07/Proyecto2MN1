#Ana Sofía Escobar Rivera - Carnet 20489
#calcular lambda optimo
   
#librerias a importar
import numpy as np

#plantear la matriz
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

#procedimiento
D=np.diagonal(A)
U = np.triu(A) - D
M = np.dot( np.linalg.inv(np.tril(A)), U); M
F = min(abs(np.linalg.eigvals(M)))

print('El valor de lambda es: ', F)

