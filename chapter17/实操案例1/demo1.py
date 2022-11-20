# 使用print方式进行输出（输出目的地是文件）

fp = open('d:/test.txt', 'w')
print('奋斗成就更好的你', file=fp)
fp.close()
# 第二种方式，使用文件读写操作
with open('d:/test1.txt', 'w') as file:
    file.write('奋斗成就更好的你')

fp = open('d:/test3.txt', 'w')
fp.write('奋斗成就更好的你')
fp.close()
