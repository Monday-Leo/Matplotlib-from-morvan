#动画animation
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig,ax = plt.subplots()
x = np.arange(0,2*np.pi,0.01)
line,=ax.plot(x,np.sin(x))

def animate(i):
	line.set_ydata(np.sin(x+i/10.0))
	#print(i)	#i从0自动累加到frame-1后重置
	return line,

def init():
	line.set_ydata(np.sin(x))
	return line,

ani = animation.FuncAnimation(fig=fig,func=animate,frames=100,init_func=init,interval=100,blit = False)
#首先执行init初始化，再执行func函数，frames表示变量i范围，执行完之后，自动重复init
plt.show()
