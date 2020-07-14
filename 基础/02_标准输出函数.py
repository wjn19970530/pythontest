# my_number1 = 100
# my_number2 = 100
# my_number3 = 100
#
# #函数中的逗号用来隔开多个函数
# print(my_number1, my_number2, my_number3, 'hello')

print('aaa',end='#')
print('bbb',end='#')
print('ccc',end='#')

# 格式化输出
name = '狗子'
age = 18
salary = 9999.01

my_format = '他的名字是%s, 他的年龄是%05d, 他的工资是%0.3f.' %(name,age,salary)
print('\n',my_format)
print('他的游戏胜率是%d%%'% 87)#  %s字符串，%d有符号十进制整数，%f浮点数 %%输出%号
print('他的名字是', name,'他的年龄是', age,'他的工资是', salary)
print('aaa' + 'bbb')
