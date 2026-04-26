import random

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
        if self.health > 0:
            return True
        else:
            return False
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

    def attack_enemy(self, damage):
        if self.a_power < self.armor:
            print("enchanted attack!")
            self.health -= damage
            return self.a_power * 0.5
        return self.a_power * 0.5

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
    a_power = 25
    armor = 200
    return Warrior(name, health, a_power, armor)

def get_mage(level):
    #mage one
    if level == "easy":
        mage_1 = "Aldric"
        health = 100
        mana = 500
        attack_p= mana*0.05
        return Mage(mage_1, health, attack_p, mana)
    elif level == "medium":
        mage_2 = "Seraphon"
        health = 1000
        mana = 800
        attack_p = mana*0.05
        return Mage(mage_2, health, attack_p, mana)
    elif level == "medium-hard":
        mage_3 = "Malachar"
        health = 1500
        mana = 1000
        attack_p = mana*0.05
        return Mage(mage_3, health, attack_p, mana)
    elif level == "hard":
        mage_4 = "Elowen"
        health = 10000
        mana = 2000
        attack_p = mana*0.1
        return Mage(mage_4, health,attack_p, mana)
    else:
        print("Invalid level")
        return False


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

def true_false():
    a = random.randrange(0,1)
    if a == 0:
        return True
    else:
        return False


def health_show(hero_health, mage_health):
    print(f"************************************************************************\n"
          f"hero's current health: {hero_health}\nMage's current health: {mage_health}\n"
          f"***********************************************************************\n")

#Game play
def game_play(level):
    # note: h represents hero
    h = get_character()
    h.introduce()
    if get_level(level) == "easy":
        mage = get_mage(get_level(level))
        mage.introduce()
        t_f =  true_false()
        print("FIGHT BEGUN!")
        if t_f:
            while True:
                print(f"HERO ATTACK!\nAttack power is {h.a_power}! Every power you over, you will lose your health!: attack wisely!")
                attack = int(input(" "))
                mage.take_damage(h.attack_enemy(attack))
                print("*"*51)
                print("mage lost health!")
                health_show(h.health, mage.health)
                if not mage.is_alive():
                    break
                mage.attack()
                print(f"mage {mage.name} attacked successfully! Poor hero :'(")
                if not h.is_alive():
                    break
                health_show(h.health, mage.health)
        else:
            while h.is_alive() or mage.is_alive():
                print(f"MAGE ATTACK! MANA POWER LOADING")
                mage.attack()
                print("Hero lost health!")
                health_show(h.health, mage.health)
                print(h.health)
                print(f"HERO ATTACK!\nAttack power is {h.a_power}! Every power you over, you will lose your health!: attack wisely!")
                attack =int(input(" "))
                mage.take_damage(h.attack_enemy(attack))
                print("mage lost health!")
                health_show(h.health, mage.health)

    print("Game Over")
    if h.is_alive():
        print("winner is hero")
        answer = input("Next level? (y/n): ")
        if answer == "y":
            level += 1
            return True
        else:
            print("Thanks for playing")
            return False
    else:
        print("winner is mage")
        answer = input("wanna try again (y/n): ")
        if answer == "y":
            return True
        else:
            print("Thanks for playing")
            return False

def get_level(level):
    if level == 0:
        return "easy"
    elif level == 1:
        return "medium"
    elif level == 2:
        return "medium-hard"
    elif level == 3:
        return "hard"
    else:
        return False
#a win means an upgrade, mage can drop some items when it is beaten, and those items may make grow hero
#but if the item is about mana, hero cannot gain any power.
#the game will over when user wants finish the game or the user's health drop to zero



def main():
    while True:
        level = 0
        game_play(level)

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