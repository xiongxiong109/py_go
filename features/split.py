# list切片
# arr = ['a', 1, '2', 'ss'];

# print(arr[:3])  0 - 3

# print(arr[-2:]) # 倒数(倒数切片同样需要从小到大取，只是起点位置倒数，但是不会倒序)

# 间隔取数
# print(arr[::2]); # 第三个冒号后面是间隔数
# 可以利用切片复制一个数组
# newArr = arr[:]

# print(newArr)

# print(newArr == arr) # 相等?

# 利用list切片来实现string的strip()效果
testStr = "  hello world   ";
specStr = "hello world";
# print(testStr.strip() == specStr);

#用一个循环找到前后索引

def trim(str):

    startIdx = -1;
    isStartReady = False;
    endIdx = 0;
    isEndReady = False;

    for char in str:
        if  str[startIdx + 1] == ' ' and not isStartReady:
            startIdx += 1;
        else:
            isStartReady = True;
        if str[endIdx - 1] == ' ' and not isEndReady:
            endIdx -= 1;
        else:
            isEndReady = True;
        if isStartReady and isEndReady:
            break;
    return str[startIdx + 1:len(str) + endIdx];

# test
if trim('hello  ') != 'hello':
    print('failed!')
elif trim('  hello') != 'hello':
    print('failed!')
elif trim('  hello  ') != 'hello':
    print('failed!')
elif trim('  hello  world  ') != 'hello  world':
    print('failed!')
elif trim('') != '':
    print('failed!')
elif trim('    ') != '':
    print('failed!')
else:
    print('success!')