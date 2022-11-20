s='天涯共此时'
print(s.encode(encoding='GBK'))
print(s.encode(encoding='UTF-8'))


byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))

byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))