from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import Image, ImageTk
from time import sleep
import random
from random import randint

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

class numbergame(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        container = Frame(self)

        container.grid()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, bullsandcows, CompareGame,UltimatePasswordGameWindow):
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

        image = Image.open('2b.jpg')
        self.bg_load = ImageTk.PhotoImage(image)  # Add self or image will be garbage collected
        bg_label = Label(self, image=self.bg_load)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        but_go = Button(bg_label, height=4, width=8, text='Come on!', command=lambda: controller.show_frame(bullsandcows))
        but_go.pack(side=BOTTOM)

class bullsandcows(Frame):
    def __init__(self, parent,controller):

        Frame.__init__(self, parent)
        self.grid()

        def nDigitNumber(n):
            numbers = random.sample(range(10), n)
            randNum = ''.join(map(str, numbers))
            return randNum

        def newGame():
            print("newGame")
            global nOfDigits
            global answer
            global count
            label.config(text='')
            resultLabel.config(text="")
            answers.delete(1.0, END)
            answer = nDigitNumber(nOfDigits)
            print(answer)
            count = 10
            chancelabel.config(text=str(count) + " chances left")


        def checkUserGuess():
            global playerGuess
            global answer
            global nOfDigits
            global count
            playerGuess = label.cget("text")

            if len(playerGuess) == nOfDigits:
                count = count - 1
                a = calA(playerGuess)
                b = calB(playerGuess)
                showResult(a, b)
                label.config(text="")
                answers.insert(INSERT, playerGuess + "   " + str(a) + "A" + str(b) + "B" + "\n")
                chancelabel.config(text=str(count)+" chances left")

            else:
                messagebox.showinfo("提醒", "位數要為" + str(nOfDigits))
                label.config(text="")

            if count == 0:
                chancelabel.config(text="Try Again!")
                count = 10
                newGame()


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
                nextLevelBtn.grid(row=0, column=4, sticky="e")
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

        def nextLevel():
            str = label.cget("Next Level")
            label.configure(text=str[0:-1])



        resultLabel = Label(self, text="0A0B", font=('arial', 20))
        var = StringVar(self)

        guessBtn = Button(self, text="Guess", command=checkUserGuess, height=3, width=20)
        newGameBtn = Button(self, text="New Game", command=newGame, height=3, width=20)
        nextLevelBtn = Button(self, text="Next Level", command=combine_funcs(lambda: controller.show_frame(CompareGame),newGame), height=3, width=20)

        chancelabel = Label(self, height=1, borderwidth=5, text="10 chances left", font=('arial', 12))
        label = Label(self, height=1, borderwidth=5, text="", font=('arial', 20))
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

        Btn1.grid(row=3, column=0)
        Btn2.grid(row=3, column=1)
        Btn3.grid(row=3, column=2, sticky="w")
        Btn4.grid(row=4, column=0)
        Btn5.grid(row=4, column=1)
        Btn6.grid(row=4, column=2, sticky="w")
        Btn7.grid(row=5, column=0)
        Btn8.grid(row=5, column=1)
        Btn9.grid(row=5, column=2, sticky="w")
        Btn0.grid(row=6, column=0, columnspan=2, sticky="w")
        BtnBack.grid(row=6, column=2, sticky="e")


        answers = Text(self, width=20, height=8, bg='black', foreground='yellow')
        answers.grid(row=5, column=4, rowspan=4, pady=2)

        label.grid(row=1, column=0, columnspan=3, sticky=W)
        chancelabel.grid(row=0, column=0, columnspan=3, sticky=W)
        resultLabel.grid(row=1, column=4)
        guessBtn.grid(row=3, column=4)
        newGameBtn.grid(row=4, column=4)



        newGame()

