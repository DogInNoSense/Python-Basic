def fun(a,b=10):
    print('a=',a)
    print('b=',b)


def fun2(*args):
    print(args)

def fun3(**args2):
    print(args2)

fun2(10,20,30,40)
fun3(a=11,b=22,c=33,d=44,e=55)
def fun4(a,b,*，c,d):#从*之后的参数，在函数调用的时候只能采用关键字参数传递
    print('a=',a)
    print('b=', b)
    print('c=', c)
    print('d=', d)


fun4(10,20,30,40)
fun4(a=10,b=20,c=30,d=40)
fun4(10,20,c=30,d=40)#前两个是位置实参传递,后两个是关键字实参传递

#若c,d只能采用关键字实参传递

def fun5(a,b,*,c,d,**args):
    pass
def fun6(*args,**args2):
    pass
def fun7(a,b=10,*args,**args2):
    pass

