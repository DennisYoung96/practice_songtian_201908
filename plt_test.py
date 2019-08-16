#0812
# import matplotlib.pyplot as plt

# plt.figure(figsize = (8,4),facecolor = 'skyblue')
# plt.show()

#plot triangle
import numpy as np  
import matplotlib.pyplot as plt
# x = np.linspace(0, 3*np.pi, 1000)
# y = np.cos(2 * np.pi * x) * np.exp(-x)+1
# y2 = np.cos(2 * np.pi * x) +1
# #'*' is not a valid value for ls; supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
# plt.plot(x, y, color='r', linewidth=3, linestyle="solid") 
# plt.plot(x, y2, color='b', linewidth=3, linestyle="dashed") 
# # plt.legend('y','y2')
# plt.show()

# import matplotlib
# matplotlib.rcParams['font.family']='SimSun'
# matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# plt.plot([1,2,4], [1,2,3])
# plt.title("坐标系标题")
# plt.xlabel('时间 (s)')
# plt.ylabel('范围 (m)')
# plt.xticks([1,2,3,4,5],[r'$\pi/3$', r'$2\pi/3$', r'$\pi$',\
#                    r'$4\pi/3$', r'$5\pi/3$'])
# plt.show()



x = np.linspace(0, 10, 1000)
y = np.cos(2*np.pi*x) * np.exp(-x)+0.8
plt.plot(x,y,'k',color='r',label="$exp-decay$",linewidth=3)
plt.axis([0,6,0,1.8])
ix = (x>0.8) & (x<3)
plt.fill_between(x, y ,0, where = ix, 
                         facecolor='grey', alpha=0.25)
plt.text(0.5*(0.8+3), 0.2, r"$\int_a^b f(x)\mathrm{d}x$",
                horizontalalignment='center')
plt.legend()
plt.show()
