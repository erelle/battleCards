import time
import random
import tkinter as tk


cards = {14: 'ace', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: "prince", 12: 'queen', 13: 'king', 15: 'joker'}

window = tk.Tk()
window.title("registration")
qframe=tk.Frame(master=window)
qframe.pack()
bframe=tk.Frame(master=window)
bframe.pack()

question= tk.Label(master=qframe, text="what is your name?")
question.grid(row=0, column=0, pady=5, sticky="w")
entry=tk.Entry(master=qframe)
entry.grid(row=0, column=1, padx=5, pady=5)
question2= tk.Label(master=qframe, text="how many cards do you want in your deck?")
entry2=tk.Entry(master=qframe)
question2.grid(row=1, column=0, pady=5, sticky="w")
entry2.grid(row=1, column=1, pady=5)


def start():
    window2 = tk.Tk()
    window2.title("lets begin")

    name = entry.get()
    number = int(entry2.get())
    greeting = tk.Label(master= window2, text="Hello " + name + " were gonna play battle!")
    deck = []
    for i in range(number):
        deck.append(random.randrange(2, 15, 1))

    window.destroy()

    greeting.pack()


b1 = tk.Button(master=bframe, command=start, text="ready", bg="black", fg="white", width=9, height=1)
b1.pack()




window.mainloop()







class Battle:
    def __init__(self,name, deck):
        self.name=name
        self.deck=deck
        self.enemyDeck = []
        self.side = []
    def start(self):
        for i in range(len(self.deck)):
            self.enemyDeck.append(random.randrange(2,15,1))
        print(self.deck,self.enemyDeck)
        while len(self.deck)>0 and len(self.enemyDeck)>0:
            myNum=self.deck.pop(0)
            self.enemyNum=self.enemyDeck.pop(0)
            print(self.name+"'s number:", cards[myNum])
            print("computer's number:", cards[self.enemyNum])
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