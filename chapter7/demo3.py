scores={'zhangsan':100,'lisi':98,'wangwu':45}
print('zhangsan' in scores)
print('zhangsan' not in scores)

del scores['zhangsan']#delete key-value
#scores.clear() clear all elements

scores['chenliu']=98#add element
print(scores)

scores['chenliu']=100#modify element
print(scores)