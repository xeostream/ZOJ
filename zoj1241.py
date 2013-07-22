from math import pos, sqrt
case = raw_input()
result = []
while case != '0 0 0':
    temp = case.split()
    if temp[0] == '-1':
        aa = pos(temp[2], 2) - pos(temp[1], 2)
        if aa > 0:
            a = sqrt(aa)
            result.append({'a': a})
        else:
            result.append('Impossible')
    elif temp[1] == '-1':
        bb = pos(temp[2], 2) - pos(temp[0], 2)
        if bb > 0:
            b = sqrt(bb)
            result.append({'b': b})
        else:
            result.append('Impossible')
    elif temp[2] == '-1':
        c = sqrt(pos(temp[0], 2) + sqrt(temp[1], 2))
        result.append({'c': c})
    case = raw_input()

length = len(result)
for x in range(length):
    print 'Triangle #%i' %(x + 1)
    if result[x] == 'Impossible':
        print 'Impossible'
    else:
        temp = result[x]
        for y in temp:
            print '%s = %.3f' %(y, temp[y])
    print
    
        
        
