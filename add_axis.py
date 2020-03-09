#一个figure中显示多张图表
import matplotlib.pyplot as plt

plt.figure()

plt.subplot(2,2,1)	#分为两行两列，图表添加在第一个位置
plt.plot([0,1],[0,1])

plt.subplot(2,2,2)
plt.plot([0,1],[0,2])

plt.subplot(2,2,3)
plt.plot([0,1],[0,3])

plt.subplot(2,2,4)
plt.plot([0,1],[0,4])

plt.show()

#其他方法
#ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)
#分为3行3列，起始在第一行第一列，垮3列，跨1行
