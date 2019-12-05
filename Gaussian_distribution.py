from math import exp, sqrt, pi

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
      y[i] = (1/sqrt(2*pi*v)) * (exp(-(x[i]-m)**2/(2*v)))
  return y