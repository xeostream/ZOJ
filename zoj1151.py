count = raw_input()
list = []
for x in range(int(count)):
	li = []
	raw_input()
	lines = raw_input()
	for y in range(int(lines)):
		line = raw_input()
		li.append(line)
	list.append(li)
	
for word in list:
	for wo in word:
		for w in wo.split():
			print w[::-1],
		print
