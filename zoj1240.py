count = raw_input()
results = []
for x in range(int(count)):
	temp = raw_input()
	result = [ chr(ord(word)+1) if word !='Z' else 'A' for word in temp ]
	result = ''.join(result)
	results.append(result)

for x in range(int(count)):
	print 'String #%i' %(x+1)
	print results[x]
	print 