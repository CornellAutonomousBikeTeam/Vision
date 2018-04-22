import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []
path = "functions/data/data.csv"
with open(path, 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		plt.scatter(row[1],row[2])
		plt.draw()
		plt.pause(0.0000001)
