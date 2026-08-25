# AH Structures 1
# Using 1D Array of Records create a record structure for a customer buying a cinema ticket

# 5 customers in the array
# 1 customer with details added by you

from dataclasses import dataclass
@dataclass
class ticket():
    movie_name: str=""
    screen: int=0
    seat: str="" 

tickets=[ticket() for x in range(5)]
tickets[0].movie_name="Odyssey"
tickets[0].screen="9"
tickets[0].seat="B4"

print (tickets)
