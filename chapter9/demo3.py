s='hello,python'
a=s.upper()#new string subject
print(a,id(a))
print(s,id(s))
print(s.lower(),id(s.lower()))
print(s,id(s))

s2='hello,Python'
print(s2.swapcase())

print(s2.title())