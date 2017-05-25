import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

importCSV(currentDir,extension)

print('####################################')
print('Welcome to opgave 1')
print('####################################\n')


print('####################################')
print('Welcome to opgave 2')
print('####################################\n')

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