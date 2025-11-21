import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

daadwerkelijkec = 4.186
t = []
m = 300
dt = 270
R = 10
I = 1.9
dT = 33.9 - 26.1
P = 0
def formuleenergie(I,R):
    P = I**2 * R
    return P
def Warmte(P,dt):
    Q = P * dt
    return Q




def formule(Q, m, dT):
    c = Q/(m * dT)
    return c

P = formuleenergie(I,R)
Q = Warmte(P, dt)
c = formule(Q,m,dT)


data = np.array([
26.1,
26.4,
26.7,
27.0,
27.3,
27.5,
27.8,
28.1,
28.4,
28.7,
29.0,
29.3,
29.6,
29.9,
30.3,
30.6,
30.9,
31.2,
31.5,
31.8,
32.1,
32.4,
32.6,
32.9,
33.1,
33.4,
33.6,
33.9])
print(c)

for i in range(len(data)):
    q = i * 10
    t = np.append(t,q)
print(t)
plt.figure()
plt.plot(t,data)
plt.show()
