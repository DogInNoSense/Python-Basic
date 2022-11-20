def sum(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return sum(n-1)+sum(n-2)


print(sum(5))

for i in range(1,7):
    print(sum(i),end='\t')