class CompareGame(Frame):
    times = 5
    scores = 0
    def new_game(self):
        global times_str
        global scores_str
        global num_str
        global result_str
        global times
        global scores

        self.times = 5
        self.scores = 0
        times_str.set(self.times)
        scores_str.set(self.scores)
        result_str.set("")
        num_str.set("")

    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.grid()
        self.createWidgets(parent,controller)


    def new_game(self):
        global times_str
        global scores_str
        global num_str
        global result_str
        global times
        global scores

        self.times = 5
        self.scores = 0
        times_str.set(self.times)
        scores_str.set(self.scores)
        result_str.set("")
        num_str.set("")



    def createWidgets(self,parent,controller):
        f1 = tkFont.Font(size=32, family="微軟正黑體")
        f2 = tkFont.Font(size=24, family="微軟正黑體")
        f3 = tkFont.Font(size=18, family="微軟正黑體")

        global times_str
        global scores_str
        global num_str
        global result_str
        global times
        global scores

        times_str = StringVar()
        scores_str = StringVar()
        num_str = StringVar()
        result_str = StringVar()
        times_str.set(self.times)
        scores_str.set(self.scores)

        imageHeart = Image.open("heartx.png")
        imageHeart = imageHeart.resize((90, 45), Image.ANTIALIAS)
        self.imageHeart = ImageTk.PhotoImage(imageHeart)
        self.lbTimes = Label(self, image=self.imageHeart)

        imageDiamond = Image.open("diamond.png")
        imageDiamond = imageDiamond.resize((90, 50), Image.ANTIALIAS)
        self.imageDiamond = ImageTk.PhotoImage(imageDiamond)
        self.lbScores = Label(self, image=self.imageDiamond)

        self.lbDisplayTimes = Label(self, height=1, width=2, textvariable=times_str, font=f1)
        self.lbDisplayScores = Label(self, height=1, width=2, textvariable=scores_str, font=f1)
        self.lbNum = Label(self, height=1, width=12, textvariable=num_str, font=f1)
        self.lbResult = Label(self, height=1, width=12, textvariable=result_str, font=f3)
        self.btnBig = Button(self, text="大", height=1, width=5, command=self.clickBtnBig, font=f2)
        self.btnSmall = Button(self, text="小", height=1, width=5, command=self.clickBtnSmall, font=f2)
        self.btnAgain = Button(self, text="Start Again", height=1, width=10, command=self.new_game,
                              font=f3)
        self.btnNext = Button(self, text="Next Level", height=1, width=10, command= combine_funcs(lambda: controller.show_frame(UltimatePasswordGameWindow),self.new_game), font=f3)

        self.lbTimes.grid(row=0, column=7, columnspan=3)
        self.lbScores.grid(row=1, column=7, columnspan=3)
        self.lbDisplayTimes.grid(row=0, column=10, columnspan=2)
        self.lbDisplayScores.grid(row=1, column=10, columnspan=2)
        self.lbNum.grid(row=2, column=0, columnspan=12)
        self.lbResult.grid(row=3, column=0, columnspan=12, sticky=NE + SW)
        self.btnBig.grid(row=4, column=0, columnspan=6)
        self.btnSmall.grid(row=4, column=6, columnspan=6)
        self.btnAgain.grid(row=5, column=3, columnspan=6)


    def num(self):
        point = random.randrange(1, 100)
        return point


    def clickBtnBig(self):
        global times_str
        global scores_str
        global num_str
        global result_str
        global times
        global scores
        self.times -= 1
        times_str.set(self.times)
        result = self.num()
        num_str.set(result)
        isBig = 51 <= result <= 100
        if self.times == 0:
            if self.scores >= 3:
                quit = messagebox.showinfo("遊戲結束", "猜對%d次，闖關成功" % self.scores)
                self.btnNext.grid(row=6, column=3, columnspan=6)

            else:
                quit = messagebox.showinfo("遊戲結束", "猜對%d次，闖關失敗" % self.scores)
                self.new_game()
        if isBig:
            self.scores += 1
            scores_str.set(self.scores)
            result_str.set('恭喜，你猜對了')
        else:
            result_str.set('很遺憾，你猜錯了')


    def clickBtnSmall(self):
        global times_str
        global scores_str
        global num_str
        global result_str
        global times
        global scores
        self.times -= 1
        times_str.set(self.times)
        result = self.num()
        num_str.set(result)
        isSmall = 1 <= result <= 50
        if self.times == 0:
            if self.scores >= 3:
                quit = messagebox.showinfo("遊戲結束", "猜對%d次，闖關成功" % self.scores)
                self.btnNext.grid(row=6, column=3, columnspan=6)

            else:
                quit = messagebox.showinfo("遊戲結束", "猜對%d次，闖關失敗" % self.scores)
                print(quit)
                self.new_game()

        if isSmall:
            self.scores += 1
            scores_str.set(self.scores)
            result_str.set('恭喜，你猜對了')
        else:
            result_str.set('很遺憾，你猜錯了')

