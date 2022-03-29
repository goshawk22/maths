from scipy.constants import golden
from math import sqrt
from matplotlib import pyplot as plt
from matplotlib.colors import Normalize
from numpy import linspace, zeros, set_printoptions, inf
set_printoptions(threshold=inf)


x_max = 5
x_min = 0
y_max = 5
y_min = 0

res = 10

shape = (int((x_max-x_min)*res + 1), int((y_max-y_min)*res) + 1)

fibonacci_term = lambda n: (golden**n - (1 - golden)**n)/sqrt(5)

terms = zeros(shape)

for real in linspace(x_min, x_max, res):
    for imaginary in linspace(y_min, y_max, res):
        number = complex(real=real, imag=imaginary)

        # Get fibonacci value of complex number
        term = fibonacci_term(number)
        terms[real][imaginary] = term

        # Get the modulus of the term
        modulus = sqrt(term.real**2 + term.imag**2)
        print(modulus)

        modulus[int(real*res)][int(imaginary*res)] = modulus

