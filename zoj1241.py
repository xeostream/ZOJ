from math import pow, sqrt
case = raw_input()
result = []
while case != '0 0 0':
    temp = case.split()
    if temp[0] == '-1':
        aa = pow(float(temp[2]), 2) - pow(float(temp[1]), 2)
        if aa > 0:
            a = sqrt(aa)
            result.append({'a': a})
        else:
            result.append('Impowsible')
    elif temp[1] == '-1':
        bb = pow(float(temp[2]), 2) - pow(float(temp[0]), 2)
        if bb > 0:
            b = sqrt(bb)
            result.append({'b': b})
        else:
            result.append('Impowsible')
    elif temp[2] == '-1':
        tem = pow(float(temp[0]), 2) + pow(float(temp[1]), 2)
        c = sqrt(tem)
        result.append({'c': c})
    case = raw_input()

length = len(result)
for x in range(length):
    print 'Triangle #%i' %(x + 1)
    if result[x] == 'Impossible':
        print 'Impowsible'
    else:
        temp = result[x]
        for y in temp:
            print '%s = %.3f' %(y, temp[y])
    print
