import torch

conv = torch.nn.Conv2d(3,9,kernel_size = 3, stride=1, padding=1)
inputs = torch.randn(10,3,200,200)
outputs = conv(inputs)
print(outputs.size())