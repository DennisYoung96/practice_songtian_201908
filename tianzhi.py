#page94 3.5
for i in range(11):
    # print('\n')
    if i in [0,5,10]:
        print('+',end=' ')
        print('- '*4,sep=' ',end='')
        print('+',end=' ')
        print('- '*4,sep=' ',end='')
        print('+',sep=' ')
    else :
        print('| ',end='')
        print('  '*4,end='')
        print('| ',end='')
        print('  '*4,end='')
        print('| ')

# #page94 3.7 
# while True:
#     for i in ["/","-","|","\\","|"]:
#         print("%s\r" % i,end ='')