def main():
    student = get_student() #return değerine göre otomatik olarak dictionary'e dönecek
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house} #zaten dictionary döndüreceği için, return değeri dictionary olacak


if __name__ == "__main__":
    main()