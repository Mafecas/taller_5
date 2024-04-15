import numpy as np
#matplotlib tiene muchos modulos.Importar uno solo
import matplotlib.pyplot as plt

#crear un ndarray de3 1 dimension,100 melementos espaciados, de 0 a 2 *PI
x=np.linspace(0,2*np.pi,100)
y=np.sin(x)

#usar mtplotlib
plt.figure(figsize=(8,4))
plt.title("Mi primer grafico cientifico en programación")
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()