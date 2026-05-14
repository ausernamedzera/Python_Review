import random
from traceback import print_tb


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
    def attack(self, attack):
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

    def attack(self, attack):
        if attack > self.a_power:
            print("enchanted attack!")
            self.health = self.health - (attack - self.a_power)
            return attack * 0.5
        return attack * 0.5

class Mage(Character):

    def __init__(self, name, health, attack_power, mana):
        super().__init__(name, health, attack_power)
        self.mana = mana

    def introduce(self):
        print(f"Hello {self.name}, my current health is {self.health}. and my attack power is {self.mana} I'll beat you!")

    def take_damage(self, damage):
        self.health -= damage

    def attack(self, attack):
        mana_power = random.weibullvariate(0.003, 0.008)
        attack = self.mana * 0.003
        return attack

def get_character():
    while True:
        try:
            name = input("Enter your hero name: ")
            if name.isspace() or len(name) == 0:
                raise ValueError
            if name.isnumeric():
                raise ValueError
            for i in range(len(name)):
                if name[i].isnumeric():
                    raise ValueError

            #possible: try later
            """
            if not name.isalpha():
                raise ValueError
            """
        except ValueError:
            print("Invalid name")
        else:
            break
    health = 100 #I want them to automatically set a default.
    a_power = 25
    armor = 200
    return Warrior(name, health, a_power, armor)

def get_mage(level):
    #mage one
    if level == 0:
        mage_1 = "Aldric"
        health = 100
        mana = 500
        attack_p= mana*0.05
        return Mage(mage_1, health, attack_p, mana)
    elif level == 1:
        mage_2 = "Seraphon"
        health = 1000
        mana = 800
        attack_p = mana*0.05
        return Mage(mage_2, health, attack_p, mana)
    elif level == 2:
        mage_3 = "Malachar"
        health = 1500
        mana = 1000
        attack_p = mana*0.05
        return Mage(mage_3, health, attack_p, mana)
    elif level == 3:
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
def hero_game(h, level):
    mage = get_mage(level)
    h.introduce()
    mage.introduce()
    t_f = true_false()
    print("FIGHT BEGUN!")
    if t_f:
        while True:
            print(
                f"HERO ATTACK!\nAttack power is {h.a_power}! Every power you over, you will lose your health!: attack wisely!")
            attack = get_attack()*crit_rate(level)
            mage.take_damage(h.attack(attack))
            print("*" * 51)
            print("mage lost health!")
            print(f"hero attack: {attack}")
            health_show(h.health, mage.health)
            if not mage.is_alive():
                break
            # attack = mage.attack(mage.a_power)
            h.take_damage(mage.attack(mage.a_power))
            print(f"mage {mage.name} attacked successfully! Poor hero :'(")
            health_show(h.health, mage.health)
            if not h.is_alive():
                break

    else:
        while True:
            print(f"MAGE ATTACK! MANA POWER LOADING")
            mage_attacked = mage.attack(mage.a_power)
            h.take_damage(mage_attacked)
            print("*" * 51)
            print("Hero lost health!")
            health_show(h.health, mage.health)
            if not h.is_alive():
                break
            print(h.health)
            print(
                f"HERO ATTACK!\nAttack power is {h.a_power}! Every power you over, you will lose your health!: attack wisely!")
            attack = get_attack()
            print(f"hero attack: {attack}")
            mage.take_damage(h.attack(attack))
            print("mage lost health!")
            health_show(h.health, mage.health)
            if not mage.is_alive():
                break


def get_attack():
    while True:
        try:
            attack = float(input(" "))
        except ValueError:
            print("Invalid input")
        else:
            break
    return attack


#hero will have multiple choices. those choices are gonna make the hero grows over game play.
def hero_level(h, level):
    if level == 0: #aynı amaca hizmet eden iki değişken tanımlarsan, yazdığın kodu tabii karıştırısın (:
        name = h.name
        health = 100
        a_power = 25
        armor = h.armor
        return Warrior(name, health, a_power, armor)
    elif level == 1:
        name = h.name
        health = 500
        a_power = 1500
        armor = h.armor
        return Warrior(name, health, a_power, armor)
    elif level == 2:
        name = h.name
        health = 10000
        a_power = 10000
        armor = 10000
        return Warrior(name, health, a_power, armor)
    elif level == 3:
        print("YOU WON THE GAME CONGRATS")
    else:
        print("over leveled up, you beat the all program")
        return False

def crit_rate(level):
    if level == 0:
        if random.random() < 0.15:
            return 2
        else:
            return 1
    elif level == 1:
        if random.random() < 0.3:
            return 2.5
        else:
            return 1
    elif level == 2:
        if random.random() < 0.5:
            return 3
        else:
            return 1
    elif level == 3:
        if random.random() < 0.8:
            return 4
        else:
            return 1
    else:
        return False

#recods may store in a csv file 1-New Game / 2-Resume ???

def true_false():
    a = random.randrange(0,2)
    if a == 0:
        return True
    else:
        return False


def health_show(hero_health, mage_health):
    print(f"************************************************************************\n"
          f"hero's current health: {hero_health}\nMage's current health: {mage_health}\n"
          f"***********************************************************************\n")

#Game play
def game_play(h, level):
    if  level == 0:
        hero_game(h, level)
    elif level == 1:
        #hero should get a level up
        h = hero_level(h, level)
        hero_game(h, level)
    elif level == 2:
        h = hero_level(h, level)
        hero_game(h, level)
    elif level == 3:
        h = hero_level(h, level)
        hero_game(h, level)
    else:
        print("Invalid level")
        return False
    print("Game Over")
    if h.is_alive():
        print("winner is hero")
        print("Next level? (y/n): ")
        answer = yn_answer()
        if answer == "y" or answer == "yes":
            return "hero"
        else:
            print("Thanks for playing")
            return False
    elif not h.is_alive():
        print("winner is mage")
        print("wanna try again (y/n): ")
        answer = yn_answer()
        if answer == "y" or answer=="yes":
            return "mage"
        else:
            print("Thanks for playing")
            return False
    else:
        print("something went wrong //def gameplay")
        return False


def yn_answer():
    while True:
        try:
            answer = str(input(" ")).lower()
            if answer not in ["y", "n", "yes", "no"]:
                raise ValueError
            else:
                return answer
        except ValueError:
            print("Invalid input")

#a win means an upgrade, mage can drop some items when it is beaten, and those items may make grow hero
#but if the item is about mana, hero cannot gain any power.
#the game will over when user wants finish the game or the user's health drop to zero

hero = get_character()
level_for_all = 0

def main(h, level):
    while True:
        result = game_play(h, level)

        if result == "mage":
            h = hero_level(h, level)
        elif result == False:
            break
        elif result == "hero":
            level += 1
        else:
            print("something went wrong")

if __name__ == "__main__":
    main(hero, level_for_all)
