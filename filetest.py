
f = open("C:/Windows/WindowsUpdate.txt",'r+')
ls = ['ni','\n','hao\n','a']
# f.writelines(ls)
# f.seek(0)
for i in f:
    print(i)
f.close()