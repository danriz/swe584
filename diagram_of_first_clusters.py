import matplotlib.pyplot as plt
import numpy as np

X, Y = np.loadtxt('objective.txt', delimiter=';', unpack=True)

plt.plot(X, Y)
plt.title('cluster center differences')
plt.xlabel('iteration')
plt.ylabel('objective function')
plt.show()
