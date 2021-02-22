import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,2*np.pi,0.01)
y1=np.sin(x)
y2=np.cos(x)

plt.title('plot of sinx and cosx') 
plt.plot(x,y1,color="blue")
plt.plot(x,y2,color="red")
plt.legend(['y=sinx','y=cosx'])







