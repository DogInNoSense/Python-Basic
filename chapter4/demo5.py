answer=input('是会员吗?y/n')
money=float(input('请输入购物金额:'))
if answer=='y':

    if money>=200:
        print('8折,付款金额为:',money*0.8)
    elif money>=100:
        print('9折,付款金额为:',money*0.9)
    else:
        print('不打折,付款金额为:',money)
else:
    if money>=200:
        print('9.5折',money*0.95)
    else:
        print('不打折,付款金额为:',money)
