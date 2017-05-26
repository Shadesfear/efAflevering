import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os

currentDir=os.listdir()
extension = '.csv'

def importCSV(directory,ext):
	global csv
	csv = {}	
	files = []
	for x in directory:
		if ext in x:
			csv[x[:-4]] = np.genfromtxt(x, delimiter=",")
			files.append(x)
	print('The following files have been imported: \n' + str(files)+'\n')
def f1(t,f,tau):
	return np.exp(-t/tau)*np.sin(2*np.pi*f*t)
def f2(x,a,b):
	return a*x**2 + b
def f3(x,c,d,e,f):
	return c*x**2 + d*np.sin(e*x+f)

importCSV(currentDir,extension)

print('####################################')
print('Welcome to opgave 1')
print('####################################\n')
f = 0.629
tau = 19.0
time = csv['exc1'][1:,0]
signal = csv['exc1'][1:,1]
error = csv['exc1'][1:,2]
print('Here we have f = '+str(f)+' and t = '+str(tau)+'\n')

print('generating plot!')
plt.figure(1)
line2, = plt.plot(time,f1(time,f,tau), label = "Theoretical Model")
line1 = plt.errorbar(time, signal,yerr = error, fmt='o', label = 'Raw Data')
plt.title('Signal as a function of time')
plt.xlabel('Time [s]')
plt.ylabel('Signal [mV]')
first_legend = plt.legend(handles = [line1], loc=1)
ax = plt.gca().add_artist(first_legend)
second_legend = plt.legend(handles = [line2], loc=4)
#plt.show()
print('####################################')
print('Welcome to opgave 2')
print('####################################\n')
x = csv['exc2'][1:,0]
y = csv['exc2'][1:,1]
yeps = csv['exc2'][1:,2]
ydata = csv['exc2'][1:,1]+csv['exc2'][1:,2]

print('We want to fit the data to the model y=a x^2 + b')

popt, pcov = curve_fit(f2, x, y, sigma=yeps)
print('The best values for a & b \n')
print(popt)
print()
print('The best values for the variance on a & b\n')
print(np.diag(pcov))
#plt.figure(2)
#plt.plot(x,y,'ro')
#plt.plot(x,f2(x,*popt))
#plt.plot(x,f2(x,2.1,0.45))
#plt.show()

print('####################################')
print('Welcome to opgave 3')
print('####################################\n')


print('####################################')
print('Welcome to opgave 4')
print('####################################\n')


print('####################################')
print('Welcome to opgave 5')
print('####################################\n')


print('####################################')
print('Welcome to opgave 6')
print('####################################\n')


print('####################################')
print('Welcome to opgave 7')
print('####################################\n')