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
    dealtcards = [card() for index in range(10)]
    selectednums = []
    # pick 10 to return
    for index in range(10):
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

def init_suit(deck):
    suits = ["hearts","clubs","diamonds","spades"]
    for card in deck:
        card.suitval=card.value + (suits.index(card.suit)+1)*0.1
    return deck

def sort_cards(deck):
    init_suit(deck)
    current=deck[1]
    for i in range(deck):
        while deck[i].size<deck[i-1].size:
            store=deck[i-1]
            deck[i-1]=deck[i]
            deck[i]=deck[i-1]
    print(deck)



# main program
cards = [card() for index in range(10)]
allcards = [card() for index in range(52)]
allcards = build_deck()
cards = draw_cards(allcards)
display_cards(cards)

# cards = sort_cards()
# display_cards(cards)