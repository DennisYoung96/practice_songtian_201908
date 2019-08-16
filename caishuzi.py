#page121 4.5
import random

def fun(a,count = 0):
    try:
        b = -2
        while(b!=a):
            count += 1
            b = eval(input("pls input ur guess number: "))
            if b == -1:
                flag = 1
                break
            if b > a:
                print("it's higher!")
            elif b == a:
                print("u r right！")
                break
            else:
                print("it's lower!")
    except NameError:
        print("the input must be a number!")
        fun(a,count)
    else:
        if flag:
            print("OK,see u next time!")
        else:
            print("game over!\nafter {} times attempt u find the number".format(count))

#random.seed(25)
a = random.randint(0,100)
print("let's start a number guess game, we will define a number between 0 - 100. \
    \n(if u want to quit，pls input -1 anytime!)")
fun(a)
#tmp = fun(a, count)
#print("after {} times attempt u find the number".format(tmp))