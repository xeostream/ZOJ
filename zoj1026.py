count = int(raw_input())

for c in range(count):
	first = raw_input().split()[1:]
	second = raw_input().split()[1:]
	third = raw_input().split()[1:]
	f_len, s_len, t_len = len(first), len(second), len(third)
	first = [int(f) for f in first]
	second = [int(s) for s in second]
	third = [int(t) for t in third]
	
	temp = [0] * (f_len + s_len - 1)
	for f in range(f_len-1, -1, -1):
		for s in range(s_len-1, -1, -1):
			temp[f+s] = (temp[f+s]+first[f]*second[s]) % 2
	for t in range(f_len+s_len-t_len):
		if temp[t] == 0: continue
		for th in range(t_len):
			temp[t+th] = (temp[t+th] + third[th]) % 2
	print t_len-1,
	for t in range(f_len+s_len-t_len, f_len+s_len-1):
		print temp[t],