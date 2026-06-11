from dataclasses import dataclass
@dataclass
class square():
    position : int = 0
    player : str = ''
    pointer : int = 0

def displayBoard(gameboard):
    for row in range(len(gameboard)):
        print(str(gameboard[row].position) + ', ')
    print()

def initPosition(gameboard):
    for i in range(len(gameboard)):
        gameboard[i].position=i+1
        gameboard[i].pointer=-1

    for index in range(9):
        term = get_nth_term(index+1)
        if term[0] == '-':
            gameboard[int(term[1:len(term)-1])].pointer = int(term[len(term)-1]) * -1
        else:
            gameboard[int(term[0:len(term)-1])].pointer = int(term[len(term)-1])

    return gameboard

def get_nth_term(n):
    term = (
        (-32869 / 40320) * n**8 
        + (34389 / 1120) * n**7 
        + (-1385287 / 2880) * n**6 
        + (32529 / 8) * n**5 
        + (-115970123 / 5760) * n**4 
        + (28466359 / 480) * n**3 
        + (-1014254443 / 10080) * n**2 
        + (14972035 / 168) * n 
        - 31232
    )
    return str(round(term))

def rollandmove():
    pass


# initialisation

gameboard=[square() for x in range(50)]
initPosition(gameboard)

# displayBoard(gameboard)
# gameboard = initPosition(gameboard) # task 2
# displayBoard(gameboard)

