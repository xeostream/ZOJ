# -*- coding: cp936 -*-
from math import pow
'''
��ʼû�кõķ���
�������������ṩ��˼·���Ƚ�2��200��3�η���ֵ���������У�������������ظ�
���㣬������ʺ���python�������Ҫע������ڲ���ʱӦ��ָ�����ҵķ�Χ��֮ǰ
�����������в��ң��õ�ʱ��Ϊ10001ms��ָ�����鷶Χ��ʱ��Ϊ6760ms��Ч���ܺ�
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
