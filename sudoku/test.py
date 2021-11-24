import pprint
import numpy as np


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
for i in range(4):
	print(yourBoard[i])



for i in range(4):
	for j in range(4):
		if (yourBoard[i][j]!=0):
			q = yourBoard[i][j]
			#actualBoard[i][j][(q-1)]=0
			for a in range(4):
				actualBoard[i][j][a] = 0

# Pass the cordinates for the cell to be solved(i, j)
# Pass the sector the cell is in(sector_x)
# Now I can say that coordinate ij == naught(sector, i, j)
def solver(i, j, x):
	#for loop iterating through all 
	#values in the naught, if !=0, add to possibilities
	pass

#isolate the sector that needs to be solved to pass to solver
print("And now this test")
for i in range(4):
	for j in range(4):
		if (yourBoard[i][j]==0):
			if ((0<=i<2) and (0 <=j<2)):
				solver(i, j, sec1)
			elif((0<=i<2) and (2<=j<4)):
				print("sector2")#solver(i, j, sec2)
			elif((2<=i) and (0<=j<2)):
				print("Sector3")#solver (i, j, sec3)
			else:
				print("sector4")#solver(i, j, sec4)
print("Test complete")
pprint.pprint(actualBoard)
print(q)
print(x)

