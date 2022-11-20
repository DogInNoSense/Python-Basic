class Student(object):
    def __init__(self,stu_name,stu_age,stu_gender,stu_score):
        self.stu_name = stu_name
        self.stu_age=stu_age
        self.stu_gender=stu_gender
        self.stu_score=stu_score
    def show(self):
        print(self.stu_name,self.stu_age,self.stu_score,self.stu_gender)
if __name__ == '__main__':
    print('请输入五位学员的信息:(姓名#年龄#成绩#性别)')
    lst=[]
    for i in range(0,5):
        s = input(f'请输入第{i+1}位学员的信息和成绩:')
        s_lst = s.split('#')
        # 创建学生对象
        stu = Student(s_lst[0],int(s_lst[1]),float(s_lst[2]),s_lst[3])
        lst.append(stu)
    # 遍历列表
    for item in lst:
        item.show()

