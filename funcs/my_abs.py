# 用def定义一个函数
def myAbs(a):
    if not isinstance(a, (int, float)): # 添加数据类型判断
        raise TypeError('bad type of', a);
    return abs(a); # abs函数需要接收数字

def pos(x, y):
    return myAbs(x), myAbs(y); # 有多个返回值的时候, 返回的是一个tuple(不可变列表)