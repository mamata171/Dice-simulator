from tkinter import *
import random
 
root=Tk()
root.geometry("700x400")

#GUI will have two basic components
#1.Button which will trigger the rolling of dice
#2.Dice label
l1=Label(root,font=("Helvetica",200))
l2=Label(root,font=("Helvetica",200))
def roll():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    #configure the label
    a=random.choice(dice)
    l1.config(text=a)
    l1.place(x=5,y=5)
    
b1=Button(root,text="Roll the Dice!",command=roll)
b1.place(x=100,y=10)

def roll2():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    b=f'{random.choice(dice)}{random.choice(dice)}'
    l2.config(text=b)
    l2.place(x=200,y=5)

def exit():
    root.destroy()
    
def clear():
    l2.config(text="")

def clear2():
    l1.config(text="")

b2=Button(root,text="Roll Two Dice!",command=roll2)
b2.place(x=350,y=10)


b5 = Button(root,text='clear dice1',command=clear2,width=18,height=2)
b5.place(x=50,y=300)
b3=Button(root,text='Exit',command=exit,width=16,height=2)
b3.place(x=200,y=300)
b4=Button(root,text='clear_dice2',command=clear,width=18,height=2)
b4.place(x=340,y=300)
root.mainloop()



    
