karakterler = [
    {"isim": "Aragorn", "sinif": "savasci", "seviye": 15, "hp": 220, "altin": 500},
    {"isim": "Gandalf", "sinif": "buyucu", "seviye": 20, "hp": 140, "altin": 300},
    {"isim": "Legolas", "sinif": "okcu", "seviye": 12, "hp": 160, "altin": 550},
    {"isim": "Gimli", "sinif": "savasci", "seviye": 10, "hp": 200, "altin": 600},
    {"isim": "Thranduil", "sinif": "okcu", "seviye": 14, "hp": 175, "altin": 900},
    {"isim": "Saruman", "sinif": "buyucu", "seviye": 18, "hp": 130, "altin": 800}
]

okcu_mu = lambda k: k["sinif"] == "okcu"

guclu_mu = lambda k: k["seviye"] > 10 and k["hp"] > 150

seviye_listesi = [k["isim"] for k in karakterler if k["seviye"] > 15]

zenginlik_listesi = [(k["isim"], "zengin" if k["altin"] > 500 else "fakir") for k in karakterler]

print("Seviyesi 15'ten büyük karakterler:")
print(seviye_listesi)

print("\nKarakterlerin zenginlik durumu:")
print(zenginlik_listesi)

print("\nKarakter Güç ve Sınıf Kontrolü:")

for k in karakterler:
    print(k["isim"], "Okçu mu?:", okcu_mu(k), "| Güçlü mü?:", guclu_mu(k))
