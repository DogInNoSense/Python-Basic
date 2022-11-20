r=range(10)#默认从0开始,步长为1
print(r)
print(list(r))

r=range(1,10)
print(list(r))

r=range(1,10,2)#指定步长为2
print(list(r))

print(10 in r)
print(9 in r)
print(10 not in r)
print(9 not in r)
#不管range的对象表示的整数序列有多长,所有的range对象占用的内存空间都是相同的,start stop step

print(range(1,20,1))
print(range(1,101,1))