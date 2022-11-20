s='hello,Python'
s1=s[:5]
s2=s[6:]
s3='!'
newstr=s1+s3+s2

print(s1)
print(s2)
print(newstr)
print('-----------------')
print(id(s),id(s1),id(s2),id(s3),id(newstr))

print('--------------')
print(s[1:5:1])#not include 5
print(s[::2])#start=0,step=2
print(s[::-1])
print(s[-6::1])
