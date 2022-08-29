import sudoku_populate
import linked_list
import math
from os import system, name
from time import sleep
import sys

def menu(answer, yourBoard):

#Manual population of a board		
	if (answer == 'i'):
		print(answer)
		nextRow = input("What row is numberToCheckour cell in?(1-9)")
		nextRow = int(nextRow)
		nextColumn = input("What column is numberToCheckour cell in?(a-i)")
		nextValue = input("What is numberToCheckour next value to populate?")
		nextValue = int(nextValue)
		setCell(nextRow, nextColumn, nextValue, yourBoard)

#Print board		
	if (answer == 'p'):
		for i in range(9):
			print(yourBoard[i])
		print()
		sleep(5)
		system("clear")

#This finds all emptnumberToCheck cells in yourBoard and creates, one at a time, an arranumberToCheck(1-9) and then eliminates possibilites
#If the arranumberToCheck length is 1, then the cell is solved
	if (answer == 's'):
		sector = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for k in range(9)]
		sectorRowNum = 0
		for boardRowOne in range(0, 9, 3):
			for boardColumnOne in range(0, 9, 3):
				sectorColumnNum=-1
				for boardRowTwo in range(3):
					for boardColumnTwo in range(3):
						sectorColumnNum+=1
						sector[sectorRowNum][sectorColumnNum] = yourBoard[(boardRowTwo+boardRowOne)][(boardColumnTwo+boardColumnOne)]
				sectorRowNum+=1
	
		
		for p in range(0, 9, 3):
			for n in range(0, 9, 3):
				for i in range(3):
					for j in range(3):
						rowNum = i+p
						columnNum = j+n

						#Creates an array holding all possible solutions
						if (yourBoard[(rowNum)][(columnNum)]==0):
							possibleSolutionArrayNumToCheck = [1, 2, 3, 4, 5, 6, 7, 8, 9]

							#Removes values found in row
							for tempColumnNum in range(9):
								numberToCheck = yourBoard[rowNum][tempColumnNum]
								checkForRemoval(numberToCheck, possibleSolutionArrayNumToCheck)
							
							#Removes values found in column			
							for tempRowNum in range(9):
								numberToCheck = yourBoard[tempRowNum][columnNum]
								checkForRemoval(numberToCheck, possibleSolutionArrayNumToCheck)

							#Removes values found in sector
							if ((rowNum<3 and columnNum<3)):
								sectorRemover(sector, 0, possibleSolutionArrayNumToCheck)
							if ((rowNum<3 and 2<columnNum<6)):
								sectorRemover(sector, 1, possibleSolutionArrayNumToCheck)
							if ((rowNum<3 and 5<columnNum<9)):
								sectorRemover(sector, 2, possibleSolutionArrayNumToCheck)			
							if ((2<rowNum<6 and columnNum<3)):
								sectorRemover(sector, 3, possibleSolutionArrayNumToCheck)
							if ((2<rowNum<6 and 2<columnNum<6)):
								sectorRemover(sector, 4, possibleSolutionArrayNumToCheck)		
							if ((2<rowNum<6 and 5<columnNum<9)):
								sectorRemover(sector, 5, possibleSolutionArrayNumToCheck)
							if ((5<rowNum<9 and columnNum<3)):
								sectorRemover(sector, 6, possibleSolutionArrayNumToCheck)		
							if ((5<rowNum<9 and 2<columnNum<6)):
								sectorRemover(sector, 7, possibleSolutionArrayNumToCheck)
							if ((5<rowNum<9 and 5<columnNum<9)):
								sectorRemover(sector, 8, possibleSolutionArrayNumToCheck)

							#Checks if solved
							if (len(possibleSolutionArrayNumToCheck)==1):
								yourBoard[rowNum][columnNum] = possibleSolutionArrayNumToCheck[0]

#Loads premade puzzle
	if (answer == '1'):
		sudoku_populate.populator(answer, yourBoard)
	
	if (answer == '2'):
		sudoku_populate.populator(answer, yourBoard)

def sectorRemover(sector, sectorRow, possibleSolutionArrayNumToCheck):
	for sectorColumnSolver in range(9):
			numberToCheck = sector[sectorRow][sectorColumnSolver]
			checkForRemoval(numberToCheck, possibleSolutionArrayNumToCheck)

def checkForRemoval(numberToCheck, possibleSolutionArrayNumToCheck):
	if ((numberToCheck != 0) and (numberToCheck in possibleSolutionArrayNumToCheck)):
		possibleSolutionArrayNumToCheck.remove(numberToCheck)

def setCell(row, column, value, yourBoard):
	setColumn(row-1, column, value, yourBoard)

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



	





