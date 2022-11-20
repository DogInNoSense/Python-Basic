class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def show(self):
        print(self.name,self.__age)


stu=Student('zhangsan',20)
stu.show()

print(stu.name)


print(dir(stu))
print(stu._Student__age)