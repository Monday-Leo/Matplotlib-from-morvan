#散点图scatter()
import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0,1,1024)		#随机生成平均数为1，方差为1的1024个数
Y = np.random.normal(0,1,1024)
T = np.arctan2(Y,X)

plt.scatter(X,Y,s=75,c=T,alpha=0.5)	#生成离散点阵，颜色为T，透明度0.5

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
plt.xticks(())
plt.yticks(())

plt.show()
