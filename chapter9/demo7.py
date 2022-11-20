s='hello,python'
print('1.',s.isidentifier())#false
print('2.','hello'.isidentifier())#true
print('3.','zhangsan_'.isidentifier())#true
print('4.','zhangsan_123'.isidentifier())#true
print('5.','\t'.isspace())
print('6.','abc'.isalpha())
print('7.','zhangsan'.isalpha())
print('8.','zhangsan1'.isalpha())

print('9.','123'.isdecimal())#true
print('10.','123四'.isdecimal())
print('11.','123'.isnumeric())
print('12.','123四'.isnumeric())#ture
print('13.','abc1'.isalnum())#true
print('14.','zhangsan123'.isalnum())#true
print('15.','abc!'.isalnum())#false
