﻿import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.stats import chisquare
from sympy import *
import os

#This is just needed for later, you can skip the latex part
message = r""" %% AMS-LaTeX Created with the Wolfram Language : www.wolfram.com

\documentclass{article}
\usepackage{amsmath, amssymb, graphics, setspace}

\newcommand{\mathsym}[1]{{}}
\newcommand{\unicode}[1]{{}}

\newcounter{mathematicapage}
\begin{document}

\begin{doublespace}
\noindent\(\pmb{x\text{:=}\frac{y^2+b}{a};}\\
\pmb{\sigma _y\text{:=}0.05;}\\
\pmb{\sigma _a\text{:=}0.1;}\\
\pmb{\sigma _b\text{:=}0.4;}\\
\pmb{\sigma _x=D[x,y]^2*\sigma _y{}^2+D[x,a]^2*\sigma _a{}^2+D[x,b]^2*\sigma _b{}^2}\)
\end{doublespace}

\begin{doublespace}
\noindent\(\pmb{\frac{\text{{``}0.16{''}}}{a^2}+\frac{\text{{``}0.01{''}} y^2}{a^2}+\frac{\text{{``}0.01{''}} \left(b+y^2\right)^2}{a^4}}\\
\pmb{D[x,y]^2}\)
\end{doublespace}

\begin{doublespace}
\noindent\(\pmb{y\text{:=}1.23;}\\
\pmb{a\text{:=}0.7;}\\
\pmb{b\text{:=}6.7;}\\
\pmb{\text{Out}[38]}\)
\end{doublespace}

\begin{doublespace}
\noindent\(3.16672\)
\end{doublespace}

\begin{doublespace}
\noindent\(\pmb{\text{Sqrt}[\text{Out}[54]]}\)
\end{doublespace}

\begin{doublespace}
\noindent\(1.77953\)
\end{doublespace}

\end{document}
"""
currentDir=os.listdir()
extension = '.csv'

#Import funntion for data in directory
def importCSV(directory,ext):
	global csv
	csv = {}	
	files = []
	for x in directory:
		if ext in x:
			csv[x[:-4]] = np.genfromtxt(x, delimiter=",")
			files.append(x)
	print('The following files have been imported: \n' + str(files)+'\n')
#functions for different opgaver
def f1(t,f,tau):
	return np.exp(-t/tau)*np.sin(2*np.pi*f*t)
def f2(x,a,b):
	return a*x**2 + b
def f3(x,c,d,e,f):
	return c*x**2 + d*np.sin(e*x+f)
def f4(x,a,b):
	return a*x**b
#Imports csv files in the current directory
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
plt.savefig('foo.png')
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
print()
print('####################################')
print('Welcome to opgave 3')
print('####################################\n')
print('We want to fit the data to the model y=c*x^2 + d sin(e*x+f)')
popt1, pcov1 = curve_fit(f3, x, y, sigma=yeps)

print('The best values for c, d, e & f\n')
print(popt1)
print('The best values for the variance on c, d, e & f\n')
print(np.diag(pcov1))
print()

print('####################################')
print('Welcome to opgave 4')
print('####################################\n')
print('Here we calculate the chisquare for opgave 2: ' +str(chisquare(x,f2(x,*popt))))
print('\n')
print('here we calculate it for opgave 3: ' + str(chisquare(x,f3(x,*popt1))))

print('####################################')
print('Welcome to opgave 5')
print('####################################\n')
f = open('calculations.tex','w')

f.write(message)
f.close
y=1.23
a=0.7
b=6.7
sigma_y=0.05
sigma_a=0.1
sigma_b=0.4
sigma_x=1.8
print('Lets use the error propagation law to calculate x with errors\n')
print('if for whatever reason you want to see the calculations i have generated a latex document with the calculations.')
print('we have: \n y = 1.23, sigma_y = 0.05 \n a = 0.7, sigma_a = 0.1 \n b = 6.7, sigma_b = 0.4')
x = (y**2+b)/a
print('we get that sigma_x  = ' + str(sigma_x))
print('Therefore x = ' +str(round(x,1)) +'+-' + str(sigma_x)+'\n')

print('####################################')
print('Welcome to opgave 6')
print('####################################\n')

print('There is no text for this part! Please wait for the plots to be generated')
a = 0.2
b = 1.9
x = csv['exc6'][1:,0]
y = csv['exc6'][1:,1]
e = csv['exc6'][1:,2]

model=f4(x,a,b)
res = model - y

plt.figure(3)
plt.errorbar(x,res,yerr=e,fmt='ro')
plt.plot([0, 18], [0, 0], 'k--', lw=2)
plt.title('Residual plot')
plt.xlabel('x')
plt.ylabel('Residual')
a = plt.axes([0.65, 0.6, 0.2, 0.2])
n, bins, patches = plt.hist(res, 30, normed=1)
plt.title('Histogram')
plt.xticks([])
plt.yticks([])
print('####################################')
print('Welcome to opgave 7')
print('####################################\n')
x = csv['exc7'][1:,0]
y = csv['exc7'][1:,1]
mean = np.mean(x)
std = np.std(x)
weightedList=[]
print('The mean of the values are ' + str(mean))
print('The std of the values are ' + str(std) + '\n')
#plt.figure(4)
#n, bins, patches = plt.hist(x,50,normed=1, color='g')
#plt.axvline(x.mean(), color='k', linestyle='dashed', linewidth=3)
print('We need to remove the values that are less than 3x'+ str(round(std,1)) + 
	' and the values that are greater that 3x' +str(round(std,1))+ '\n')
for i in x:
	if i > mean-3*std and i < mean+3*std:
		weightedList.append(i)
#print(weightedList)
#f = open('test.csv','w')
#for r in weightedList:
#	f.write(str(r)+'\n')
#f.close
newmean = np.mean(weightedList)
newstd = np.std(weightedList)
print('The new mean and new std are in order ' + str(newmean) + ' and ' + str(newstd))


print('\n\n\n#########################')
print('This is the end, thanks for running this script')
print('Regards Christopher Carman')
print('#########################')
plt.show()

