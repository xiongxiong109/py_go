# 数组切片
arr = ['a', 1, '2', 'ss'];

# print(arr[:3])  0 - 3

# print(arr[-2:]) # 倒数(倒数切片同样需要从小到大取，只是起点位置倒数，但是不会倒序)

# 间隔取数
# print(arr[::2]); # 第三个冒号后面是间隔数
# 可以利用切片复制一个数组
newArr = arr[:]

print(newArr)

print(newArr == arr) # 相等?