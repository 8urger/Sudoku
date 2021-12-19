yourBoard = [[0 for a in range(9)] for b in range(9)]
yourBoard[0][2]=8
yourBoard[0][5]=7
yourBoard[0][6]=5
yourBoard[0][7]=4
yourBoard[1][0]=4
yourBoard[1][3]=5
yourBoard[1][4]=2
yourBoard[1][6]=7
yourBoard[1][8]=9
yourBoard[2][3]=8
yourBoard[2][4]=3
yourBoard[3][1]=4
yourBoard[3][3]=2
yourBoard[3][5]=3
yourBoard[3][8]=8
yourBoard[4][1]=3
yourBoard[4][2]=7
yourBoard[4][4]=4
yourBoard[4][6]=2
yourBoard[4][7]=5
yourBoard[5][0]=5
yourBoard[5][3]=7
yourBoard[5][5]=9
yourBoard[5][7]=1
yourBoard[6][4]=7
yourBoard[6][5]=6
yourBoard[7][0]=3
yourBoard[7][2]=5
yourBoard[7][4]=8
yourBoard[7][5]=2
yourBoard[7][8]=1
yourBoard[8][1]=2
yourBoard[8][2]=6
yourBoard[8][3]=9
yourBoard[8][6]=4
for i in range(9):
	print(yourBoard[i])



print("Now for the test")
print(yourBoard[0])
yourBoard[0].remove(8)
print("Deletion has happened")
for i in range(9):
	print(yourBoard[i])#this is working because it's printing the rows, not each element

print("Adding it back in")
yourBoard[0] = [0, 0, 8, 0, 0, 7, 5, 4, 0]
for i in range(9):
	print(yourBoard[i])

print("The zero delete test")
deleteArray = [0, 1, 3, 0, 0, 5]
print(deleteArray)
for y in range(len(deleteArray)):
	if (deleteArray[y] == 0):
		pass


print("And now the board")
for i in range(9):
	print(yourBoard[i])

toSolve = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def solver(yourBoard, full, i, j):
	
	print("Here is i and j")
	print(i)
	print(j)
	for m in range(len(full)):
		if (yourBoard[i][m]!=0):
			x = yourBoard[i][m]
			for i in range(len(full)):
				if (full[i] == x):
					print("hi")
					

	def compare_num(self, x):
		cur_node = self.head
		while cur_node:
			if (cur_node.data == x):
				return True

	for n in range(9):
		if (yourBoard[n][j]!=0):
			x = yourBoard[n][j]
			for i in range(len(full)):
				if (full[j]==x):
					full[j]=0

	print(full)
	x=0
	for i in range(len(full)):
		if (full[i]==0):
			x=x+1
			
	print(x)
	print(yourBoard[i][j])
	return full
x=0
#for i in range(9):
#	for j in range(9):
#		if (yourBoard[i][j]==0):
#			solver(yourBoard, i, j)
full = [1, 2, 3, 4, 5, 6, 7, 8, 9]
solver(yourBoard, full, 0, 0)
print(full)
