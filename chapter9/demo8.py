s='hello,Python'
print(s.replace('Python','Java'))
s1='hello,Python,Python,Python'
print(s1.replace('Python','Java',2))
lst=['hello','java','python']
print('|'.join(lst))
print(''.join(lst))

t=('hello','Java','低头思故乡')
print(''.join(t))
print('*'.join('低头思故乡'))