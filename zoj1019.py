count = int(raw_input())
results = []
for x in range(count):
	base, moves = [], []
	result = 0
	row_col = raw_input().split()
	row = int(row_col[0])
	col = int(row_col[1])
	for y in range(row):
		base.append(raw_input().split())
	while True:
		move = raw_input().split()
		if move[0] == move[1] == '0': break
		move[0] = int(move[0])
		move[1] = int(move[1])
	moves.append(move)
	for y in row:
		for z in col:
			position_y, position_z = y, z
			if base[y][z] == '1': continue
			elif movef(base, moves, 0, y, z, row, col):
				result += 1
	results.append(result)

for r in results:
	print r

def movef(base, moves, i, x, y, row, col):
	if i < len(moves):
		if moves[i][2] == 'R' and y+moves[i][0] < col:
			for j in range(1,min(moves[i][1]+1,col-y)):
				if base[x][y+j] == '1': return False
			for begin in range(moves[i][0], min(moves[i][1]+1, col-y)):
				movef(base, moves, i+=1, x, y+begin, row, col)
		elif moves[i][2] == 'L' and y-moves[i][0] >= 0:
			for j in range(1, min(moves[i][1]+1, y+1)):
				if base[x][y-j] == '1': return False
			for begin in range(moves[i][0], min(moves[i][1]+1, y+1)):
				movef(base, moves, i+=1, x, y-begin, row, col)
		elif moves[i][3] == 'U' and x-moves[i][0] >= 0:
			for j in range(1, min(moves[i][1]+1, x+1)):
				if base[x-j][y] == '1': return False
			for begin in range(moves[i][0], min(moves[i][1]+1, x+1)):
				movef(base, moves, i+=1, x-begin, y, row, col)
		elif moves[i][3] == 'D' and x+moves[i][0] < rol:
			for j in range(1, min(moves[i][1]+1, rol-x)):
				if base[x+j][y] == '1': return False
			for begin in range(moves[i][0], min(moves[i][1]+1, rol-x)):
				movef(base, moves, i+=1, x+begin, y, row, col)
		else:
			return False
	else:
		return True