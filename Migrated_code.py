from tkinter import *
from AnimatedGif import *
from tkinter import messagebox
from PIL import Image, ImageTk
from time import sleep
import pygame
import random
from random import randint 

game1_pass = False
game2_pass = False
game3_pass = False

pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)  # frequency, size, channels, buffersize
pygame.mixer.music.load('Fantasy_Game_Background_Looping.mp3')  # Loading File Into Mixer
pygame.mixer.music.play(loops=-1)  # keep playing bgm

door_sound = pygame.mixer.Sound('creaky_door.wav')
victory_sound = pygame.mixer.Sound('victory.wav')


class TreasureHunter(Tk):
    def __init__(self):
        Tk.__init__(self)
        container = Frame(self)
        container.grid()
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.master.title('Treasure Hunter')  # 設置視窗的標題

        # 初始化所有Frame，每個Frame都有被啟動
        # 透過一次秀一個Frame的方式，來做到Frame與Frame的切換
        # 所有的Frame都有被啟動，即使一次只展示一個Frame，但視窗的大小會取決於最大的那個Frame的大小
        self.frames = {}
        for page in (BeginningPage, DoorPage, Game1IntroPage, Game2IntroPage, Game3IntroPage, Game1MainPage, Game2MainPage, Game3MainPage, EndPage):
            frame = page(container, self)
            self.frames[page] = frame
            frame.grid(row=0, column=0, sticky=NSEW)
        #  切換至古墓尋寶之初始頁面
        self.show_frame(BeginningPage)

    def show_frame(self, container):
        global game1_pass
        global game2_pass
        global game3_pass
        print('show_frame:', container)
        frame = self.frames[container]

        if container == DoorPage:
            if game1_pass is True and game2_pass is True and game3_pass is True:  # 如果三個遊戲都已通關
                pygame.mixer.music.stop()
                victory_sound.play()
                self.show_frame(EndPage)
            else:
                if game1_pass is True:
                    frame.change_door_state('left')
                if game2_pass is True:
                    frame.change_door_state('mid')
                if game3_pass is True:
                    frame.change_door_state('right')
                frame.tkraise()
        elif container == Game1MainPage or container == Game2MainPage:
            frame.reset_if_needed()  # 將一些變數初始化，比如：猜的次數
            frame.tkraise()

        elif container == Game1IntroPage or container == Game2IntroPage or container == Game3IntroPage:
            door_sound.play()
            frame.tkraise()

        else:
            frame.tkraise()


# 初始畫面
class BeginningPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, width=600, height=400)
        image = Image.open('beginning_with_description.png')
        image = image.resize((860, 620), Image.ANTIALIAS)
        self.bg_load = ImageTk.PhotoImage(image)
        bg_label = Label(self, image=self.bg_load)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.bg1 = Button(self, width=10, height=1, command=lambda: controller.show_frame(DoorPage), borderwidth=1, text="遊戲開始", font=('微軟正黑體', 16))
        self.bg1.place(relx=0.52, rely=0.6, anchor=CENTER)


