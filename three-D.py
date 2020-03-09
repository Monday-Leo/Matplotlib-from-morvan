#3D图像plot_surface()
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)		#创建3D
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)   	#绑定网格
R = np.sqrt(X**2+Y**2)
Z=np.sin(R)*1.2

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap='rainbow')
#创建图像，分割为1*1，颜色为彩虹
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')
#建立等高图，沿着z轴投影，投影到z=-2平面

ax.set_zlim(-2,2)
plt.show()
