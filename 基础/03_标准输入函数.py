# input_content = input('请输入您的尊姓大名：')
# print('欢迎您 %s !' % input_content)

#使用INPUT完成加法计算器
left_num = input('请输入第一个数字:')
right_num = input('请输入第二个数字:')

# 打印两个变量的类型
print(type(left_num),type(right_num))
# 由于各种原因，我们拿到的数据不是我们想要的类型，所以我们要数据转换
# 前提是数据能转换成目标类型

#进行加法计算
left_num_int = int(left_num)
right_num_int = int(right_num)



result = left_num_int + right_num_int
print(result)
print('%d + %d = %d' % (left_num_int,right_num_int,result))