# 三扇門畫面
class DoorPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, width=600, height=400)
        global game1_pass
        global game2_pass
        global game3_pass
        self.config(bg='grey9')
        # Load the initial Locked doors

        locked_image_width = 200
        locked_image_height = 430

        unlocked_image_width = locked_image_width
        unlocked_image_height = locked_image_height

        door_button_width = locked_image_width
        door_button_height = locked_image_height

        self.image1 = Image.open('door_left_locked.png')
        self.image1 = self.image1.resize((locked_image_width, locked_image_height), Image.ANTIALIAS)
        self.image2 = Image.open('door_mid_locked.png')
        self.image2 = self.image2.resize((locked_image_width, locked_image_height), Image.ANTIALIAS)
        self.image3 = Image.open('door_right_locked.png')
        self.image3 = self.image3.resize((locked_image_width, locked_image_height), Image.ANTIALIAS)

        # Load the initial unlocked doors
        self.image1_unlock = Image.open('door_left_unlocked.png')
        self.image1_unlock = self.image1_unlock.resize((unlocked_image_width, unlocked_image_height), Image.ANTIALIAS)
        self.image2_unlock = Image.open('door_mid_unlocked.png')
        self.image2_unlock = self.image2_unlock.resize((unlocked_image_width, unlocked_image_height), Image.ANTIALIAS)
        self.image3_unlock = Image.open('door_right_unlocked.png')
        self.image3_unlock = self.image3_unlock.resize((unlocked_image_width, unlocked_image_height), Image.ANTIALIAS)

        self.bg1_load = ImageTk.PhotoImage(self.image1)  # Add self or image will be garbage collected
        self.bg2_load = ImageTk.PhotoImage(self.image2)
        self.bg3_load = ImageTk.PhotoImage(self.image3)
        self.bg1_unlock_load = ImageTk.PhotoImage(self.image1_unlock)
        self.bg2_unlock_load = ImageTk.PhotoImage(self.image2_unlock)
        self.bg3_unlock_load = ImageTk.PhotoImage(self.image3_unlock)

        self.bg1 = Button(self, width=door_button_width, height=door_button_height, image=self.bg1_load, command=lambda: controller.show_frame(Game1IntroPage), borderwidth=0, highlightthickness=0)
        self.bg2 = Button(self, width=door_button_width, height=door_button_height, image=self.bg2_load, command=lambda: controller.show_frame(Game2IntroPage), borderwidth=0, highlightthickness=0)
        self.bg3 = Button(self, width=door_button_width, height=door_button_height, image=self.bg3_load, command=lambda: controller.show_frame(Game3IntroPage), borderwidth=0, highlightthickness=0)
        self.bg2.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.bg1.pack(side=LEFT)
        self.bg3.pack(side=RIGHT)

    def change_door_state(self, door_location):
        if door_location == 'left':
            self.bg1.config(image=self.bg1_unlock_load)
        elif door_location == 'mid':
            self.bg2.config(image=self.bg2_unlock_load)
        elif door_location == 'right':
            self.bg3.config(image=self.bg3_unlock_load)


class Game1IntroPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, width=600, height=600)
        self.controller = controller
        self.createWidgets()

    def createWidgets(self):
        label1 = Label(self, text="歡迎來到猜大小遊戲", font=('微軟正黑體', 30), bg='black', fg='white')
        label2 = Label(self, text="規則說明:", font=('微軟正黑體', 24))
        label3 = Label(self, text="每一回合，系統會產生一個數字(1-100)，", font=('微軟正黑體', 18))
        label4 = Label(self, text="要去猜此數字是大(51以上)，", font=('微軟正黑體', 18))
        label5 = Label(self, text="還是小(50以下)，", font=('微軟正黑體', 18))
        label6 = Label(self, text="在五個回合中猜中三個回合即算成功", font=('微軟正黑體', 18))
        btn1 = Button(self, text="遊戲開始", height=1, width=8, command=lambda: self.controller.show_frame(Game1MainPage), bg='black', foreground='white',
                      font=('微軟正黑體', 24))

        label1.pack(side="top", fill="both", expand=True)
        label2.pack(side="top", fill="both", expand=True)
        label3.pack(side="top", fill="both", expand=True)
        label4.pack(side="top", fill="both", expand=True)
        label5.pack(side="top", fill="both", expand=True)
        label6.pack(side="top", fill="both", expand=True)
        btn1.pack()


