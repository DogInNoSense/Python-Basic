try:
    a=int(input('please enter the first num'))
    b=int(input('please enter the second num'))
    result=a/b
except BaseException as e:
    print('The error:',e)
else:
    result=a/b
    print('result=',result)