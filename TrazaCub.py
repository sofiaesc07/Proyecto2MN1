# Ana Sofía Escobar Rivera - 20489

#librerias necesarias para que funcione el programa 
from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt

#datos a utilizar
x = [18.89210699, 217.82483371, 545.75069278]
y = [25,201,145]

#Determinar la gráfica creada por medio de trazadores cubicos. 
f = CubicSpline(x, y, bc_type='natural')
x_new = np.linspace(15, 550, 100)
y_new = f(x_new)

print(f(x_new))

#Imprimir gráfico 
plt.plot(x_new, y_new, label = 'Polinomios', color='black')
plt.plot(x, y,'o', label = 'Puntos', color = 'purple')
plt.legend()
plt.xlabel('Producción total')
plt.ylabel('Demanda Total')
plt.show()