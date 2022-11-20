lst=[20,40,10,98,54]
print('before sorting',id(lst),lst)
lst.sort()
print('after sorting',id(lst),lst)


lst.sort(reverse=True)
print(lst)
lst.sort(reverse=False)
print(lst)

print('--------using sorted---------')#generate a new list
lst=[20,40,10,98,54]
newlist=sorted(lst)
print(lst)
print(newlist)


desclist=sorted(lst,reverse=True)
print(desclist)