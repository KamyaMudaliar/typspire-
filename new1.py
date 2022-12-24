import pprint
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from timeit import default_timer as timer
import random

lst=[]
acc = 0.0
acc1 =0.0
total = 0
acc_w=0
inc_w = 0
global a
global a1
#function that appends the time into the list
def return_pressed(event):
    global lst
    start = timer()
    lst.append(start)

#The main function that will go into the words icon command
def random_words():
    lst2=[]
    
    #Function that gets the user typed words into a list
    def get_words():
        global acc
        global total
        global acc_w
        global inc_w
        inputvalues = btn.get("1.0","end-1c")
        lst2=inputvalues.split()
        lst3 = [i for i, j in zip(lst2, word) if i == j]
        print(lst3)
        acc= (len(lst3)/len(word))*100 
        total= len(word)
        acc_w= len(lst3)
        inc_w= len(word)-len(lst3)
        window.destroy()

    start= timer()
    window= tk.Tk() # creating a new window once the button is pressed
    window.geometry("1366x768")
    window['bg']= '#322C2C'
    root.destroy()

    #Generating random words from the text file
    words= []
    fl= open("random_words.txt")
    data= fl.read()
    words= data.split(" ")
    word= random.sample(words,5)
    rw= tk.Label(window, text= word, font="times 23", bg= "#322C2C", fg="white").place(x=20,y=10)

    #Textbox where you type the given words
    btn= tk.Text(window)
    btn.bind('<KeyPress>', return_pressed)
    btn.focus()
    btn.place(x=300, y=233)
    submit= Button(window, text="submit",command= get_words).place(x=300, y=300)
    window.mainloop()
    print(lst)
    a=int(lst[-1]-lst[0]) #Final time minus the initial time

    #New window to see results
    if a!=0:
        window_rw= tk.Tk()
        window_rw.geometry("1366x768")
        #To display speed
        tk.Label(window_rw, text="the speed is").place(x=0,y=0)
        tk.Label(window_rw,text=a).place(x=10, y=10)
        #To display the accuracy
        tk.Label(window_rw,text="the accuracy is ").place(x=50, y=30)
        tk.Label(window_rw, text=acc).place(x=60, y=40)
        #To display the total number of words
        tk.Label(window_rw, text= "total no. of words typed are").place(x=100, y=150)
        tk.Label(window_rw, text= total).place(x=150, y= 200)
        #To display the number of correct words
        tk.Label(window_rw, text="the number of correct words typed are").place(x=300, y=350)
        tk.Label(window_rw, text= acc_w).place(x=350, y=400)
        #To display the number of incorrect words
        tk.Label(window_rw, text="the number of incorrect words typed are").place(x=500, y=550)
        tk.Label(window_rw, text= inc_w).place(x=600, y=650)



    else: #Does not work
        window_rw=tk.Tk()
        tk.Label(window_rw, text="Enter the given set of words").place(x=0,y=0)
        window_rw.mainloop()

#The main function that will go into the quote_icon
def random_quotes():
    lst4=[]
    #Function that gets the user typed words into a list
    def get_quote():
        global acc1
        global total1
        global acc_q
        global inc_q
        inputvalues1= btn1.get("1.o", "end=1c")
        lst4=inputvalues1.split()
        lst5= [i for i, j in zip(lst4, quote)if i==j]
        print(lst5)
        acc1=(len(lst5)/len(quote))*100
        total1= len(quote)
        acc_q=len(lst5)
        inc_q=len(quote)-len(lst5)
        window1.destroy()

    start1= timer()
    window1 =tk.Tk()# creating a new window once the button is pressed
    window1.geometry("1366x768")
    window1['bg']= '#322C2C'
    root.destroy()

    #Generating random quotes from the text file
    quotes=[]
    fl1=open("random_quotes.txt")
    data1=fl1.read()
    quotes=data1.split(".")
    quo=random.sample(quotes,1)
    quote=[]
    for elem in quo:
        quote.extend(elem.strip('][').split(" "))
        quote.append(" .")
        print(quote)
    rq=tk.Label(window1, text = quote, font="times23", bg="#322C2C" , fg="white").place(x=20, y=10)
    
    #Textbox where you type the given quote
    btn1=tk.Text(window1)
    btn1.bind('<KeyPress>', return_pressed)
    btn1.focus()
    btn1.place(x=300, y=233)
    submit1= Button(window1, text="submit", command=get_quote).place(x=300, y=300)
    window1.mainloop()
    print(lst)
    a1= int(lst[-1]-lst[0])#Final time minus the initial time

    #New window to see results
    if a1!=0:
        window_rq=tk.Tk()
        window_rq.geometry("1366x768")
        #To display speed
        tk.Label(window_rq, text="the speed is").place(x=0,y=0)
        tk.Label(window_rq,text=a1).place(x=10, y=10)
        #To display the accuracy
        tk.Label(window_rq,text="the accuracy is ").place(x=50, y=30)
        tk.Label(window_rq, text=acc1).place(x=60, y=40)
        #To display the total number of words
        tk.Label(window_rq, text= "total no. of words typed are").place(x=100, y=150)
        tk.Label(window_rq, text= total1).place(x=150, y= 200)
        #To display the number of correct words
        tk.Label(window_rq, text="the number of correct words typed are").place(x=300, y=350)
        tk.Label(window_rq, text= acc_q).place(x=350, y=400)
        #To display the number of incorrect words
        tk.Label(window_rq, text="the number of incorrect words typed are").place(x=500, y=550)
        tk.Label(window_rq, text= inc_q).place(x=600, y=650)

    
root=tk.Tk()
root['bg']='#322C2C'
root.geometry("1366x768")


words_icon= PhotoImage(file='/home/kami/Pictures/words.png')
words_btn=tk.Button(root,image= words_icon,bg="#322C2C",command=random_words)

words_btn.grid(row=7,column=1)

quote_icon = PhotoImage(file='/home/kami/Pictures/quotes.png')
quote_btn=tk.Button(root,image=quote_icon,bg="#322C2C",command=random_quotes)
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