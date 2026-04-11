class Student: #our own data type
    ...


def main():
    """
    student = get_student() #return değerine göre otomatik olarak dictionary'e dönecek
    print(f"{student['name']} from {student['house']}") #dictionaries are mutable
"""
    student = get_student()
    print(f"{student.name} from {student.house}")
def get_student():
    """""
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house} #zaten dictionary döndüreceği için, return değeri dictionary olacak
"""
    student = Student() #classes have their "Attributes" #this is a object
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


###CLASSES###
#you can create your own data type
#when you create a class, you also create its objects

if __name__ == "__main__":
    main()