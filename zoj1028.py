#encoding = utf-8
'''
这次自己看懂题意了，悲剧的是没有发现规律
思前想后还是想不明白，所以google了一下(以下分析源自网络)
设位置编号为1,2,3,...,n，n为小球的总数目。
若n为偶数，则不管如何交换小球，各个小球的位置编号奇偶性保持不变，因为交换的步长为2。
如果黑球是连续，当且仅当奇位置上的黑球个数与偶位置上的黑球个数相差不大于1。
因为最后连续的时候，黑球的编号是连续的，奇偶黑球的个数差最多为1.
若n为奇数，则不管如何小球的布局如何，一定能使黑白球各自连续。因为在这种情况下，
奇位置上的小球通过交换可以移动到偶位置上。
'''

count = raw_input()
for c in range(int(count)):
	line = raw_input().split()
	if int(line[0]) % 2:
		print 'YES'
	else:
		result = [0, 0]
		for l in range(int(line[0])):
			if line[l+1] == '1':
				result[l % 2] += 1
		if abs(result[0]-result[1]) <= 1:
			print 'YES'
		else:
			print 'NO'