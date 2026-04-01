"""```
name = "Ayaka"
age = 26
height = 1.75
active = True


print(name, age, height, active)
print(type(name), type(age), type(height), type(active))


mesaj = f"Hello, this is {name}, and your age is {age}, and your height is {height}"
print(mesaj)
print(mesaj.upper())
print(mesaj.replace("Hello", "HI"))
print(mesaj)
print(len(mesaj))

### List and Loops ###

fruits = ["apple", "banana", "cherry", "mango"]

print(fruits[-4]) # tersten -1 ile başlar
print(fruits[0])  # düzden 0 ile başlar

print(fruits[1:3])

fruits.append("çilek")
print(fruits)

fruits.insert(2, "üzüm")

print(fruits)

fruits.pop(3)
print(fruits)

print(len(fruits)) #eleman sayısı
print(fruits)
fruits.insert(2,1)
for i in fruits:
    if type(i)==str:
        print(f"{i} is a fruit")
    else:
        print("i didn't recognize these")

"""

sayac = 0
while sayac < 5:
    print(f"sayaç: {sayac}")
    sayac += 1
print(sayac)
# break ve continue
for i in range(10):
    if i == 3:
        continue    # 3'ü atla
    elif i == 7:
        break       # 7'de dur
    print(i)
    