import itertools
from enum import Enum
from math import factorial


def variations(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


class Suit(Enum):
    Spades = 0
    Clubs = 1
    Diamonds = 2
    Hearts = 3


class Value(Enum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    # ...


class Card:
    def __init__(self, value, suit):
        self.range = value
        self.suit = suit

    def __str__(self):
        return "[" + str(self.range.name) + " of " + str(self.suit.name) + "]"


class Deck:
    def __init__(self, ranges, suits):
        self.cards = list()
        for r in ranges:
            for s in suits:
                self.cards.append(Card(r, s))

    def size(self):
        return len(self.cards)

    def totalSets(self, quantity):
        return variations(len(self.cards), quantity)

    def sets(self, quantity):
        return list(itertools.permutations(self.cards, quantity))


deck = Deck([Value.Ace, Value.Two, Value.Three], [Suit.Spades, Suit.Hearts])

print("Deck size is: ", deck.size())

quantity = 2

print(deck.totalSets(quantity), "variations could be combined using", quantity, "cards from this deck.")

cardSets = deck.sets(quantity)

for cardSet in cardSets:
    print("set:")
    setString = str()
    for card in cardSet:
        setString += str(card)
    print(setString)
