import tkinter as tk
import tkinter.font as tkFont
import random
from PIL import Image
from PIL import ImageTk
import tkinter.messagebox

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
        quit = tk.messagebox.showinfo("遊戲結束","猜對%d次，闖關成功" %self.scores)
        if quit == "ok":
            self.master.destroy()

      else: 
        quit = tk.messagebox.showinfo("遊戲結束","猜對%d次，闖關失敗" %self.scores)
        
        if quit == "ok":
            self.master.destroy()
        
         


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
        quit = tk.messagebox.showinfo("遊戲結束","猜對%d次，闖關成功" %self.scores)        
        if quit == "ok":
            self.master.destroy()
      else: 
        quit = tk.messagebox.showinfo("遊戲結束","猜對%d次，闖關失敗" %self.scores)
        print(quit)
        if quit == "ok":
            self.master.destroy()
             
    
    if isSmall:
      self.scores += 1
      scores_str.set(self.scores)
      result_str.set('恭喜，你猜對了')
    else:
      result_str.set('很遺憾，你猜錯了')





cg = CompareGame()
cg.master.title("猜大小")
cg.mainloop()
print(quit)
#if quit == "ok":
#    cg.destory()