import math;
# 求解二元一次方程 ax^2 + bx + c = 0; x = (-b +- math.sqrt(b * b - 4 * a * c)) / 2a
def quadratic(a, b, c):
    delta = math.pow(b, 2) - 4 * a * c; # 根的判别式delta
    positiveRst = (- b + math.sqrt(delta)) / (2 * a); # 正根
    negativeRst = (- b - math.sqrt(delta)) / (2 * a); # 负根
    return (positiveRst, negativeRst);