class Game1MainPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, width=600, height=600)
        self.controller = controller

        self.remaining_times_int = 5
        self.accumulated_score_int = 0
        self.raised_count = 0

        self.createWidgets()

    def update_label_text(self, target_object, text):
        target_object.configure(text=text)

    def reset_if_needed(self):
        if self.raised_count == 0:
            self.raised_count += 1
        else:
            self.remaining_times_int = 5
            self.accumulated_score_int = 0
            self.remaining_times_str.set(self.remaining_times_int)
            self.accumulated_score_str.set(self.accumulated_score_int)
            self.remaining_times_label.configure(textvariable=self.remaining_times_str)
            self.accumulated_score_label.configure(textvariable=self.accumulated_score_str)

            self.guess_big_button.place(relx=0.3, rely=0.7, anchor=CENTER)
            self.guess_small_button.place(relx=0.7, rely=0.7, anchor=CENTER)
            self.back_to_door_page_button.place_forget()

    def createWidgets(self):

        # Background
        self.image_heart = Image.open("heartx.png")
        self.image_heart = self.image_heart.resize((90, 45), Image.ANTIALIAS)
        self.image_heart = ImageTk.PhotoImage(self.image_heart)
        self.image_heart_label = Label(self, image=self.image_heart)
        # self.imageHeartLabel.grid(row=0, column=8, columnspan=2)

        self.image_diamond = Image.open("diamond.png")
        self.image_diamond = self.image_diamond.resize((90, 50), Image.ANTIALIAS)
        self.image_diamond = ImageTk.PhotoImage(self.image_diamond)
        self.image_diamond_label = Label(self, image=self.image_diamond)
        # self.imageDiamondLabel.grid(row=1, column=8, columnspan=2)

        self.remaining_times_str = StringVar()
        self.accumulated_score_str = StringVar()
        self.descirption_str = StringVar()

        self.remaining_times_str.set(self.remaining_times_int)
        self.accumulated_score_str.set(self.accumulated_score_int)

        self.remaining_times_label = Label(self, height=1, width=2, textvariable=self.remaining_times_str, font=('微軟正黑體', 32))
        self.accumulated_score_label = Label(self, height=1, width=2, textvariable=self.accumulated_score_str, font=('微軟正黑體', 32))
        self.descirption_label = Label(self, height=1, width=50, textvariable=self.descirption_str, font=('微軟正黑體', 12))
        self.guess_big_button = Button(self, text="大", height=1, width=5, command=self.click_guess_big_button, font=('微軟正黑體', 24), bg='black', foreground='white')
        self.guess_small_button = Button(self, text="小", height=1, width=5, command=self.click_guess_small_button, font=('微軟正黑體', 24), bg='black', foreground='white')

        self.back_to_door_page_button = Button(self, text="回到主畫面", height=1, width=15, command=self.back_to_door, font=('微軟正黑體', 24), bg='black', foreground='white')

        # location
        self.image_diamond_label.place(relx=0.43, rely=0.25, anchor=CENTER)
        self.image_heart_label.place(relx=0.43, rely=0.1, anchor=CENTER)

        self.remaining_times_label.place(relx=0.57, rely=0.1, anchor=CENTER)
        self.accumulated_score_label.place(relx=0.57, rely=0.25, anchor=CENTER)
        self.descirption_label.place(relx=0.5, rely=0.4, anchor=CENTER)
        self.guess_big_button.place(relx=0.3, rely=0.7, anchor=CENTER)
        self.guess_small_button.place(relx=0.7, rely=0.7, anchor=CENTER)

    def generate_num(self):
        point = random.randrange(1, 100)
        print(point)
        return point

    def click_guess_big_button(self):
        global game1_pass

        self.number = self.generate_num()
        isBig = 51 <= self.number <= 100

        self.remaining_times_int -= 1
        self.remaining_times_str.set(self.remaining_times_int)

        if isBig:
            self.accumulated_score_int += 1
            self.accumulated_score_str.set(self.accumulated_score_int)

        if self.remaining_times_int == 0:
            if self.accumulated_score_int >= 3:
                text = "系統產生的數字為" + str(self.number) + "，您猜大，遊戲結束，猜對" + str(self.accumulated_score_int) + "次，闖關成功"
                game1_pass = True
            else:
                text = "系統產生的數字為" + str(self.number) + "，您猜大，遊戲結束，猜對" + str(self.accumulated_score_int) + "次，闖關失敗"
            print(text)
            self.descirption_str.set(text)
            self.prepare_to_back_to_door()
        else:
            if isBig:
                text = '系統產生的數字為%d，您猜大，恭喜猜對了' % self.number
            else:
                text = '系統產生的數字為%d，您猜大，很遺憾，猜錯了' % self.number
            self.accumulated_score_str.set(self.accumulated_score_int)
            self.remaining_times_str.set(self.remaining_times_int)
            self.descirption_str.set(text)

    def click_guess_small_button(self):
        global game1_pass
        self.number = self.generate_num()
        isSmall = 1 <= self.number <= 50
        self.remaining_times_int -= 1
        self.remaining_times_str.set(self.remaining_times_int)

        if isSmall:
            self.accumulated_score_int += 1
            self.accumulated_score_str.set(self.accumulated_score_int)

        if self.remaining_times_int == 0:
            if self.accumulated_score_int >= 3:
                text = "系統產生的數字為" + str(self.number) + "，您猜小，遊戲結束，猜對" + str(self.accumulated_score_int) + "次，闖關成功"
                self.accumulated_score_str.set(self.accumulated_score_int)
                self.remaining_times_str.set(self.remaining_times_int)
                game1_pass = True
            else:
                text = "系統產生的數字為" + str(self.number) + "，您猜小，遊戲結束，猜對" + str(self.accumulated_score_int) + "次，闖關失敗"
                self.accumulated_score_str.set(self.accumulated_score_int)
                self.remaining_times_str.set(self.remaining_times_int)
            self.descirption_str.set(text)
            self.prepare_to_back_to_door()
        else:
            if isSmall:
                text = '系統產生的數字為%d，您猜小，恭喜猜對了' % self.number
            else:
                text = '系統產生的數字為%d，您猜小，很遺憾，猜錯了' % self.number
            self.accumulated_score_str.set(self.accumulated_score_int)
            self.remaining_times_str.set(self.remaining_times_int)
            self.descirption_str.set(text)

    def prepare_to_back_to_door(self):
        self.guess_big_button.place_forget()
        self.guess_small_button.place_forget()
        self.back_to_door_page_button.place(relx=0.5, rely=0.7, anchor=CENTER)

    def back_to_door(self):
        self.controller.show_frame(DoorPage)


