base = ('0','1','2','3','4','5','6','7','8','9',\
	'a','b','c','d','e','f','g','h','i','j')
results = []
first = raw_input()
while first != '':
	second = raw_input()
	if second != '':
		line_one = ['0'] * 100
		line_two = line_one[:]
		first_size = len(first)
		second_size = len(second)
		for x in range(first_size):
			line_one[99-x] = first[first_size-x-1]
		for y in range(second_size):
			line_two[99-y] = second[second_size-y-1]
		max_size = max(first_size, second_size)
		result = [0] * (max_size+1)
		add = 0
		for z in range(max_size-1,-1,-1):
			result[z+1] += (base.index(line_one[z+100-max_size]) +\
			base.index(line_two[z+100-max_size]))
			if result[z+1] >= 20:
				result[z] = 1
				result[z+1] -= 20
		for m in range(max_size+1):
			result[m] = base[result[m]]
		if result[0] == '0': result= result[1:]
		results.append(result)
	first = raw_input()
for result in results:
	print ''.join(result)
