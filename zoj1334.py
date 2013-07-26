from math import pow
import sys

base = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',\
 'A', 'B', 'C', 'D', 'E', 'F']
results = []

line = raw_input()
while line != '':
	result = []
	line = line.split()
	first = line[0]
	second = int(line[1])
	third = int(line[2])
	temp = 0
	if len(first) > 7 or second ==1 or third ==1: sys.exit(1)
	for x in range(len(first)):
		temp += pow(second, x) * base.index(first[-(x+1)])
	while temp > 0:
		result.append(base[int(temp%third)])
		temp = temp // third
	if len(result) > 7:
		result = 'ERROR'
	else:
		result.reverse()
		result = ''.join(result)
	results.append(result)
	line = raw_input()

for result in results:
	print '%7s' %result