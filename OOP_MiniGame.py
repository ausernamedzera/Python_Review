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

class Warrior(Character): #inherited

    def __init__(self, w_name, w_health, w_attack_power, armor):
        super().__init__(w_name, w_health, w_attack_power) #no need to use parent's direct name
        #Character.__init__(self, w_name, w_health, w_attack_power)
        self.armor = armor

    def introduce(self):
        print(f"hello I am a warrior! my name is {self.name}, my health {self.health}, my attack power {self.a_power} and my  armor def {self.armor}")

class Mage(Character):

    def __init__(self, mana, name, health, attack_power):
        super().__init__(name, health,attack_power)
        self.mana = mana

    def introduce(self):
        print(f"Hello {self.name}, your current health is {self.health}. and your attack power is {self.mana}")


    def take_damage(self, damage):
        self.mana -= damage

def get_character():
    name = input("Enter your hero name: ")
    health = 100 #I want them to automatically set a default.
    attack_power = 25
    armor = 200
    return Warrior(name, health, attack_power, armor)

hero = get_character()
hero.introduce()

