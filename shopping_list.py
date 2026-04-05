shopping_list = []

#Take Item
def take_item():
    item = input("Welcome to your Shopping List Add item in it:").capitalize()
    return item

#Control the type of item
def item_type(item):
    if type(item) == str:
        return True
    else:
        print("Item is not valid")
        return False

#Control the item if it is shopping list or not
def item_control(item):
    if item in shopping_list:
      #  print(f"{item} Already Exists")
        return True
    else:
        return False

#Delete
def delete_item(item):
    if item_control(item):
        print(f"the {item} is not in your Shopping List. delete failed")
        return False
    else:
        shopping_list.remove(item)
        return True

#Show the list
def show_shopping_list():
    a = 1
    if not shopping_list: # not kalıbıyla listenin içini kontrol ettik
        print("Your Shopping List is empty")
        return False
    else:
        for i in shopping_list:
            print(f"{a}-{i}")
            a += 1

# Add the item
def add_item(item):
    if item_type(item) & item_control(item)!= True:
        print("item added")
        shopping_list.append(item)
        return True
    elif not item_type(item):
        print(f"Item is not valid")
        return False
    elif item_control(item):
        print(f"the {item} is already existed")
        return False
    else:
        print("something is wrong")
        return False

#yes_no
def yn(answer):
    if answer == "yes" or answer == "y":
        answer = "yes"
        return answer
    elif answer == "no" or answer == "n":
        answer = "no"
        return answer
    else:
        print("answer is not valid")        #burada bir hata olabilir. answer is not validse... loopta kalsın
        return False

# The Menu
def greeting():
    print("=== Shopping List ===")
    answer = input("Commands: (use only a digit)\n"
                   "1-Show your list, 2-Add your list, 3-Delete from the list, 4-Quit: ")
    #answering type'ı string olmalı

    while answer == "1" or answer == 1:
        if not show_shopping_list():
            answer_y_n = input("Wanna add items? y/n")
            if yn(answer_y_n) == "yes":
                add_item(take_item())
                print("items added")
                greeting()
            elif yn(answer_y_n) == "no":
                greeting()
            else:
                print("something is wrong")

    if answer == "2":
        shopping_item = take_item()
        if add_item(shopping_item):
            while True:
                answer_y_n = input("Wanna add items? y/n")
                if yn(answer_y_n) == "yes":
                    a= take_item()
                    add_item(a)
                elif yn(answer_y_n) == "no":
                    greeting()
                else:
                    break

    elif answer == "3":
        answer_delete_item = delete_item(input("Item to be deleted?"))
        if answer_delete_item:
            print("Item deleted")
            print("your new list")
            show_shopping_list()
            greeting()
        else:
            print("something is wrong")
    elif answer == "4":
        print("Thank you for using Shopping List, see you next time!")
        return False
    else:
        print("please enter only digits 1 to 4")
        return False

#Main function
def main():
    while True:
        if not greeting():
            break
#Run the Program
main()