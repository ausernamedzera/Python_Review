# empty dictionary

market = {
    "Fruit": "Price",
    "Strawberry": 13.4
}

#adding new products
def add_product(product, p_value):
    #value must be checked, value must be "float"
    try:
        if not float(p_value):
            print("Please enter a valid price")
            return False
        else:
            market[product] = float(p_value)
            return True
    except ValueError:
        print("Please enter a valid price, val err")
        return False

#show the market's products
def show_products():
    """
    Uzun yol
    #for key, value in market.items():
     #   print(key, value) #daha estetik durması için ayarlama yap
    max_key = ""
    for key in market.keys():
        if len(key) > len(max_key):
            max_key = key #en uzun lenght i bul.
    """
    #kısa yoldan hizalama
    max_len = len(max(market.keys(), key=len))
    for key, value in market.items():
        print(f"{key:<{max_len+1}}| {value} TL")


#delete a product
def delete_product(product):
    #var mı yok mu?
    #var
        #sil, return true
    #yok
        #ürün yok return false
    pass

#total
def total():
    pass

#quit belki bunu fonksiyon olarak yazmam henüz bilmiyorum
def close_market():
    return False

def greeting():
    pass

def main():
    pass


#add_product("Fruit", 13)
add_product("Strawberry", "1.34")
show_products()