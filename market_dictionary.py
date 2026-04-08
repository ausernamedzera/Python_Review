# empty dictionary
market = {
    "Fruit": "Price",
    "Strawberry": 13.4
}

#adding new products
def add_product(product, value):
    #value must be checked, value must be int
    market[product] = value

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