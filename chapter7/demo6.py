d={'name':'zhangsan','name':'lisi'}#repeat is not allowed
print(d)
d={'name':'zhangsan','nickname':'zhangsan'}#value can repeat
print(d)
lst=[10,20,30]
lst.insert(1,100)
print(lst)

#d={lst:100}TypeError: unhashable type: 'list'
