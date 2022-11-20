scores={'zhangsan':100,'lisi':98,'wangwu':45}
#get all keys
keys=scores.keys()
print(keys)
print(type(keys))
print(list(keys))#convert to a list
#get all values
values=scores.values()
print(values)
print(type(values))

#get all value pairs
items=scores.items()
print(items)
print(list(items))#after converting