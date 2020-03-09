#展示图片
import matplotlib.pyplot as plt
import numpy as np

# image data
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)

#a为虚拟图片

plt.imshow(a, interpolation='nearest', cmap='bone', origin='lower')
#展示a,格式为nearest最清楚，向下展示，向上为upper
plt.colorbar(shrink=.92)
#旁边显示涂色，缩放比92%

plt.xticks(())
plt.yticks(())
plt.show()
