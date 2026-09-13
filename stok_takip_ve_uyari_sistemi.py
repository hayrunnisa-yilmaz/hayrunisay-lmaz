urunler = []

for i in range(3):
    print(f"{i+1}. Ürün Bilgilerini Girin:")
    ad = input("Ürün Adı: ")
    fiyat = float(input("Fiyatı: "))
    stok = int(input("Stok Sayısı: "))
    

    yeni_urun = {"ad": ad, "fiyat": fiyat, "stok": stok}
    urunler.append(yeni_urun)

print("\n--- Ürün Listesi ---")

for urun in urunler:
    print(f"Ad: {urun['ad']}, Fiyat: {urun['fiyat']}, Stok: {urun['stok']}")

print("\n--- Kritik Stok Uyarıları ---")

for urun in urunler:
    if urun["stok"] < 5:
        print(f"Kritik stok uyarısı: {urun['ad']} (Kalan: {urun['stok']})")

print("\n--- Toplam Stok Değeri ---")

toplam_deger = 0
for urun in urunler:
    toplam_deger += urun["fiyat"] * urun["stok"]

print(f"Toplam değer: {toplam_deger}")
