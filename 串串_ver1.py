from tkinter import *
from AnimatedGif import *
from tkinter import messagebox
from PIL import Image, ImageTk
from time import sleep
import pygame
import random
from random import randint

answer = ""
playerGuess = ""
nOfDigits = 4
count = 10
call_count = int()
game1_pass = False
game2_pass = False
game3_pass = False


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

        for F in (StartPage, Intro1, Intro2, Intro3, MainWin1, MainWin2, MainWin3, EndPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

        self.show_frame(StartPage)

    def show_frame(self, cont):
        global call_count
        global game1_pass
        global game2_pass
        global game3_pass

        call_count += 1
        print(call_count)
        frame = self.frames[cont]

        # 檢查是不是回到門然後看要不要換成開門
        if (call_count - 1) % 3 == 0 and call_count > 3:
            if game1_pass is True:
                StartPage.change_door_state(frame, 1)
            if game2_pass is True:
                StartPage.change_door_state(frame, 2)
            if game3_pass is True:
                StartPage.change_door_state(frame, 3)

        frame.tkraise()

class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        global game1_pass
        global game2_pass
        global game3_pass
        if game1_pass is True and game2_pass is True and game3_pass is True:
            controller.show_frame(EndPage)

        # Load the initial Locked doors
        self.image1 = Image.open('door1_locked.png')
        self.image1 = self.image1.resize((190, 400), Image.ANTIALIAS)
        self.image2 = Image.open('door2_locked.png')
        self.image2 = self.image2.resize((160, 380), Image.ANTIALIAS)
        self.image3 = Image.open('door3_locked.png')
        self.image3 = self.image3.resize((190, 400), Image.ANTIALIAS)

        # Load the initial unlocked doors
        self.image1_unlock = Image.open('door1_unlock.png')
        self.image1_unlock = self.image1_unlock.resize((190, 400), Image.ANTIALIAS)
        self.image2_unlock = Image.open('door2_unlock.png')
        self.image2_unlock = self.image2_unlock.resize((168, 380), Image.ANTIALIAS)
        self.image3_unlock = Image.open('door3_unlock.png')
        self.image3_unlock = self.image3_unlock.resize((190, 400), Image.ANTIALIAS)

        self.bg1_load = ImageTk.PhotoImage(self.image1)  # Add self or image will be garbage collected
        self.bg2_load = ImageTk.PhotoImage(self.image2)
        self.bg3_load = ImageTk.PhotoImage(self.image3)
        self.bg1_unlock_load = ImageTk.PhotoImage(self.image1_unlock)
        self.bg2_unlock_load = ImageTk.PhotoImage(self.image2_unlock)
        self.bg3_unlock_load = ImageTk.PhotoImage(self.image3_unlock)

        self.bg1 = Button(self, width=170, height=400, image=self.bg1_load, command=lambda: controller.show_frame(Intro1))
        self.bg2 = Button(self, width=170, height=390, image=self.bg2_load, command=lambda: controller.show_frame(Intro2))
        self.bg3 = Button(self, width=170, height=400, image=self.bg3_load, command=lambda: controller.show_frame(Intro3))
        self.bg1.pack(side=LEFT)
        self.bg2.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.bg3.pack(side=RIGHT)

    def change_door_state(self, which):
        if which == 1:
            self.bg1.config(image=self.bg1_unlock_load)
        elif which == 2:
            self.bg2.config(image=self.bg2_unlock_load)
        elif which == 3:
            self.bg3.config(image=self.bg3_unlock_load)

class Intro1(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        self.createWidgets()

    def createWidgets(self):

        label1 = Label(self, text="歡迎來到猜大小遊戲", font=('微軟正黑體', 30))
        label2 = Label(self, text="規則說明:", font=('微軟正黑體', 24))
        label3 = Label(self, text="總共有1-100數字，", font=('微軟正黑體', 18))
        label4 = Label(self, text="51以上是大，50以下是小，", font=('微軟正黑體', 18))
        label5 = Label(self, text="在五次機會中猜中三次即算成功", font=('微軟正黑體', 18))
        btn1 = Button(self, text="遊戲開始", height=1, width=8, command=lambda: self.controller.show_frame(MainWin1), font=('微軟正黑體', 24))

        label1.grid(row=1, column=3, columnspan=6)
        label2.grid(row=2, column=3, columnspan=6)
        label3.grid(row=3, column=3, columnspan=6)
        label4.grid(row=4, column=3, columnspan=6)
        label5.grid(row=5, column=3, columnspan=6)
        btn1.grid(row=9, column=3, columnspan=6)

class MainWin1(Frame):

    times = 5
    scores = 0

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # Background
        imageHeart = Image.open("heartx.png")
        imageHeart = imageHeart.resize((90, 45), Image.ANTIALIAS)
        self.imageHeart = ImageTk.PhotoImage(imageHeart)
        self.lbTimes = Label(self, image=self.imageHeart)
        self.lbTimes.grid(row=0, column=6, columnspan=2)

        imageDiamond = Image.open("diamond.png")
        imageDiamond = imageDiamond.resize((90, 50), Image.ANTIALIAS)
        self.imageDiamond = ImageTk.PhotoImage(imageDiamond)
        self.lbScores = Label(self, image=self.imageDiamond)
        self.lbScores.grid(row=1, column=6, columnspan=2)

        self.createWidgets()

    def createWidgets(self):

        global times_str
        global scores_str
        global num_str
        global result_str

        times_str = StringVar()
        scores_str = StringVar()
        num_str = StringVar()
        result_str = StringVar()
        times_str.set(self.times)
        scores_str.set(self.scores)

        lbDisplayTimes = Label(self, height=1, width=2, textvariable=times_str, font=('微軟正黑體', 32))
        lbDisplayScores = Label(self, height=1, width=2, textvariable=scores_str, font=('微軟正黑體', 32))
        lbNum = Label(self, height=1, width=12, textvariable=num_str, font=('微軟正黑體', 32))
        lbResult = Label(self, height=1, width=12, textvariable=result_str, font=('微軟正黑體', 18))
        btnBig = Button(self, text="大", height=1, width=5, command=self.clickBtnBig, font=('微軟正黑體', 24))
        btnSmall = Button(self, text="小", height=1, width=5, command=self.clickBtnSmall, font=('微軟正黑體', 24))

        lbDisplayTimes.grid(row=0, column=8, columnspan=2)
        lbDisplayScores.grid(row=1, column=8, columnspan=2)
        lbNum.grid(row=2, column=1, columnspan=7)
        lbResult.grid(row=3, column=1, columnspan=7)
        btnBig.grid(row=4, column=0, columnspan=6)
        btnSmall.grid(row=4, column=5, columnspan=6)

    def generate_num(self):
        point = random.randrange(1, 100)
        print(point)
        return point

    def clickBtnBig(self):
        self.times -= 1
        times_str.set(self.times)
        result = self.generate_num()
        num_str.set(result)
        isBig = 51 <= result <= 100
        if self.times == 0:
            if self.scores >= 3:
                end = messagebox.showinfo("遊戲結束", "猜對%d次，闖關成功" % self.scores)
                if end == "ok":
                    global game1_pass
                    game1_pass = True
                    sleep(1)
                    self.controller.show_frame(StartPage)
            else:
                end = messagebox.showinfo("遊戲結束", "猜對%d次，闖關失敗" % self.scores)
                if end == "ok":
                    sleep(1)
                    self.controller.show_frame(StartPage)

        if isBig:
            self.scores += 1
            scores_str.set(self.scores)
            result_str.set('恭喜，你猜對了')
        else:
            result_str.set('很遺憾，你猜錯了')

    def clickBtnSmall(self):
        self.times -= 1
        times_str.set(self.times)
        result = self.generate_num()
        num_str.set(result)
        isSmall = 1 <= result <= 50
        if self.times == 0:
            if self.scores >= 3:
                end = messagebox.showinfo("遊戲結束", "猜對%d次，闖關成功" % self.scores)
                if end == "ok":
                    global game1_pass
                    game1_pass = True
                    sleep(1)
                    self.controller.show_frame(StartPage)
            else:
                end = messagebox.showinfo("遊戲結束", "猜對%d次，闖關失敗" % self.scores)
                print(end)
                if end == "ok":
                    sleep(1)
                    self.controller.show_frame(StartPage)

        if isSmall:
            self.scores += 1
            scores_str.set(self.scores)
            result_str.set('恭喜，你猜對了')
        else:
            result_str.set('很遺憾，你猜錯了')

class Intro2(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        self.createWidgets()

    def createWidgets(self):
        init_text = u'有' + str(5) + u'次機會,猜一個數字, 數字介於' + str(1) + u'至' + str(
            100) + u'之間\n若猜錯, 會給予提示\n' + \
                    '請輸入一個介於 ' + str(1) + '-' + str(100) + ' 之間的整數\n'
        lb = Label(self, height=4, width=50, text=init_text)
        lb.place(relx=0.5, rely=0.4, anchor=CENTER)
        btn1 = Button(self, text="遊戲開始", height=1, width=8, command=lambda: self.controller.show_frame(MainWin2),
                      font=('微軟正黑體', 24))
        btn1.place(relx=0.5, rely=0.6, anchor=CENTER)

class MainWin2(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        self.lower_bound = 1
        self.upper_bound = 100
        self.guess_count_limit = 5
        self.guess_count = 0
        self.answer = randint(self.lower_bound, self.upper_bound)
        print('self.answer:', self.answer)

        self.bg_pic = AnimatedGif(self, 'green.gif', 0.04)
        self.bg_pic.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_pic.start()

        # Build Object/建立物件

        self.txt = Text(self, height=1, width=10)
        self.txt.bind('<Return>', self.click_enter_keyboard)
        self.btn = Button(self, height=2, width=15, text="Enter", command=self.click_enter_btn)

        # Assign Position/指定位置
        # self.lb.grid(row=0, column=0)
        # self.txt.grid(row=2, column=0)
        # self.btn.grid(row=5, column=0, sticky=NSEW)

        self.txt.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.btn.place(relx=0.5, rely=0.6, anchor=CENTER)

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
        target_object.delete("1.0", "end")  # 尚無法清掉Ent

    # 更新Label的文字
    def update_label_text(self, target_object, text):
        target_object.configure(text=text)

    # 滑鼠按下Enter按鈕後會觸發的事件
    def click_enter_btn(self):
        print('click_enter_btn')

        # 讀取文字輸入框的文字
        inp = self.txt.get("1.0", 'end-1c')
        # 去除空白 換行 字元
        inp = inp.strip()

        self.clear_text_text(self.txt)

        try:
            guess_number = int(inp)
        except ValueError:
            text = u'格式錯誤，請輸入數字'
            self.update_label_text(self.lb, text)
            return None

        self.guess_count += 1

        print('guess_number:', guess_number)
        print('self.lower_bound:', self.lower_bound)
        print('self.upper_bound:', self.upper_bound)

        if guess_number < self.lower_bound or guess_number > self.upper_bound:
            text = u'避免浪費您的機會, 請輸入 ' + str(self.lower_bound) + '-' + str(self.upper_bound) + u'之間的整數\n'
            print(text)
            self.update_label_text(self.lb, text)
            return None

        if guess_number == self.answer:
            global game2_pass
            text = u'恭喜猜對！門已解鎖'
            # self.update_label_text(self.lb, text)
            game2_pass = True
            self.controller.show_frame(StartPage)
            # return None
        elif guess_number < self.answer:
            self.lower_bound = guess_number + 1

            if self.guess_count < self.guess_count_limit:
                text = u'答案不是' + str(guess_number) + u', 請再接再厲, 還剩下' + str(self.guess_count_limit-self.guess_count) +  u'次機會\n' + u'答案介於 ' + str(self.lower_bound) + '-' + str(self.upper_bound) + u'之間'
            else:
                text = u'沒有猜對, 機會已用完, 遊戲結束, 您的回答為:' + str(guess_number) + u' 正確答案為:' + str(self.answer)
                self.controller.show_frame(StartPage)
            self.update_label_text(self.lb, text)
        else:
            self.upper_bound = guess_number - 1

            if self.guess_count < self.guess_count_limit:
                text = u'答案不是' + str(guess_number) + u', 請再接再厲, 還剩下' + str(self.guess_count_limit - self.guess_count) + u'次機會\n'  + u'答案介於 ' + str(self.lower_bound) + '-' + str(self.upper_bound) + u'之間'
            else:
                text = u'沒有猜對, 機會已用完, 遊戲結束, 您的回答為:' + str(guess_number) + u' 正確答案為:' + str(self.answer)
                # self.update_label_text(self.lb, text)
                self.controller.show_frame(StartPage)  # 結束遊戲後回主頁面

        # 因為label移到Intro了所以我暫時comment掉喔
        # self.update_label_text(self.lb, text)

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

class Intro3(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.controller = controller
        self.createWidgets()

    def createWidgets(self):

        label1 = Label(self, text="歡迎來到猜大小遊戲", font=('微軟正黑體', 30))
        label2 = Label(self, text="規則說明:", font=('微軟正黑體', 24))
        label3 = Label(self, text="總共有1-100數字，", font=('微軟正黑體', 18))
        label4 = Label(self, text="51以上是大，50以下是小，", font=('微軟正黑體', 18))
        label5 = Label(self, text="在五次機會中猜中三次即算成功", font=('微軟正黑體', 18))
        btn1 = Button(self, text="遊戲開始", height=1, width=8, command=lambda: self.controller.show_frame(MainWin3), font=('微軟正黑體', 24))

        label1.pack()
        label2.pack()
        label3.pack()
        label4.pack()
        label5.pack()
        btn1.pack()

class MainWin3(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
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
                global game3_pass
                result = "You Win"
                game3_pass = True
                # sleep(1)
                self.controller.show_frame(StartPage)
            else:
                result = str(a) + "A" + str(b) + "B"

            resultLabel.config(text=result)

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

class EndPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        image = Image.open('all_unlock.png')
        self.bg_load = ImageTk.PhotoImage(image)  # Add self or image will be garbage collected
        bg_label = Label(self, image=self.bg_load)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

app = NumberGame()
app.mainloop()
