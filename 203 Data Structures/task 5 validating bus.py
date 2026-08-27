seat = [ ['' for col in range(5)] for row in range(2)]
seat[0][0] = 'D'
seat[0][1] = 'AB'
seat[0][2] = 'MD'
seat[1][4] = 'LL'
seat[1][0] = 'ES'
seat[1][2] = 'T'


for row in range(2):
    print(seat[row])


# TODO 1: ask the user for their initials, and a row and column for their seat
initials=input("please enter your initials: ")
seatgiven=False
while(not seatgiven): 
    row=int(input("please enter the row you want to sit in: "))
    col=int(input("please enter the column you want to sit in: "))

    if row<0 or row>1 or col<0 or col>4:
        print("error those seats are out side the bus and for legal reasons we cant let you sit there: ")
    elif seat[row][col]!="":
        print("snooze you lose")
    else:
        print("FINE YOU CAN GET ON THE BUS")
        seatgiven=True
        seat[row][col]=initials
        for i in range(2):
            print(seat[i])
# TODO 2: check whether that row and column is free (equal to '')


# TODO 3: if it is free, store the initials at that row and column


# TODO 4: if it is not free, display an error message and ask again for a row and column
