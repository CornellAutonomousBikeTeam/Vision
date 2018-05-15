import numpy as np 
import matplotlib.pyplot as plt

og = np.load('og.npy').reshape(128,109)

print(og)

plt.imshow(og)
plt.show()