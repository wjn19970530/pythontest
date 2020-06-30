def my_caculator (left , right , operator):
    a = left
    b = right

    if operator == '+':
        ret = a + b
    elif operator == '-' :
        ret = a - b
    elif operator == '*':
        ret = a * b
    elif operator == '/':
        ret = a / b
    else:
        print('您输入的操作符有误')
        ret = None
    return ret

# ret = my_caculator(10,20,'*')
# print( ret )


def my_add(num1 , num2):
    result = num1 + num2
    print('num1 + num2 =',result)

# #从左向右依次对应
# my_add(10 , 20)
# my_add(num2=20 , num1=10)

from random import randint


def roll_dice(n=2):
    """
    摇色子

    :param n: 色子的个数
    :return: n颗色子点数之和
    """
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    return a + b + c

"""
# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice(5))
# 摇三颗色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 传递参数时可以不按照设定的顺序进行传递
print(add(c=50, a=100, b=200))
"""



def leijiahe(start,end):
    is_int = isinstance(start , int)
    if not is_int:
        print('start应该是一个数字！')
        return None

    is_int = isinstance(end , int)
    if not is_int:
        print('end应该是一个数字！')
        return None

    if start < end:
        print('start 应该小于 end！')
        return #等价于return None

        i = start
        my_sum = 0
        while i <= end:
            my_sum += i
            i += 1

        return my_sum
#
# ret = leijiahe(1 , 100)
# print('ret:' , ret)



#函数需要一个参数，调用的时候必须要传递一个参数
#my_function（200）

# 我们再给函数形参设置默认参数时，并不是会给所有的参数都设置默认值
# 注意点：如果某一个位置形参设置了默认参数，那么该位置之后的所有参数都必须设置默认参数
def my_function(a,b=20,c=30):
    return a+b+c

a = my_function(10)
print(a)
b = my_function(10,100)
print(b)
c = my_function(10,100,1000)
print(c)