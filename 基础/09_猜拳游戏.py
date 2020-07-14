#导入random工具库
import random
#获得用户输入的拳头
while True:
    user_quan =int(input('请出拳 石头（0）、剪刀（1）、布（2）、退出游戏（3）：'))
    if user_quan == 3:
        print('退出游戏')
        break
    #获得电脑的拳头

    computer_quan = random.randint(0,2)
    if (user_quan == 0 and computer_quan == 1) or \
            (user_quan == 1 and computer_quan == 2) or \
            (user_quan == 2 and computer_quan == 0):
        print('你赢了！')
    elif user_quan == computer_quan:
        print('平局')
    elif user_quan != 0 and user_quan != 1 and user_quan != 2 and user_quan != 3:
        print('输入错误！')
    else:
        print('你输了！')

