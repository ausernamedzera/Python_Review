shopping_list = []
def take_item():
    item = input("Welcome to your Shopping List Add item in it:").capitalize()
    return item

def item_control(item):
    if item in shopping_list:
        print("Item Already Exists")
        return False
    elif item not in shopping_list:
        print(f"the {item} is not in your Shopping List. delete failed")


def add_item(item):
    if item_type(item):
        if item in shopping_list:
            print("Item Already Exists")
            return False
            # item listede varsa looptan bir daha istemesi lazım.
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


def greeting():
    print("=== Shopping List ===")
    answer = input("Commands: 1-Show your list, 2-Add your list, 3-Delete from the list, 4-Quit: ")
    #answering type'ı string olmalı
    if answer == "1":
        return True
    elif answer == "2":
        shopping_item = take_item()
        add_item(shopping_item)
        yes_no = input("Item Added \n do you want to add another item?")
        if yes_no == "yes":
            return True
        else:
            return False
    else:
        print("Item is not valid")
        return False

def main():
    while True:
        if not greeting():
            break


main()