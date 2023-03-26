from tkinter import *
from tkinter.messagebox import showinfo
import random
from PIL import Image,ImageTk

def input_verify(a,b):
    global BD,BN,bnl
    BD=int(a)
    BN=int(b)
    
    if BD<=0.0 or BD>10:   
        showinfo("Error!","The given board dimensions is unfeasible!")
        Boarddimensionentry.delete(0,END)
        
    elif BN<=0.0 or BN>(BD**2-1):
        showinfo("Error!","The given number of mines is impossible to plant!")
        Bombnumberentry.delete(0,END)

    else:
        for i in range(BN):
            bnl.append(random.randrange(BD**2))
        print(bnl)
        frame1.pack_forget()
        f2()

def check(a):
    global bnl,lb,MineIMG
    if a in bnl:
        lb[a-1].config(image=MineIMG)
        showinfo("Game Over!","You dug a MINE! \n So the game is Over!")
        win.destroy()
    else:
        n=random.randrange(1,3)
        lb[a-1].config(text=n,fg="blue" if n==1 else "green")

win=Tk()
win.title("Minesweeper")
frame1=Frame(win)

Namelabel=Label(frame1,text="Please enter your name:")
Nameentry=Entry(frame1,width=20)
Namelabel.pack()
Nameentry.pack()

Boarddimensionlabel=Label(frame1,text="Enter the board dimension between 1 and 10:")
Boarddimensionentry=Entry(frame1,text="1")
Boarddimensionlabel.pack()
Boarddimensionentry.pack()

Bombnumberlabel=Label(frame1,text="Enter the number of bombs to be in the game:")
Bombnumberentry=Entry(frame1,text="5")
Bombnumberlabel.pack()
Bombnumberentry.pack()

BD,BN=0,0

MineIMG=ImageTk.PhotoImage(Image.open("minesweeperIMG.jpg"))

Startgamebutton=Button(frame1,text="Start Game",command=lambda:input_verify(Boarddimensionentry.get(),Bombnumberentry.get()))
Startgamebutton.pack()

bnl=[]
lb=[]

frame1.pack()

