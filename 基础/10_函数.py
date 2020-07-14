
def game_caiquan():
    # 导入random工具库
    import random
    # 获得用户输入的拳头
    while True:
        user_quan = int(input('请出拳 石头（0）、剪刀（1）、布（2）、退出游戏（3）：'))
        if user_quan == 3:
            print('退出游戏')
            break
        # 获得电脑的拳头

        computer_quan = random.randint(0, 2)
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
def game_caishuzi():
    import random
    answer = random.randint(1, 100)
    counter = 0
    while True:
        counter += 1
        number = int(input('请输入: '))
        if number < answer:
            print('大一点')
        elif number > answer:
            print('小一点')
        else:
            print('恭喜你猜对了!')
            break
    print('你总共猜了%d次' % counter)
    if counter > 7:
        print('你的智商余额明显不足')
def game_shaizi():
    from random import randint

    face = randint(1, 6)
    if face == 1:
        result = '唱首歌'
    elif face == 2:
        result = '跳个舞'
    elif face == 3:
        result = '学狗叫'
    elif face == 4:
        result = '做俯卧撑'
    elif face == 5:
        result = '念绕口令'
    else:
        result = '讲冷笑话'
    print(result)
def game_craps():
    """
    Craps赌博游戏
    玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
    如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
    玩家再次要色子 如果摇出7点 庄家胜
    如果摇出第一次摇的点数 玩家胜
    否则游戏继续 玩家继续摇色子
    玩家进入游戏时有1000元的赌注 全部输光游戏结束

    Version: 0.1
    Author: 骆昊
    Date: 2018-03-02
    """
    from random import randint

    money = 1000
    while money > 0:
        print('你的总资产为:', money)
        needs_go_on = False
        while True:
            debt = int(input('请下注: '))
            if debt > 0 and debt <= money:
                break
        first = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % first)
        if first == 7 or first == 11:
            print('玩家胜!')
            money += debt
        elif first == 2 or first == 3 or first == 12:
            print('庄家胜!')
            money -= debt
        else:
            needs_go_on = True

        while needs_go_on:
            current = randint(1, 6) + randint(1, 6)
            print('玩家摇出了%d点' % current)
            if current == 7:
                print('庄家胜')
                money -= debt
                needs_go_on = False
            elif current == first:
                print('玩家胜')
                money += debt
                needs_go_on = False

    print('你破产了, 游戏结束!')
print(game_craps())

