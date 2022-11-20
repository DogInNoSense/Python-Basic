def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        if not i%2:
            even.append(i)

    return odd,even

lst=[10,29,34,23,44,53,55]
print(fun(lst))#得到元组