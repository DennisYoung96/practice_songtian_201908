# practice259.py
#fangbo page259 9.1
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# def fun(t,w=1, k= 100):
#     s = 0
#     for j in range(1,k):
#         s += 4*np.sin((2*j -1)*w*t)/((2*j-1)*np.pi)
#     return s

# t = np.linspace(0, 4*np.pi, 1000)
# f = fun(t,3) #t为时间信号，w为周期，k为正弦波个数
# plt.subplot(111)
# plt.plot(t, f, 'b',label = "方波",linewidth = 1)
# plt.xlabel('时间(s)')
# plt.ylabel('幅度')
# plt.title("方波的无穷级数拟合")
# plt.legend()
# # plt.savefig('fangbo.JPG')
# plt.show()

# 9.2
# ρ=a(1+cosθ)（心型朝右）
# ρ=a(1-cosθ)（心型朝左）
x = np.linspace(0, 2*np.pi,100)
y1 = (1+np.cos(x))*8
y2 = (1-np.cos(x))*8
y3 = (1+np.sin(x))*8
y4 = (1-np.sin(x))*8
fig = plt.figure(facecolor="white")
plt.subplot(111,polar = True)
plt.plot(x, y1, 'b',label = 'right', linewidth = 2)
# plt.fill(x, y1, facecolor = 'b')
plt.plot(x, y2, 'r',label = 'left', linewidth = 2)
# plt.fill(x, y2, facecolor = 'r')
plt.plot(x, y3, 'k',label = 'top', linewidth = 2)
# plt.fill(x, y3, facecolor = 'k')
plt.plot(x, y4, 'y',label = 'bottom', linewidth = 2)
# plt.fill(x, y4, facecolor = 'y')
plt.legend()
plt.savefig('heartcurve.jpg')
plt.show()