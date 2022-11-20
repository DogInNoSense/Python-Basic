def fun(*args):#可变的位置参数,传多少都可以
    print(args)
    print(args[0])

fun(10)
fun(10,30)
fun(30,405,50)

def fun1(**args):#字典
    print(args)

fun1(a=10)
fun1(a=20,b=30,c=40)

#def fun2(*args,*a)只能是一个error
   # pass

def fun2(*args1,**args2):
     pass

# def fun3(**args1,*args2):  在一个函数的定义过程中，既有可变的关键字形参，又有个数可变的位置形参，要求个数可变的位置形参放在个数可变的关键字形参之前
 #    pass
