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
    for key, value in market.items():
        print(key, value) #daha estetik durması için ayarlama yap

#delete a product
def delete_product(product):
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