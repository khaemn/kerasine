from decker import Card, Deck, Value, Suit


class IDetector:
    @staticmethod
    def detect(binaryList = list()):
        raise 'Abstract class!'

    @staticmethod
    def checkLength(binaryList = list()):
        if len(binaryList) != Deck.DECK_LENGTH:
            raise 'Wrong input binary list length!'




class PairDetector(IDetector):
    @staticmethod
    def isPair(card1 = Card(), card2 = Card()):
        return card1.isValid() and card2.isValid() and card1.val == card2.val

    @staticmethod
    def isInBinaryList(binaryList = list()):
        IDetector.checkLength(binaryList)

        # todo: impl!



