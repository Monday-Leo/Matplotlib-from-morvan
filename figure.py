#figure图像
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure()				#创建一个figure
plt.plot(x,y1)				#导入横坐标和纵坐标

plt.figure(num=3,figsize = (8,5))	#创建第二个figure，并且编号3，长宽定为8和5
plt.plot(x,y2)				#导入y2
plt.plot(x,y1,color = 'red',
	linewidth = 10,linestyle = '--')#导入y1,颜色红色，线宽10，改为虚线

plt.show()				#展示图片
