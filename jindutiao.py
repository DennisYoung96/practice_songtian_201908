#page94 3.6
import time

# scale = 50
# t = time.perf_counter()
# for i in range(scale):
#     n = ((i+1)/scale)*100 
#     t = time.perf_counter() 
#     print("\rStarting {:3.0f}% Done!".format(n),end='')
#     time.sleep(0.2)

#3.8
from tqdm import tqdm

for i in tqdm(range(1,50)):
    time.sleep(0.1)