class UltimatePasswordGameWindow(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.grid()

        lower_bound = 1
        upper_bound = 100
        guess_count_limit = 5

        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.guess_count_limit = guess_count_limit
        self.guess_count = 0
        self.grid()

        self.answer = randint(lower_bound, upper_bound)
        print('self.answer:', self.answer)
        #Build Object/建立物件
        init_text = u'有' + str(guess_count_limit) + u'次機會,猜一個數字, 數字介於' + str(lower_bound) + u'至' + str(upper_bound) + u'之間\n若猜錯, 會給予提示\n'  + \
                    '請輸入一個介於 ' + str(lower_bound) + '-' + str(upper_bound) + ' 之間的整數\n'

        self.lb = Label(self, height=4, width=50, text=init_text)
        #self.lb.pack()
        self.txt = Text(self, height=1, width=10)
        self.txt.bind('<Return>', self.click_enter_keyboard)
        self.btn = Button(self, height=2, width=15, text="Enter", command=self.click_enter_btn)
        self.playagain = Button(self, height=2, width=15, text="Play Again", command=lambda: controller.show_frame(StartPage))

        #Assign Position/指定位置
        self.lb.grid(row=0, column=0)
        self.txt.grid(row=2, column=0)
        self.btn.grid(row=5, column=0)


        # 尚未試成功的code
        # self.bind('<Return>', self.click_enter_keyboard)
        # self.focus_set()


    # 在文字輸入框 , 鍵盤按下Enter按鈕後會觸發的事件
    def click_enter_keyboard(self, event):
        print("click_enter_keyboard")
        self.click_enter_btn()

    # 更新Text的文字
    def update_text_text(self, target_object, text):
        target_object.delete("1.0", "end")
        target_object.insert("1.0", text)

    # 清除Text的文字
    def clear_text_text(self, target_object):
        target_object.delete("1.0", "end") # 尚無法清掉Ent

    # 更新Label的文字
    def update_label_text(self, target_object, text):
        target_object.configure(text = text)
        #target_object.pack()

    # 滑鼠按下Enter按鈕後會觸發的事件
    def click_enter_btn(self):
        print('click_enter_btn')

        # 讀取文字輸入框的文字
        input = self.txt.get("1.0",'end-1c')
        # 去除空白 換行 字元
        input = input.strip()

        self.clear_text_text(self.txt)

        try:
            guess_number = int(input)
        except ValueError:
            text = u'格式錯誤，請輸入數字'
            self.update_label_text(self.lb, text)
            return None

        self.guess_count += 1

        print('guess_number:',guess_number)
        print('self.lower_bound:', self.lower_bound)
        print('self.upper_bound:', self.upper_bound)

        if guess_number < self.lower_bound or guess_number > self.upper_bound:
            text = u'避免浪費您的機會, 請輸入 ' + str(self.lower_bound) + '-' + str(self.upper_bound) + u'之間的整數\n'
            print(text)
            self.update_label_text(self.lb, text)
            return None

        if guess_number == self.answer:
            text = u'恭喜猜對！門已解鎖'
            self.update_label_text(self.lb, text)
            self.playagain.grid(row=6, column=0)
            return None
        elif guess_number < self.answer:
            self.lower_bound = guess_number + 1

            if self.guess_count < self.guess_count_limit:
                text = u'答案不是' + str(guess_number) + u', 請再接再厲, 還剩下' + str(self.guess_count_limit-self.guess_count) +  u'次機會\n' + u'答案介於 ' + str(self.lower_bound) + '-' + str(self.upper_bound) + u'之間'
            else:
                text = u'沒有猜對, 機會已用完, 遊戲結束, 您的回答為:' + str(guess_number) + u' 正確答案為:' + str(self.answer)
                self.end_game()
            self.update_label_text(self.lb, text)
        else:
            self.upper_bound = guess_number - 1

            if self.guess_count < self.guess_count_limit:
                text = u'答案不是' + str(guess_number) + u', 請再接再厲, 還剩下' + str(self.guess_count_limit - self.guess_count) + u'次機會\n'  + u'答案介於 ' + str(self.lower_bound) + '-' + str(self.upper_bound) + u'之間'
            else:
                text = u'沒有猜對, 機會已用完, 遊戲結束, 您的回答為:' + str(guess_number) + u' 正確答案為:' + str(self.answer)
                self.end_game()
        self.update_label_text(self.lb, text)

    # 將按鈕的事件更換
    def end_game(self):
        print('end_game')
        self.txt.grid_remove()
        self.btn['command'] = self.end_frame

    # 清除與關掉此Frame
    def end_frame(self):
        print('end_frame')
        self.destroy()
        self.quit()

answer = ""
playerGuess = ""
nOfDigits = 4
count = 10

app = numbergame()
app.mainloop()