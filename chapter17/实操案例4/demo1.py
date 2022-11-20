pwd=input('支付密码:')
if pwd.isdigit():
    print('支付数据合法')
else:
    print('支付密码不合法')

print('-----------------')
print('支付数据合法' if pwd.isdigit() else '支付数据不合法')