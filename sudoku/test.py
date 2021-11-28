import pprint



yourBoard = [[0 for a in range(4)] for b in range(4)]
for i in range(4):
	print(yourBoard[i])
actualBoard = [[[0 for a in range(4)] for c in range(4)] for c in range(4)]

print("")
for i in range(4):
	for j in range(4):
		for h in range(4):
			actualBoard[i][j][h] = h+1

sec1 = [1, 0, 3, 4]
sec2 = [3, 0, 1, 2]
sec3 = [4, 1, 2, 3]
sec4 = [2, 3, 4, 1]
naught1 = [0, 2, 0, 0]
naught2 = [0, 4, 0, 0]
naught3 = [0, 0, 0, 0]
naught4 = [0, 0, 0, 0]

pprint.pprint(actualBoard)

print("3D array element")

print(actualBoard[0][0][0])

print("")

yourBoard[0][0] = 1
yourBoard[0][1] = 0
yourBoard[0][2] = 3
yourBoard[0][3] = 0
yourBoard[1][0] = 3
yourBoard[1][1] = 4
yourBoard[1][2] = 1
yourBoard[1][3] = 2
yourBoard[2][0] = 4
yourBoard[2][1] = 1
yourBoard[2][2] = 2
yourBoard[2][3] = 3
yourBoard[3][0] = 2
yourBoard[3][1] = 3
yourBoard[3][2] = 4
yourBoard[3][3] = 1
x = 0
print("This is the actual board missing 2 and 4")
for i in range(4):
	print(yourBoard[i])



for i in range(4):
	for j in range(4):
		if (yourBoard[i][j]!=0):
			q = yourBoard[i][j]#holds the value of number found
			#actualBoard[i][j][(q-1)]=0
			for a in range(4):
				actualBoard[i][j][a] = 0
				#now arrays for completed cells hold all zeros

print("3d array")
pprint.pprint(actualBoard)


# Pass the cordinates for the cell to be solved(i, j)
# Pass the sector the cell is in(sector_x)
# Now I can say that coordinate ij == naught(sector, i, j)
def solver(i, j, x, y):
	print("This is i(row) and j(column) values")
	print(i)
	print(j)
	#for loop iterating through all 
	#values in the naught, if !=0, add to possibilities
	print("This is my row")
	print(yourBoard[i])
	for n in range(4):
		print(yourBoard[n][j])#this prints the column
	print("Done with row and column, here is the sector")
	print(x)



#now I have the row, sector, and column, should be able to
#itterate through to solve
#if actualBoard[ij](holds all possible) ==row[i]||column[j]
#||sector, delete that value. Once absolute value of
#actualBoard[ij]==1, found that cells value


	print("This is the not array for the cell missing")
	print(actualBoard[i][j])
	print("This is x and y, sector and naughtsec")
	print(x)#this is printing the sector that I want
	print(y)#this prints the naughtsector
	print("End of x and y")
	for i in range(4):
		if ((y)[i]!=0):
			a = y[i]#this prints the value in naught
			print(x)
			actualBoard[i-1][j][(a-1)]=9#













#isolate the sector that needs to be solved to pass to solver
print("And now this test")
for i in range(4):
	for j in range(4):
		if (yourBoard[i][j]==0):#yourBoard is 2d array
			if ((0<=i<2) and (0 <=j<2)):
				solver(i, (j), sec1, naught1)#this works, just need to figure out what to pass
				#I can pass i, j, to represent the column and row
				#this isolates the sector, so now I have all three 
				#to pass to SOLVER


#this is passing sector2 for some reason

			elif((0<=i<2) and (2<=j<4)):
				print("Ha")#solver(i, j, sec2, naught2)
			elif((2<=i) and (0<=j<2)):
				print("Sector3")#solver (i, j, sec3, naught4)
			else:
				print("sector4")#solver(i, j, sec4, naught4)
print("Test complete, here is the 3d array")
pprint.pprint(actualBoard)
print(q)
print(x)
