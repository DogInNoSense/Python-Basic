lst=[10,20,30]
print('before adding elements',lst,id(lst))
lst.append(100)#append
print('after adding elements',lst,id(lst))
lst2=['hello','world']
#lst.append(lst2)#add lst2 as an element to the end of the list
lst.extend(lst2)#add multiple elements to the end of the list at once
print(lst)
#add an element anywhere
lst.insert(1,90)
print(lst)

lst3=[True,False,'hello']
#add multiple elements anywhere
lst[1:]=lst3
print(lst)
