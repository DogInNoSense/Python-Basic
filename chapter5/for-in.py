for item in 'python':
    print(item)

for i in range(10):
    print(i)

for _ in range(5):
    print('hello')

print('计算1加到100偶数和')
sum=0
for item in range(1,101):
    if item%2==0:
        sum+=item
print('1到100之间的偶数和',sum)