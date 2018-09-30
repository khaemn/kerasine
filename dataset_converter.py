inputFilename = "poker-hand-training-true.data.txt"
outputFilename = "trainingdata.txt"

inputFile = open(inputFilename, "r")
outputFile = open(outputFilename, "w")

'''
      Ordinal (0-9)

      0: Nothing in hand; not a recognized poker hand 
      1: One pair; one pair of equal ranks within five cards
      2: Two pairs; two pairs of equal ranks within five cards
      3: Three of a kind; three equal ranks within five cards
      4: Straight; five cards, sequentially ranked with no gaps
      5: Flush; five cards with the same suit
      6: Full house; pair + different rank three of a kind
      7: Four of a kind; four equal ranks within five cards
      8: Straight flush; straight + flush
      9: Royal flush; {Ace, King, Queen, Jack, Ten} + flush
'''

def handLine(number):
   return {
      '0': "1,0,0,0,0,0,0,0,0,0\n",
      '1': "0,1,0,0,0,0,0,0,0,0\n",
      '2': "0,0,1,0,0,0,0,0,0,0\n",
      '3': "0,0,0,1,0,0,0,0,0,0\n",
      '4': "0,0,0,0,1,0,0,0,0,0\n",
      '5': "0,0,0,0,0,1,0,0,0,0\n",
      '6': "0,0,0,0,0,0,1,0,0,0\n",
      '7': "0,0,0,0,0,0,0,1,0,0\n",
      '8': "0,0,0,0,0,0,0,0,1,0\n",
      '9': "0,0,0,0,0,0,0,0,0,1\n"
   }[number]

for line in inputFile:

   lastDigit = line[-2:-1]
   newString = line[0:-2] + handLine(lastDigit)

   print (line, "->", newString)

   outputFile.write(newString)

inputFile.close()
outputFile.close()
