# 递归函数调用

# 定义阶乘函数
def fact(n):
    sum = 1;
    if n == 1:
        return 1;
    return n * fact(n - 1);

# 当直接通过python调用该脚本的时候, __name__ == __main__, 作为模块调用的时候则不会
if __name__ == '__main__':
    print(fact);