from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from time import sleep
import random

answer = ""
playerGuess = ""
nOfDigits = 4

class numbergame(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        container = Frame(self)

        container.grid()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, mainWin):
            frame = F(container , self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=NSEW)
        self.show_frame(StartPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()



class StartPage(Frame):
    def __init__(self, parent,controller):
        Frame.__init__(self, parent)

        image = Image.open('C:\\Users\\carl_dis2003\\Desktop\\大學\\大三上\\python\\2b.jpg')
        self.bg_load = ImageTk.PhotoImage(image)  # Add self or image will be garbage collected
        bg_label = Label(self, image=self.bg_load)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        but_go = Button(bg_label, height=4, width=8, text='Come on!', command=lambda: controller.show_frame(mainWin))
        but_go.pack(side=BOTTOM)

class mainWin(Frame):

    def __init__(self, parent,controller):
        Frame.__init__(self, parent)
        self.grid()

        load_1 = Image.open('C:\\Users\\carl_dis2003\\Desktop\\大學\\大三上\\python\\reenter.png')
        self.reenter_img = ImageTk.PhotoImage(load_1)

        self.setUpWidgets()

    def setUpWidgets(self):

        def nDigitNumber(n):
            numbers = random.sample(range(10), n)
            randNum = ''.join(map(str, numbers))
            return randNum

        def newGame():
            print("newGame")
            global nOfDigits
            global answer
            label.config(text='')
            resultLabel.config(text="")
            answers.delete(1.0, END)
            answer = nDigitNumber(nOfDigits)
            print(answer)

        def reenter():
            label.config(text="")

        def checkUserGuess():
            global playerGuess
            global answer
            global nOfDigits
            playerGuess = label.cget("text")
            if len(playerGuess) == nOfDigits:
                a = calA(playerGuess)
                b = calB(playerGuess)
                showResult(a, b)
                label.config(text="")
                answers.insert(INSERT, playerGuess + "   " + str(a) + "A" + str(b) + "B" + "\n")
            else:
                messagebox.showinfo("提醒", "位數要為" + str(nOfDigits))
                label.config(text="")

        def calA(guess):
            global answer
            a = 0
            for i in range(len(answer)):
                if guess[i] == answer[i]:
                    a = a + 1

            return a

        def calB(guess):
            global answer
            b = 0
            k = len(answer)
            for i in range(k):
                for j in range(k):
                    if i != j:
                        if guess[i] == answer[j]:
                            b = b + 1
            return b

        def showResult(a, b):
            if a == nOfDigits:
                result = "You Win"
            else:
                result = str(a) + "A" + str(b) + "B"

            resultLabel.config(text=result)

        def clickBut1():
            label.configure(text=label.cget("text") + "1")

        def clickBut2():
            label.configure(text=label.cget("text") + "2")

        def clickBut3():
            label.configure(text=label.cget("text") + "3")

        def clickBut4():
            label.configure(text=label.cget("text") + "4")

        def clickBut5():
            label.configure(text=label.cget("text") + "5")

        def clickBut6():
            label.configure(text=label.cget("text") + "6")

        def clickBut7():
            label.configure(text=label.cget("text") + "7")

        def clickBut8():
            label.configure(text=label.cget("text") + "8")

        def clickBut9():
            label.configure(text=label.cget("text") + "9")

        def clickBut0():
            label.configure(text=label.cget("text") + "0")

        def clickButBack():
            str = label.cget("text")
            label.configure(text=str[0:-1])

        resultLabel = Label(self, text="0A0B", font=('arial', 20))
        var = StringVar(self)

        guessBtn = Button(self, text="Guess", command=checkUserGuess, height=3, width=20)
        newGameBtn = Button(self, text="New Game", command=newGame, height=3, width=20)
        reenterBtn = Button(self, image=self.reenter_img, command=reenter, height=30, width=35)

        label = Label(self, height=4, borderwidth=5, text="", font=('arial', 20))
        Btn1 = Button(self, text="1", command=clickBut1, height=3, width=6)
        Btn2 = Button(self, text="2", command=clickBut2, height=3, width=6)
        Btn3 = Button(self, text="3", command=clickBut3, height=3, width=6)
        Btn4 = Button(self, text="4", command=clickBut4, height=3, width=6)
        Btn5 = Button(self, text="5", command=clickBut5, height=3, width=6)
        Btn6 = Button(self, text="6", command=clickBut6, height=3, width=6)
        Btn7 = Button(self, text="7", command=clickBut7, height=3, width=6)
        Btn8 = Button(self, text="8", command=clickBut8, height=3, width=6)
        Btn9 = Button(self, text="9", command=clickBut9, height=3, width=6)
        Btn0 = Button(self, text="0", command=clickBut0, height=4, width=14)
        BtnBack = Button(self, text="←", command=clickButBack, height=4, width=6)

        Btn1.grid(row=2, column=0)
        Btn2.grid(row=2, column=1)
        Btn3.grid(row=2, column=2, sticky="w")
        Btn4.grid(row=3, column=0)
        Btn5.grid(row=3, column=1)
        Btn6.grid(row=3, column=2, sticky="w")
        Btn7.grid(row=4, column=0)
        Btn8.grid(row=4, column=1)
        Btn9.grid(row=4, column=2, sticky="w")
        Btn0.grid(row=5, column=0, columnspan=2, sticky="w")
        BtnBack.grid(row=5, column=2, sticky="e")

        answers = Text(self, width=20, height=8, bg='black', foreground='yellow')
        answers.grid(row=4, column=4, rowspan=4, pady=2)

        label.grid(row=0, column=0, columnspan=3, sticky=W)
        resultLabel.grid(row=0, column=4)
        guessBtn.grid(row=2, column=4)
        newGameBtn.grid(row=3, column=4)
        reenterBtn.place(x=320, y=20)

        newGame()

app = numbergame()
app.mainloop()