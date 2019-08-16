#BBP PI
import time
import math
k = 0
pi = 0
n = 100
t = time.perf_counter()
print("start!")
while(k<=n):
    t = time.perf_counter()
    pi += (4.0/(8*k+1)-2.0/(8*k+4)-1/(8*k+5)-1/(8*k+6))/math.pow(16,k)
    print("\rprocessing {:.0%} Done! {:.2f}seconds pi = {:.64f}".format(k/n,t,pi),end='')
    time.sleep(0.1)
    k += 1
print("\nfinished! pi = {:.8f}".format(pi))