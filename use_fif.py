import fif
import numpy as np
import matplotlib.pyplot as plt

#u = np.array([0.0,0.4,0.7,1.0])
#v = np.array([0.0,0.5,0.2,0.0])
u = np.random.uniform(low=0.0, high=1.0, size=(5,))
v = np.random.uniform(low=0.0, high=1.0, size=(5,))
U = np.vstack((u,v)).T
U = fif.G( U, 0.1, balance=0 )
X = fif.FIF( U, 0.01, balance=1 )

plt.plot( U[:,0], U[:,1], '.-' )
plt.show()
plt.plot( X[:,0], X[:,1], '.-' )
plt.show()
