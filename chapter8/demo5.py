s={2,3,4,5,6,6,7,7}#no repeat
print(s)

s1=set(range(6))
print(s1,type(s1))

s2=set([1,2,4,5,5,5,6,6])
print(s2,type(s2))

s3=set((1,2,4,4,5,65))#disorder
print(s3,type(s3))

s4=set('python')
print(s4,type(s4))

s5=set({12,34,556,45})
print(s5,type(s5))
#define an empty collection
s6={}
print(type(s6))

s7=set()
print(s7,type(s7))