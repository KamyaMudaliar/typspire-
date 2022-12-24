import pprint
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from timeit import default_timer as timer
import random


lst=[]
global a

def return_pressed(event):
  global lst
  start = timer()
  lst.append(start)



def random_words():
  start = timer()
  window = tk.Tk()
  window.geometry("1366x768")
  window['bg']='#322C2C'
  root.destroy()
  words=[]
  fl = open("random_words.txt")
  data =fl.read()
  words=data.split(" ")
  word= random.sample(words,5)
  rw= tk.Label(window, text=word , font ="times 23", bg="#322C2C", fg="white").place(x=20,y= 10)
  #entry_word= Text(window).place(x= 200, y=55)

  btn= tk.Text(window)
  
  btn.bind('<KeyPress>',return_pressed)
  btn.focus()
  btn.place(x=300,y=233)
  submit= Button(window, text = "submit", command=results)
  submit.place(x=350, y= 300)
  #result= Text(window,height = 10, width=10)
  #result.place(x=20,y=20)
  window.mainloop()
  print(lst)
  a=int(lst[-1]-lst[0])
  def results(text):
    return(a)
  


root=tk.Tk()
root['bg']='#322C2C'
root.geometry("1366x768")


words_icon= PhotoImage(file='/home/kami/Pictures/words.png')
words_btn=tk.Button(root,image= words_icon,bg="#322C2C",command=random_words)

words_btn.grid(row=7,column=1)

quote_icon = PhotoImage(file='/home/kami/Pictures/quotes.png')
quote_btn=tk.Button(root,image=quote_icon,bg="#322C2C")
quote_btn.grid(row=10, column=1)

number_icon= PhotoImage(file='/home/kami/Pictures/numbers.png')
number_btn = tk.Button(root, image=number_icon,bg="#322C2C")
number_btn.grid(row=13, column=1)

language_icon= PhotoImage(file='/home/kami/Pictures/languages.png')
language_btn= tk.Button(root, image=language_icon, bg="#322C2C")
language_btn.grid(row=16, column=1)

#Title of the application
title_icon= PhotoImage(file='/home/kami/Pictures/titleee.png')
title_label=tk.Label(root, image= title_icon, bg="#322C2C")
title_label.grid(row=1, column=3)

# Buttons on the top right 

home_icon = PhotoImage(file='/home/kami/Pictures/home.png')
home_btn=tk.Button(root, image= home_icon,bg="#322C2C")
home_btn.grid(row=1 , column=5)

login_icon = PhotoImage(file='/home/kami/Pictures/login.png')
login_btn=tk.Button(root, image= login_icon,bg="#322C2C")
login_btn.grid(row=1 , column=7)

root.resizable(False,False)
root.mainloop()