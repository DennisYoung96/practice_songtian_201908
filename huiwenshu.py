#回文数 page93 3.4
def fun():
    # n = eval(input('请输入一个回文数：'))
    n = input('请输入一个回文数：')
    if n == '-1':
        print("{:-^20}".format('game over!'))
        return n
    elif not n.isnumeric():
        print("{:-^20}".format("retry!"))
        return fun()
    else:
        # m = ''
        # for i in range(1,len(n)+1):
        #     m += n[-i]
        m = n[-1:-1-len(n):-1] 

        if m in n and n in m:
            print("{:-^20}".format('True'))
        else:
            print("{:-^20}".format('False'))
        return fun()

fun()