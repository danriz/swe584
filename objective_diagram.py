import matplotlib.pyplot as plt
import numpy as np

X, Y = np.loadtxt('c1.txt', delimiter=';', unpack=True)

plt.scatter(X, Y, c='coral')

X, Y = np.loadtxt('c2.txt', delimiter=';', unpack=True)

plt.scatter(X, Y, c='lightblue')


X, Y = np.loadtxt('c3.txt', delimiter=';', unpack=True)

plt.scatter(X, Y, c='grey')

X, Y = np.loadtxt('finalcenters.txt', delimiter=';', unpack=True)

plt.scatter(X, Y, c='black')


plt.title('Scatter Diagram of final 3 data set')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
