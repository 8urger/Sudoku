import boardBuilder
import soduku_populate

def main():
	answer = 'z'
	print("Welcome to the Sudoku solver!")
	while (answer != 'q'):
		print("What would you like to do next?")
		print("Press i to populate a cell.")
		print("Press p to print your Sudoku table.")
		print("Press 1-9 to load pre-programmed puzzles in.")
		print("Press r to populate all columns, rows, and sectors")
		print("Press s to solve!")
		answer = input("Press q to quit.")
		boardBuilder.menu(answer, yourBoard)

if __name__ == "__main__":
	yourBoard = [[0 for a in range(9)] for b in range(9)]
	main()




