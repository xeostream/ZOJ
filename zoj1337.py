from math import sqrt
from fractions import gcd
import sys

results = []
count = raw_input()
while 0 < int(count) < 50:
    data = []
    for x in range(int(count)):
        temp = raw_input()
        data.append(int(temp)) if 0 < int(temp) < 32 else sys.exit(1)
        result = 0
    for x in range(int(count)):
        for y in range(x+1, int(count)):
                if gcd(data[x], data[y]) == 1:
                    result += 1
                
    if result > 0:
        count = int(count)
        count = count * (count - 1) / 2
        res = sqrt((6 * count) / result)
        results.append(res)
    else:
        results.append('No estimate for this data set.')
    count = raw_input()

for x in results:
    if type(x) is float:
        print "%.6f" %x
    else:
        print x
