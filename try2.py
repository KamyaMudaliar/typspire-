#import timer
import random
def random_quotes():
    #start1= timer()
    # window1 =tk.Tk()# creating a new window once the button is pressed
    # window1.geometry("1366x768")
    # window1['bg']= '#322C2C'
    # root.destroy()

    #Generating random quotes from the text file
    quotes= []
    fl1= open("random_quotes.txt")
    data1= fl1.read()
    quotes= data1.split(".")
    quo= random.sample(quotes,1)
    quot= quo.split(" ")
    print(quo)
    print(quot)
random_quotes()
