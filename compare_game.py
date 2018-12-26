import tkinter as tk
import tkinter.font as tkFont
import random
from PIL import Image, ImageTk




class CompareGame(tk.Frame):

  times = 5
  scores = 0
  
  def __init__(self):
    tk.Frame.__init__(self) 
    self.grid()
    self.createWidgets()

  def createWidgets(self):
    f1 = tkFont.Font(size = 32, family = "微軟正黑體")
    f2 = tkFont.Font(size = 24, family = "微軟正黑體")
    f3 = tkFont.Font(size = 18, family = "微軟正黑體")
    
    global times_str
    global scores_str
    global num_str
    global result_str
    times_str  = tk.StringVar()
    scores_str = tk.StringVar()
    num_str    = tk.StringVar()
    result_str = tk.StringVar()
    times_str.set(self.times)
    scores_str.set(self.scores)

    imageHeart           = Image.open("heartx.png")
    imageHeart           = imageHeart.resize((90, 45), Image.ANTIALIAS)
    self.imageHeart      = ImageTk.PhotoImage(imageHeart)  
    self.lbTimes         = tk.Label(self, image = self.imageHeart)

    imageDiamond         = Image.open("diamond.png")
    imageDiamond         = imageDiamond.resize((90, 50), Image.ANTIALIAS)
    self.imageDiamond    = ImageTk.PhotoImage(imageDiamond)    
    self.lbScores        = tk.Label(self, image = self.imageDiamond)

    self.lbDisplayTimes  = tk.Label(self, height = 1, width = 2, textvariable = times_str, font = f1)
    self.lbDisplayScores = tk.Label(self, height = 1, width = 2, textvariable = scores_str, font = f1)
    self.lbNum           = tk.Label(self, height = 1, width = 12, textvariable = num_str, font = f1) 
    self.lbResult        = tk.Label(self, height = 1, width = 12, textvariable = result_str, font = f3) 
    self.btnBig          = tk.Button(self, text = "大", height = 1, width = 5, command = self.clickBtnBig, font = f2) 
    self.btnSmall        = tk.Button(self, text = "小", height = 1, width = 5, command = self.clickBtnSmall, font = f2) 

    self.lbTimes.grid(row = 0, column = 7, columnspan = 3)
    self.lbScores.grid(row = 1, column = 7, columnspan = 3)
    self.lbDisplayTimes.grid(row = 0, column = 10, columnspan = 2)
    self.lbDisplayScores.grid(row = 1, column = 10, columnspan = 2)
    self.lbNum.grid(row = 2, column = 0, columnspan = 12)
    self.lbResult.grid(row = 3, column = 0, columnspan = 12, sticky = tk.NE + tk.SW)
    self.btnBig.grid(row = 4, column = 0, columnspan = 6)
    self.btnSmall.grid(row = 4, column = 6, columnspan = 6)
  

  def num(self):
    point = random.randrange(1, 100)
    return point

  def clickBtnBig(self):
    self.times -= 1
    times_str.set(self.times)
    result = self.num()
    num_str.set(result)
    isBig = 51 <= result <= 100
    if self.times == 0:
      if self.scores >=3:
        self.master.destroy()
        game_win().master.geometry("425x200+100+100")


      else: 
        self.master.destroy()
        game_loss().master.geometry("490x200+100+100")

    if isBig:
      self.scores += 1
      scores_str.set(self.scores)
      result_str.set('恭喜，你猜對了')
    else:
      result_str.set('很遺憾，你猜錯了')

  def clickBtnSmall(self):
    self.times -= 1
    times_str.set(self.times)
    result = self.num()
    num_str.set(result)
    isSmall = 1 <= result <= 50
    if self.times == 0:
      if self.scores >=3:
        self.master.destroy()
        game_win().master.geometry("425x200+100+100")
 
      else: 
          self.master.destroy()     
          game_loss().master.geometry("490x200+100+100")
    
    if isSmall:
      self.scores += 1
      scores_str.set(self.scores)
      result_str.set('恭喜，你猜對了')
    else:
      result_str.set('很遺憾，你猜錯了')


