# import pandas
import numpy
import torch

# # 1.打印99乘法表
# for i in range(1,10):
#     # print('\n')
#     s = ''
#     for j in range(1,i+1):
#         s += str(j)+'*'+str(i)+'='+str(i*j)+'\t'
#     print(s)  

# # 2.一行代码编写一个回声程序，将用户输入的内容直接打印出来
# print("您输入的是 = {}".format(input("回声程序=")))

#海龟画画
import turtle

# #画标靶
# pensize = 10
# circle_r = 20
# turtle.setup(192*6,108*6,400,300)
# turtle.pensize(pensize)
# turtle.pencolor("gold")
# for i in range(9):
#     if i >0 :
#         turtle.pu()
#         turtle.seth(0)
#         turtle.fd(circle_r)
#     turtle.pd()
#     turtle.seth(90)
#     turtle.circle(i*circle_r)
# turtle.done()

#画六芒星
import math
pensize = 10
l = 300
turtle.setup(192*6,108*6,400,300)
turtle.pensize(pensize)
turtle.pencolor("gold")
    
turtle.pu()
turtle.seth(180)
turtle.fd(l*math.sqrt(3)/3)
turtle.seth(30)
turtle.pd()
turtle.fd(l)
turtle.seth(-90)
turtle.fd(l)
turtle.seth(150)
turtle.fd(l)

turtle.pu()
turtle.seth(60)
turtle.fd(l*math.sqrt(3)/3)
turtle.seth(-30)
turtle.pd()
turtle.fd(l)
turtle.seth(-150)
turtle.fd(l)
turtle.seth(90)
turtle.fd(l)

turtle.done()