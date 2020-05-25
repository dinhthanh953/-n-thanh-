from tkinter import *
from tkinter import messagebox
import random
# khoi tao so luot doan va chon ngau nhien so de doan
luot_doan=5
so = random.randint(1,20)
# tao ham de choi lai
def restart():
    global luot_doan,so
    luot_doan=5
    so = random.randint(1,20)
#ham de kiem tra so
def kiem_tra_so():
    global luot_doan,so 
    name=ten.get()
    name=str(name)
    a=so_doan.get()
    a=int(a)
    if 0<luot_doan:
        if a==so:
            messagebox.showinfo('ketqua',name+' doan dung roi!so do la:  '+str(so))
            return 
        else:
            if a<so:
                messagebox.showinfo('ketqua',name+' doan sai roi. Con so to dang nghi lon hon so cua ban')
            else:
                messagebox.showinfo('ketqua',name+' doan sai roi. Con so to dang nghi nho hon so cua ban')
    luot_doan=luot_doan-1

    if luot_doan==0:
        messagebox.showinfo('ketqua',name+' doan doan het luot roi!so do la:  '+str(so))
#khoi tao khung giao dien 
game=Tk()
game.geometry("400x300+200+200")
game.title('game doan so')
#tao label gioi thieu tro choi
lb=Label(game,text='minh nghi mot con so tu 1 den 20,ban co 5 luot de doan')
lb.pack()
#tao label va entry de lay ten nguoi choi
lbten=Label(game,text='nhap ten')
lbten.pack()
ten=Entry(game)
ten.pack()
#tao label va entry de lay so doan
lbso=Label(game,text='moi ban doan')
lbso.pack()
so_doan=Entry(game)
so_doan.pack()
#tao button de kiem tra so doan
kiem_tra=Button(game,text='kiem tra',command=kiem_tra_so)
kiem_tra.pack()
#tao button de choi lai
choi_lai=Button(game,text='choi lai',command=restart)
choi_lai.pack()

game.mainloop()
