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
    pass

class Mage(Character):
    pass

def get_character():
    name = input("Enter your hero name: ")
    health = 100 #I want them to automatically set a default.
    attack_power = 25
    return Character(name, health, attack_power)

