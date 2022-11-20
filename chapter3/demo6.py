a,b=1,2
print(a==1 and b==2)#true
print(a==1 and b<2)
print(a!=1 and b==2)
print(a!=1 and b!=2)

print('-----------or------------')
print(a==1 or b==2)
print(a==1 or b<2)
print(a!=1 or b!=2)

print('----------------not-------------对bool类型操作数取反')
f=True
f2=False
print(not f)
print(not f2)

print('---------------------in与not in--------------')
s='helloworld'
print('w' in s)
print('w' not in s)
print('k' not in s)