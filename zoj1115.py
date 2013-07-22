raw = raw_input()
while raw != '0':
	temp = 0
	for x in list(raw):
		temp += int(x)
	while temp >= 10:
		tem = str(temp)
		temp = 0
		for x in list(tem):
			temp += int(x)
	
	print temp
	raw = raw_input()
