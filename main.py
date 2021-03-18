import random
import numpy

suits = {0: 'null', 1: 'Spades', 2: 'Hearts', 3: 'Clubs', 4: 'Diamonds'}
values = {0: 'null', 11: 'Jack', 12: 'Queen', 13: 'King', 1: 'Ace',
          2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}
shortSuit = {'null': 'n', 'Spades': '♠', 'Hearts': '♥', 'Clubs': '♣', 'Diamonds': '♦'}
shortValue = {'null': 'n', 'Jack': 'J', 'Queen': 'Q', 'King': 'K', 'Ace': 'A',
              '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9', '10': 'T'}


class Card:
    value = ""
    suit = ""

    def __init__(self, v: str, s: str):
        self.value = v
        self.suit = s

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def setValue(self, v: str):
        self.value = v

    def setSuit(self, s: str):
        self.suit = s

    def toString(self):
        if self.value != 'null':
            return self.value + " of " + self.suit
        else:
            return 'null card'

    def toShorten(self):
        if self.value != 'null':
            return shortValue.get(self.value) + shortSuit.get(self.suit)
        else:
            return 'nc'


class Player:
    name = ""
    hand = [Card] * 2
    stack = 0
    position = ""

    def __init__(self, n: str, h: [], buyIn: int, p: str):
        self.name = n
        for c in h:
            self.hand[c] = h[c]
        self.stack = buyIn
        self.position = p

    def toString(self):
        print(self.name, "Current Hand:", self.hand[0].toShorten(), self.hand[1].toShorten(), self.stack, "chips")


def playRound(passDeck: list):

    nullHand = [nullCard, nullCard]

    hands = [nullHand] * numPlayers

    communityCards = [nullCard, nullCard, nullCard, nullCard, nullCard]

    deal(passDeck, hands)

    betRound()

    flop()

    betRound()

    turn()

    betRound()

    river()

    betRound()

    showDown()

    for hand in hands:
        printCardListShort(hand)


def deal(passDeck: list, hands: list):

    # dealing out the first round of cards to each hand
    for x in range(numPlayers):
        handAdd = [nullCard, nullCard]
        handAdd[0] = passDeck.pop()
        handAdd[1] = passDeck.pop()
        hands.__setitem__(x, handAdd)


# simulates a betting round preflop, before the turn, before the river, and after the river
def betRound():
    tablePlayersList


# burns one card from the deck, then adds the next 3 to the community
def flop():
    tablePlayersList


# burns one card from the deck, then adds the next card to the community
def turn():
    tablePlayersList


# burns one card from the deck, then addes the next card to the community
def river():
    tablePlayersList


# compares the best possible hands that players can make and determines which player won the hand
def showDown():
    tablePlayersList


# gives the chips to the winner of the pot, also handles any possible side-pots that were made
def payout():
    tablePlayersList


# prints a list of cards in shortened format
def printCardListShort(hand: list):
    for card in hand:
        print(card.toShorten(), end=' ')
    print()


# prints a list of cards in long format
def printCardListLong(hand: list):
    for card in hand:
        print(card.toString(), end=' ')
    print()


# NEEDS IMPLEMENTATION
def tableToString(hands: list, players: list):
    for player in players:
        print()


nullCard = Card(0, 0)
deck = []
counter = 0
tablePlayersList = []

# initializing deck and shuffling
suitNum = 4
valueNum = 13
for newSuit in range(suitNum):
    for newValue in range(valueNum):
        newCard = Card(values.get(newValue + 1), suits.get(newSuit + 1))
        deck.append(newCard)

random.shuffle(deck)

# viewing the whole deck in order for debugging purposes
print("deck:")
for dCard in deck:
    print(dCard.toShorten(), end=' ')

print()
# end debugging

stopGame = False
numPlayers = 4

while not stopGame:
    # this will be one hand in the game
    playRound(deck)
    stopGame = True
