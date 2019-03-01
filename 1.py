C = [[5, 3, 1],
	 [3, 2, 4],
	 [4, 1, 2]]
A = [10, 20, 30]
B = [15, 20, 25]
deltaC = []
_deltaC = []
PLAN = [['-' for i in range(len(A))] for j in range(len(B))]
_A = A.copy()
_B = B.copy()

def checkOptimum():
	for i in range(len(deltaC)):
		for j in range(len(deltaC[i])):
			if deltaC[i][j] < 0:
				return False
	return True

def createCickle(y, x):
	index = 1
	count = 0
	while x-index >= 0:
		if PLAN[y][x-index] != '-':
			count += 1
			second = x-index
		index += 1
	index = 1
	while x+index < len(A):
		if PLAN[y][x+index] != '-':
			count += 1
			second = x+index
		index += 1
	if count > 1:
		index = 1
		count = 0
		while y-index >= 0:
			if PLAN[y-index][x] != '-':
				count += 1
				second = y-index
			index += 1
		index = 1
		while y+index < len(B):
			if PLAN[y+index][x] != '-':
				count += 1
				second = y+index
			index += 1
		if count > 1:
			print('ERROR!')
			return
		answer = True
		coord = [second, x]
	else:
		answer = False
		coord = [y, second]
	if answer:
		_x = coord[1]
		_y = coord[0]
		index = 1
		count = 0
		third = -1
		while _x-index >= 0:
			if PLAN[_y][_x-index] != '-':
				count += 1
				third = _x-index
			index += 1
		index = 1
		if third == -1:
			while _x+index < len(A):
				if PLAN[_y][_x+index] != '-':
					count += 1
					third = _x+index
				index += 1
		k1 = [y, x]
		k2 = [second, x]
		k3 = [second, third]
		k4 = [y, third]
		return [k1, k2, k3, k4]
	else:
		_x = coord[1]
		_y = coord[0]
		index = 1
		count = 0
		third = -1
		while _x-index >= 0:
			if PLAN[_y-index][_x] != '-':
				count += 1
				third = _y-index
			index += 1
		index = 1
		if third == -1:
			while _x+index < len(A):
				if PLAN[_y+index][_x] != '-':
					count += 1
					third = _y+index
				index += 1
		k1 = [y, x]
		k2 = [second, x]
		k3 = [second, third]
		k4 = [y, third]
		return [k1, k2, k3, k4]
	
def main():
	# ШАГ 1
	global C
	global A 
	global B 
	global deltaC 
	global _deltaC 
	global PLAN
	global _A 
	global _B 

	# ШАГ 2
	if not (sum(A) == sum(B)):
		print ("Error")

	# ШАГ 3
	arr = [0] * len(C) * len(C[0])
	index = 0
	for i in range(len(C)):
		for j in range(len(C[i])):
			arr[index] = [C[i][j], [i, j]]
			index += 1

	for i in range(len(arr) - 1):
		for j in range(len(arr) - i - 1):
			if arr[j][0] > arr[j+1][0]:
				arr[j], arr[j+1] = arr[j+1], arr[j]


	for i in range(len(arr)):
		if (sum(_A) == 0 and sum(_B) == 0):
			break
		top = arr[i][1][0]
		gor = arr[i][1][1]
		if (_A[top] < _B[gor]) and (_A[top] != 0):
			PLAN[top][gor] = _A[top]
			_B[gor] -= _A[top]
			_A[top] = 0
		if (_A[top] >= _B[gor]) and (_B[gor] != 0):
			PLAN[top][gor] = _B[gor]
			_A[top] -= _B[gor]
			_B[gor] = 0

	# ШАГ 4
	basis = []
	index = 0
	for i in range(len(PLAN)):
		for j in range(len(PLAN[i])):
			if PLAN[i][j] is not '-':
				index += 1
				basis.append([i, j])
	if index < len(A) + len(B) - 1:
		print('План вырожденный')

	while True:
		# ШАГ 5
		U = [None] * len(A)
		V = [None] * len(B)

		U[basis[0][0]] = 0
		for k in range(len(basis)):
			for i in range(len(basis)):
				if U[basis[i][0]] == None and V[basis[i][1]] is not None:
					U[basis[i][0]] = C[basis[i][0]][basis[i][1]] - V[basis[i][1]]
				if V[basis[i][1]] == None and U[basis[i][0]] is not None:
					V[basis[i][1]] = C[basis[i][0]][basis[i][1]] - U[basis[i][0]]

		# ШАГ 6
		deltaC = []
		for i in range(len(C)):
			deltaC.append(C[i].copy())

		for i in range(len(A)):
			for j in range(len(B)):
				deltaC[i][j] = C[i][j] - (U[i] + V[j])
		
		# ШАГ 7
		if not checkOptimum():
			_deltaC = []
			for i in range(len(deltaC)):
				for j in range(len(deltaC[i])):
					_deltaC.append([deltaC[i][j], [i, j]])

		min_deltaC = _deltaC[0][0]
		koord_min_deltaC = _deltaC[0][1]
		for i in range(len(_deltaC)):
			if _deltaC[i][0] < min_deltaC:
				min_deltaC = _deltaC[i][0]
				koord_min_deltaC = _deltaC[i][1]

		args = createCickle(koord_min_deltaC[0], koord_min_deltaC[1])
		args[0] = [args[0], "+"]
		args[1] = [args[1], '-']
		args[2] = [args[2], '+']
		args[3] = [args[3], '-']

		PLAN[args[0][0][0]][args[0][0][1]] = min(PLAN[args[1][0][0]][args[1][0][1]], PLAN[args[3][0][0]][args[3][0][1]])
		PLAN[args[1][0][0]][args[1][0][1]] -= min(PLAN[args[1][0][0]][args[1][0][1]], PLAN[args[3][0][0]][args[3][0][1]])
		PLAN[args[2][0][0]][args[2][0][1]] += min(PLAN[args[1][0][0]][args[1][0][1]], PLAN[args[3][0][0]][args[3][0][1]])
		PLAN[args[3][0][0]][args[3][0][1]] -= min(PLAN[args[1][0][0]][args[1][0][1]], PLAN[args[3][0][0]][args[3][0][1]])

		for i in range(len(PLAN)):
			for j in range(len(PLAN[i])):
				if PLAN[i][j] == 0:
					PLAN[i][j] = '-'

		# ШАГ 8
		if not checkOptimum():
			break

	# ШАГ 9
	Z = 0
	for i in range(len(PLAN)):
		for j in range(len(PLAN[i])):
			if PLAN[i][j] != '-':
				Z += PLAN[i][j] * C[i][j]
	print(Z)
	
main()