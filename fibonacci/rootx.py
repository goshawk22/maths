from cmath import sqrt
from matplotlib import pyplot as plt
from numpy import linspace


y = lambda x: sqrt(x).real
z = lambda x: sqrt(x).imag

X = linspace(-10, 10, 10000)
Y = [y(x) for x in X]
Z = [z(x) for x in X]

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(X, Y, Z, 'red')
#ax.scatter3D(X, Y, Z, c=X, cmap='cividis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()