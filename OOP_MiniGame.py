class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.a_power = attack_power

    def introduce(self):
        print(f"Hello {self.name}, your current health is {self.health}. and your attack power is {self.a_power}")

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0
    def attack(self):
        return self.a_power

class Warrior(Character): #inherited

    def __init__(self, w_name, w_health, w_attack_power, armor):
        super().__init__(w_name, w_health, w_attack_power) #no need to use parent's direct name
        #Character.__init__(self, w_name, w_health, w_attack_power)
        self.armor = armor

    def introduce(self):
        print(f"hello I am a warrior! my name is {self.name}, my health {self.health}, my attack power {self.a_power} and my  armor def {self.armor}")

class Mage(Character):

    def __init__(self, name, health, attack_power, mana):
        super().__init__(name, health, attack_power)
        self.mana = mana

    def introduce(self):
        print(f"Hello {self.name}, my current health is {self.health}. and my attack power is {self.mana} I'll beat you!")

    def take_damage(self, damage):
        self.health -= damage

    def attack(self):
        return self.mana * 0.5

def get_character():
    name = input("Enter your hero name: ")
    health = 100 #I want them to automatically set a default.
    attack_power = 25
    mana = 200
    return Character(name, health, attack_power)

hero = get_character()
mage = Mage("Magist", 80, 0, 200)

hero.introduce()
mage.introduce()

hero.take_damage(30)
mage.take_damage(30)

print(hero.is_alive())
print(mage.is_alive())
print(hero.health)
print(mage.health)

