#设置坐标轴与图例legend()
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure(num=3,figsize = (8,5))	#创建第二个figure，并且编号3，长宽定为8和5
l1,=plt.plot(x,y2)				#导入y2
l2,=plt.plot(x,y1,color = 'red',
	linewidth = 10,linestyle = '--')#导入y1,颜色红色，线宽10，改为虚线


plt.xlim((-1,2))			#x展示的范围
plt.ylim((-2,3))			#y展示的范围
plt.xlabel('I am X')			#在x轴下册给x加标签
plt.ylabel('I am Y')			#在y轴左侧给y加标签

new_ticks = np.linspace(-1,2,5)
plt.xticks(new_ticks)			#改变x轴上上的数字
plt.yticks([-2,-1.8,-1,1.22,3],
	   [r'$really\ bad$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$'])
#将y轴数改为文字，$用于改变字体，空格需要\转译

ax = plt.gca()  			
ax.spines['right'].set_color('none')	#去掉右边框线
ax.spines['top'].set_color('none')	#去掉顶部框线
ax.xaxis.set_ticks_position('bottom')	#将底部框线设置为x轴
ax.yaxis.set_ticks_position('left')	#将左边框线设置为y轴
ax.spines['bottom'].set_position(('data',1))#将x轴位置放在y=1的位置
ax.spines['left'].set_position(('data',0))#将y轴位置放在x=0的位置

plt.legend(handles=[l1,l2],labels=['a','b'],loc='best')
#在最佳位置显示图例

plt.show()				#展示图片

