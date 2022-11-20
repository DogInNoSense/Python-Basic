coffee_name=('蓝山','卡布奇诺','拿铁','皇家咖啡','女五咖啡','美丽与哀愁')
print('欢迎光临')
print('本店经营的咖啡有')
for index,item in enumerate(coffee_name):
    print(index+1,'.',item,end=' ')
index = int(input('\n请输入你喜欢的咖啡编号'))
if 0<=index<=len(coffee_name):
    print(f'你的咖啡{coffee_name[index-1]}好了')