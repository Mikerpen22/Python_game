from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

import random

answer = ""
playerGuess = ""
nOfDigits = 4



class StartWin(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master



class MainWin(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

    def nDigitNumber(self, n):
        numbers = random.sample(range(10), 4)
        randNum = ''.join(map(str, numbers))
        return randNum

    def newGame(self):
        print("newGame")
        global nOfDigits
        global answer
        self.resultLabel.config(text="")
        label.config(text="")
        self.answers.delete(1.0, END)
        answer = self.nDigitNumber(nOfDigits)
        print(answer)


    def reenter(self):
        label.config(text="")

    def checkUserGuess(self):
        global playerGuess
        global answer
        global nOfDigits
        global label
        playerGuess = label.cget("text")
        if len(playerGuess) == nOfDigits:
            a = self.calA(playerGuess)
            b = self.calB(playerGuess)
            self.showResult(a, b)
            label.config(text="")
            self.answers.insert(INSERT, playerGuess + "   " + str(a) + "A" + str(b) + "B"+"\n")
        else:
            messagebox.showinfo("¥£øÙ", "¶Ïº∆≠n¨∞" + str(nOfDigits))
            label.config(text="")


    def calA(self, guess):
        global answer
        a = 0
        for i in range(len(answer)):
            if guess[i] == answer[i]:
                a = a + 1

        return a


    def calB(self, guess):
        global answer
        b = 0
        k = len(answer)
        for i in range(k):
            for j in range(k):
                if i != j:
                    if guess[i] == answer[j]:
                        b = b + 1
        return b


    def showResult(self, a, b):
        if a == nOfDigits:
            result = "You Win"
        else:
            result = str(a) + "A" + str(b) + "B"

        self.resultLabel.config(text=result)


    def clickBut1(self):
        label.configure(text=label.cget("text")+"1")


    def clickBut2(self):
        label.configure(text=label.cget("text")+"2")


    def clickBut3(self):
        label.configure(text=label.cget("text")+"3")


    def clickBut4(self):
        label.configure(text=label.cget("text")+"4")


    def clickBut5(self):
        label.configure(text=label.cget("text")+"5")


    def clickBut6(self):
        label.configure(text=label.cget("text")+"6")


    def clickBut7(self):
        label.configure(text=label.cget("text")+"7")


    def clickBut8(self):
        label.configure(text=label.cget("text")+"8")


    def clickBut9(self):
        label.configure(text=label.cget("text")+"9")


    def clickBut0(self):
        label.configure(text=label.cget("text")+"0")

    def clickButBack(self):
        str = label.cget("text")
        label.configure(text=str[0:-1])

    mainWin = Tk()

    mainWin.title("1A2B")

    mainWin.geometry("440x440")

    resultLabel = Label(mainWin, text="0A0B", font=('arial', 32))
    var = StringVar(mainWin)

    load_1 = Image.open('reenter.png')
    reenter_img = ImageTk.PhotoImage(load_1)

    guessBtn = Button(mainWin, text="Guess", command=checkUserGuess, height=3, width=20)
    newGameBtn = Button(mainWin, text="New Game", command=newGame, height=3, width=20)
    reenterBtn = Button(mainWin, image=reenter_img, command=reenter, height=30, width=35)

    label = Label(text="", font=('arial', 30))
    Btn1 = Button(mainWin, text="1", command=clickBut1, height=3, width=6)
    Btn2 = Button(mainWin, text="2", command=clickBut2, height=3, width=6)
    Btn3 = Button(mainWin, text="3", command=clickBut3, height=3, width=6)
    Btn4 = Button(mainWin, text="4", command=clickBut4, height=3, width=6)
    Btn5 = Button(mainWin, text="5", command=clickBut5, height=3, width=6)
    Btn6 = Button(mainWin, text="6", command=clickBut6, height=3, width=6)
    Btn7 = Button(mainWin, text="7", command=clickBut7, height=3, width=6)
    Btn8 = Button(mainWin, text="8", command=clickBut8, height=3, width=6)
    Btn9 = Button(mainWin, text="9", command=clickBut9, height=3, width=6)
    Btn0 = Button(mainWin, text="0", command=clickBut0, height=3, width=14)
    BtnBack = Button(mainWin, text="°ˆ", command=clickButBack, height=3, width=6)



    answers = Text(width=21, height=8)
    answers.grid(row=5, column=4, rowspan=4, padx=10, pady=2)
    label.grid(row=0, column=0, columnspan=3)
    resultLabel.grid(row=0, column=4)
    guessBtn.grid(row=3, column=4)
    newGameBtn.grid(row=4, column=4)
    reenterBtn.place(x=390, y=29)


    Btn1.grid(row=3, column=0)
    Btn2.grid(row=3, column=1)
    Btn3.grid(row=3, column=2, sticky="w")
    Btn4.grid(row=4, column=0)
    Btn5.grid(row=4, column=1)
    Btn6.grid(row=4, column=2, sticky="w")
    Btn7.grid(row=5, column=0)
    Btn8.grid(row=5, column=1)
    Btn9.grid(row=5, column=2, sticky="w")
    Btn0.grid(row=6, column=0, columnspan=2,sticky="n")
    BtnBack.grid(row=6, column=2, sticky="w")



def show_frame(cont):
    frame = container.frames[cont]
    frame.tkraise()

root = Tk()
container = Frame(root)
container.frames = dict()
container.frames[StartWin] = StartWin(container)
container.frames[MainWin] = MainWin(container)
show_frame(StartWin)
# MainWin.newGame()
root.mainloop()
