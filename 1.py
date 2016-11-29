from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm

tau = 0.01
h = 0.1
N = 100000

def f(x, t):
    return x*(x + 2*t) + 1

def U(x, t):
    return t*x**2 + x

def phi(t):
    return 0

def psi(x):
    return x

X = [[i*h for j in range(100000)] for i in range(100000)]
Y = [[j*tau for j in range(100000)] for i in range(100000)]
Z = [[0 for j in range(100000)] for i in range(100000)]

X1 = [[i*h for j in range(100000)] for i in range(100000)]
Y1 = [[j*tau for j in range(100000)] for i in range(100000)]
Z1 = [[U(X1[i][j], Y1[i][j]) for j in range(100000)] for i in range(100000)]

def U_sol(i, j):
    return tau*h/(tau + h)*(f(X[i][j], Y[i][j]) + Z[i][j-1]/tau + Z[i-1][j]/h)

print(X[0])
print(Y[0])

for i in range(100000):
    Z[i][0] = psi(X[i][0])

for j in range(100000):
    Z[0][j] = phi(Y[0][j])

for i in range(1, 100000):
    for j in range(1, 100000):
        Z[i][j] = U_sol(i, j)

fig = plt.figure()
ax = fig.gca(projection='3d')
# X, Y, Z = axes3d.get_test_data(0.05)
# print(Y)
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3, color='red')
ax.plot_surface(X1, Y1, Z1, rstride=8, cstride=8, alpha=0.3, color='green')
# cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
# cset = ax.contour(X, Y, Z, zdir='x', offset=0, cmap=cm.coolwarm)
# cset = ax.contour(X, Y, Z, zdir='y', offset=0, cmap=cm.coolwarm)

ax.set_xlabel('X')
ax.set_xlim(0, 100*h)
ax.set_ylabel('Y')
ax.set_ylim(0, 100*tau)
ax.set_zlabel('Z')
ax.set_zlim(-300*h, 300*h)

plt.show()
