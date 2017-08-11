import numpy as np
import matplotlib.pyplot as plt

# define the co-rdinates
x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, np.tan(x))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()