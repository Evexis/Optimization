import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def fitFuntion(x, a, b, c):
    return a * np.exp(-b * x) + c

def fitFuntion2(x, a, b):
    return -a * np.sqrt(x) + b

xdata = np.linspace(0, 5, 50)

#function I
ydata = fitFuntion(xdata, 3, 1.6, -0.1) + 0.18 * np.random.normal(size=xdata.size) # adding some random noise

plt.subplot(211)
plt.title('a*exp(-bx)+c')

plt.plot(xdata, ydata, 'bo', label='data')

popt, pcov = curve_fit(fitFuntion, xdata, ydata)
plt.plot(xdata, fitFuntion(xdata, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

popt, pcov = curve_fit(fitFuntion, xdata, ydata, bounds=(-1, [2.5, 1.5, 0.5]))
plt.plot(xdata, fitFuntion(xdata, *popt), 'g--', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

#function II
ydata = fitFuntion2(xdata, -5, 0.25) + 0.5 * np.random.normal(size=xdata.size) # adding some random noise
plt.subplot(212)
plt.title('-a*sqrt(x)+b')
plt.plot(xdata, ydata, 'bo', label='data')

popt, pcov = curve_fit(fitFuntion2, xdata, ydata)
plt.plot(xdata, fitFuntion2(xdata, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f' % tuple(popt))

popt, pcov = curve_fit(fitFuntion2, xdata, ydata, bounds=(-4, [-2., 3.]))
plt.plot(xdata, fitFuntion2(xdata, *popt), 'g--', label='fit: a=%5.3f, b=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()