score = float(input('请输入您的分数：'))
if score >= 0 and score <= 100:

    if score >= 90 and score <= 100:
        print('A档')
    elif score >= 80 and score < 90:
        print('B档')
    elif score >= 70 and score < 80:
        print('C档')
    elif score >= 60 and score < 70:
        print('D档')
    else:
        print('你完了')
else:
    print('输入错误')