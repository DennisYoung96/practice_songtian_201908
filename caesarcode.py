import numpy as np 

ming = input("请输入明文：")
mi = ''
for m in ming:
    if ord('a') <= ord(m) <=ord('z'):
        mi += chr(ord('a')+(ord(m)-ord('a')+3)%26)
        print(chr(ord('a')+(ord(m)-ord('a')+3)%26),end='')
    elif ord('A') <= ord(m) <=ord('Z'):
        mi += chr(ord('A')+(ord(m)-ord('A')+3)%26)
        print(chr(ord('A')+(ord(m)-ord('A')+3)%26),end='')
    else:
        mi += m
        print(m,end='')

#jiema
#print('\n'+mi)
print('\n 解码后：')
for n in mi:
    if ord('a') <= ord(n) <=ord('z'):
        print(chr(ord('a')+(ord(n)-ord('a')-3)%26),end='')
    elif ord('A') <= ord(n) <=ord('Z'):
        print(chr(ord('A')+(ord(n)-ord('A')-3)%26),end='')
    else:
        print(n,end='')    
