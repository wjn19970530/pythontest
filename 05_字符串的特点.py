# my_str = 'abcd1234'
#
# my_str[0] = 'Q'
# print(my_str)
#
# #1.字符串一旦定义不允许修改
# #2.字符串容器中的元素都为字符类型
#
#
# # user_email = 'wangjianning@itcast.cn'
# # 1.找到字符串中@的位置
# # 2.获得字符串中的子串
user_email = 'wangjianning@itcast.cn'
char_count = user_email.count('@')
if char_count > 1:
    print('你的邮箱不合法')
#如果查找到，返回子串第一次出现的位置
#如果查找不到，返回-1
position = user_email.find('@')
if position == -1:
    print('@不存在，邮箱不合法！')
else:
    print('@的位置是：' , position)

result = user_email.split('@')
print(result[0],result[1])
#split 根据@将字符串截取为多个部分

#
# #字符串提供了一种语法，用来获取字符串中的一个子串
# print(user_email[0])
# #切片语法 左闭右开
# print(user_email[0:12])
# string_length = len(user_email)
# print(user_email[12: string_length])
#
# print(user_email[: 12])#起始值不写默认为0
# print(user_email[13:])#结束值不写默认到最后
# print(user_email[:])#默认全部
# #步长
# print(user_email[0:12:1])
# #起始值 结束值 步长都可以为复数
# print(user_email[6:1:-1])
# print(user_email[::-1])
#
# username = user_email[0:position]
# houozhui = user_email[position+1:]
# print('用户名是：' , username)
# print('邮箱后缀：' , houozhui)