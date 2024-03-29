#e17.1HandDrawPic.py
from PIL import Image
import numpy as np
vec_el = np.pi/2.2 # 光源的俯视角度，弧度值
vec_az = np.pi*3/4. # 光源的方位角度，弧度值
depth = 50. # (0-100)
im = Image.open('yy8.jpg').convert('L')
a = np.asarray(im).astype('float')
grad = np.gradient(a) #取图像灰度的梯度值
grad_x, grad_y = grad #分别取横纵图像梯度值
grad_x = grad_x*depth/100.
grad_y = grad_y*depth/100.
dx = np.cos(vec_el)*np.cos(vec_az) #光源对x 轴的影响
dy = np.cos(vec_el)*np.sin(vec_az) #光源对y 轴的影响
dz = np.sin(vec_el) #光源对z 轴的影响
A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A
a2 = 255*(dx*uni_x + dy*uni_y + dz*uni_z) #光源归一化
a2 = a2.clip(0,255)
im2 = Image.fromarray(a2.astype('uint8')) #重构图像
im2.save('yy8n_HandDraw.jpg')

# im0 = np.array(Image.open("img3.jpg").convert('L'))
# im1 = 255  - im0
# im2 = 150 + (100/255)*im0
# im3 = 255*(im1/255)**2
# p = Image.fromarray(np.uint(im3))
# p.show()
