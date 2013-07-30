from collections import deque
import sys

base = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',\
	'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
results = []

def vafify(t, number):
	if t >= number:
		t = t % number
	if t < 0:
		t = number + t
	return t

number = raw_input()
while number != '0':
	number = int(number)
	first = list(raw_input())
	second = list(raw_input())
	third = list(raw_input())
	f_index, s_index, t_index = [], [], []
	for x in range(number):
		f_index.append(base.index(first[x])-x)
		s_index.append(base.index(second[x])-x)
		t_index.append(base.index(third[x])-x)
	f_index, s_index, t_index = deque(f_index), deque(s_index), deque(t_index)
	count = int(raw_input())
	f_rotor, s_rotor, t_rotor = 0, 0, 0
	for x in range(count):
		result = []
		test = raw_input()
		for y in test:
			f_rotor += 1
			temp = (base[first.index(base[second.index(base[third.index(y)])])]).lower()
			result.append(temp)
			f_index.rotate(1)
			for z in range(number):
				t = z + f_index[z]
				t = vafify(t, number)
				first[z] = base[t]
			if f_rotor == number:
				s_rotor += 1
				f_rotor = 0
				s_index.rotate(1)
				for z in range(number):
					t = z + s_index[z]
					t = vafify(t, number)
					second[z] = base[t]
			if s_rotor == number:
				t_rotor += 1
				s_rotor = 0
				t_index.rotate(1)
				for z in range(number):
					t = z + t_index[z]
					t = vafify(t, number)
					third[z] = base[t]
		results.append(result)
	number = raw_input()

for x in range(len(results)):
	print 'Enigma %i:' %(x + 1)
	print ''.join(results[x])
	print