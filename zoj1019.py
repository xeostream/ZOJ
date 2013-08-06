count = int(raw_input())

def initbase(row, col):
	base = []
	for r in range(row):
		line = raw_input().split()[:col]
		line = [int(l) for l in line]
		base.append(line)
	return base

def initmove():
	moves = []
	while (True):
		move = raw_input()
		if move == '0 0': break
		move = move.split()
		move[0], move[1] = int(move[0]), int(move[1])
		moves.append(move)
	return moves

def checknode(base, r, c, row, col):
	if 0 <= r < row and 0 <= c < col and base[r][c] == 0: return True
	return False

def check(base, moves, i, r, c, row, col):
	if i <len(moves):
		if moves[i][2] == 'R':
			for ro in range(1, moves[i][0]):
				if not checknode(base, r+ro, c, row, col): return False
			for ro in range(moves[i][0], moves[i][1]+1):
				if not checknode(base, r+ro, c, row, col): return False
				if check(base, moves, i+1, r+ro, c, row, col): return True
		elif moves[i][2] == 'L':
			for ro in range(1, moves[i][0]):
				if not checknode(base, r-ro, c, row, col): return False
			for ro in range(moves[i][0], moves[0][1]+1):
				if not checknode(base, r-ro, c, row, col): return False
				if check(base, moves, i+1, r+ro, c, row, col): return True
		elif moves[i][2] == 'U':
			for co in range(1, moves[i][0]):
				if not checknode(base, r, c-co, row, col): return False
			for co in range(moves[i][0], moves[i][1]+1):
				if not checknode(base, r, c-co, row, col): return False
				if check(base, moves, i+1, r, c-co, row, col): return True
		elif moves[i][2] == 'D':
			for co in range(1, moves[i][0]):
				if not checknode(base, r, c+co, row, col): return False
			for co in range(moves[i][0], moves[i][1]+1):
				if not checknode(base, r, c+co, row, col): return False
				if check(base, moves, i+1, r, c+co, row, col): return True
	elif i == len(moves):
		if checknode(base, r, c, row, col): return True
		else: return False
		
for x in range(count):
	result = 0
	row_col = raw_input().split()
	row = int(row_col[0])
	col = int(row_col[1])
	base = initbase(row, col)
	moves = initmove()
	for r in range(row):
		for c in range(col):
			if base[r][c] == 0 and check(base, moves, 0, r, c, row, col):
				result += 1
	print result