admin = 'xyz'
pwd = '8888'
for i in range(1,4):
    user_name=input('请输入用户名')
    user_pwd=input('请输入密码:')
    if user_name=='admin' and user_pwd=='pwd':
        print('登录成功')
        break
    else:
        if i<3:
            print('error\t'+'你还有'+str(3-i)+'次机会!')
        else:
            print('3次均输错')
