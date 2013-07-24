# -*- coding: cp936 -*-
from math import pow
'''
开始没有好的方法
后来根据网上提供的思路首先将2到200的3次方的值存在数组中，避免接下来的重复
运算，此题很适合用python解决，需要注意的是在查找时应该指定查找的范围，之前
在整个数组中查找，用的时间为10001ms，指定数组范围的时间为6760ms，效果很好
'''
base = []
for x in range(2, 201):
    base.append(pow(x, 3))
results = []

length = len(base)
for x in range(length):
    for y in range(x, length):
        for z in range(y, length):
            temp = base[x] + base[y] + base[z]
            if temp in base[z+1:length]:
                result = [base.index(temp), x, y, z]
                result = [elem + 2 for elem in result]
                results.append(result)
results.sort()
for x in results:
    print 'Cube = %i, Triple = (%i,%i,%i)' %(x[0], x[1], x[2], x[3])