class Game2IntroPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, width=600,height=400)
        self.controller = controller
        self.createWidgets()
    def createWidgets(self):
        label1 = Label(self, text="歡迎來到終極密碼遊戲", font=('微軟正黑體', 30), bg='black', fg='white')
        label2 = Label(self, text="規則說明:", font=('微軟正黑體', 24))
        label3 = Label(self, text="系統會產生一個數字(1-100)，", font=('微軟正黑體', 18))
        label4 = Label(self, text="要去猜中此數字的數值，", font=('微軟正黑體', 18))
        label5 = Label(self, text="猜錯會依據猜的數字給予提示，", font=('微軟正黑體', 18))
        label6 = Label(self, text="共有6次機會", font=('微軟正黑體', 18))
        btn1 = Button(self, text="遊戲開始", height=1, width=8, command=lambda: self.controller.show_frame(Game2MainPage), bg='black', foreground='white', font=('微軟正黑體', 24))

        label1.pack(side="top", fill="both", expand=True)
        label2.pack(side="top", fill="both", expand=True)
        label3.pack(side="top", fill="both", expand=True)
        label4.pack(side="top", fill="both", expand=True)
        label5.pack(side="top", fill="both", expand=True)
        label6.pack(side="top", fill="both", expand=True)

        btn1.pack()


