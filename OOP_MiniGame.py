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

    def take_damage(self, damage):
        self.health -= damage
        self.armor -= damage

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
    armor = 200
    return Warrior(name, health, attack_power, armor)


#mage(villain)
#it will have same structure with hero, but not with choices, it is gonna get a random upgrade level to level

#hero
def hero_game(name, attack_power, health, armor):
    pass


#hero will have multiple choices. those choices are gonna make the hero grows over game play.
def hero_level():
    pass

#every restart will have new choice
def next_level():
    pass

#recods may store in a csv file 1-New Game / 2-Resume ???

#Game play
#a win means an upgrade, mage can drop some items when it is beaten, and those items may make grow hero
#but if the item is about mana, hero cannot gain any power.
#the game will over when user wants finish the game or the user's health drop to zero



def main():
    while True:
        #note: h represents hero
        h = get_character()
        h.introduce()
        hero_game(h.name, h.a_power, h.health, h.armor)

if __name__ == "__main__":
    main()


"""""
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

"""