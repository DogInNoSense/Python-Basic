lst=[10,20,30,40,50,60,30]
lst.remove(30)#remove an element from the list.if there is a duplicate element,only remove the first element.
print(lst)
#lst.remove(100)

#remove elements according to the index
lst.pop(1)
print(lst)
#lst.pop(5)
lst.pop()#remove the last
print(lst)

print('---------------')
newlist=lst[1:3]
print('after cutting',newlist)

#do not generate new list objects,but delete the contents of the original list
lst[1:3]=[]
print(lst)


lst.clear()
print(lst)

del lst
