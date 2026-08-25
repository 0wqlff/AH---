# AH Structures 1
# Using 1D Array of records create a record structure for acustomer buying a cinema ticket

#5 customers in the array
#1 customer with details added by you
class ticket:

    def __init__(self):
        self.movie=''
        self.seat=''
        self.screen=0

    #setters
    def setMovie(self, moviename):
        self.movie=moviename

    def setSeat(self, seatno):
        self.seat=seatno

    def setScreen(self, screeno):
        self.screen=screeno

    #getters
    def getScreen(self):
        return self.screen

    def getMovie(self):
        return self.movie

    def getSeat(self):
        return self.seat

clients=[ticket() for x in range(5)]

#use setters
clients[0].setMovie('Odyssey')
clients[0].setScreen(9)
clients[0].setSeat('B4')

#use getters
print(clients[0].getMovie())
print(clients[0].getScreen())
print(clients[0].getSeat())