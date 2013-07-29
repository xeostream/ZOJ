from collections import deque

base = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',\
	'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
results = []
number = raw_input()
while number != '0':
	first = list(raw_input())
	second = list(raw_input())
	third = list(raw_input())
	f_index, s_index, t_index = [], [], []
	for x in range(int(number)):
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
			temp = third.index(y)
			temp = base[temp]
			temp = second.index(temp)
			temp = base[temp]
			temp = first.index(temp)
			temp = (base[temp]).lower()
			result.append(temp)
			f_index.rotate(1)
			for z in range(int(number)):
				t = z + f_index[z]
				t = t % number if t >= number
				t = number + t if t < 0
				first[z] = base[t]
			if f_rotor == int(number):
				s_rotor += 1
				f_rotor = 0
				s_index.rotate(1)
				for z in range(int(number)):
					t = z + s_index[z]
					t = t % number if t >= number
					t = number + t if t < 0
					second[z] = base[t]
			if s_rotor == int(number):
				t_rotor += 1
				s_rotor = 0
				t_index.rotate(1)
				for z in range(int(number)):
					t = z + t_index[z]
					t = t % number if t >= number
					t = number + t if t < 0
					third[z] = base[t]
		results.append(result)
	number = raw_input()