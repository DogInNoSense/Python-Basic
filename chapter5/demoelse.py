for item in range(3):
    pwd=input('please enter the password')
    if pwd=='8888':
        print('correct')
        break
    else:
        print('error')
else:
    print('You have tyied three times')
