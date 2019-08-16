#day5
#1
def Narcissistic():
    x= []
    for i in range(100,1000):
        a,b,c = i//100, i//10%10,i%10
        if a**3+b**3+c**3 == i:
            print("{0}^3+{1}^3+{2}^3={3}".format(a,b,c,i))
            x.append(i)
    print("the end!")
# Narcissistic()

def Perfect(n=3):
    i, j = 0, 2
    while i<=n:
        s = 0
        for k in range(1,j//2+1):
            if j%k == 0:
                s += k
        if s == j:
            i +=1
            print("number{0}:{1}".format(i,j))
        j+=1
    print("the end!")
# Perfect()

def hundred():
    for a in range(0,20):
        if (200-14*a)%8 != 0:
            continue
        elif (200-14*a)/8 < 0 or (200-14*a)/8 >33:
            continue
        else:
            b = (200-14*a)/8
            if (100-a-b)%3 != 0:
                continue
            else:
                c = 100-a-b
                print("a={0},b={1},c={2}".format(a,b,c))
    print("the end!")
# copy
# def hundred():
#     for x in range(0, 20):
#         for y in range(0, 33):
#             z = 100 - x - y
#             if 5 * x + 3 * y + z / 3 == 100:
#                 print('公鸡: %d只, 母鸡: %d只, 小鸡: %d只' % (x, y, z))
# hundred()