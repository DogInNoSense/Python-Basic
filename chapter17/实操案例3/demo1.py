def fun():
    num=int(input('请输入一个十进制的整数'))
    print(num,'的二进制数为:',bin(num))
    print(str(num)+'的二进制数为:'+bin(num))
    print('%s的二进制数为：%s' % (num,bin(num)))
    print('{0}的二进制数为:{1}'.format(num,bin(num)))
    print(f'{num}的二进制数为：{bin(num)}')

    print('-----------------------------')
    print(f'{num}的八进制数为:{oct(num)}')
    print(f'{num}的十六进制数为:{hex(num)}')
if __name__ == '__main__':
    try:
        fun()
    except:
        print('输入有误')
        fun()
