from scipy.constants import golden
from math import sqrt
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize
from numpy import linspace, zeros, set_printoptions, inf
set_printoptions(threshold=inf)


x_max = 1
x_min = 0
y_max = 1
y_min = 0

res = 10

shape = (len(linspace(x_min, x_max, res)), len(linspace(y_min, y_max, res)))

fibonacci_term = lambda n: (golden**n - (1 - golden)**n)/sqrt(5)

heatmap = zeros(shape)

for real in linspace(x_min, x_max, res):
    for imaginary in linspace(y_min, y_max, res):
        number = complex(real=real, imag=imaginary)
        
        # Get fibonacci value of complex number
        term = fibonacci_term(number)

        # print(term)

        # Get the modulus of the term
        modulus = sqrt(term.real**2 + term.imag**2)
        # print(modulus)
        # print(int(real*res))
        # print(int(imaginary*res))
        print(real)
        print(imaginary)
        print((real*res), round(real*res))
        print((imaginary*res), round(imaginary*res))
        heatmap[round(real*res)-1][round(imaginary*res)-1] = modulus

figure, axes = plt.subplots()

# print(heatmap)
c = axes.imshow(heatmap, origin="lower")
figure.colorbar(c)
plt.show()