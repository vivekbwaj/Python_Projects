import numpy as np
import matplotlib.pyplot as plt

def shoot():
    plt.xlabel('Angle [rad]')
    plt.ylabel('tan(x)')
    plt.axis('tight')
    plt.show()

# define the co-rdinates
x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, np.tan(x))
shoot()

plt.plot(x, np.sin(x))
shoot()

plt.plot(x, np.cos(x))
shoot()
