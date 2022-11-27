from math import tan, pi

n = int(input())
l = float(input())

area = n * (l ** 2) / (4 * tan(pi / n))

print('%.0f' % area)