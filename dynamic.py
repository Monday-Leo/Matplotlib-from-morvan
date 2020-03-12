import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots()
y1=[]
for i in range(50):
    a = np.random.uniform(1,0)
    y1.append(a)
    ax.cla()
    ax.plot(y1,label='test')
    ax.legend()
    plt.pause(0.1)
