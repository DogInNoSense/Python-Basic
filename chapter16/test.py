student_old=["{'id': '1001', 'name': 'zhangsan', 'english': 65, 'python': 67, 'java': 68}\n"]
for item in student_old:
    d = dict(eval(item))

d['name']='zhangsan'
print(d)
print(str(d))
#d=dict(eval(item))
#print(d)
