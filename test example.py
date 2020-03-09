#基本用法
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
y = 2*x+1
plt.plot(x,y)		#导入横坐标和纵坐标，函数连续
plt.show()		#展示图片
