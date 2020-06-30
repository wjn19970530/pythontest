"""
1.获得用户输入的注册用户名
2，用户在输入用户名时，可能在用户名两个不小心输入多个空格，我们需要去除用户名两侧的空格
3.判断用户名是否全部为字母（用户名组成由我们来规定，这里我们规定必须为字母）
4，处理完毕之后，显示注册成功
"""

username = input('请输入您要注册的用户名')
#strip 函数默认去除字符串两侧的空格
new_username = username.strip()
#isalpha 判断字符串所有元素是否都是字母
#isdigit 判断字符串所有元素是否都是数字
if new_username.isalpha():
    print('注册成功！')
else:
    print('注册失败！')


def my_add(num1,num2,num3,num4):
    """

    :param num1:1
    :param num2:1
    :param num3:1
    :param num4:1
    :return:
    """
    result = num1 + num2 + num3 + num4
    return result
# print(my_add(100,num2=200,num4=300,num3=400))



