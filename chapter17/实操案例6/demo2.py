lst = []
for i in range(0,5):
    goods = input('请输入商品编写和商品名进入商品的入库，每次输入一件:\n')
    lst.append(goods)
for item in lst:
    print(item)
cart = []
while True:
    num = input('请输入要购买的商品编号')
    for item in lst:
        if item.find(num) != -1:
            cart.append(item)
            break
    if num == 'q':
        break
print('您购物车已经选好的商品为:')
for m in range(len(cart)-1,-1,-1):
    print(cart[m])