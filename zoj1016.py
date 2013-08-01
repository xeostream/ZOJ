count = int(raw_input())
results = []
for x in range(count):
	length = int(raw_input())
	base = [-1] * (length * 2)
	temp = []
	p = raw_input().split()
	result = []
	for y in range(len(p)):
		if y == 0:
			base[int(p[y])] = 1
			temp.append(int(p[y]))
			continue;
		base[int(p[y])+y] = 1
		temp.append(int(p[y])+y)
	for y in range(len(temp)):
		for z in range(temp[y]-1,0,-1):
			tem = base[z:temp[y]+1]
			if base[z] == -1 and tem.count(0) % 2 == 0 and tem.count(-1) == tem.count(1):
				base[z] = base[temp[y]] = 0
				result.append(base[z:temp[y]+1].count(0)/2)
				break;
	result.append(length)
	results.append(result)
print
for r in results:
	for rr in r:
		print rr,
	print