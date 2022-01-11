import soduku_populate
import linked_list
import math

def menu(answer, yourBoard):
#Mostly for debugging. This creates arrays for all columns, rows, and sectors to include 
#arrays for the naught(values not present in the column, row, or sector) as well
	if (answer == 'r'):

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


#This allows manual population of a board by calling setCell		
	if (answer == 'i'):
		print(answer)
		nextRow = input("What row is your cell in?(1-9)")
		nextRow = int(nextRow)
		nextColumn = input("What column is your cell in?(a-i)")
		nextValue = input("What is your next value to populate?")
		nextValue = int(nextValue)
		setCell(nextRow, nextColumn, nextValue, yourBoard)

#This prints the board		
	if (answer == 'p'):
		for i in range(9):
			print(yourBoard[i])
		print()
		
#This is to create a linked list for all unsolved cells
#Not currently working, the idea was to store all linked lists in a dictionary
	#if (answer == 's'):
	#	linked_list.create(yourBoard)

#This finds all empty cells in yourBoard and creates, one at a time, an array(1-9) and then eliminates possibilites
#If the array length is 1, then the cell is solved
	if (answer == 's'):
		sector = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for k in range(9)]
		o4 = 0
		for o1 in range(0, 9, 3):
			for o2 in range(0, 9, 3):
				o3=-1
				for o5 in range(3):
					for o6 in range(3):
						o3+=1
						sector[o4][o3] = yourBoard[(o5+o1)][(o6+o2)]
				o4+=1
	
		
		for p in range(0, 9, 3):
			for n in range(0, 9, 3):
				for i in range(3):
					for j in range(3):

#i+p is the row, j+n the column allowing itteration through the entire 9x9 board
						rowNum = i+p
						columnNum = j+n
						if (yourBoard[(i+p)][(j+n)]==0):
							other = [1, 2, 3, 4, 5, 6, 7, 8, 9]
							#This traverses the row the cell is in. If it finds any values in that row, it removes them from other[]
							for ii in range(9):
								x = yourBoard[i+p][ii]
								if ((x != 0) and (x in other)):# and (x not in array)):
									other.remove(x)
#This traverses the column the cell is in. If it finds any values in that row, it removes them from other[]			
							for pp in range(9):
								y = yourBoard[pp][j+n]
								if ((y!=0) and (y in other)):
									other.remove(y)
			
							if ((rowNum<3 and columnNum<3)):
								for q in range(9):
									y = sector[0][q]
									if ((y!=0) and (y in other)):
										other.remove(y)
	
							if ((rowNum<3 and 2<columnNum<6)):
								for q in range(9):
									y = sector[1][q]
									if ((y!=0) and (y in other)):
										other.remove(y)
			
							if ((rowNum<3 and 5<columnNum<9)):
								for q in range(9):
									y = sector[2][q]
									if ((y!=0) and (y in other)):
										other.remove(y)					
					
							if ((2<rowNum<6 and columnNum<3)):
								for q in range(9):
									y = sector[3][q]
									if ((y!=0) and (y in other)):
										other.remove(y)
							
							if ((2<rowNum<6 and 2<columnNum<6)):
								for q in range(9):
									y = sector[4][q]
									if ((y!=0) and (y in other)):
										other.remove(y)			
				
							if ((2<rowNum<6 and 5<columnNum<9)):
								for q in range(9):
									y = sector[5][q]
									if ((y!=0) and (y in other)):
										other.remove(y)
				
							if ((5<rowNum<9 and columnNum<3)):
								for q in range(9):
									y = sector[6][q]
									if ((y!=0) and (y in other)):
										other.remove(y)
											
							if ((5<rowNum<9 and 2<columnNum<6)):
								for q in range(9):
									y = sector[7][q]
									if ((y!=0) and (y in other)):
										other.remove(y)

							if ((5<rowNum<9 and 5<columnNum<9)):
								for q in range(9):
									y = sector[8][q]
									if ((y!=0) and (y in other)):
										other.remove(y)
#This finds if there is only one value left, then solves the cell
							if (len(other)==1):
								yourBoard[i+p][j+n] = other[0]

#This allows a user to load in sudoku puzzles from a book I transcribed
#Will load more later, for now there is only 1
	if (answer == '1'):
		soduku_populate.populator(answer, yourBoard)




#receivers a row(int), column(char), value(int), board([[]]) and inserts the value by calling set column
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



	











