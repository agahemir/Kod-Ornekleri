sayi = int(input("Sayının Başlangıcını Girin: ")) #Başlangıç Sayısı Girdi Olarak Alınıyor
kadar = int(input("Sayının Bitişini Girin: ")) #Bitiş Sayısı Girdi Olarak Alınıyor
adim = int(input("Adım Noktasını Girin: ")) #Adım Sayısı Girdi Olarak Alınıyor
for i in range(sayi,kadar,adim): #Belirtilen Girdilere Göre For Döngüsü ve Range Deyimi Kullanılarak Verilen Girdiye Göre Başlangıç Bitiş Adım Sayıları Belirleniyor.
    print(i) #Çıktı Verme
