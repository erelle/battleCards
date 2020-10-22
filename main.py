import time
import random


name=input("whats your name? ")
print("hello "+name+" were gonna play battle!")
deckSize=int(input("how many cards do you want to have in your deck?  "))
deck=[]
for i in range (deckSize):
        deck.append(random.randrange(1, 14, 1))
print("your deck is set")

class Battle:
    def __init__(self,name, deck):
        self.name=name
        self.deck=deck
        self.enemyDeck = []
        self.side = []
    def start(self):
        for i in range(len(self.deck)):
            self.enemyDeck.append(random.randrange(1,14,10))
        print(self.deck,self.enemyDeck)
        while len(self.deck)>0 and len(self.enemyDeck)>0:
            myNum=self.deck.pop(0)
            self.enemyNum=self.enemyDeck.pop(0)
            print(self.name+"'s number:", myNum)
            print("computer's number:", self.enemyNum)
            if myNum>self.enemyNum:
                print(self.name+" wins")
                self.deck.append(myNum)
                self.deck.append(self.enemyNum)
                for i in self.side:
                    self.deck.append(i)
                self.side.clear()
                time.sleep(2)
            elif self.enemyNum>myNum:
                print("computer wins")
                self.enemyDeck.append(self.enemyNum)
                self.enemyDeck.append(myNum)
                for i in self.side:
                    self.deck.append(i)
                self.side.clear()
                time.sleep(2)
            else:
                print("its a tie")
                time.sleep(2)
                self.side.append(myNum)
                self.side.append(self.enemyNum)
                self.start()
        if len(self.deck)==0:
            print("computer wins the game!!")
        else:
            print(self.name+" win the game")





me=Battle(name,deck)
me.start()