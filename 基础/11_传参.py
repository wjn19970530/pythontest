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