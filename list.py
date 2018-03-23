# list 列表类型操作
a = [1, 'a', True];

# 获取元素个数
# print(len(a));

# 读取某个元素
# print(a[1])
# -1可以倒序访问列表
# print(a[-1])
# print(a[len(a) - 1])
# 剔除列表末尾元素(pop方法同时也会返回这个元素)
# print(a.pop())
# a.pop()
# print(a);

# 插入元素(在index的前面插入元素)
# a.insert(1, 'hello')
# print(a)

# 在后面append元素
# a.append('hello');
# hasHello = 'hello' in a;

# if hasHello:
#     print(a);
# else:
#     print('404 not found');

# :间断取值
# a.append(1)
# a.append(2)
# a.append(3)
# a.append(4)
# print(a);
# print(a[1:3])
# print(a[0:len(a):2]) # 每隔两个取一次值
# 取索引
# print(a.index('a'))
if 'a' in a:
    a.pop(a.index('a'))
print(a)