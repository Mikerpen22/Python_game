from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from time import sleep
import pygame
import random

answer = ""
playerGuess = ""
nOfDigits = 4
count = 10

# 我無聊亂放音樂
pygame.init()
pygame.mixer.music.load('Fantasy_Game_Background_Looping.mp3')  # Loading File Into Mixer
pygame.mixer.music.play()


class NumberGame(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = Frame(self)

        container.grid()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, MainWin3, EndPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        image = Image.open('gate.jpg')
        self.bg_load = ImageTk.PhotoImage(image)  # Add self or image will be garbage collected
        bg1 = Button(self, width=130, height=260, image=self.bg_load)
        bg2 = Button(self, width=130, height=260, image=self.bg_load)
        bg2 = Button(self, width=130, height=260, image=self.bg_load)
        bg3 = Button(self, width=130, height=260, image=self.bg_load, command=lambda: controller.show_frame(MainWin3))
        bg1.pack(side=LEFT)
        bg2.place(relx=0.5, rely=0.5, anchor=CENTER)
        bg3.pack(side=RIGHT)
        # bg3.place(x=0, y=0, relwidth=1, relheight=1)

        # but_go = Button(bg3, height=4, width=8, text='Come on!', command=lambda: controller.show_frame(MainWin3))
        # but_go.pack(side=BOTTOM)


class EndPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        image = Image.open('key.jpg')
        self.bg_load = ImageTk.PhotoImage(image)  # Add self or image will be garbage collected
        bg_label = Label(self, image=self.bg_load)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        but_go = Button(bg_label, height=4, width=8, text='Come on!', command=lambda: controller.show_frame(MainWin3))
        but_go.pack(side=BOTTOM)


class MainWin3(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.grid()
        self.setup_widgets()
        self.controller = controller

    def setup_widgets(self):

        def n_digit_num(n):
            numbers = random.sample(range(10), n)
            rand = ''.join(map(str, numbers))
            return rand

        def new_game():
            print("new_game")
            global nOfDigits
            global answer
            label.config(text='')
            resultLabel.config(text="")
            answers.delete(1.0, END)
            answer = n_digit_num(nOfDigits)
            print(answer)

        def check_guess():
            global playerGuess
            global answer
            global nOfDigits
            global count
            playerGuess = label.cget("text")

            if len(playerGuess) == nOfDigits:
                count = count - 1
                a = cal_a(playerGuess)
                b = cal_b(playerGuess)
                show_result(a, b)
                label.config(text="")
                answers.insert(INSERT, playerGuess + "   " + str(a) + "A" + str(b) + "B" + "\n")
                chanceLabel.config(text=str(count)+" chances left")

            else:
                messagebox.showinfo("提醒", "位數要為" + str(nOfDigits))
                label.config(text="")

            if count == 0:
                chanceLabel.config(text="Try Again!")
                count = 10

        def cal_a(guess):
            global answer
            a = 0
            for i in range(len(answer)):
                if guess[i] == answer[i]:
                    a = a + 1

            return a

        def cal_b(guess):
            global answer
            b = 0
            k = len(answer)
            for i in range(k):
                for j in range(k):
                    if i != j:
                        if guess[i] == answer[j]:
                            b = b + 1
            return b

        def show_result(a, b):
            if a == nOfDigits:
                result = "You Win"
            else:
                result = str(a) + "A" + str(b) + "B"

            resultLabel.config(text=result)
            sleep(1)
            self.controller.show_frame(EndPage)

        def click_but1():
            label.configure(text=label.cget("text") + "1")

        def click_but2():
            label.configure(text=label.cget("text") + "2")

        def click_but3():
            label.configure(text=label.cget("text") + "3")

        def click_but4():
            label.configure(text=label.cget("text") + "4")

        def click_but5():
            label.configure(text=label.cget("text") + "5")

        def click_but6():
            label.configure(text=label.cget("text") + "6")

        def click_but7():
            label.configure(text=label.cget("text") + "7")

        def click_but8():
            label.configure(text=label.cget("text") + "8")

        def click_but9():
            label.configure(text=label.cget("text") + "9")

        def click_but0():
            label.configure(text=label.cget("text") + "0")

        def click_butBack():
            s = label.cget("text")
            label.configure(text=s[0:-1])

        resultLabel = Label(self, text="0A0B", font=('arial', 20))
        guessBtn = Button(self, text="Guess", command=check_guess, height=3, width=20)
        new_gameBtn = Button(self, text="New Game", command=new_game, height=3, width=20)
        chanceLabel = Label(self, height=1, borderwidth=5, text="10 chances left", font=('arial', 12))

        label = Label(self, height=1, borderwidth=5, text="", font=('arial', 20))
        btn_1 = Button(self, text="1", command=click_but1, height=3, width=6)
        btn_2 = Button(self, text="2", command=click_but2, height=3, width=6)
        btn_3 = Button(self, text="3", command=click_but3, height=3, width=6)
        btn_4 = Button(self, text="4", command=click_but4, height=3, width=6)
        btn_5 = Button(self, text="5", command=click_but5, height=3, width=6)
        btn_6 = Button(self, text="6", command=click_but6, height=3, width=6)
        btn_7 = Button(self, text="7", command=click_but7, height=3, width=6)
        btn_8 = Button(self, text="8", command=click_but8, height=3, width=6)
        btn_9 = Button(self, text="9", command=click_but9, height=3, width=6)
        btn_0 = Button(self, text="0", command=click_but0, height=4, width=14)
        btn_back = Button(self, text="←", command=click_butBack, height=4, width=6)

        btn_1.grid(row=3, column=0)
        btn_2.grid(row=3, column=1)
        btn_3.grid(row=3, column=2, sticky="w")
        btn_4.grid(row=4, column=0)
        btn_5.grid(row=4, column=1)
        btn_6.grid(row=4, column=2, sticky="w")
        btn_7.grid(row=5, column=0)
        btn_8.grid(row=5, column=1)
        btn_9.grid(row=5, column=2, sticky="w")
        btn_0.grid(row=6, column=0, columnspan=2, sticky="w")
        btn_back.grid(row=6, column=2, sticky="e")

        answers = Text(self, width=20, height=8, bg='black', foreground='yellow')
        answers.grid(row=5, column=4, rowspan=4, pady=2)

        label.grid(row=1, column=0, columnspan=3, sticky=W)
        chanceLabel.grid(row=0, column=0, columnspan=3, sticky=W)
        resultLabel.grid(row=1, column=4)
        guessBtn.grid(row=3, column=4)
        new_gameBtn.grid(row=4, column=4)

        new_game()


app = NumberGame()
app.mainloop()