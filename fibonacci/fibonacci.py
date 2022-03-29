from scipy.constants import golden
from cmath import sqrt
from matplotlib import pyplot as plt
from numpy import linspace

def drange(start, stop, step):
    values = []
    r = start
    while r <= stop:
        values.append(r)
        r += step
    
    return values

#print(golden)


fibonacci_term = lambda n: (golden**n - (1 - golden)**n)/sqrt(5)

#print(fibonacci_term(0.1))

#print(drange(0, 1, 0.1))

print(linspace(0, 1, 1001))
'''
X = [fibonacci_term(x).real for x in linspace(0, 6, 10001).tolist()]
Y = [fibonacci_term(x).imag for x in linspace(0, 6, 10001).tolist()]

plt.plot(X,Y, color='red')
plt.axvline(x=0, c="black", label="x=0")
plt.axhline(y=0, c="black", label="y=0")
plt.show()
'''
'''
complex_num = lambda real: complex(0, real)

X = linspace(0, 10, 1001)
Y = linspace(0, 10, 1001)
Z = [sqrt(fibonacci_term(x + complex_num(x)).real**2 + fibonacci_term(x + complex_num(x)).imag**2) for x in X]


fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot3D(X, Y, Z, 'red')
#ax.scatter3D(X, Y, Z, c=X, cmap='cividis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
'''

X = linspace(0, 6, 10001)
Y = []
for x in X:
    term = fibonacci_term(x)
    real = term.real
    imag = term.imag
    print(real, imag)
    real_square = real**2
    imag_square = imag**2
    print(real_square, imag_square)
    sum = real_square + imag_square
    mod = sqrt(sum.real)
    print(mod.real)
    Y.append(mod.real)

#Y = [sqrt((fibonacci_term(x).real**2) + (fibonacci_term(x).imag)**2) for x in X]

test_x = fibonacci_term(1.2).imag**2
test_y = fibonacci_term(1.2).real**2
test_add = test_x + test_y
print(test_x)
print(test_y)
print(test_add)
print(sqrt(test_add).real)


#print(Y)

plt.plot(X,Y, color='red')
plt.axvline(x=0, c="black", label="x=0")
plt.axhline(y=0, c="black", label="y=0")
plt.show()