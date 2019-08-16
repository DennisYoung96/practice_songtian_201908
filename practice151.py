#page151 practice

#5.1
def tianzi():
    for i in range(21):
        if i in [0,5,10,20,15]:
            a = ' + - - - -'
            print(a * 4,'+')
        else:
            b = ' |        '
            print(b*4,'|')

#5.2
def isOdd(a):
    if isinstance(a, int):
        if a%2 == 0:
            return False
        else:
            return True
    else:
        s = "it's not a int!"
        return s
# print(isOdd(0))
# print(isOdd(-3))
# print(isOdd(2.000))
# print(isOdd('2.000'))

#5.3
def isNum(s):
    try:
        a = eval(s)
        if isinstance(a, int) or isinstance(a, float) or isinstance(a, complex):
            return True
        else:
            return False
    except NameError:
        return False
# print(isNum(' 0.33'))
# print(isNum('asdas456465'))
# print(isNum('0.335+2j'))

#5.4 + liaoxuefeng
# def multi(*a):
def product(*a):
    if not a:
        # return None
        raise TypeError
    else:
        s = 1
        for i in a:
            s *= i
        return s
# print(multi(3,4,5,6))
# print(multi(3))
# print(multi())
# print(multi((3,4)))
# print('product(5) =', product(5))
# print('product(5, 6) =', product(5, 6))
# print('product(5, 6, 7) =', product(5, 6, 7))
# print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
# if product(5) != 5:
#     print('测试失败!')
# elif product(5, 6) != 30:
#     print('测试失败!')
# elif product(5, 6, 7) != 210:
#     print('测试失败!')
# elif product(5, 6, 7, 9) != 1890:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试失败!')
#     except TypeError:
#         print('测试成功!')

#5.5
def isPrime(x):
    try:
        if not isinstance(x, int):
            raise TypeError
        elif x <= 1:
            return 'the int should greater than 1'
        else:
            flag = 0
            for i in range(2,round(x/2)+1):
                if x % i == 0:
                    flag = 1
                    break
            if flag:
                return False
            else:
                return True
    except TypeError:
        return 'Wrong Type'
        
# print(isPrime(39999931))
# print(isPrime(57))
# print(isPrime('s'))
# print(isPrime(3.0))
# print(isPrime('2'))
# print(isPrime(1))
# print(isPrime(0))
# print(isPrime(-2))

#5.7 copy自网络，增加了计数器count
def hanoi(n, a, b, c, count = 0):
    if n == 1:
        print(a, '-->', c)
        count += 1
    else:
        count += hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        count += 1
        count += hanoi(n - 1, b, a, c)
    return count
# print(hanoi(10, 'A', 'B', 'C'))