import sys

base = ('_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',\
	'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',\
	'v', 'w', 'x', 'y', 'z', '.')
line = raw_input()
while line != '0':
	line = line.split()
	first, second = int(line[0]), list(line[1])
	length = len(second)
	if not (0 < first < 300 and length < 70):
		sys.exit(1)
	ciphercode = [base.index(x) for x in second]
	plaincode = ciphercode[:]
	for i in range(length):
		plaincode[(first*i)%length] = ciphercode[i] + i\
		if ciphercode[i] + i <= 27 else ciphercode[i] + i - 28
	result = ''.join([base[x] for x in plaincode])
	print result
	line = raw_input()
	