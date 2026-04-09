# empty dictionary

market = {
    "Strawberry": 13.4,
    "muz" : 43
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

# find the product

def check_product(product):
    for p in market.keys():
        if p != product:
            return False
        else:
            return True

#delete a product
def delete_product(product):
    if check_product(product):
        del market[product]  #del market, dersek bütün dictionaryi silmiş oluruz TAMAMEN
        return True
    else:
        print(f"{product} is not in market. delete failed.")
        return False

#total
def total():
    sum = 0
    for value in market.values():
        sum += float(value)
    print(sum)

#quit belki bunu fonksiyon olarak yazmam henüz bilmiyorum
def close_market():
    print("Thanks For Using Our Program")
    return False

def greeting():
    print("*"*41)
    print("*GREETINGS, WELCOME TO MY MARKET CATALOG*")
    print("*"*41)

    answer = input("1-Show Catalog\n"
                   "2-Add Product\n"
                   "4-Delete Product\n"
                   "5-All Products Total Price\n"
                   "6-Quit: ")
    if answer == "1":
        print("*"*41)
        show_products()
        print("*"*41)
        while True:
            y_n = input("Do you wanna add products? Y/N: ").lower()
            if y_n == "y" or y_n == "yes":
                product_key = input("Enter product name: ")
                price_value = input("Enter product price: ")
                add_product(product_key, price_value)
            elif y_n == "n" or y_n == "no":
                return True
            else:
                print("Please enter a valid option")
                print("*"*41)




def main():
    while True:
        if not greeting():
            return False


main()