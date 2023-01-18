#key olusturma
from cryptography.fernet import Fernet

anahtar= Fernet.generate_key() #sifrelemek ve sifreyi acmak icin kullanilan anahtar uretımı

with open("Gizlianahtar.key","wb") as file:#anahtarin kayit edilmesi
    file.write(anahtar)