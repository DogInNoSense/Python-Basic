def fun(a,b,c):
    print('a=',a,'b=',b,'c=',c)

fun(10,20,30)
lst=[11,22,33]
fun(*lst)#将列表每个元素都转换为位置实参传入

fun(a=100,c=300,b=200)
dic={'a':111,'b':222,'c':333}
fun(**dic)