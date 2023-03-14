from tkinter import*
import tkinter.font as font
import math

root = Tk()
root.title("Kalkulator")
root["bg"] = "#F1DEC9"
root.geometry("320x400")

myfont  = font.Font(size=15)

e = Entry(root,width=25,borderwidth=0)
e["font"]= myfont
e["bg"] = "#F1DEC9"
e.grid(row = 0,columnspan=4,pady=20,padx=20)


def cetak(nilai):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(nilai))
def tambah():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "penjumlahan"
    n_awal = float(nomor_awal)
    e.delete(0,END)
def kurang():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "pengurangan"
    n_awal = float(nomor_awal)
    e.delete(0,END)
def bagi():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "pembagian"
    n_awal = float(nomor_awal)
    e.delete(0,END)
def kali():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "perkalian"
    n_awal = float(nomor_awal)
    e.delete(0,END)

def desimal():
    current = e.get() 
    if '.' not in current:
        e.insert(END, '.')

def delete_one():
    current = e.get()
    e.delete(len(current) - 1, END)

def pangkat():
    nomor_awal = e.get()
    global n_awal
    n_awal = float(nomor_awal)
    e.delete(0,END)
    e.insert(0,n_awal **2)

def hapus():
    e.delete(0,END)
def samadengan():
    nomor_akhir = e.get()
    e.delete(0,END)
    if mtk == "penjumlahan":
        hitung = n_awal + float(nomor_akhir)
        hasil = round(hitung, 5)
        e.insert(0, hasil)
    elif mtk == "pengurangan":
        hitung = n_awal + float(nomor_akhir)
        hasil = round(hitung, 5)
        e.insert(0, hasil)
    elif mtk == "pembagian":
        try:
            hitung = n_awal / float(nomor_akhir)
            e.insert(0,hitung)
        except ZeroDivisionError:
            e.insert(0,"maaf komputer tidak bisa")
            
    elif mtk == "perkalian":
        e.insert(0,n_awal * int(nomor_akhir))
    elif mtk == "desimal":
        e.insert(0,n_awal . int(nomor_akhir))
    
# the UI buton 
btn  = Button(root,text="1",padx = 30,bg="#C8B6A6",fg="white", pady = 20,command=lambda:cetak(1))
btn2  = Button(root,text="2",padx = 30,bg="#C8B6A6",fg="white", pady = 20,command=lambda:cetak(2))
btn3  = Button(root,text="3",padx = 30,bg="#C8B6A6",fg="white", pady = 20,command=lambda:cetak(3))
btn4  = Button(root,text="4",padx = 30,bg="#C8B6A6",fg="white", pady = 20,command=lambda:cetak(4))
btn5 = Button(root,text="5",padx = 30,bg="#C8B6A6",fg="white", pady = 20,command=lambda:cetak(5))
btn6  = Button(root,text="6",padx = 30,bg="#C8B6A6",fg="white", pady = 20,command=lambda:cetak(6))
btn7  = Button(root,text="7",padx = 30,bg="#C8B6A6",fg="white", pady = 20,command=lambda:cetak(7))
btn8  = Button(root,text="8",padx = 30,bg="#C8B6A6",fg="white", pady = 20,command=lambda:cetak(8))
btn9  = Button(root,text="9",padx = 30,bg="#C8B6A6",fg="white", pady = 20,command=lambda:cetak(9))
btn0  = Button(root,text="0",padx = 30,bg="#C8B6A6",fg="white", pady = 20,command=lambda:cetak(0))
tam = Button(root,text="+",padx = 28,bg="#C8B6A6",fg="white", pady = 20,command=tambah)
kur = Button(root,text="-",padx = 30,bg="#C8B6A6",fg="white", pady = 20,command=kurang)
bag  = Button(root,text=":",padx = 31,bg="#C8B6A6",fg="white", pady = 20,command=bagi)
kal = Button(root,text="x",padx = 30,bg="#C8B6A6",fg="white", pady = 20,command=kali)
pang = Button(root,text="x2",padx = 27,bg="#C8B6A6",fg="white", pady = 20,command=pangkat)
btn_del = Button(root, text="DEL", padx=25, bg="#C8B6A6", fg="white", pady=20, command=delete_one)
dec = Button(root,text=".",padx = 30,bg="#C8B6A6",fg="white", pady = 20,command=desimal)
hap = Button(root,text="C",padx = 30,bg="#8D7B68",fg="white", pady = 20,command=hapus)
equal = Button(root,text="=",padx = 68,bg="#8D7B68", fg="white", pady = 20,command=samadengan)

# Button location
btn.grid(row=3,column=0,pady=2)
btn2.grid(row=3,column=1,pady=2)
btn3.grid(row=3,column=2,pady=2)
btn4.grid(row=2,column=0,pady=2)
btn5.grid(row=2,column=1,pady=2)
btn6.grid(row=2,column=2,pady=2)
btn7.grid(row=1,column=0,pady=2)
btn8.grid(row=1,column=1,pady=2)
btn9.grid(row=1,column=2,pady=2)
btn0.grid(row=4,column=1,pady=2) 
tam.grid(row=1,column=3,pady=2)
kur.grid(row=2,column=3,pady=2)
bag.grid(row=3,column=3,pady=2)
kal.grid(row=4,column=3,pady=2)
hap.grid(row=4,column=0,pady=2)
equal.grid(row=5,column=2,columnspan=2)
pang.grid(row =5,column=0,pady=2)
btn_del.grid(row =5,column=1,pady=2)
dec.grid(row =4,column=2,pady=2)



root.mainloop()