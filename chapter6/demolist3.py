lst=[10,20,30,40,50,60,70,80]
#start=1,stop=6,step=1 letf is close,right is open
print(lst[1:6:1])
print('original list:',id(lst))
lst2=lst[1:6:1]
print('cut clips:',id(lst2))
print(lst[1:6])#default step length is 1
print(lst[1:6:])

print(lst[1:6:2])#step=2
print(lst[:6:2])#default start=0
print(lst[1::2])#default stop=end
print('-----------if the step is negative----------------')
print(lst[::-1])
print(lst[7::-1])
print(lst[-2::-1])
print(lst[6::-1])