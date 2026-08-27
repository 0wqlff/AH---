students = ['Ali', 'Bea', 'Cal', 'Dee', 'Eve']
marks = [
	[14, 16, 12, 18],
	[9,  11, 15, 10],
	[20, 19, 18, 20],
	[7,  8,  10, 6],
	[15, 14, 16, 17]
]
 
for r in range(len(marks)):
	print(students[r], marks[r])
      
total=0
for i in range(len(students)):
    total=0
    for j in range(len(marks[i])):
        total+=marks[i][j]
    print(students[i]+" "+str(total/4))
    total=0

for i in range(4):
    total=0
    for j in range(5):
        total+=marks[j][i]
    print(f"test {i} had an average of "+str(total/5))

max_mark=marks[0][0]
row_max_mark=0
col_max_mark=0

for i in range(len(marks)*len(marks[0])):
    row=i//len(marks)
    col=i%len(marks[0])

    if (marks[row][col]>max_mark):
        max_mark=marks[row][col]
        row_max_mark=row
        col_max_mark=col

print("The highest mark was " + str(max_mark) + " achieved by " + students[row_max_mark] + " in test " + str(col_max_mark+1))

print("")

# TODO 4: lowest mark, student and test

min_mark=marks[0][0]
row_min_mark=0
col_min_mark=0
for i in range(len(marks)*len(marks[0])):
    row=i//len(marks)
    col=i%len(marks[0])

    if (marks[row][col]<max_mark):
        min_mark=marks[row][col]
        row_min_mark=row
        col_min_mark=col

print("The lowest mark was " + str(min_mark) + " achieved by " + students[row_min_mark] + " in test " + str(col_min_mark+1))