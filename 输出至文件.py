file1 = open('data.txt', 'w')  # 打开文件
print(123, 'abc', 45, 'book', file = file1)  # 用 file 参数指定输出到文件
file1.close()  # 关闭文件
print(open('data.txt').read())# 输出从文件中读出的内容
