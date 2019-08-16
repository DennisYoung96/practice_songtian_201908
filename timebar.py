import time

scale = 50
print("strat!")
# t = time.clock()
t = time.perf_counter()
for i in range(scale+1):
    a, b = '**' * i,'..' * (scale-i)
    c = (i/scale)*100
    # t -= time.clock()
    t = time.perf_counter()
    # print("%{:^3.0f}[{}-->{}]".format(c,a,b))
    # print("\r{:2}%".format(c),end='')
    print("\r{:^3.0f}%[{}-->{}]{:.2f}seconds".format(c,a,b,t),end='')
    time.sleep(0.1)
print("\nthe end!")
    