import random #Rastgele değerler için random modülü import edilir.
try: #Yanlış bir değer girilmesi durumunda hata ayıklamayı sağlamak için try bloğu kullanıldı.
    aralik = int(input("Seçtiğiniz İlk Aralık Sayısını Giriniz...")) #Kullanıcıdan başlangıç aralığı girdi olarak alınır.
    aralik2 = int(input("Seçtiğiniz Son Aralık Sayısını Giriniz...")) #Kullanıcıdan bitiş aralığı girdi olarak alınır.
    tahminSayisi = random.randint(aralik,aralik2) #Kullanıcıdan alınan başlangıç ve bitiş sayılarından rastgele sayı belirlenir.
    print("Belirlediğiniz aralıktaki sayılardan biri rastgele olarak seçildi, şimdi bu sayıyı tahmin edin ve oyuna başlayın (:")
    while True: #Sonuç "true" olana kadar döngü devam eder.
        girisSayisi = int(input("Tahmin Edilen Sayı: ")) #Kullanıcıdan tahmin sayısı istenir.
        if girisSayisi < tahminSayisi: #Girilen sayıdan tahmin sayısı küçük olduğunda gerçekleşecek durum.
            print("Tuttuğunuz sayı, tahmin edilen sayıdan küçük. Tekrar deneyiniz...")
        elif girisSayisi > tahminSayisi: #Girilen sayıdan tahmin sayısı büyük olduğunda gerçekleşecek durum.
            print("Tuttuğunuz say1ı, tahmin edilen sayıdan büyük. Tekrar deneyiniz...")
        elif girisSayisi == tahminSayisi: #Girilen sayıdan tahmin sayısı eşit olduğunda gerçekleşecek durum.
            print("Tuttuğunuz sayı, tahmin edilen sayı ile aynı. Tebrikler...")
            break #Döngüden çıkılıyor...
except ValueError: #"ValueError" hatası alındığında gerçekleşecek durum.
    print("Lütfen Sayı Giriniz!")
#Geçti
