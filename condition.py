# if elif else
print('Your height (m)')
height = float(input())
print('Your weight (kg)')
weight = float(input())
BMIValue = weight / (height * height)

if BMIValue < 18.5:
    print('过轻')
elif BMIValue <= 25:
    print('正常')
elif BMIValue <= 28:
    print('过重')
elif BMIValue <= 32:
    print('肥胖')
else:
    print('严重肥胖')