import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

K = 5   
L = 3 
G = 1  
Tw = 1  

nx, ny = 50, 50  
x = np.linspace(0, L, nx)
y = np.linspace(0, L, ny)
X, Y = np.meshgrid(x, y)

T = ((G * L) / (2 * K)) * (1 - (X / L)) + Tw

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, T, cmap='coolwarm')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Temperature')
ax.set_title('Temperature Distribution Across the Wall')

# Add a color bar
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
