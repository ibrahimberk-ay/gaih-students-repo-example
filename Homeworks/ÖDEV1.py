#Generating a 3x3 matrix with 9 random prime numbers.
"""Öncelikle matrisi oluşruturcak listelerimi oluşturuyorum."""
listx = []
listy = []
listz = []
"""Sonrasında her bir liste için 3 adımlık for döngüsü oluşturuyorum ki 3*3'lük matris oluşturacak eleman girebileyim"""
for i in range(3):
    a = int(input("Bir sayi giriniz: "))
    listx.append(a)
for j in range(3):
    b = int(input("Bir sayi giriniz: "))
    listy.append(b)
for k in range(3):
    c = int(input("Bir sayi giriniz: "))
    listz.append(c)
end_list = list(zip(listx, listy, listz))  # Burada oluşacak matris için bir değişken tanımlıyorum.
print("Matrisiniz: ", end_list)
input('Cikmak icin ENTER tusuna basiniz.')
# Programın .py dosyasının çalışması durumunda işlem bittikten sonra direkt kapanmaması için sona böyle bir şey ekledim.
