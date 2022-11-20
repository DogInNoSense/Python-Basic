s={10,20,30,405,60}
print(10 in s)
print(100 in s)
print(100 not in s)
#add
s.add(80)#one
print(s)

s.update({200,400,300})#at least one
print(s)

s.update([100,34,56],(78,64,90))
print(s)
#delete
s.remove(100)
print(s)

s.discard(500)
s.pop()
s.pop()
#s.pop(400) error
print(s)

s.clear()
print(s)