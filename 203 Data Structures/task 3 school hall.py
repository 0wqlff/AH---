rows = 4
cols = 6
seats = [['-' for c in range(cols)] for r in range(rows)]
 
# TODO 1: fill every seat with '-'
 
# TODO 3: mark seats (1,1), (2,4) and (3,0) as 'X'
seats[1][1]="X"
seats[2][4]="X"
seats[3][0]="X"
# TODO 2: display the grid neatly, one row per line
for row in range(rows):
	print(" ".join(seats[row]))
 
# TODO 4: count and display the number of free seats
counter=0
for i in range(len(seats)):
    for r in range(len(seats[0])):
        if (seats[i][r]=="-"):
            counter+=1
print(counter)