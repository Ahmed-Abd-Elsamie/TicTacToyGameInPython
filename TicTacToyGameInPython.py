from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint


root=Tk()

style=ttk.Style()
style.theme_use('classic')
root.title('Tick Tack Toe : Player 1')

ActivePlayer=1

p1 = []  #Selected by player 1
p2 = []  #Selected by player 2



bu1=ttk.Button(root , text=' ' )
bu1.grid(row=0 , column=0 ,ipadx=40 , ipady=40 , sticky='snew')
bu1.config(command= lambda :BuClick(1))

bu2=ttk.Button(root , text=' ' )
bu2.grid(row=0 , column=1 ,ipadx=40 , ipady=40 , sticky='snew')
bu2.config(command= lambda :BuClick(2))

bu3=ttk.Button(root , text=' ' )
bu3.grid(row=0 , column=2 ,ipadx=40 , ipady=40 , sticky='snew')
bu3.config(command= lambda :BuClick(3))

bu4=ttk.Button(root , text=' ' )
bu4.grid(row=1 , column=0 ,ipadx=40 , ipady=40 , sticky='snew')
bu4.config(command= lambda :BuClick(4))

bu5=ttk.Button(root , text=' ' )
bu5.grid(row=1 , column=1 ,ipadx=40 , ipady=40 , sticky='snew')
bu5.config(command= lambda :BuClick(5))

bu6=ttk.Button(root , text=' ' )
bu6.grid(row=1 , column=2 ,ipadx=40 , ipady=40 , sticky='snew')
bu6.config(command= lambda :BuClick(6))

bu7=ttk.Button(root , text=' ' )
bu7.grid(row=2 , column=0 ,ipadx=40 , ipady=40 , sticky='snew')
bu7.config(command= lambda :BuClick(7))

bu8=ttk.Button(root , text=' ' )
bu8.grid(row=2 , column=1 ,ipadx=40 , ipady=40 , sticky='snew')
bu8.config(command= lambda :BuClick(8))

bu9=ttk.Button(root , text=' ' )
bu9.grid(row=2 , column=2 ,ipadx=40 , ipady=40 , sticky='snew')
bu9.config(command= lambda :BuClick(9))



def BuClick(id):
    print(id)
    global p1
    global p2
    global ActivePlayer

    if(ActivePlayer == 1):
        setLayout(id , 'X')
        p1.append(id)
        ActivePlayer=2
        root.title('Tick Tack Toe : Player 2')
        print("P1:{}".format(p1))
        AutoPlay() # To Play With PC ==> if you Wanna play with a friend => Just Remove Autoplay Function

    elif(ActivePlayer == 2):
        setLayout(id , 'O')
        p2.append(id)
        ActivePlayer = 1
        root.title('Tick Tack Toe : Player 1')
        print("P2:{}".format(p2))
    CheckWinner()



def setLayout(id,txt):
    if (id==1):
        bu1.config(text=txt)
        bu1.state(['disabled'])
    elif (id == 2):
        bu2.config(text=txt)
        bu2.state(['disabled'])
    elif (id == 3):
        bu3.config(text=txt)
        bu3.state(['disabled'])
    elif (id == 4):
        bu4.config(text=txt)
        bu4.state(['disabled'])
    elif (id == 5):
        bu5.config(text=txt)
        bu5.state(['disabled'])
    elif (id == 6):
        bu6.config(text=txt)
        bu6.state(['disabled'])
    elif (id == 7):
        bu7.config(text=txt)
        bu7.state(['disabled'])
    elif (id == 8):
        bu8.config(text=txt)
        bu8.state(['disabled'])
    elif (id == 9):
        bu9.config(text=txt)
        bu9.state(['disabled'])



def CheckWinner():
    Winner=0

    if((1 in p1) and (2 in p1) and 3 in p1):
        Winner=1;
    if((1 in p2) and (2 in p2) and 3 in p2):
        Winner=2

    if((4 in p1) and (5 in p1) and 6 in p1):
        Winner=1;
    if((4 in p2) and (5 in p2) and 6 in p2):
        Winner=2

    if((7 in p1) and (8 in p1) and 9 in p1):
        Winner=1;
    if((7 in p2) and (8 in p2) and 9 in p2):
        Winner=2

    if((1 in p1) and (4 in p1) and 7 in p1):
        Winner=1;
    if((1 in p2) and (4 in p2) and 7 in p2):
        Winner=2

    if((2 in p1) and (5 in p1) and 8 in p1):
        Winner=1;
    if((2 in p2) and (5 in p2) and 8 in p2):
        Winner=2

    if((3 in p1) and (6 in p1) and 9 in p1):
        Winner=1;
    if((3 in p2) and (6 in p2) and 9 in p2):
        Winner=2

    if((1 in p1) and (5 in p1) and 9 in p1):
        Winner=1;
    if((1 in p2) and (5 in p2) and 9 in p2):
        Winner=2

    if((3 in p1) and (5 in p1) and 7 in p1):
        Winner=1;
    if((3 in p2) and (5 in p2) and 7 in p2):
        Winner=2


    if(Winner==1):
        messagebox.showinfo('Congratulation!' , 'Player 1 is Winner')
    if(Winner==2):
        messagebox.showinfo('Congratulation!' , 'Player 2 is Winner')



def AutoPlay():
    global p1
    global p2
    EmptyCell=[]
    for cell in range(9):
        if(not((cell+1 in p1) or (cell+1 in p2))):
            EmptyCell.append(cell+1)
    RanIndex=randint(0 , len(EmptyCell)-1)
    BuClick(EmptyCell[RanIndex])


root.mainloop()