class Game2MainPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, width=600, height=400)
        self.controller = controller
        self.display_count = 0
        self.lower_bound = 1
        self.upper_bound = 100
        self.guess_count_limit = 6
        self.guess_count = 0
        self.answer = randint(self.lower_bound, self.upper_bound)
        print('Game2 answer:', self.answer)

        self.bg_pic = AnimatedGif(self, 'green_1.gif', 0.20)
        self.bg_pic.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_pic.start()

        init_text = u'請輸入一個介於 ' + str(self.lower_bound) + '-' + str(self.upper_bound) + ' 之間的整數\n'
        self.lb = Label(self, height=4, width=40, text=init_text, bg="PaleTurquoise2")

        self.txt = Text(self, height=1, width=10)
        self.txt.bind('<Return>', self.click_enter_keyboard)
        self.btn = Button(self, height=2, width=15, text="Enter", command=self.click_enter_btn, bg='black', foreground='white')

        self.lb.place(relx=0.5, rely=0.35, anchor=CENTER)
        self.txt.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.btn.place(relx=0.5, rely=0.6, anchor=CENTER)

    @staticmethod
    def update_label_text(target_object, text):
        target_object.configure(text=text)

    def reset_if_needed(self):
        if self.display_count == 0:  # 若是第一次被呼叫來展示，還不須要再reset，因為使用者還沒玩過遊戲，變數尚未更動
            self.display_count += 1
        else:
            print('reset ................')
            self.guess_count = 0

            self.lower_bound = 1
            self.upper_bound = 100
            self.answer = randint(self.lower_bound, self.upper_bound)
            print('self.answer:', self.answer)
            init_text = u'請輸入一個介於 ' + str(self.lower_bound) + '-' + str(self.upper_bound) + ' 之間的整數\n'
            self.update_label_text(self.lb, init_text)
            self.display_count += 1

            self.btn['text'] = 'Enter'
            self.btn[' command'] = self.click_enter_btn

    # 在文字輸入框 , 鍵盤按下Enter按鈕後會觸發的事件
    def click_enter_keyboard(self, event):
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
        # 讀取文字輸入框的文字
        input = self.txt.get("1.0", 'end-1c')
        # 去除空白 換行 字元
        input = input.strip()

        self.clear_text_text(self.txt)

        try:
            guess_number = int(input)
        except ValueError:
            text = u'格式錯誤，請輸入數字'
            self.update_label_text(self.lb, text)
            return None

        if guess_number < self.lower_bound or guess_number > self.upper_bound:
            text = u'避免浪費您的機會, 請輸入 ' + str(self.lower_bound) + '-' + str(self.upper_bound) + u'之間的整數\n'
            print(text)
            self.update_label_text(self.lb, text)
            return None

        self.guess_count += 1

        if guess_number == self.answer:
            global game2_pass
            text = u"恭喜闖關成功，您猜了%d次" % self.guess_count
            self.update_label_text(self.lb, text)
            game2_pass = True
            self.prepare_to_back_to_door()

        elif guess_number < self.answer:
            self.lower_bound = guess_number + 1

            if self.guess_count < self.guess_count_limit:
                text = u'答案不是' + str(guess_number) + u', 請再接再厲, 還剩下' + str(self.guess_count_limit-self.guess_count) +  u'次機會\n' \
                       + u'答案介於 ' + str(self.lower_bound) + '-' + str(self.upper_bound) + u'之間'
                self.update_label_text(self.lb, text)
            else:
                text = u'您最後一次回答為:' + str(guess_number) + u' 正確答案為:' + str(self.answer) + u'闖關失敗'
                self.update_label_text(self.lb, text)
                self.prepare_to_back_to_door()
        else:
            self.upper_bound = guess_number - 1

            if self.guess_count < self.guess_count_limit:
                text = u'答案不是' + str(guess_number) + u', 請再接再厲, 還剩下' + str(self.guess_count_limit - self.guess_count) + u'次機會\n' \
                       + u'答案介於 ' + str(self.lower_bound) + '-' + str(self.upper_bound) + u'之間'
                self.update_label_text(self.lb, text)
            else:
                text = u'您最後一次回答為:' + str(guess_number) + u' 正確答案為:' + str(self.answer) + u'闖關失敗'
                self.update_label_text(self.lb, text)
                self.prepare_to_back_to_door()

    def prepare_to_back_to_door(self):
        self.btn['text'] = u'回到主畫面'
        self.btn['command'] = self.back_to_door

    def back_to_door(self):
        self.controller.show_frame(DoorPage)
        #         self.bg_pic.stop()


