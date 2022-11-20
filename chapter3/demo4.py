i=3+4
print(i)
a=b=c=20#链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))


a=20
a+=30
print(a)
a-=10
print(a)

a*=2
print(a)

a/=3
print(a)

a//=2
print(a)

a%=3
print(a)


a,b,c=20,30,40
print(a,b,c)

a,b=10,20
a,b=b,a
print('交换',a,b)