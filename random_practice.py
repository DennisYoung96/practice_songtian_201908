import random 

#4.18(1)
ls = []
for i in range(10):
    ls.append(random.randint(0,100))
print(ls)
# print(random.sample(range(101),10))

#(2)
a = [2*x+1 for x in range(50)]
ls2 = []
for i in range(10):
    ls2.append(random.choice(a))
print(ls2)

#(3)
st = 'abcdefghij'
print(random.sample(st,4))

#(4)
st2 = ['apple','pear','peach','orange','banana']
print(random.sample(st2,1))
