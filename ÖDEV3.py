#ad-soyad: Hayrunnisa Yılmaz
#öğrenci numarası: 300125002

def kural_uzunluk(sifre):
    """En az 8 karakter kontrolü"""
    return len(sifre) >= 8

def kural_buyuk(sifre):
    """En az 1 büyük harf (isupper) kontrolü"""
    for karakter in sifre:
        if karakter.isupper():
            return True
    return False

def kural_kucuk(sifre):
    """En az 1 küçük harf (islower) kontrolü"""
    for karakter in sifre:
        if karakter.islower():
            return True
    return False

def kural_rakam(sifre):
    """En az 1 rakam (isdigit) kontrolü"""
    for karakter in sifre:
        if karakter.isdigit():
            return True
    return False

def sifre_kontrol(sifre):
    """Eksik kuralları bir liste olarak toplar ve döndürür."""
    eksikler = []
    
    if kural_uzunluk(sifre) == False:
        eksikler.append("En az 8 karakter olmalı")
    
    if kural_buyuk(sifre) == False:
        eksikler.append("En az 1 büyük harf içermeli")
        
    if kural_kucuk(sifre) == False:
        eksikler.append("En az 1 küçük harf içermeli")
        
    if kural_rakam(sifre) == False:
        eksikler.append("En az 1 rakam içermeli")
        
    return eksikler


girilen_sifre = input("Şifrenizi girin: ")

hatalar = sifre_kontrol(girilen_sifre)

if not hatalar: 
    print("Şifre Geçerli")
else:           
    print("Geçerli Değil")
    print("Eksik kurallar:", hatalar)