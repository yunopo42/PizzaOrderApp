import tkinter

my_window = tkinter.Tk()
my_window.geometry('500x600+400+100')
my_window.title("Pizza Sipariş Program")

#giris yazısı
baslık  = tkinter.Label(text="Pizza Siparis Programına Hosgeldiniz", fg="black", bg="#FF0000", font="Times 17 italic")
baslık.pack()


#içerik
label_ad = tkinter.Label(text="Ad-Soyad:",bg="pink",fg="black",font="Times 12 italic").place(x=10,y=40)
label_boyut = tkinter.Label(text="Boyut:",bg="pink",fg="black",font="Times 12 italic").place(x=10,y=70)
label_ic = tkinter.Label(text="İçindekiler:",bg="pink",fg="black",font="Times 12 italic").place(x=10,y=100)
label_adres = tkinter.Label(text="Adres:",bg="pink",fg="black",font="Times 12 italic").place(x=10,y=130)

#istenen bilgiler
my_name = tkinter.StringVar()
my_location = tkinter.StringVar()
ad_entry = tkinter.Entry(bg="light blue",fg="black",textvariable=my_name).place(x= 100,y=43)
adres_entry = tkinter.Entry(bg="light blue",fg="black",textvariable=my_location).place(x= 100,y=134)

boyut = tkinter.StringVar()
radbutton_kucuk = tkinter.Radiobutton(text="Küçük Boy",value="küçük boy",variable=boyut).place(x=100,y=72)
radbutton_orta = tkinter.Radiobutton(text="Orta Boy",value="orta boy",variable=boyut).place(x=180,y=72)
radbutton_buyuk = tkinter.Radiobutton(text="Büyük Boy",value="büyük boy",variable=boyut).place(x=260,y=72)


deger1 = tkinter.StringVar()
deger2 = tkinter.StringVar()
deger3 = tkinter.StringVar()
my_check_button = tkinter.Checkbutton(text="Sucuklu",variable=deger1,onvalue="Sucuklu").place(x=100,y=100)
my_check_button = tkinter.Checkbutton(text="Mantarlı",variable=deger2,onvalue="Mantarlı").place(x=180,y=100)
my_check_button = tkinter.Checkbutton(text="Zeytinli",variable=deger3,onvalue="Zeytinli").place(x=260,y=100)


def siparis_ver():
    label_ad = tkinter.Label(text="Ad-Soyad:", bg="pink", fg="black", font="Times 12 italic").place(x=10, y=250)
    label_boyut = tkinter.Label(text="Boyut:", bg="pink", fg="black", font="Times 12 italic").place(x=10, y=280)
    label_ic = tkinter.Label(text="İçindekiler:", bg="pink", fg="black", font="Times 12 italic").place(x=10, y=310)
    label_adres = tkinter.Label(text="Adres:", bg="pink", fg="black", font="Times 12 italic").place(x=10, y=340)

    label_ad1 = tkinter.Label(text=my_name.get(), fg="black", font="Times 12 italic").place(x=150, y=250)
    label_boyut1 = tkinter.Label(text=boyut.get(), fg="black", font="Times 12 italic").place(x=150, y=280)
    label_ic1 = tkinter.Label(text=deger1.get() +" "+ deger2.get() +" "+ deger3.get(), fg="black", font="Times 12 italic").place(x=150, y=310)
    label_adres1 = tkinter.Label(text=my_location.get(), fg="black", font="Times 12 italic").place(x=150, y=340)



def iptal_et():
    quit()
siparis = tkinter.Button(text="Sipariş Ver",activebackground="orange",command=siparis_ver).place(x=158,y=160)
iptal = tkinter.Button(text="İptal",activebackground="red",command=iptal_et).place(x=238,y=160)

#Sipariş bilgileri
info_label = tkinter.Label(text="Siparişiniz: ",bg="yellow",font="Times 15 italic").place(y=210)

#hesap özeti




my_window.mainloop()
