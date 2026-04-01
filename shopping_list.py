shopping_list = []
def take_item():
    item = input("Welcome to your Shopping List Add item in it:").capitalize()
    return item

def add_item(item):
    if item_type(item) == True:
        if item in shopping_list:
            print("Item Already Exists")
            return False
            # item listede varsa looptan bir daha isemesi lazım.
        else:
            shopping_list.append(item)
            return True
    else:
        print("Item is not valid")
        return False

def item_type(item):
    if type(item) == str:
        return True
    else:
        return False