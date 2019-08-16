# #page77 3.12
# for i in range(1,11):
#     n = i/1000
#     x = 1.0
#     for j in range(365):
#         if j%7 in [1,2,3,4]:
#             x *=(1+n)
#         else:
#             pass
#     print('N={}时，年终值={}'.format(n,x))

# #page78 3.13
# for i in range(1,11):
#     n = i/1000
#     x = 1.0
#     for j in range(365):
#         if j%7 in [1,2,3,4,5]:
#             x *=(1+n)
#         else:
#             pass
#     print('N={}时，年终值={}'.format(n,x))

# #page78 3.15
# for i in range(1,11):
#     n = i/1000
#     x = 1.0
#     for j in range(360):
#         if j%30 < 10:
#             x *=(1+n)
#         else:
#             pass
#     print('N={}时，年终值={}'.format(n,x))
# #page93 3.2
# n = 1/100
# x = 1.0
# for j in range(365):
#     if j%7 > 2:
#         x *=(1+n)
#     else:
#         pass
# print('N={}时，年终值={}'.format(n,x))
#page93 3.3
n = 1/100
x = 1.0
a = [i*11 for i in range(1,34)]
j = 1
while (j <=365):
    for i in range(7):
        if (i+j in a) or (i+j > 365):
            j = j+i+1
            break
        elif i in [0,1,2]:
            pass
        elif i in [3,4,5]:
            x *= (1+n)
        else :
            x *= (1+n)
            j += 7
print('N={}时，年终值={}'.format(n,x))
# print(j,i)