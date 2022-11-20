#print(dir(object))

class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
class D(A):
    pass
#创建c类的对象
x=C('Jack',20)#x是C类型的一个实例对象
print(x.__dict__)#实例对象的属性字典
print(C.__dict__)

print(x.__class__)#输出了对象所属于的类
print(C.__bases__)#C类的父类的元素
print(C.__base__)
print(C.__mro__)#类的层次结构
print(A.__subclasses__())#子类的列表

