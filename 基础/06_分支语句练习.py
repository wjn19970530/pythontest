#获得用户输入的用户名
input_username =input('请输入你的用户名：')
input_password =input('请输入你的密码：')
#正确的用户名
correct_name = 'admin'
correct_pass = '123456'
if input_username == correct_name :
    #如果用户名正确 判断密码是否正确
    if input_password == correct_pass:
        print('欢迎 %s 登陆系统' % input_username)
    else:
        print('您的用户名或密码错误!')


else:
    print('您的用户名或密码错误!')