class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'eating')
stu1=Student('zhangsan',20)
stu2=Student('lisi',30)
print(id(stu1))
print(id(stu2))
print('为stu2动态的绑定性别属性')
stu2.gender='female'
#print(stu1.name,stu1.age,stu1.gender)
print(stu2.name,stu2.age,stu2.gender)


def show():
    print('定义在类之外的，称为函数')
stu1.show=show
stu1.show()