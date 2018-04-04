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

for env in envArr:
    if (envMap.get(env)):
        print('found env', env, envMap[env]);
    else:
        print('env', env, 'not found');