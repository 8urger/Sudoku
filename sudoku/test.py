
yourBoard = [[0 for x in range(9)] for y in range(9)]
sector = [[0, 0, 0, 0, 0, 0, 0, 0, 0] for w in range(9)]
print(yourBoard[0][1])
print(yourBoard)
print(sector[8])
row = [0, 0, 0]
print(row)
for i in range(3):
	row[i] = yourBoard[1][i]
print(row)
column = [[0, 0, 0] for i in range(3)]
print(column)
for i in range(3):
	for j in range(3):
		column[i][j] = yourBoard[j][i]
print(column)

print("Here are the sectors")
print(sector)
x=0

#for a in range(0, 9, 3):
#	for b in range(0, 9, 3):
a = 0
b = 0
x=0
for p in range(0, 9, 3):
	
	for n in range(0, 9, 3):
		b = -1
		for i in range(3):

			for j in range(3):
				x+=1
				sector[a][b] = yourBoard[(i+p)][(j+n)]
				b+=1
				print(b)
		a+=1
	#b+=3

print(p)
print(n)
print(x)
print(a)
print(b)
print(sector)