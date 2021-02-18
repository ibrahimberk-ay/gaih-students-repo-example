# Write a program that includes information about the grades of 5 students in a school.
AdSoyad = []
for j in range(5):  # 5 öğrencinin isimleri için bir değişken tanımlayıp 5 seferlik bir döngüye soktum.
    a = input("Ad Soyad Giriniz: ")
    AdSoyad.append(a)  # Her girilen a değerini AdSoyad listesine yazdırdım.
AdSoyad.sort()      # AdSoyad listesini alfabetik sıraya göre sıralattım.
"""Vize, Final ve Odev olarak 3 sözlük oluşturdum sonrasında da sözlüklerin anahtar kelimelerini de alfabetik sıraya 
soktuğum isimlerden aldım."""
Vize = {}
Final = {}
Odev = {}
input("Vize notları girilecek devam etmek için ENTER tuşuna basın")
for i in AdSoyad:
    Vize[i] = int(input("%s Kişisinin Vize Notu: " % i))
input("Final notları girilecek devam etmek için ENTER tuşuna basın")
for k in AdSoyad:
    Final[k] = int(input("%s Kişisinin Final Notu: " % k))
input("Ödev notları girilecek devam etmek için ENTER tuşuna basın")
for t in AdSoyad:
    Odev[t] = int(input("%s Kişisinin Ödev Notu: " % t))
info = {}
for x in AdSoyad:
    info[x] = Vize[x], Final[x], Odev[x]
print(info)
Ortalama = {}
for y in AdSoyad:
    Ortalama[y] = (Vize[y]+Final[y]+Odev[y])/3
print(Ortalama)
"""Sözlüğü kalıcı sıraya sokamadığım için bir liste oluşturdum (OrtalamaSiralama) ve listeyi Ortalama adlı sözlüğün değ-
erlerinin sıralanmış haline eşitledim."""
OrtalamaSiralama = sorted(Ortalama.values())
for y3 in Ortalama.keys():
    if OrtalamaSiralama[-1] == Ortalama[y3]:
        print("Tebrikler %s" % y3)
"""Burada da oluşturduğum listenin en büyük değeri, Ortalama sözlüğündeki y3 anahtarının değerine ulaşana kadar for dön-
güsüne soktum."""
input('Cikmak icin ENTER tusuna basiniz.')
