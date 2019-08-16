#practice180

#6.1 
import random
def fun1():
    a = [chr(i) for i in range(ord('a'),ord('z')+1)]
    a += [chr(i) for i in range(ord('A'),ord('Z')+1)]
    a += [i for i in range(1,10)]

    for j in range(10):
        # b = []
        # for k in range(8):
        #     b.append( random.choice(a))
        b = ''
        for k in range(8):
            b += str(random.choice(a))
        print(b)

#6.3
def fun3(x):
    if not isinstance(x, list):
        return "it's not a list"
    else:
        s = set(x)
        if len(s)<len(x):
            return True
        else :
            return False
# print(fun3([5,6,5,7,8,5,';']))
# print(fun3([]))
# print(fun3([5,6,7,8,';']))
# print(fun3({5,6,5,7,8,5,';'}))

#6.5
import random
def fun5(n, y=23):
    month = [x for x in range(1,13)]
    count = 0
    for i in range(n):
        shengri = set()
        for j in range(y):
            m = random.choice(month)
            if m in [1,3,5,7,8,10,12]:
                day = [x for x in range(1,32)]
            elif m in [4,6,9,11]:
                day = [x for x in range(1,31)]
            else:
                day = [x for x in range(1,29)]
            d = random.choice(day)
            shengri.add((m,d))
        if len(shengri) < y:
            count += 1
    return float(count/n)

cishu = 10000
fangjian = [10,23,30,60]
for i in fangjian:
    print("模拟{0}次，若一个班级有{1}人，则至少有两人同月同日生的概率为{2:.2%}".format(cishu,i,fun5(cishu, i)))


