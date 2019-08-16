#page 121 4.6
import random

men = ['goat','goat','car']
n = 10000
i = 0
count1, count2 = 0, 0
while(i<=n):
    random.shuffle(men)
    a = random.randint(0,2)
    b = [x for x in range(3) if x != a]
    if men[b[0]] == 'goat':
        c = b[1]
    if men[b[1]] == 'goat':
        c = b[0]
    if men[c] == 'car':
        count1 += 1
    if men[a] == 'car':
        count2 +=1
    i += 1

print("模拟{}次，换了选择获胜概率为{:.2%},不换选择获胜概率为{:.2%}".format(n, count1/n, count2/n))