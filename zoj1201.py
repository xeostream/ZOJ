key = raw_input()
results = []
while key != '0':
	result = [0] * int(key)
	line = raw_input().split()
	nums = [int(x) for x in line[1:]]
	if line[0] == 'P':
		for x in range(len(nums)):
			count = 0
			for y in range(x):
				if nums[x] < nums[y]:
					count += 1
			result[nums[x]-1] = count
		results.append(result)
	elif line[0] == 'I':
		for x in range(len(nums)):
			count = -1
			for y in range(int(key)):
				if result[y] == 0:
					count += 1
					if count == nums[x]:
						result[y] = x + 1
		results.append(result)
	key = raw_input()

for x in results:
	for y in x:
		print y,
	print