import numpy as np 

def test(dog):
	print(dog)

def menu(answer, yourBoard):
	if (answer == 'i'):
		print(answer)
		nextRow = input("What row is your cell in?(1-9)")
		nextRow = int(nextRow)
		nextColumn = input("What column is your cell in?(a-i)")
		nextValue = input("What is your next value to populate?")
		nextValue = int(nextValue)
		setCell(nextRow, nextColumn, nextValue, yourBoard)
		
	if (answer == 'p'):
		print(np.matrix(yourBoard))

	if (answer == 's'):
		rows = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for i in range(9)]
		columns = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for j in range(9)]
		sector = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for k in range(9)]
		rowNaughts = [[1, 2, 3, 4, 5, 6, 7, 8, 9] for l in range(9)]
		columnNaughts = [[1, 2, 3, 4, 5, 6, 7, 8, 9] for m in range(9)]
		sectorNaughts = [[1, 2, 3, 4, 5, 6, 7, 8, 9] for n in range(9)]
		
		for i in range(9):
			for j in range(9):
				rows[i][j] = yourBoard[i][j]
		for i in range(9):
			for j in range(9):
				columns[i][j] = yourBoard[j][i]
		a = 0
		for p in range(0, 9, 3):
			for n in range(0, 9, 3):
				b=-1
				for i in range(3):
					for j in range(3):
						b+=1
						sector[a][b] = yourBoard[(i+p)][(j+n)]
				a+=1

		for i in range(9):
			for j in range(9):
				if (sector[i][j] != 0):
					x = sector[i][j]
					sectorNaughts[i][(x-1)] = 0
		for i in range(9):
			for j in range(9):
				if (rows[i][j] != 0):
					x = rows[i][j]
					rowNaughts[i][(x-1)] = 0
		for i in range(9):
			for j in range(9):
				if (columns[i][j] != 0):
					x = columns[i][j]
					columnNaughts[i][(x-1)] = 0

		for i in range(9):
			print(rows[i])
			print(columns[i])
			print(sector[i])
			print(rowNaughts[i])
			print(columnNaughts[i])
			print(sectorNaughts[i])
			print("")

#receivers a row(int), column(char), value(int), board([[]])
def setCell(row, column, value, yourBoard):
	if (row == 1):
		setColumn(0, column, value, yourBoard)
		return yourBoard
	if (row == 2):
		setColumn(1, column, value, yourBoard)
		return yourBoard
	if (row == 3):
		setColumn(2, column, value, yourBoard)
		return yourBoard
	if (row == 4):
		setColumn(3, column, value, yourBoard)
		return yourBoard
	if (row == 5):
		setColumn(4, column, value, yourBoard)
		return yourBoard
	if (row == 6):
		setColumn(5, column, value, yourBoard)
		return yourBoard
	if (row == 7):
		setColumn(6, column, value, yourBoard)
		return yourBoard
	if (row == 8):
		setColumn(7, column, value, yourBoard)
		return yourBoard
	if (row == 9):
		setColumn(8, column, value, yourBoard)
		return yourBoard

def setColumn(row, column, value, yourBoard):
	if (column == 'a'):
		yourBoard[row][0] = value
	if (column == 'b'):
		yourBoard[row][1] = value
	if (column == 'c'):
		yourBoard[row][2] = value
	if (column == 'd'):
		yourBoard[row][3] = value
	if (column == 'e'):
		yourBoard[row][4] = value
	if (column == 'f'):
		yourBoard[row][5] = value
	if (column == 'g'):
		yourBoard[row][6] = value
	if (column == 'h'):
		yourBoard[row][7] = value
	if (column == 'i'):
		yourBoard[row][8] = value



	






