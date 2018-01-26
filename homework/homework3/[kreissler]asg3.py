# for use in shuffling

#Does iter have to be in the same class as player
#what is keep count and what is play card supposed to do



import random


class Deck(object):
    def __init__(self):
        self.l = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
        self.m = ['Spades','Hearts','Clubs','Diamonds']
        self.x = {}
        self.y = []
        z = 0
        for i in self.l:
            self.x[z] = []
            for n in self.m:
                self.x[z] += [i+' of '+n]
                self.y += [i+' of '+n]
            z += 1



    def shuffleDeck(self):
        random.shuffle(self.y)
        return self.x, self.y
#
# This object represents a player. EAch player has a name,
# a count of cards one, and a hand of cards
#

class Player(object):

    def __init__(self,name,hand = None):
        self.name = name
        self.remaining = 26
        self.score1 = 0
        self.hand = hand
        self.card = None

#
# return card played (top of hand)
# 
    def playCard(self):
        print(self.hand[26-self.remaining])
# return number of cards left in hand
#
    def cardsLeft(self):
        return self.remaining
#
# keep count of number of cards
#
    def keepCount(self):
        return self.score1

#
# show number of cards won
#
    def score(self):
        return self.score1
#
# set up an iteration showing the cards at hand
# from last one dealt to first
#
    def sneakPeek(self):
        x = iter(self.hand)
        print("{}: {}".format(None, next(x)))
    def __iter__(self):
        self.i = len(self.lst)-1
        self.lst = self.hand
        return self.hand
    def __next__(self):
        if self.i <= 0:
            raise StopIteration
        index = self.i
        self.i -= 1
        return self.lst[index]
#
# set up the iter
#
    class Iter:
        def __init__(self,lst):
            self.lst = lst
            self.i = len(self.lst)-1

        def __iter__(self):
            return self
    
# set up to show cards in reverse order (last card dealt to first)
    def __next__(self):
        if self.i >= 0:
            index = self.i
            self.i -= 1
            return self.lst[index]
        else:
            raise StopIteration


#
# This is the class for a game. This class will use dealHands to define
# person objects (2 max)
#
class Game(object):
    
    # any inits
    def __init__(self):
        self.d = {}
        self.a = 0
        self.ties = 0

    # get the cards and return a shuffled deck
    
    def getDeck(self):
        self.x = Deck()

        self.y, self.cards = self.x.shuffleDeck()

    #
    # Deal each player a hand (1/2 the deck)
    #
    
    def dealHands(self,name1,name2):
        self.p1 = Player(name1)
        self.p2 = Player(name2)

        self.d[name1] = []
        self.d[name2] = []
        for i in range(len(self.cards)):
            if i % 2 == 0:
                self.d[name1] += [self.cards[i]]
            else:
                self.d[name2] += [self.cards[i]]
        self.p1.hand = self.d[name1]
        self.p2.hand = self.d[name2]


     #
     # return score
     # see sample output
     #
     
    def gameScore(self):
        print('{}: {}, {}: {}'.format(self.p1.name, self.p1.score1, self.p2.name, self.p2.score1))
    #
    # loop to play all hands consecutively
    #
    def playAllCards(self):
        while (self.p1.score1+self.p2.score1+(self.ties*2)!=52):
            self.playCards()
            print('=================')
        if self.p1.score1 > self.p2.score1:
            print("Game Winner: {}".format(self.p1.name))
        elif self.p1.score1 == self.p1.score1:
            print("TIE!")
        else:
            print("Game Winner: {}".format(self.p1.name))
        print("Ties: {}".format(self.ties))
        print("{}: {}, {}: {}".format(self.p1.name,self.p1.score1,self.p2.name,self.p2.score1))
    
    #
    # check if any cards left to play
    # if none, declare winner
    # see sample output
    #
    def checkDone(self):
        if self.a == 26:
            if self.p1.score1 > self.p2.score1:
                print("Game Winner: {}".format(self.p1.name))
            elif self.p1.score1 == self.p1.score1:
                print("TIE!")
            else:
                print("Game Winner: {}".format(self.p1.name))
            print("Ties: {}".format(self.ties))
            print("{}: {}, {}: {}".format(self.p1.name, self.p1.score1, self.p2.name, self.p2.score1))
        else:
            print('Game not over')


    #
    # Get playing card from top of each player's hand
    # Reformat for suit and cards greater than 10
    # Compare cards and determine winner. Winner card count
    # gets incremented by 2. Ties are not counted.
    # Check if any cards left
    #

    def playCards(self):
        self.p1.remaining -= 1
        self.p2.remaining -= 1
        self.p1.card = self.d[list(self.d.keys())[0]][self.a]
        self.p2.card =self.d[list(self.d.keys())[1]][self.a]
        self.p1.name = list(self.d.keys())[0]
        self.p2.name = list(self.d.keys())[1]

        print("{} played {}".format(self.p1.name,self.p1.card))
        print("{} played {}".format(self.p2.name, self.p2.card))

        for keys in self.y:
            if self.p1.card in self.y[keys]:
                player1 = keys
            if self.p2.card in self.y[keys]:
                player2 = keys

        if player1 > player2:
            print("{} won this battle".format(self.p1.name))
            self.p1.score1 += 2
        elif player1 == player2:
            self.ties += 1
        else:
            print("{} won the battle".format(self.p2.name))
            self.p2.score1 += 2

        print('{}: {}, {}: {}'.format(self.p1.name,self.p1.score1,self.p2.name,self.p2.score1))
        self.a +=1

x = Game()

x.getDeck()

print(x.cards)

x.dealHands('Jean','George')

print(x.p1.name)

print(x.p2.name)

print(x.p1.hand)

print(x.p2.hand)

x.p1.sneakPeek()


x.checkDone()
x.playCards()
x.p1.playCard()
print(x.p1.remaining)