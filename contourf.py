#等高图contourf()
import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
	z = (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)	
	return z

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)		#绑定网格

plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)
#设置等高图三个坐标，分成10块，透明度0.75，颜色hot

C = plt.contour(X,Y,f(X,Y),8,colors='black')
#画出等高线

plt.clabel(C,inline = True,fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()
