def menu():
    print("\n--- ALIŞVERİŞ SEPETİ ---")
    print("1 - Ürün Ekle")
    print("2 - Sepeti Göster")
    print("3 - Ürün Sil")
    print("4 - Toplam Tutar")
    print("5 - Çıkış")


sepet = []


def urun_ekle():
    isim = input("Ürün adı: ")
    fiyat = float(input("Fiyat: "))
    adet = int(input("Adet: "))

    sepet.append({
        "isim": isim,
        "fiyat": fiyat,
        "adet": adet
    })
    print(f"{isim} sepete eklendi.")


def sepeti_goster():
    if not sepet:
        print("Sepet boş.")
        return

    print("\n--- SEPETTEKİ ÜRÜNLER ---")
    for i, urun in enumerate(sepet):
        print(f"{i + 1}. {urun['isim']} - {urun['adet']} adet - {urun['fiyat']} TL")


def urun_sil():
    sepeti_goster()
    if not sepet:
        return

    secim = int(input("Silmek istediğiniz ürün numarası: ")) - 1
    if 0 <= secim < len(sepet):
        silinen = sepet.pop(secim)
        print(f"{silinen['isim']} sepetten silindi.")
    else:
        print("Geçersiz seçim.")


def toplam_tutar():
    toplam = sum(urun["fiyat"] * urun["adet"] for urun in sepet)
    print(f"Toplam Tutar: {toplam} TL")


while True:
    menu()
    secim = input("Seçiminiz: ")

    if secim == "1":
        urun_ekle()
    elif secim == "2":
        sepeti_goster()
    elif secim == "3":
        urun_sil()
    elif secim == "4":
        toplam_tutar()
    elif secim == "5":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim.")