class game_loss(tk.Frame):

  def __init__(self):
    tk.Frame.__init__(self) 
    self.grid()
    self.createWidgets()

  def createWidgets(self):
    f1 = tkFont.Font(size = 32, family = "微軟正黑體")
    f2 = tkFont.Font(size = 24, family = "微軟正黑體")
    f3 = tkFont.Font(size = 18, family = "微軟正黑體")


    self.label1 = tk.Label(self, text ="遊戲結束",font = f1)
    self.label2 = tk.Label(self,text = " 沒有獲得超過3個鑽石，闖關失敗" , font = f2)
    self.btn1 = tk.Button(self, text = "退出遊戲", height = 1, width = 8,command = self.clickBtn1, font = f2) 
    self.btn2 = tk.Button(self, text = "再試一次", height = 1, width = 8,command = self.clickBtn2, font = f2)
    self.label1.grid(row = 1,column = 3,columnspan = 6)
    self.label2.grid(row = 2,column = 3,columnspan = 6)
    self.btn1.grid(row = 5, column = 0, columnspan = 6)
    self.btn2.grid(row = 5, column = 6, columnspan = 6)
 
    
  def clickBtn1(self):
      self.master.destroy()
      

  def clickBtn2(self):
      self.master.destroy()
      CompareGame().master.geometry("320x300+100+100")

class game_win(tk.Frame):

  def __init__(self):
    tk.Frame.__init__(self) 
    self.grid()
    self.createWidgets()

  def createWidgets(self):
    f1 = tkFont.Font(size = 32, family = "微軟正黑體")
    f2 = tkFont.Font(size = 24, family = "微軟正黑體")
    f3 = tkFont.Font(size = 18, family = "微軟正黑體")

    self.label1 = tk.Label(self, text ="遊戲結束",font = f1)
    self.label2 = tk.Label(self,text = " 獲得超過3個鑽石，闖關成功", font = f2)
    self.btn1 = tk.Button(self, text = "退出遊戲", height = 1, width = 8,command = self.clickBtn1, font = f2) 
    
    self.label1.grid(row = 1,column = 3,columnspan = 6)
    self.label2.grid(row = 3,column = 3,columnspan = 6)
    self.btn1.grid(row = 5, column = 3, columnspan = 6)

 
    
  def clickBtn1(self):
      self.master.destroy()
      
class game_start(tk.Frame):

  def __init__(self):
    tk.Frame.__init__(self) 
    self.grid()
    self.createWidgets()

  def createWidgets(self):
    f1 = tkFont.Font(size = 32, family = "微軟正黑體")
    f2 = tkFont.Font(size = 24, family = "微軟正黑體")
    f3 = tkFont.Font(size = 18, family = "微軟正黑體")

    self.label1 = tk.Label(self,text = "歡迎來到猜大小遊戲", font = f1)
    self.label2 = tk.Label(self,text = "規則說明:", font = f2)
    self.label3 = tk.Label(self,text = "總共有1-100數字，", font = f3)
    self.label4 = tk.Label(self,text = "51以上是大，50以下是小，", font = f3)
    self.label5 = tk.Label(self,text = "在五次機會中猜中三次即算成功", font = f3)
    self.btn1 = tk.Button(self, text = "遊戲開始", height = 1, width = 8,command = self.clickBtn1, font = f2) 

    self.label1.grid(row = 1,column = 3,columnspan = 6)
    self.label2.grid(row = 2,column = 3,columnspan = 6)
    self.label3.grid(row = 3,column = 3,columnspan = 6)
    self.label4.grid(row = 4,column = 3,columnspan = 6)
    self.label5.grid(row = 5,column = 3,columnspan = 6)
    self.btn1.grid(row = 9, column = 3, columnspan = 6)

  def clickBtn1(self):
    self.master.destroy()
    CompareGame().master.geometry("320x300+100+100")



cg = game_start()
cg.master.title("猜大小")
cg.master.geometry("+100+100")
cg.mainloop()