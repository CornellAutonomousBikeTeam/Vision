import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import time

dx = 0.0
dy = 0.0
lat0 = 42.4440549
lng0 = -76.482057

while True:
	dx += 50*(np.random.random())
	dy += 50*(np.random.random())
	x = lat0 + (180/np.pi)*(dy/6378137)
	y = lng0 + (180/np.pi)*(dx/6378137)/np.cos(lng0)

	plt.scatter(x, y)
	plt.draw()
	plt.pause(0.00000000001)
