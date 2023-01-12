# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 14:40:52 2023

@author: Sümeyra Nihal GELMEZ
"""
import sqlite3
conn = sqlite3.connect('users.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS users(name TEXT, age INTEGER)''')
conn.commit()
conn.close()


conn = sqlite3.connect('users.db')
c = conn.cursor()
name = "urun_ekle"
number = 20
c.execute("INSERT INTO users VALUES (?, ?)", (name, number))

conn.commit()
conn.close()



users = [
   ("elma", 10),
   ("armut", 21),
   ("şeftali", 11)
   
   
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.executemany("INSERT INTO users VALUES (?, ?)", users)

conn.commit()
conn.close()   

conn = sqlite3.connect('users.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM users'):
   print(row)

names = [row[0] for row in c.execute('SELECT * FROM users')]
number = [row[1] for row in c.execute('SELECT * FROM users')]

combined = [f"Name: {row[0]} - Age: {row[1]}" for row in c.execute('SELECT * FROM users')]

print(names, ages)

print(combined)

conn.close()

conn = sqlite3.connect('users.db')
c = conn.cursor()
result = c.execute("SELECT * FROM users")
print(result.fetchall())
conn.close()
























from abc import ABC, abstractmethod
class Urun(ABC):
	@abstractmethod
	def urun_ekle(self):
		pass
	@abstractmethod
	def fiyat_hesapla(self):
		pass
    def urun_listele(self):
        pass
    


def fiyat_hesapla(x) -> int:
toplam = 0
if x == 1:
for i in urun_liste[1:]:
toplam += int(i[2])
elif x == 2:
for i in urun_liste[1:]:
toplam += int(i[3])
return toplam


def urun_ekle():
ad = input('ÜRÜN ADI GİRİNİZ: ')
adet = input('ÜRÜN ADEDİ GİRİNİZ: ')
fiyat = input('ÜRÜN FİYATI GİRİNİZ: ')
urun = [f'{len(urun_liste)}.', ad, adet, fiyat]
urun_liste.append(urun)
kontrol = input("ÜRÜN EKLENDİ. TEKRAR EKLEMEK İÇİN D'YE ÇIKIŞ İÇİN Ç'YE BASINIZ.")
if kontrol.lower() == "d":
pass
elif kontrol.lower() == "ç":
exit()
else:
print('Hatalı girdi. Programdan çıkılıyor.')
exit()


def urun_listele():
sutun_genislik = max(len(eleman) for urun in urun_liste for eleman in urun)
for urun in urun_liste:
index = urun_liste.index(urun)
if index == 0:
print()
urun_txt = "".join(eleman.ljust(sutun_genislik) for eleman in urun)
print(urun_txt)
print(f'TOPLAM ÜRÜN ADEDİ: {topla(1)}')
print(f'TOPLAM TUTAR: {topla(2)}')


def main():
secenek = input("ÜRÜN KAYIT İÇİN 1'E, ÜRÜNLERİ LİSTELEMEK İÇİN 2'YE, ÇIKIŞ İÇİN Ç'YE BASINIZ.")
if secenek == "1":
urun_ekle()
elif secenek == "2":
urun_listele()
elif secenek.lower() == "ç":
exit()
else:
print('Hatalı girdi. Tekrar deneyin.')
return main()
