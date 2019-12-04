import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline 
import math

#================================================================

def mean(array):
    L = len(array)
    sum = 0
    for i in range(L):
        sum = sum + array[i]
    return sum / L

#================================================================

def var(array):
    mu = mean(array)
    L = len(array)
    sum = 0
    for i in range(L):
        sum = sum + (array[i] - mu) ** 2
    return sum / L

#================================================================

def gaussian(array):
  x = array
  m = mean(array)
  v = var(array)
  L = len(array)
  y = [0]*L
  for i in range(L) :
      y[i] = (1/math.sqrt(2*math.pi*v)) * (math.exp(-(x[i]-m)**2/(2*v)))
  return y

#================================================================

X = np.array([1,2,3,4,5])
K = gaussian(X)
Y = np.array(K)

X_new = np.linspace(X.min(), X.max(), 300)  

Y_smooth = spline(X, Y, X_new)

plt.plot(X_new, Y_smooth)
plt.show()