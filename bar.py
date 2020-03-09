#条形图bar()
import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1-X/n)*np.random.uniform(0.5,1.0,n) #随机生成从0.5到1.0共n个数
Y2 = (1-X/n)*np.random.uniform(0.5,1.0,n)

plt.bar(X,Y1,facecolor='#9999ff',edgecolor='white') #生成条形图，并改变主体和边框颜色
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')

for x,y in zip(X,Y1):
	plt.text(x,y+0.05,'%.2f'%y,ha='center',va='bottom')
#生成标注，水平方向居中，数值方向沉底

for x,y in zip(X,Y2):
	plt.text(x,-y-0.05,'-%.2f'%y,ha='center',va='top')
#生成标注，水平方向居中，数值方向沉底

plt.xlim(-0.5,n)
plt.ylim(-1.25,1.25)
plt.xticks(())
plt.yticks(())

plt.show()
