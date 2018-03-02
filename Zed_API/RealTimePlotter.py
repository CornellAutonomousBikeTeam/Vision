
import matplotlib.pyplot as plt
import numpy as np
import time

import gmplot

x = 0.0
y = 0.0

gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)

while True:
	x += random.random()
	y += random.random()
	time.sleep(0.5)

	gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
	gmap.scatter(more_lats, more_lngs, '#3B0B39', size=40, marker=False)
	gmap.scatter(marker_lats, marker_lngs, 'k', marker=True)
	gmap.heatmap(heat_lats, heat_lngs)

	gmap.draw("mymap.html")

plt.ion() ## Note this correction
fig=plt.figure()
plt.axis([0,1000,0,1])

i=0
x=list()
y=list()

while i <1000:
    temp_y=np.random.random();
    x.append(i);
    y.append(temp_y);
    plt.scatter(i,temp_y);
    i+=1;
    plt.show()
    plt.pause(0.0001) #Note this correction
