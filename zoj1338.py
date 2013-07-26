from __future__ import division

line = raw_input()
while line != '0':
	line = line.split()
	line = [int(l) for l in line[:-1]]
	length = len(line)
	if max(line) == min(line):
		print 'Nr values =%i: %.6f %6f' %(length, 0, 0)
	else:
		up_count, up_list_count, down_count, down_list_count = 0, 0, 0, 0
		equal_count = 0
		up_in, down_in, equal_in = False, False, False
		if line[1] > line[0]:
			up_count += 1
			up_in = True
			up_list_count += 1
		elif line[1] == line[0]:
			equal_count += 1
			equal_in = True
		else:
			down_count += 1
			down_in = True
			down_list_count += 1
		for x in range(2, length):
			if line[x] > line[x-1]:
				up_count += (1 + equal_count) if equal_in else 1
				#up_count += equal_count if down_in and not up_in else 0
				if (down_in or equal_in) and not up_in:
					up_list_count += 1
				up_in, down_in, equal_in = True, False, False
				equal_count = 0
			elif line[x] == line[x-1]:
				if down_in:
					down_count += 1
				elif up_in:
					up_count += 1
				equal_count += 1
			else:
				down_count += (1 + equal_count) if equal_in else 1
				#down_count += equal_count if up_in and not down_in else 0
				if (up_in or equal_in) and not down_in:
					down_list_count += 1
				up_in, down_in, equal_in = False, True, False
				equal_count = 0
		up = up_count / up_list_count if up_list_count > 0 else 0
		down = down_count / down_list_count if down_list_count > 0 else 0
		print 'Nr values = %i:  %.6f %6f' %(length, up, down)
	line = raw_input()