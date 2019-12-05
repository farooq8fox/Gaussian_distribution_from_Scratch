import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import spline
from Gaussian_distribution import mean, var, gaussian

#=====================================================

# Input Array 
X = np.array([1,2,3,4,5,6,7,8,9,10])


# Parameters
mu = mean(X)
sigma = np.sqrt(var(X))
Y = gaussian(X)
Y_array = np.array(Y)

# Defining number of intervals 
L = len(X)
if L < 100 :
    P = 300
else :
    P = L

# Plot 
X_new = np.linspace(X.min(), X.max(), P)  
Y_new = spline(X, Y_array, X_new)

print(f"\n The Mean is : {mu}", f"\n The Stddev is : {sigma}")

plt.plot(X_new, Y_new)
plt.show()