class Game3IntroPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent,width=600, height=400)
        self.controller = controller
        self.createWidgets()

    def createWidgets(self):

        label1 = Label(self, text="歡迎來到1A2B遊戲", font=('微軟正黑體', 30), bg='black', fg='white')
        label2 = Label(self, text="規則說明:", font=('微軟正黑體', 24))
        label3 = Label(self, text="系統會產生一個四位數的數字，", font=('微軟正黑體', 18))
        label4 = Label(self, text="要去猜此四位數字，", font=('微軟正黑體', 18))
        label5 = Label(self, text="如果猜錯，會給予提示，", font=('微軟正黑體', 18))
        label6 = Label(self, text="1A代表有一個位數的數字的值與位置皆是對的", font=('微軟正黑體', 18))
        label7 = Label(self, text="1B代表有一個位數的數字的值是對的，但位置是錯的", font=('微軟正黑體', 18))
        label8 = Label(self, text="2B代表有2個位數的數字的值是對的，但位置是錯的", font=('微軟正黑體', 18))
        label9 = Label(self, text="共有10次機會", font=('微軟正黑體', 18))
        btn1 = Button(self, text="遊戲開始", height=1, width=8, command=lambda: self.controller.show_frame(Game3MainPage), bg='black', foreground='white', font=('微軟正黑體', 24))

        label1.pack(side="top", fill="both", expand=True)
        label2.pack(side="top", fill="both", expand=True)
        label3.pack(side="top", fill="both", expand=True)
        label4.pack(side="top", fill="both", expand=True)
        label5.pack(side="top", fill="both", expand=True)
        label6.pack(side="top", fill="both", expand=True)
        label7.pack(side="top", fill="both", expand=True)
        label8.pack(side="top", fill="both", expand=True)
        label9.pack(side="top", fill="both", expand=True)
        btn1.pack()


