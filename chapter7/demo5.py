scores={'zhangsan':100,'lisi':98,'wangwu':45}
#traversal of dictionary elements
for item in scores:
    print(item,scores[item],scores.get(item))