import matplotlib.pyplot as plt
import numpy as np

b, a = np.meshgrid(np.linspace(0, 3, 9), np.linspace(0, 2, 9))
print(np.linspace(0, 3, 9))
print(b)
print(a)

c = ( a ** 2 + b ** 2) * np.exp(-a ** 2 - b ** 2)
print(c)
c = c[:-1, :-1]
l_a=a.min()
r_a=a.max()
l_b=b.min()
r_b=b.max()
l_c,r_c  = -np.abs(c).max(), np.abs(c).max()

figure, axes = plt.subplots()

c = axes.pcolormesh(a, b, c, cmap='cool_r', vmin=l_c, vmax=r_c)
axes.set_title('Heatmap')
axes.axis([l_a, r_a, l_b, r_b])
figure.colorbar(c)

plt.show()