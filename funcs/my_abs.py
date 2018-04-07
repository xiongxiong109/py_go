import math

# 用def定义一个函数
def myAbs(a):
    if not isinstance(a, (int, float)): # 添加数据类型判断
        raise TypeError('bad type of', a);
    return abs(a); # abs函数需要接收数字

def pos(x, y):
    return myAbs(x), myAbs(y); # 有多个返回值的时候, 返回的是一个tuple(不可变列表)

def abstractFun(str): # 定义一个空函数, 用pass来占位
    if (str):
        pass

# 给函数参数默认值(默认参数必须指向不可变对象, 否则每次调用时都会记住上一次的变化)
def power(x, n = 2):
    return math.pow(x, n);

def appendA(L = []):
    L.append('END');
    return L;

def appendB(L = None):
    if L == None:
        L = [];
    L.append('END');
    return L;