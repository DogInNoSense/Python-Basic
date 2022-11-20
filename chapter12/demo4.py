class Student:
    native_pace = 'Linyi'

    def __init__(self, name, age):
        self.name = name  # self.name称为实体属性，进行了一个赋值的操作，将局部变量的name的值赋给实体属性
        self.age = age

    def eat(self):
        print('you are eating')

    # 静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法,因为我使用了classmethod进行修饰')

    # 在类之外定义的称为函数， 在类之内定义的成为方法
def drink():
    print('喝水')

#创建Student类的对象
stu1=Student('zhangsan',20)
stu1.eat()
print(stu1.name)
print(stu1.age)

print('----------------------')
Student.eat(stu1)#32 and 27功能相同