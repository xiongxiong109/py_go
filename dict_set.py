# 字典与枚举类型
envMap = {
    "dev": "localhost",
    "beta": "m.beta",
    "prd": "m.com"
}

# print(envMap['beta']);
# 判断字典里的key是否存在(直接获取一个不存在的key的值会报错)

# env = 'prd';

# if envMap.get(env):
# if env in envMap:
#     print(envMap[env])
# else:
#     print('not found')

envArr = ['dev', 'fat', 'fws', 'beta', 'uat', 'lpt', 'prod', 'prd', 'pro'];

# for env in envArr:
    # print(envMap.get(env)); # 获取不到的时候会返回None
    # if (envMap.get(env)):
    #     print('found env', env, envMap[env]);
    # else:
    #     print('env', env, 'not found');

# dict是一组key不可变的集合
# set也是一组key的集合，但不存储value, set 传入一个list, 但是set不是有序的
envS1 = set(envArr)
envS2 = set(envArr)
envS1.add('lpt'); # 添加key值
envS2.remove('dev'); # 移除key值
print(envS1 & envS2); # 两组set可以做交集和并集运算
print(envS1 | envS2);