class Game3MainPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, width=600, height=400)
        print("Game3MainPage - init")
        self.controller = controller
        self.answer = ''
        self.playerGuess = ''
        self.nOfDigits = 4
        self.count = 10
        self.setup_widgets()

    def n_digit_num(self, n):
        numbers = random.sample(range(10), n)
        rand = ''.join(map(str, numbers))
        return rand

    def new_game(self):
        global count
        print("Game3MainPage - new_game")
        self.label.config(text='')
        self.resultLabel.config(text="")
        self.answers.delete(1.0, END)
        self.answer = self.n_digit_num(self.nOfDigits)
        print('Game3MainPage answer:', self.answer)
        self.count = 10
        self.chanceLabel.config(text=str(self.count) + " chances left")

    def check_guess(self):
        global count
        self.playerGuess = self.label.cget("text")

        if len(self.playerGuess) == self.nOfDigits:
            self.count = self.count - 1
            a = self.cal_a(self.playerGuess)
            b = self.cal_b(self.playerGuess)
            self.show_result(a, b)
            self.label.config(text="")
            self.answers.insert(INSERT, self.playerGuess + "   " + str(a) + "A" + str(b) + "B" + "\n")
            self.chanceLabel.config(text=str(self.count)+" chances left")

        else:
            messagebox.showinfo("提醒", "位數要為" + str(self.nOfDigits))
            self.label.config(text="")

        if self.count == 0:
            self.chanceLabel.config(text="Try Again!")
            self.count = 10

    def cal_a(self, guess):
        a = 0
        for i in range(len(self.answer)):
            if guess[i] == self.answer[i]:
                a = a + 1
        return a

    def cal_b(self, guess):
        b = 0
        k = len(self.answer)
        for i in range(k):
            for j in range(k):
                if i != j:
                    if guess[i] == self.answer[j]:
                        b = b + 1
        return b

    def show_result(self, a, b):
        if a == self.nOfDigits:
            global game3_pass
            result = "You Win"
            game3_pass = True
            # sleep(1)
            self.controller.show_frame(DoorPage)
        else:
            result = str(a) + "A" + str(b) + "B"

        self.resultLabel.config(text=result)

    def click_but1(self):
        self.label.configure(text=self.label.cget("text") + "1")

    def click_but2(self):
        self.label.configure(text=self.label.cget("text") + "2")

    def click_but3(self):
        self.label.configure(text=self.label.cget("text") + "3")

    def click_but4(self):
        self.label.configure(text=self.label.cget("text") + "4")

    def click_but5(self):
        self.label.configure(text=self.label.cget("text") + "5")

    def click_but6(self):
        self.label.configure(text=self.label.cget("text") + "6")

    def click_but7(self):
        self.label.configure(text=self.label.cget("text") + "7")

    def click_but8(self):
        self.label.configure(text=self.label.cget("text") + "8")

    def click_but9(self):
        self.label.configure(text=self.label.cget("text") + "9")

    def click_but0(self):
        self.label.configure(text=self.label.cget("text") + "0")

    def click_butBack(self):
        s = self.label.cget("text")
        self.label.configure(text=s[0:-1])

    def setup_widgets(self):

        self.resultLabel = Label(self, text="0A0B", font=('arial', 28), height=2)
        self.guessBtn = Button(self, text="Guess", command=self.check_guess, height=4, width=20)
        self.new_gameBtn = Button(self, text="New Game", command=self.new_game, height=4, width=20)
        self.Back_Main = Button(self, text="Back To Main Menu", command=lambda: self.controller.show_frame(DoorPage),
                                height=4, width=20)
        self.chanceLabel = Label(self, height=2, borderwidth=5, text="10 chances left", font=('arial', 18))

        self.label = Label(self, height=2, borderwidth=5, text="", font=('arial', 28))
        self.btn_1 = Button(self, text="1", command=self.click_but1, height=4, width=8)
        self.btn_2 = Button(self, text="2", command=self.click_but2, height=4, width=8)
        self.btn_3 = Button(self, text="3", command=self.click_but3, height=4, width=8)
        self.btn_4 = Button(self, text="4", command=self.click_but4, height=4, width=8)
        self.btn_5 = Button(self, text="5", command=self.click_but5, height=4, width=8)
        self.btn_6 = Button(self, text="6", command=self.click_but6, height=4, width=8)
        self.btn_7 = Button(self, text="7", command=self.click_but7, height=4, width=8)
        self.btn_8 = Button(self, text="8", command=self.click_but8, height=4, width=8)
        self.btn_9 = Button(self, text="9", command=self.click_but9, height=4, width=8)
        self.btn_0 = Button(self, text="0", command=self.click_but0, height=4, width=18)
        self.btn_back = Button(self, text="←", command=self.click_butBack, height=4, width=8)

        self.btn_1.grid(row=3, column=0)
        self.btn_2.grid(row=3, column=1)
        self.btn_3.grid(row=3, column=2, sticky="w")
        self.btn_4.grid(row=4, column=0)
        self.btn_5.grid(row=4, column=1)
        self.btn_6.grid(row=4, column=2, sticky="w")
        self.btn_7.grid(row=5, column=0)
        self.btn_8.grid(row=5, column=1)
        self.btn_9.grid(row=5, column=2, sticky="w")
        self.btn_0.grid(row=6, column=0, columnspan=2, sticky="w")
        self.btn_back.grid(row=6, column=2, sticky="e")

        self.answers = Text(self, width=20, height=12, bg='black', foreground='white', font=('arial', 15))
        self.answers.grid(row=3, column=5, rowspan=4, pady=4, padx=10)

        self.label.grid(row=0, column=0, columnspan=3, rowspan=3)
        self.chanceLabel.grid(row=0, column=5, columnspan=3, rowspan=3)
        self.resultLabel.grid(row=0, column=4, rowspan=3)
        self.guessBtn.grid(row=3, column=4)
        self.new_gameBtn.grid(row=4, column=4)
        self.Back_Main.grid(row=5, column=4)

        self.new_game()


class EndPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, width=600, height=400)
        self.config(bg='grey9')
        self.bg_pic = AnimatedGif(self, 'ending.gif', 0.04)
        self.bg_pic.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_pic.start()
        self.quit_but = Button(self, text="QUIT", command=self.quit, height=2, width=10, bg='black', foreground='white')  # Button to quit
        self.quit_but.place(relx=0.5, rely=0.9, anchor=CENTER)


app = TreasureHunter()
app.mainloop()
