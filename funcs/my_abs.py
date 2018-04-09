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

# 可变参数 * 表示长度可变, 对应的实参也要带上*
def summy(*nums):
    sum = 0;
    for n in nums:
        sum += n;
    return sum

# 必选参数、命名关键字参数、默认参数 **表示关键字参数, 对应的实参也要带上**
def person(nm = 'xiong', age = 25, **keywords):
    print(nm, 'aged', age, keywords);

# 命名关键字参数, * 隔开, *后面的参数都是可选参数
def superperson(nm, age, *, job = '', gender = 'male'):
    print(nm, age, job, gender);