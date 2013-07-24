count = raw_input()
results = []
while count != '0':
	count = int(count)
	if 1 <= count <= 50:
		line = raw_input().split()[:count]
		line = [int(x) for x in line]
		temp = 0
		for x in line:
			if 1 <= x <= 100:
				temp += x
			else:
				temp = -1
				break
		if temp > 0 and temp % count == 0:
			avg = temp / count
			result = 0
			for x in line:
				result += (avg - x) if avg > x else 0
			results.append(result)
		else:
			break
	count = raw_input()
length = len(results)
for x in range(1, length+1):
	print 'Set #%i' %x
	print 'The minimum number of moves is %i.' %results[x-1]
	print