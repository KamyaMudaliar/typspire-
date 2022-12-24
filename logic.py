"""x = []
    
fl= open("random_words.txt","r")
data= fl.read()
x=data.split(" ")
y= random.sample(x, 20)
print(y)
fl.close()
word = random.randint(0, (len(y)-1))
"""
"""import tkinter as tk
from tkinter import ttk
from timeit import default_timer as timer

lst= []
def return_pressed(event):
  global lst
  start = timer()
  lst.append(start) 

a=int(lst[-1]-lst[0])
if a!=0:
   window_rw= tk.Tk()
   tk.Label(window_rw, text= a).place(x=0, y=0)
   window_rw.mainloop()
else:
   print("enter the words")"""


"""def results(res):
    print(res)
    if res!=0:
        speed.insert(END,"The speed is "+res+"WPM")
        
    else:
        speed.insert(END,"Enter the given words")"""

import random
quotes= []
a= open("random_quotes.txt")
data= a.read()
quotes=data.split(".")
print(quotes)
quo=random.sample(quotes,1)
print(quo)
#b= [elem.strip('][').split(" ") for elem in quote]
#print(b)
quote= []
for elem in quo:
    quote.extend(elem.strip('][').split(" "))
print(quote)
quote.append(" .")
print(quote)





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