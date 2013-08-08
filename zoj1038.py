bases = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
count = int(raw_input())
for c in range(count):
	temps = {}
	dict_size = int(raw_input())
	for d in range(dict_size):
		line = raw_input().split()
		temps[line[0]] = int(line[1])
	tests = []
	tests_size = int(raw_input())
	for t in range(tests_size):
		test = raw_input()
		tests.append(test)
	print 'Scenario #%i:' %(c + 1)
	for test in tests:
		temp = temps.copy()
		for t in range(len(test)-1):
			base = bases[int(test[t]) - 2]
			key, value = 0, 0
			for te in temp:
				if temp[te] == -1: continue
				if len(te) <= t or not te[t] in base:
					temp[te] = -1
				elif temp[te] > value:
						key, value = te, temps[te]
			try:
				print key[:t+1]
			except:
				print 'MANUALLY'
		print
	print