import tkinter as tk
from  tkinter  import ttk
from random import randint


class UltimatePasswordGameWindow(tk.Frame):
    def __init__(self, lower_bound = 1, upper_bound = 100, guess_count_limit = 5):
        tk.Frame.__init__( self )

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

        self.lb = tk.Label(self, height=4, width=50, text=init_text)
        self.txt = tk.Text(self, height=2, width=10)
        self.btn = tk.Button(self, height=2, width=15, text="Enter", command=self.click_enter)

        #Assign Position/指定位置
        self.lb.grid(row=0, column=0)
        self.txt.grid(row=1, column=0)
        self.btn.grid(row=3, column=0)
        self.mainloop()

    def update_text_text(self, target_object, text):
        target_object.delete("1.0", "end")
        target_object.insert("1.0", text)

    def update_label_text(self, target_object, text):
        target_object.configure(text = text)

    def click_enter(self):
        print('clickBtn')
        try:
            guess_number = int(self.txt.get("1.0",'end-1c'))
        except ValueError:
            text = u'格式錯誤，請輸入數字'
            print(text)
            self.update_label_text(self.lb, text)
            return None

        self.guess_count += 1

        print('guess_number:',guess_number)
        print('self.lower_bound:', self.lower_bound)
        print('self.upper_bound:', self.upper_bound)

        # https://www.tutorialspoint.com/python/tk_text.htm
        if guess_number <= self.lower_bound or guess_number >= self.upper_bound:
            text = u'請輸入 ' + str(self.lower_bound) + '-' + str(self.upper_bound) + u'之間的整數\n'
            print(text)
            self.update_label_text(self.lb, text)
            return None

        if guess_number == self.answer:
            text = u'恭喜猜對！門已解鎖'
            print(text)
            self.update_label_text(self.lb, text)
            return None
        elif guess_number < self.answer:
            self.lower_bound = guess_number
            if self.guess_count < self.guess_count_limit:
                text = u'請再接再厲, 還剩下' + str(self.guess_count_limit-self.guess_count) +  u'次機會\n' + u'答案介於 ' + str(self.lower_bound) + '-' + str(self.upper_bound) + u'之間'
            else:
                text = u'沒有猜對, 機會已用完, 遊戲結束, 您的回答為:' + str(guess_number) + u' 正確答案為:' + str(self.answer)
            self.update_label_text(self.lb, text)
        else:
            self.upper_bound = guess_number
            if self.guess_count < self.guess_count_limit:
                text = u'請再接再厲, 還剩下' + str(self.guess_count_limit-self.guess_count) +  u'次機會\n' + u'答案介於 ' + str(self.lower_bound) + '-' + str(self.upper_bound) +  u'之間'
            else:
                text = u'沒有猜對, 機會已用完, 遊戲結束, 您的回答為:' + str(guess_number) + u' 正確答案為:' + str(self.answer)
        self.update_label_text(self.lb, text)

window = UltimatePasswordGameWindow()