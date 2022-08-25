 import threading
 import time
 import random

 from Tkinter import *
 import tkMessageBox
 import Tkinter as tki
 import tkFileDialog as th1

 class SpeechRecognizer(threading.Thread):

     ANSWERS = ["foo", "bar"]

     def __init__(self):
         super(SpeechRecognizer, self).__init__()
         self.setDaemon(True)
         self.recognized_text = "initial"

     def run(self):
         while True:
             time.sleep(1.0)
             self.recognized_text = random.choice(self.ANSWERS)


 recognizer = SpeechRecognizer()
 recognizer.start()

 class App(object):

     def __init__(self,root):
         self.root = root

     # create a Frame for the Text and Scrollbar
         txt_frm = tki.Frame(self.root, width=900, height=900)
         txt_frm.pack(fill="both", expand=True)
         # ensure a consistent GUI size
         txt_frm.grid_propagate(False)

     # create first Text label, widget and scrollbar
         self.lbl1 = tki.Label(txt_frm, text="Type")
         self.lbl1.grid(row=0,column=0,padx=2,pady=2)

         self.recognized_text = StringVar()
         self.txt1 = tki.Text(txt_frm, borderwidth=3, relief="sunken", height=4,width=55,
         )
         self.txt1.config(font=("consolas", 12), undo=True, wrap='word')
         self.txt1.grid(row=25, column=7, sticky="nsew", padx=2, pady=2)
         root.after(100, self.update_recognized_text)

     def update_recognized_text(self):
         self.txt1.delete(0.0, END)
         self.txt1.insert(0.0, recognizer.recognized_text)
         root.after(100, self.update_recognized_text)

     def clearBox(self):
         if a == "clear":
             self.txt1.delete('1.0', 'end')

 root = tki.Tk()
 app = App(root)
 root.mainloop()