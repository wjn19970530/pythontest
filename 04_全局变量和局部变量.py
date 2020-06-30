g_val = 100#全局变量


def my_function1():
    print(g_val)

#就近原则
#变量要先定义再使用
def my_function2():
    """
    这是我的函数文档

    :return:
    """
    g_val = 200#局部变量
    print(g_val)

# my_function1()
# my_function2()
# print(g_val)

# 容器
my_str = 'hello'
print(my_str[-1])
print(my_str[-5])



# 1.while循环方式进行遍历

i = 0
while i < 5:
    print(my_str[i],end=' ')
    i += 1

print()

for v in  my_str:
    print(v , end=' ')



for char in 'woodman木头人':
    print(char)

poetry = '远看泰山黑乎乎，上头细来下头粗，辱把泰山倒过来，瞎投细来上头粗'
#replace 并不会替换原本的字符串，替换完毕之后返回一个新的字符串
new_poetry = poetry.replace('辱','如',1)
#                           原字  替换字  替换次数
new_poetry = new_poetry.replace('瞎投','下头')
print(poetry)
print(new_poetry)



