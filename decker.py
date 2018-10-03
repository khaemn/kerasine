#https://www.calculator.net/permutation-and-combination-calculator.html

import itertools
from enum import Enum
from math import factorial


def variations(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)


class Suit(Enum):
    Empty = -1
    Spades = 0
    Clubs = 1
    Diamonds = 2
    Hearts = 3


class Value(Enum):
    Empty = 0
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    # ...


class Card:
    SUIT_LENGTH = Value.King.value
    def __init__(self, value = Value.Empty, suit = Suit.Empty):
        self.val = value
        self.suit = suit

    def __str__(self):
        return "[" + str(self.val.name) + " of " + str(self.suit.name) + "]"

    @staticmethod
    def fromSuitValue(suitValue):
        print("suitValue", suitValue)
        if len(suitValue) != 2:
            print("Error: can not convert", suitValue, "to a Card!")
            return Card()
        suit = Suit(suitValue[0])
        value = Value(suitValue[1])
        return Card(value, suit)

    def indexIn52Deck(self):
        suitIndex = self.suit.value
        valueIndex = self.val.value
        return (suitIndex * self.SUIT_LENGTH) + valueIndex

    def isValid(self):
        return self.val != Value.Empty and self.suit != Suit.Empty


class Deck:
    DECK_LENGTH = 52
    def __init__(self, ranges = frozenset(), suits = frozenset()):
        self.cards = set()
        for r in ranges:
            for s in suits:
                self.cards.add(Card(r, s))

    def size(self):
        return len(self.cards)

    def totalSets(self, quantity):
        return variations(len(self.cards), quantity)

    def sets(self, quantity):
        return list(itertools.combinations(self.cards, quantity))

    @staticmethod
    def to52binary(hand = list()):
        binaryList = []
        for i in range(0, Deck.DECK_LENGTH):
            binaryList.append(0)
        for card in hand:
            binaryList[card.indexIn52Deck()] = 1
        return binaryList

    @staticmethod
    def from52binary(binaryList = list()):
        if len(binaryList) != 52:
            print("error: can not convert", binaryList, "to a card set!")
            return []




deck = Deck([Value.Ace], [Suit.Spades, Suit.Clubs, Suit.Diamonds, Suit.Hearts])

print("Deck size is: ", deck.size())

quantity = 3

print(deck.totalSets(quantity), "variations could be combined using", quantity, "cards from this deck.")

cardSets = deck.sets(quantity)

i = 0
for cardSet in cardSets:
    i += 1
    print("set",i,":")
    setString = str()
    for card in cardSet:
        setString += str(card)
    setString += " | "
    asBinaryList = Deck.to52binary(cardSet)
    for char in asBinaryList:
        setString += (str(char) + ',')
    print(setString)
