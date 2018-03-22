# 引号转义问题
# print('I\'m', 'Bear');
# 用r''表示字符串都不转义
# print(r"I'm Bear \t Carmbridge ");
# print("I'm \n Bear \t Carmbridge ");

# 多重换行
# print('''hello
# I 'm Bear "Xiong"''')

# Boolean (and, or, not)

# print(True or False)
# print(True and False)
# print(not False) # 非

# a = 1

# if not a:
#     print('ok')
# else:
#     print('hello')

# 浮点除法与地板除法
# print(10 / 3)
# 地板除, 永远取整数
# print(10 // 3)
# print(10 % 3)

# 字符编码
# codea = ord('a')
# char65 = chr(65)
# print(codea)
# print(char65)
# print(ord('中')) # 十进制的20013 -> 转成十六进制为4e2d, 输出字符即可
# print('\u4e2d')

# 占位符替换 %d 整数 %s 字符串 %f 浮点数(.2f可以保留有效位数) %x 十六进制
# print('Hello %s, 需要支付 &yen; %.2f 元' % ('world', 16.32))
# 用%格式化字符串的时候, 遇到%, 直接%%即可
# print('%d%%' % (10))
# 用format方法格式化字符串
print('hello {0} need pay {1:.2f}'.format('Xiong', 12.505))