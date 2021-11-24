import boardBuilder
import numpy as np


def main():
	answer = 'z'
	print("Welcome to the Sudoku solver!")
	while (answer != 'q'):
		print("What would you like to do next?")
		print("Press i to populate a cell.")
		print("Press p to print your Sudoku table.")
		answer = input("Press q to quit.")
		boardBuilder.menu(answer, yourBoard)
	
	



if __name__ == "__main__":
	yourBoard = [[0 for a in range(9)] for b in range(9)]
	main()



