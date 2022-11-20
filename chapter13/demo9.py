a=20
b=100
c=a+b
d=a.__add__(b)

print(c)
print(d)

class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self,other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)

stu1=Student('zhangsan')  #实现了两个对象的加法运算（因为在Student类中 编写__add__特殊的方法）
stu2=Student('lisi')

print(stu1+stu2)
s=stu1.__add__(stu2)
print(s)


print('-----------------------')
lst=[11,22,33,44]
print(len(lst))#len是内容函数len
print(lst.__len__())
print(len(stu1))