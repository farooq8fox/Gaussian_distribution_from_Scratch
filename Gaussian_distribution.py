import matplotlib.pyplot as plt
import numpy as np
import random
from math import exp, sqrt, pi


def mean(array):
    L = len(array)
    sum = 0
    for i in range(L):
        sum = sum + array[i]
    return sum / L


def var(array):
    mu = mean(array)
    L = len(array)
    sum = 0
    for i in range(L):
        sum = sum + (array[i] - mu) ** 2
    return sum / L


def gaussian(array):
  x = array
  m = mean(array)
  v = var(array)
  L = len(array)
  y = [0]*L
  for i in range(L) :
      y[i] = (1/sqrt(2*pi*v)) * (exp(-(x[i]-m)**2/(2*v)))
  return y


# random input
a, b, c = random.randint(1,50), random.randint(60, 200), random.randint(30, 300)
X = np.array([random.randint(a, b) for iter in range(c)])
Y = gaussian(X)

# Parameters
mu = mean(X)
sigma = np.sqrt(var(X))

textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu, ),
    r'$\sigma=%.2f$' % (sigma, )))

fig, ax = plt.subplots()
ax.scatter(X, Y)
# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# place a text box in upper left in axes coords
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

plt.show()