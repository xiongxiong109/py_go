from multiple import multi;

# 测试
print('multi(5) =', multi(5))
print('multi(5, 6) =', multi(5, 6))
print('multi(5, 6, 7) =', multi(5, 6, 7))
print('multi(5, 6, 7, 9) =', multi(5, 6, 7, 9))
if multi(5) != 5:
    print('测试失败!')
elif multi(5, 6) != 30:
    print('测试失败!')
elif multi(5, 6, 7) != 210:
    print('测试失败!')
elif multi(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        multi()
        print('测试失败!')
    except TypeError:
        print('测试成功!')