def f2():
    global lb
    frame2=Frame(win)

    b1=Button(frame2,height=1,width=2,command=lambda:check(1))
    b2=Button(frame2,height=1,width=2,command=lambda:check(2))
    b3=Button(frame2,height=1,width=2,command=lambda:check(3))
    b4=Button(frame2,height=1,width=2,command=lambda:check(4))
    b5=Button(frame2,height=1,width=2,command=lambda:check(5))
    b6=Button(frame2,height=1,width=2,command=lambda:check(6))
    b7=Button(frame2,height=1,width=2,command=lambda:check(7))
    b8=Button(frame2,height=1,width=2,command=lambda:check(8))#1
    b9=Button(frame2,height=1,width=2,command=lambda:check(9))
    b10=Button(frame2,height=1,width=2,command=lambda:check(10))

    b11=Button(frame2,height=1,width=2,command=lambda:check(11))
    b12=Button(frame2,height=1,width=2,command=lambda:check(12))
    b13=Button(frame2,height=1,width=2,command=lambda:check(13))#2
    b14=Button(frame2,height=1,width=2,command=lambda:check(14))
    b15=Button(frame2,height=1,width=2,command=lambda:check(15))
    b16=Button(frame2,height=1,width=2,command=lambda:check(16))
    b17=Button(frame2,height=1,width=2,command=lambda:check(17))
    b18=Button(frame2,height=1,width=2,command=lambda:check(18))
    b19=Button(frame2,height=1,width=2,command=lambda:check(19))
    b20=Button(frame2,height=1,width=2,command=lambda:check(20))

    b21=Button(frame2,height=1,width=2,command=lambda:check(21))
    b22=Button(frame2,height=1,width=2,command=lambda:check(22))
    b23=Button(frame2,height=1,width=2,command=lambda:check(23))
    b24=Button(frame2,height=1,width=2,command=lambda:check(24))#3
    b25=Button(frame2,height=1,width=2,command=lambda:check(25))
    b26=Button(frame2,height=1,width=2,command=lambda:check(26))
    b27=Button(frame2,height=1,width=2,command=lambda:check(27))
    b28=Button(frame2,height=1,width=2,command=lambda:check(28))
    b29=Button(frame2,height=1,width=2,command=lambda:check(29))
    b30=Button(frame2,height=1,width=2,command=lambda:check(30))

    b31=Button(frame2,height=1,width=2,command=lambda:check(31))
    b32=Button(frame2,height=1,width=2,command=lambda:check(32))
    b33=Button(frame2,height=1,width=2,command=lambda:check(33))
    b34=Button(frame2,height=1,width=2,command=lambda:check(34))#4
    b35=Button(frame2,height=1,width=2,command=lambda:check(35))
    b36=Button(frame2,height=1,width=2,command=lambda:check(36))
    b37=Button(frame2,height=1,width=2,command=lambda:check(37))
    b38=Button(frame2,height=1,width=2,command=lambda:check(38))
    b39=Button(frame2,height=1,width=2,command=lambda:check(39))
    b40=Button(frame2,height=1,width=2,command=lambda:check(40))

    b41=Button(frame2,height=1,width=2,command=lambda:check(41))
    b42=Button(frame2,height=1,width=2,command=lambda:check(42))
    b43=Button(frame2,height=1,width=2,command=lambda:check(43))
    b44=Button(frame2,height=1,width=2,command=lambda:check(44))
    b45=Button(frame2,height=1,width=2,command=lambda:check(45))
    b46=Button(frame2,height=1,width=2,command=lambda:check(46))
    b47=Button(frame2,height=1,width=2,command=lambda:check(47))#5
    b48=Button(frame2,height=1,width=2,command=lambda:check(48))
    b49=Button(frame2,height=1,width=2,command=lambda:check(49))
    b50=Button(frame2,height=1,width=2,command=lambda:check(50))

    b51=Button(frame2,height=1,width=2,command=lambda:check(51))
    b52=Button(frame2,height=1,width=2,command=lambda:check(52))
    b53=Button(frame2,height=1,width=2,command=lambda:check(53))
    b54=Button(frame2,height=1,width=2,command=lambda:check(54))
    b55=Button(frame2,height=1,width=2,command=lambda:check(55))
    b56=Button(frame2,height=1,width=2,command=lambda:check(56))#6
    b57=Button(frame2,height=1,width=2,command=lambda:check(57))
    b58=Button(frame2,height=1,width=2,command=lambda:check(58))
    b59=Button(frame2,height=1,width=2,command=lambda:check(59))
    b60=Button(frame2,height=1,width=2,command=lambda:check(60))

    b61=Button(frame2,height=1,width=2,command=lambda:check(61))
    b62=Button(frame2,height=1,width=2,command=lambda:check(62))
    b63=Button(frame2,height=1,width=2,command=lambda:check(63))
    b64=Button(frame2,height=1,width=2,command=lambda:check(64))
    b65=Button(frame2,height=1,width=2,command=lambda:check(65))
    b66=Button(frame2,height=1,width=2,command=lambda:check(66))#7
    b67=Button(frame2,height=1,width=2,command=lambda:check(67))
    b68=Button(frame2,height=1,width=2,command=lambda:check(68))
    b69=Button(frame2,height=1,width=2,command=lambda:check(69))
    b70=Button(frame2,height=1,width=2,command=lambda:check(70))

    b71=Button(frame2,height=1,width=2,command=lambda:check(71))
    b72=Button(frame2,height=1,width=2,command=lambda:check(72))
    b73=Button(frame2,height=1,width=2,command=lambda:check(73))
    b74=Button(frame2,height=1,width=2,command=lambda:check(74))
    b75=Button(frame2,height=1,width=2,command=lambda:check(75))#8
    b76=Button(frame2,height=1,width=2,command=lambda:check(76))
    b77=Button(frame2,height=1,width=2,command=lambda:check(77))
    b78=Button(frame2,height=1,width=2,command=lambda:check(78))
    b79=Button(frame2,height=1,width=2,command=lambda:check(79))
    b80=Button(frame2,height=1,width=2,command=lambda:check(80))

    b81=Button(frame2,height=1,width=2,command=lambda:check(81))
    b82=Button(frame2,height=1,width=2,command=lambda:check(82))
    b83=Button(frame2,height=1,width=2,command=lambda:check(83))
    b84=Button(frame2,height=1,width=2,command=lambda:check(84))
    b85=Button(frame2,height=1,width=2,command=lambda:check(85))
    b86=Button(frame2,height=1,width=2,command=lambda:check(86))
    b87=Button(frame2,height=1,width=2,command=lambda:check(87))#9
    b88=Button(frame2,height=1,width=2,command=lambda:check(88))
    b89=Button(frame2,height=1,width=2,command=lambda:check(89))
    b90=Button(frame2,height=1,width=2,command=lambda:check(90))

    b91=Button(frame2,height=1,width=2,command=lambda:check(91))
    b92=Button(frame2,height=1,width=2,command=lambda:check(92))
    b93=Button(frame2,height=1,width=2,command=lambda:check(93))
    b94=Button(frame2,height=1,width=2,command=lambda:check(94))
    b95=Button(frame2,height=1,width=2,command=lambda:check(95))
    b96=Button(frame2,height=1,width=2,command=lambda:check(96))#10
    b97=Button(frame2,height=1,width=2,command=lambda:check(97))
    b98=Button(frame2,height=1,width=2,command=lambda:check(98))
    b99=Button(frame2,height=1,width=2,command=lambda:check(99))
    b100=Button(frame2,height=1,width=2,command=lambda:check(100))

    lb=[b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,b32,b33,b34,b35,b36,b37,b38,b39,b40,
        b41,b42,b43,b44,b45,b46,b47,b48,b49,b50,b51,b52,b53,b54,b55,b56,b57,b58,b59,b60,b61,b62,b63,b64,b65,b66,b67,b68,b69,b70,b71,b72,b73,b74,b75,b76,b77,b78,b79,b80,
        b81,b82,b83,b84,b85,b86,b87,b88,b89,b90,b91,b92,b93,b94,b95,b96,b97,b98,b99,b100] #putting buttons in a list to reduce code size and complexity
    counter=0
    for i in range(BD):
        for j in range(BD):
            lb[counter].grid(column=i,row=j)
            counter+=1
    frame2.pack()
    
    win.mainloop()
