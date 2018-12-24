import tkinter as tk
from random import randint


class UltimatePasswordGameWindow(tk.Frame):
    def __init__(self, lower_bound = 1, upper_bound = 100, guess_count_limit = 5):
        tk.Frame.__init__( self )

        # 尚未試成功的code
        # filename =  tk.PhotoImage(file="C:\\Users\\frank\\PycharmProjects\\PythonCourse\\Lily_Project\\green.gif")
        # self.bg_label = tk.Label(self, image=filename)
        # self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # 視窗的Title
        self.master.title('UltimatePasswordGame')

        # 變數初始化
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

        photo = tk.PhotoImage(file="green.gif")

        self.lb = tk.Label(self, text = init_text,justify = tk.LEFT,image = photo,compound = tk.CENTER,font = ("华文行楷", 10),fg = "white")  # 前景色
        self.lb.place(x=0, y=0, relwidth=1, relheight=1)

        #self.lb = tk.Label(self, height=4, width=50, text=init_text)
        #self.lb.pack()
        self.txt = tk.Text(self, height=1, width=10)
        self.txt.bind('<Return>', self.click_enter_keyboard)
        self.btn = tk.Button(self, height=2, width=15, text="Enter", command=self.click_enter_btn)

        #Assign Position/指定位置
        self.lb.grid(row=0, column=0)
        self.txt.grid(row=2, column=0)
        self.btn.grid(row=5, column=0)

        # 尚未試成功的code
        # self.bind('<Return>', self.click_enter_keyboard)
        # self.focus_set()

        self.mainloop()

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
        # 移除文字輸入框
        self.txt.grid_remove()
        # 將按鈕觸發的事件 改綁定為關掉視窗的funciton
        self.btn['command'] = self.end_frame

    # 清除與關掉此Frame
    def end_frame(self):
        print('end_frame')
        # 把內容清空
        self.destroy()
        # 把視窗關閉
        self.quit()

# 開啟終極密碼遊戲,  遊戲結束時, 會自行關閉
UltimatePasswordGameWindow()

# 關閉後 再開啟另一個遊戲 (先以再次開啟 同樣遊戲為例)
# UltimatePasswordGameWindow()