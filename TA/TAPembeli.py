from tkinter import *
from tkinter import messagebox

Win2 = Tk()
    
#1=Modul1 Variabel
#2=Modul2 Pengkondisian
#3=Modul4 Function
#4=Modul5 OOP1
#5=Modul6 OOP2
#6=Modul8 GUI

#OOP1
class harga :
    def totalpesanan():
        #variabel
        uang = int(JumPesan.J_Uang.get())
        bayam = int(JumPesan.J_bayam.get())
        kubis = int(JumPesan.J_kubis.get())
        wortel = int(JumPesan.J_wortel.get())
        sapi = int(JumPesan.J_sapi.get())
        ayam = int(JumPesan.J_ayam.get())
        udang = int(JumPesan.J_udang.get())

        totalharga = int((bayam*8000)+(kubis*8000)+(wortel*7000)+(sapi*130000)+(ayam*24000)+(udang*72000))
        totalharga_s = str(totalharga)
        
        #if-else
        if uang<totalharga:
            messagebox.showinfo("Pesanan Anda","Uang tidak Mencukupi" )
        else:
            messagebox.showinfo("Pesanan Anda","Terima kasih, Pesanan anda akan segera dikirim" + "\nTotal Harga : Rp. " +totalharga_s)
            
    def konfirmasi():
        konfirmasi = messagebox.askyesno("Quit","Apakah anda yakin akan keluar ?")
        if konfirmasi == 1:
            Win2.destroy()
        else :
            Win2.destroy()
            import TAPembeli

class visual :
    # Pengaturan Background dan icon
    Win2.title ("Toko Sayuran")
    Win2.geometry("950x720")
    Win2.iconbitmap('d:/TA/Gambar/icon.ico')
    Win2.resizable(width= 0 , height= 0)

    bg = PhotoImage(file='d:/TA/Gambar/BgSayur.png')
    Labelbg = Label(Win2, image=bg)
    Labelbg.place(x=-20,y=-50)

class NamaToko :
    Label1 = Label(Win2, text="Selamat Datang di Toko Sayur Jaya", font=("times new roman", 20))
    Label1.place(x=325,y=15)
    
class Gambar :
    fBayam= PhotoImage(file='d:/TA/Gambar/Bayam.png')
    kBayam = fBayam.subsample(2) 
    LBayam = Label(Win2, image=kBayam)
    LBayam.place(x=100,y=80)
    
    fKubis= PhotoImage(file='d:/TA/Gambar/Kol.png')
    kKubis = fKubis.subsample(1) 
    LKubis = Label(Win2, image=kKubis)
    LKubis.place(x=350,y=80)
    
    fWortel= PhotoImage(file='d:/TA/Gambar/Wortel.png')
    kWortel = fWortel.subsample(1) 
    LWortel = Label(Win2, image=kWortel)
    LWortel.place(x=650,y=80)
    
    fdSapi= PhotoImage(file='d:/TA/Gambar/dSapi.png')
    kdSapi = fdSapi.subsample(1) 
    LdSapi = Label(Win2, image=kdSapi)
    LdSapi.place(x=100,y=345)
    
    fdAyam= PhotoImage(file='d:/TA/Gambar/dAyam.png')
    kdAyam = fdAyam.subsample(1) 
    LdAyam = Label(Win2, image=kdAyam)
    LdAyam.place(x=350,y=345)
    
    fUdang= PhotoImage(file='d:/TA/Gambar/Udang.png')
    kUdang = fUdang.subsample(1) 
    LUdang = Label(Win2, image=kUdang)
    LUdang.place(x=650,y=325)
    
class JumPesan:
    J_bayam = Entry(Win2, width=15)
    J_bayam.insert(0,"0")
    J_bayam.place(x=185,y=310)

    J_kubis = Entry(Win2, width=15)
    J_kubis.place(x=450,y=310)
    J_kubis.insert(0, "0")
    
    J_wortel = Entry(Win2, width=15)
    J_wortel.place(x=720,y=310)
    J_wortel.insert(0,"0")
        
    J_sapi = Entry(Win2, width=15)
    J_sapi.place(x=185,y=590)
    J_sapi.insert(0,"0")
        
    J_ayam = Entry(Win2, width=15)
    J_ayam.place(x=450,y=590)
    J_ayam.insert(0,"0")
    
    J_udang = Entry(Win2, width=15)
    J_udang.place(x=720,y=590)
    J_udang.insert(0,"0")
    
    J_Uang = Entry(Win2, width=15)
    J_Uang.place(x=450,y=630)
    J_Uang.insert(0,"250000")
     
class L_Nama : 
    H_bayam = Label(Win2, text="Bayam", )
    H_bayam.place(x=215,y=265)
    
    H_kubis = Label(Win2, text="Kubis")
    H_kubis.place(x=480,y=265)
    
    H_wortel = Label(Win2, text="Wortel")
    H_wortel.place(x=740,y=265)
    
    H_sapi = Label(Win2, text="Daging Sapi")
    H_sapi.place(x=200,y=545)
    
    H_ayam = Label(Win2, text="Daging Ayam")
    H_ayam.place(x=460,y=545)
    
    H_udang = Label(Win2,text="Udang")
    H_udang.place(x=745,y=545)
    
    H_uang = Label(Win2,text="Uang anda :")
    H_uang.place(x=380,y=630)

class Keterangan :
    K_bayam = Label(Win2, text="800 gr/Rp. 8,000")
    K_bayam.place(x=195,y=285)
    
    K_kubis = Label(Win2, text="800 gr/Rp. 8,000")
    K_kubis.place(x=460,y=285)
    
    K_wortel = Label(Win2, text="800 gr/Rp. 7,000")
    K_wortel.place(x=720,y=285)
    
    K_sapi = Label(Win2, text="1000 gr/Rp. 130,000")
    K_sapi.place(x=180,y=565)
    
    K_ayam = Label(Win2, text="1000 gr/Rp. 24,000")
    K_ayam.place(x=440,y=565)
    
    K_udang = Label(Win2,text="1000 gr/Rp. 72,000")
    K_udang.place(x=725,y=565)   

#OOP2
class katakatabk:
    def init(self, kata = 0):
        self.katta = kata

    def setkatta(self, x):
        self.katta = x

    def getkatta(self):
        return self.katta
katakata = katakatabk()
katakata.setkatta("Rebahin Aja Biar Kita Kerja")
katakata = Label(Win2, text=katakata.getkatta())
katakata.place(x=455, y=55)

but_Pesanan= Button (Win2, text="Proses", command=harga.totalpesanan).place(x=450,y=675)
but_Quit = Button (Win2, text="Quit",command=harga.konfirmasi).place(x=800,y=675)

Win2.mainloop()