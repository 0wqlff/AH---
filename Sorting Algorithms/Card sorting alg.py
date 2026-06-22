from dataclasses import dataclass
import random
@dataclass
class card():
    suit : str = ''
    value : int = 0
    suitval: float=0.0

def build_deck():
    # setup all cards and return ten of them
    thesecards = [card() for index in range(52)]
    suits = ['hearts', 'clubs','diamonds','spades']
    count = 0
    for s in range(0,4):
        for index in range(1,14):
            thesecards[count].suit = suits[s]
            thesecards[count].value = index
            count += 1
    return thesecards

def draw_cards(thesecards):
    dealtcards = [card() for index in range(4)]
    selectednums = []
    # pick 10 to return
    for index in range(4):
        selectednum = random.randint(0,51)
        while selectednum in selectednums:
            selectednum = random.randint(0,51)
        selectednums.append(selectednum)
        dealtcards[index] = thesecards[selectednum]
    return dealtcards

def display_cards(cardarray):
    for index in range(len(cardarray)):
        output = cardarray[index].suit
        output = output + " : " + str(cardarray[index].value)
        print(output)
    print()

def init_suit(deck):
    suits = ["hearts","clubs","diamonds","spades"]
    for card in deck:
        card.suitval=card.value + (suits.index(card.suit)+1)*0.1
    return deck

def sort_cards(deck):

    current=1
    swaps=0
    swapcheck=False
    noswaps=0

    while current<len(deck):
        position=current


        while deck[position].suitval < deck[position-1].suitval and position>0:
            deck[position],deck[position-1]=deck[position-1],deck[position]
            swaps+=1
            swapcheck=True
            position-=1
            display_cards(deck)
            print()

        if swapcheck==False:
            display_cards(deck)
            print("noswap")
            noswaps+=1
            print()
        swapcheck=False
        current+=1

    print(f"{swaps} swaps were made, {noswaps} no swaps were made")



# main program
cards = [card() for index in range(4)]
allcards = [card() for index in range(52)]


allcards = build_deck()
cards = draw_cards(allcards)

init_suit(cards)
display_cards(cards)
sort_cards(cards)

# cards = sort_cards()
# display_cards(cards)