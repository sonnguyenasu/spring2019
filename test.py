import numpy as np
import matplotlib.pyplot as plt
X = np.arange(-10,10,0.001)
rho = 0.01
y = np.exp(-(X-2)**2)/(2*rho**2*np.sqrt(np.pi))
plt.plot(X,y)
plt.show()