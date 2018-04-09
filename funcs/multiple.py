# 乘法函数
def multi(*args):
    if args == None:
        raise TypeError('测试失败!');
    rst = 1;
    for i in args:
        rst *= i;
    return rst;