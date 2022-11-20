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

print(Student.native_pace)
stu1=Student('zhangsan',20)
stu2=Student('lisi',30)
print(stu1.native_pace)
print(stu2.native_pace)
Student.native_pace='Tianjin'
print(stu1.native_pace)
print(stu2.native_pace)
print('类方法的使用方式')
Student.cm()
print('静态方法的使用方式')
Student.method()