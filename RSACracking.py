import random
from time import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def isPrime(p):
    '''checks to see if the number is prime, if prime return=True, if not prime return=False'''
    if p < 2:
        return False
    for i in range(2, int(p**.5) + 1):
        if p % i == 0:
            return False
    return True

def nBitPrime(n):
    '''Makes a random number that is n bits long, creates number then checks if it is prime, if it is prime the number is returned, if not it iterates until a prime number is returned'''
    num = int(random.random() * (2**n))
    if num >= 2 and isPrime(num):
        return num
    else:
        return nBitPrime(n)

pq = nBitPrime(20) * nBitPrime(20)

def factor(pq):
    '''We check every number from 2 to pq and see if it is evenly divisible, it outputs the two factors p and q that are evenly divisable. We know its evenly divisible because of the pq % i'''
    for i in range(2, pq):
        if pq % i == 0:
            return i, pq // i
    return None

n_values = np.arange(15, 30, 1)
times_factorization = []


for n in n_values:
    num = nBitPrime(n)

    t1 = time()
    factors = factor(num)
    t2 = time()

    mtime = (t2-t1) * 1000
    times_factorization.append(mtime)

def exponential(x, a, b):
    return a * np.exp(b * x)

#we will use the scipy package to use curve_fit to fit the exponential curve
params, covariance = curve_fit(exponential, n_values, times_factorization)
fit_a, fit_b = params

fit_y = exponential(n_values, fit_a, fit_b)

#for 1024-bit predicted time
predict_1024bit = exponential(1024, fit_a, fit_b)
print(f"The predicted time for a 1024-bit factoring is {predict_1024bit:.2e} milliseconds or {predict_1024bit / 31557600000:.2e} years.")

#plot for out data and exponential curve
plt.figure(figsize=(10, 5))
plt.plot(n_values, times_factorization, '-o', color='blue', label='Factorization Time')
plt.xlim([n_values[0], n_values[-1]])
plt.plot(n_values, fit_y, '--', label=f'Fit: a={fit_a:2f}, b={fit_b:.2f}')
plt.xlabel('Number of Bits (n)')
plt.ylabel('Time (ms)')
plt.title('Factorization Time vs. Number of Bits')
plt.legend()
plt.show()

#The predicted time for a 1024-bit factoring is 4.65e+264 milliseconds or 1.47e+254 years.