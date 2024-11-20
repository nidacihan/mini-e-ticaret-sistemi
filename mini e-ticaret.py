#mini e-ticaret

products = {
    "T-shirt": 200,
    "jean": 500,
    "elbise":600,
    "ceket":1000,
    "ayakkabı":1200,
}

cart = {}

def show_products():

    print("\n=== Mevcut Ürünler ===")
    for product, price in products.items():
        print(f"{product}: {price} TL")

def add_to_cart(product_name, quantity):
            if product_name in products:
                if product_name in cart:
                    cart[product_name] += quantity
                else:
                    cart[product_name] = quantity
                    print(f"{quantity} adet {product_name} sepete eklendi.")
            else:
                    print(f"Hata: {product_name} mevcut bir ürün değil.")
def remove_from_cart(product_name):
    if product_name in cart:
        try:
            quantity = int(input(f"kaç adet {product_name} sepetten çıkartmak istiyorsunuz?"))
            if quantity >= cart[product_name]:
                del cart[product_name]
                print(f"{product_name} tamamen sepetten çıkartıldı.")
            else:
                cart[product_name] -= quantity
                print(f"{quantity} adet {product_name} sepetten çıkartıldı. Kalan {product_name} sayısı: {cart[product_name]} adet.")
        except ValueError:
            print("Hata: Lütfen sayısal bir miktar girin.")
    else:
        print(f"Hata: {product_name} sepetinizde bulunmuyor.")
def calculate_total():
    total = 0
    for product, quantity in cart.items():
        total += products[product] * quantity
    return total

def show_cart():

    if cart:
        print("\n sepetiniz")
        for product, quantity in cart.items():
            print(f"{product}: {quantity} adet")

        print(f"toplam fiyat:{calculate_total()} TL")
    else:
            print("sepetiniz boş.")


def main():
        print("\n mini e_ticaret sistemi")
        print("1. Ürünleri Görüntüle")
        print("2. Sepete Ürün Ekle")
        print("3. Sepetten Ürün Çıkar")
        print("4. Sepeti Görüntüle")
        print("5. Çıkış")
        print("Menüyü tekrar görmek için 'm' yazabilirsiniz.\n")

        while True:
           choice = input("seçiminizi yapın (1-5) or 'm': ")

           if choice == "1":
               show_products()
           elif choice == "2":
               product_name = input("Eklenecek ürün adını girin: ")
               try:
                  quantity = int(input("Kaç adet eklemek istiyorsunuz?: "))
                  add_to_cart(product_name, quantity)
               except ValueError:
                  print("Hata: Lütfen sayısal bir miktar girin.")
           elif choice == "3":
               product_name = input("Çıkarılacak ürün adını girin: ")
               remove_from_cart(product_name)
           elif choice == "4":
               show_cart()
           elif choice == "5":
               print("Çıkış yapılıyor. İyi günler!")
               break
           elif choice == "m":
               print("\nMini E-Ticaret Sistemi")
               print("1. Ürünleri Görüntüle")
               print("2. Sepete Ürün Ekle")
               print("3. Sepetten Ürün Çıkar")
               print("4. Sepeti Görüntüle")
               print("5. Çıkış")
           else:
               print("Hata: Geçersiz bir seçim yaptınız.")
if __name__ == "__main__":
    main()















