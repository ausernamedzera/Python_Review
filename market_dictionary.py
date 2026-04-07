# empty dictionary
market = {
    "Fruit": "Price",
    "Strawberry": 13.4
}
print(len(market))


#adding new products
def add_product(product, value):
    market[product] = value

#show the market's products
def show_products():
    for key, value in market.items():
        print(key, value)

#delete a product
def delete_product(product):
    pass

#total
def total(product):
    pass

#quit belki bunu fonksiyon olarak yazmam henüz bilmiyorum
def close_market():
    pass
