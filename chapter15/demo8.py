file=open('c.txt','a')
file.write('hello')
lst=['Java','go','python']
file.writelines(lst)
file.close()