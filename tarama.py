import os
global arr
dosyayolu=""
for root,dirs,files in os.walk('C:\\'): # walk fonksiyonu ile istedigimiz kalsorlerde tarama
    for file in files:
        if file.endswith(".docx"): #uzantisi istenen dosyayi bulma
            #print(os.path.join(root,file))
            asd=os.path.join(root,file) #bulunan dosyanin yolunun kaydi yapildi
            dosyayolu+=asd+","

arr=dosyayolu.split(",") #kayit yapilan string listeye atildi
for a in range(0,len(arr)-1):
    arr[a] = arr[a].lstrip() #olusabilecek bosluklar silindi
    print(arr[a])