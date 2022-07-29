import random
from colorama import Fore, Back, Style
import time

class Sean_Bean(object):
    health = 3000
    strength = 200
    charge = 400
    defence = 15
    energy = 10

class bean (object):
    name = "Bean"
    health = 600
    str = 75
    crit = 200

class bigbean (object):
    name = "Big Bean"
    health = 800
    str = 75
    crit = 200

class slimeybean (object):
    name = "Slimey Bean"
    health = 650
    str = 70
    crit = 140

class direbean (object):
    name = "Dire Bean"
    health = 800
    str = 90
    crit = 180

class flyingbean (object):
    name = "Flying Bean"
    health = 650
    str = 80
    crit = 160

class beangiant (object):
    name = "Bean Giant"
    health = 1100
    str = 110
    crit = 220

class beangunman (object):
    name = "Bean Gunman"
    health = 850
    str = 100
    crit = 200

class beansoldier (object):
    name = "Bean Soldier"
    health = 900
    str = 90
    crit = 145

class drybean (object):
    name = "Dry Bean"
    health = 1000
    str = 100
    crit = 200

class beanstatue (object):
    name = "Bean Statue"
    health = 1250
    str = 120
    crit = 240

class thebean (object):
    name = "The Beaninator"
    health = 2000
    str = 200
    crit = 400

class mrbean (object):
    name = "Mr Bean"
    health = 1750
    str = 175
    crit = 350

class supbean (object):
    name = "The Supreme Bean"
    health = 2000
    str = 200
    crit = 400

def gameover(character, tins):
    if character.health <1:
        print(Fore.RED + "__     ______  _    _ ___      ________   ____  ______ ______ _   _    _____  ______     ________ _____")
        print("\ \   / / __ \| |  | ( ) \    / /  ____| |  _ \|  ____|  ____| \ | |  / ____|/ __ \ \   / /  ____|  __ \ ")
        print("_\ \_/ / |  | | |  | |/ \ \  / /| |__    | |_) | |__  | |__  |  \| | | (___ | |  | \ \_/ /| |__  | |  | |")
        print("__\   /| |  | | |  | |   \ \/ / |  __|   |  _ <|  __| |  __| | . ` |  \___ \| |  | |\   / |  __| | |  | |")
        print("___| | | |__| | |__| |    \  /  | |____  | |_) | |____| |____| |\  |  ____) | |__| | | |  | |____| |__| |")
        print("___|_|  \____/ \____/      \/   |______| |____/|______|______|_| \_| |_____/ \____/  |_|  |______|_____/ ")
        time.sleep(0.5)
        print("You have lost all you Tins of Beans")
        time.sleep(0.5)
        print("Thank you for playing please try again")
        exit()

def heroselect():
    selection = Sean_Bean
    if selection == Sean_Bean:
        character = Sean_Bean
        print(Fore.YELLOW + "---------------------------------")
        print(Back.BLACK + "__________                                ________   _____   ___________       __          ")
        print(             "\______   \ ____ _____    ____   ______   \_____  \_/ ____\  \_   _____/____ _/  |_  ____  ")
        print(             " |    |  _// __ \\__  \  /    \ /  ___/    /   |   \   __\    |    __) \__  \\   __\/ __ \ ")
        print(             " |    |   \  ___/ / __ \|   |  \\___ \    /    |    \  |      |     \   / __ \|  | \ ___/ ")
        print(             " |______  /\___  >____  /___|  /____  >  \_______  /__|      \___  /  (____  /__|  \___  > ")
        print(             "        \/     \/     \/     \/     \/          \/             \/        \/          \/    ")
        print()
        time.sleep(1)
        print("Welcome to the world of Heinz, Sean Bean")
        time.sleep(1)
        print("You find yourself in a dark cave.")
        time.sleep(1)
        print("You have",character.health,"Health.")
        time.sleep(1)
        print("lose all your health and you die!")
        time.sleep(1)
        print("You will have two options for battle.")
        time.sleep(1)
        print("Your standard attack will deal",character.strength, "damage and cost you 1 energy")
        time.sleep(1)
        print("Your charged attack will deal",character.charge, "damage and cost you 2 energy")
        time.sleep(1)
        print("you will only have",character.energy,"energy so use it wisely.")
        time.sleep(1)
        print("---------------------------------")
        time.sleep(1)
        print ("OH NO... A BEAN APPEARS!!")
        print("---------------------------------")
        time.sleep(1)
        return character
    else:
        heroselect()

def enemyselect(bean):
    enemylist = (bean)
    enemy = enemylist
    return enemy

def battlestate1(tins):
    enemy = enemyselect(bean)
    print("A wild", enemy.name, "has appeared it has", enemy.health, "Health")
    time.sleep(0.5)
    while enemy.health >0:
        choice = input("Type 1. standard attack (200 dmg)(1 energy) \nType 2. charged attack  (400 dmg)(2 energy) ")
        time.sleep(0.5)
        if character.energy <= 0:
            print("You have no energy left and must recharge this turn")
            time.sleep(0.5)
            character.health = character.health - enemy.str
            print("You took" , enemy.str, "from the wild", enemy.name,)
            time.sleep(0.5)
            print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
            time.sleep(0.5)
            character.energy = character.energy + 6
            print("You have", character.energy, "energy left")
            time.sleep(0.5)
            continue
        if choice == "1":
            print("You swing your weapon at the enemy")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 1:
                enemy.health = enemy.health - character.strength
                character.energy = character.energy - 1
                print("You dealt 200 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(1)
                if enemy.health >0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, " damage from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                else:
                    if enemy.name == "Bean":
                        enemy.health = 600
                        tins = tins + 3

                    print("you have defeated the wild", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    print("You also gained some health from that battle")
                    time.sleep(0.5)
                    character.health = 3000
                    print("Your current health is now", character.health)
                    time.sleep(0.5)
                    character.energy = 10
                    return tins
                    break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 1
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
               
        elif choice == "2":
            print("you charge up for your next attack")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance >3:
                enemy.health = enemy.health - character.charge
                character.energy = character.energy - 2
                print("Your charged attack dealt 400 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(1)
                if enemy.health > 0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "damage from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                else:
                    if enemy.name == "Bean":
                        enemy.health = 600
                        tins = tins + 3

                    print("you have defeated the wild", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    print("You also gained some health from that battle")
                    time.sleep(0.5)
                    character.health = 3000
                    print("Your current health is now", character.health)
                    time.sleep(0.5)
                    character.energy = 10
                    return tins
                    break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 2
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
        elif choice != 1 or 2:
            print("That is an invalid input please select another option")
            time.sleep(0.5)
            continue

       
def enemyselect(bigbean):
    enemylist = (bigbean)
    chance = random.randint(0,1)
    enemy = enemylist
    return enemy

def battlestate2(tins):
    enemy = enemyselect(bigbean)
    print("A wild", enemy.name, "has appeared it has", enemy.health, "Health")
    time.sleep(0.5)
    while enemy.health >0:
        choice = input("Type 1. standard attack (200 dmg)(1 energy) \nType 2. charged attack  (400 dmg)(2 energy) ")
        time.sleep(0.5)
        if character.energy <= 0:
            print("You have no energy left and must recharge this turn")
            time.sleep(0.5)
            character.health = character.health - enemy.str
            print("You took" , enemy.str, "damage from the wild", enemy.name,)
            time.sleep(0.5)
            print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
            time.sleep(0.5)  
            character.energy = character.energy + 6
            print("You have", character.energy, "energy left")
            time.sleep(0.5)
            continue
        if choice == "1":
            print("You swing your weapon at the enemy")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 1:
                enemy.health = enemy.health - character.strength
                character.energy = character.energy - 1
                print("You dealt 200 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                time.sleep(0.7)
                if enemy.health >0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "damage from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "Big Bean":
                        enemy.health == 800
                        tins = tins + 3
                    print("you have defeated the wild", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    print("You also gained some health from that battle")
                    time.sleep(0.5)
                    character.health = 3000
                    print("Your current health is now", character.health)
                    time.sleep(0.5)
                    character.energy = 10
                    return tins
                    break
            else:
                time.sleep(0.7)
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 1
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
                
        elif choice == "2":
            print("you charge up for your next attack")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 1:
                enemy.health = enemy.health - character.charge
                character.energy = character.energy - 2
                print("Your charged attack dealt 400 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health > 0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "damage from the wild",)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                   if enemy.name == "Big Bean":
                        enemy.health == 800
                        tins = tins + 3

                        time.sleep(0.7)
                        print("you have defeated the wild", enemy.name)
                        time.sleep(0.5)
                        print("They dropped some Tins of Beans")
                        time.sleep(0.5)
                        print("You also gained some health from that battle")
                        time.sleep(0.5)
                        character.health = 3000
                        print("Your current health is now", character.health)
                        time.sleep(0.5)
                        character.energy = 10
                        return tins
                        break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 2
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
        elif choice != 1 or 2:
            print("That is an invalid input please select another option")
            time.sleep(0.5)
            continue

def enemyselect(slimeybean):
    enemylist = (slimeybean)
    chance = random.randint(0,1)
    enemy = enemylist
    return enemy

def battlestate3(tins):
    enemy = enemyselect(slimeybean)
    print(Fore.LIGHTGREEN_EX + "A wild", enemy.name, "has appeared it has", enemy.health, "Health")
    time.sleep(0.5)
    while enemy.health >0:
        choice = input("Type 1. standard attack (200 dmg)(1 energy) \nType 2. charged attack  (400 dmg)(2 energy) ")
        time.sleep(0.5)
        if character.energy <= 0:
            print("You have no energy left and must recharge this turn")
            time.sleep(0.5)
            character.health = character.health - enemy.str
            print("You took" , enemy.str, "damage from the wild", enemy.name,)
            time.sleep(0.5)
            print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
            time.sleep(0.5)
            character.energy = character.energy + 6
            print("You have", character.energy, "energy left")
            time.sleep(0.5)
            continue
        if choice == "1":
            print("You swing your weapon at the enemy")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 2:
                enemy.health = enemy.health - character.strength
                character.energy = character.energy - 1
                print("You dealt 200 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.7)
                if enemy.health >0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "damage from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "Slimey Bean":
                        enemy.health = 650
                        tins = tins + 3
                        
                    time.sleep(0.7)
                    print("you have defeated the wild", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    return tins
                    break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 1
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
                
        elif choice == "2":
            print("you charge up for your next attack")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 2:
                enemy.health = enemy.health - character.charge
                character.energy = character.energy - 2
                print("Your charged attack dealt 400 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health > 0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "damage from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "Slimey Bean":
                        enemy.health = 650
                        tins = tins + 3

                    time.sleep(0.7)
                    print("you have defeated the wild", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    return tins
                    break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 2
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
        elif choice != 1 or 2:
            print("That is an invalid input please select another option")
            time.sleep(0.5)
            continue
 
def enemyselect2(direbean):
    enemylist = (direbean)
    chance = random.randint(0,1)
    enemy = enemylist
    return enemy

def battlestate4(tins):
    enemy = enemyselect(direbean)
    print(Fore.LIGHTRED_EX + "A wild", enemy.name, "has appeared it has", enemy.health, "Health")
    time.sleep(0.5)
    while enemy.health >0:
        choice = input("Type 1. standard attack (200 dmg)(1 energy) \nType 2. charged attack  (400 dmg)(2 energy) ")
        time.sleep(0.5)
        if character.energy <= 0:
            print("You have no energy left and must recharge this turn")
            time.sleep(0.5)
            character.health = character.health - enemy.str
            print("You took" , enemy.str, "damage from the wild", enemy.name,)
            time.sleep(0.5)
            print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
            time.sleep(0.5)
            character.energy = character.energy + 6
            print("You have", character.energy, "energy left")
            time.sleep(0.5)
            continue
        if choice == "1":
            print("You swing your weapon at the enemy")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 2:
                enemy.health = enemy.health - character.strength
                character.energy = character.energy - 1
                print("You dealt 200 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.7)
                if enemy.health >0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "damage from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "Dire Bean":
                        enemy.health == 800
                        tins = tins + 3
                        
                    time.sleep(0.7)
                    print("you have defeated the wild", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    print("You also gained some health from that battle")
                    time.sleep(0.5)
                    print("Your current health is now", character.health)
                    time.sleep(0.5)
                    character.energy = 10
                    enemy.health = 800
                    return tins
                    break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 1
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
           
        elif choice == "2":
            print("you charge up for your next attack")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 2:
                enemy.health = enemy.health - character.charge
                character.energy = character.energy - 2
                print("Your charged attack dealt 400 damage to the wild", enemy.name,)
                time.sleep(0.5)
                print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health > 0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "damage from the wild", enemy.name, "you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                   if enemy.name == "Dire Bean":
                        enemy.health == 800
                        tins = tins + 3

                        time.sleep(0.7)
                        print("you have defeated the wild", enemy.name)
                        time.sleep(0.5)
                        print("They dropped some Tins of Beans")
                        time.sleep(0.5)
                        print("You also gained some health from that battle")
                        time.sleep(0.5)
                        print("Your current health is now", character.health)
                        time.sleep(0.5)
                        character.energy = 10
                        enemy.health = 800
                        return tins
                        break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 2
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
        elif choice != 1 or 2:
            print("That is an invalid input please select another option")
            time.sleep(0.5)
            continue

def enemyselect(flyingbean):
    enemylist = (flyingbean)
    chance = random.randint(0,1)
    enemy = enemylist
    return enemy

def battlestate7(tins):
    enemy = enemyselect(flyingbean)
    print(Fore.LIGHTBLUE_EX + "A wild", enemy.name, "has appeared it has", enemy.health, "Health")
    time.sleep(0.5)
    while enemy.health >0:
        choice = input("Type 1. standard attack (200 dmg)(1 energy) \nType 2. charged attack  (400 dmg)(2 energy) ")
        time.sleep(0.5)
        if character.energy <= 0:
            print("You have no energy left and must recharge this turn")
            time.sleep(0.5)
            print("You took" , enemy.str, "damage from the wild", enemy.name,)
            character.health = character.health - enemy.str
            print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
            time.sleep(0.5)
            character.energy = character.energy + 6
            print("You have", character.energy, "energy left")
            time.sleep(0.5)
            continue
        if choice == "1":
            print("You swing your weapon at the enemy")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 4:
                enemy.health = enemy.health - character.strength
                character.energy = character.energy - 1
                print("You dealt 200 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health >0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "Flying Bean":
                        enemy.health = 650
                        tins = tins + 4
                        
                    time.sleep(0.7)
                    print("you have defeated the wild", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    return tins
                    break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 1
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
                
        elif choice == "2":
            print("you charge up for your next attack")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance >4:
                enemy.health = enemy.health - character.charge
                character.energy = character.energy - 2
                print("Your charged attack dealt 400 damage to the wild", enemy.name,)
                time.sleep(0.5)
                print("You took" , enemy.str, "damage from the wild", enemy.name,)
                time.sleep(0.5)
                
                if enemy.health > 0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    print("You have", character.energy, "energy left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "Flying Bean":
                        enemy.health = 650
                        tins = tins + 4

                    time.sleep(0.7)
                    print("you have defeated the wild", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    return tins
                    break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 2
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
        elif choice != 1 or 2:
            print("That is an invalid input please select another option")
            time.sleep(0.5)
            continue

                
def enemyselect2(beangiant):
    enemylist = (beangiant)
    chance = random.randint(0,1)
    enemy = enemylist
    return enemy

def battlestate8(tins):
    enemy = enemyselect(beangiant)
    print(Fore.WHITE + "A wild", enemy.name, "has appeared it has", enemy.health, "Health")
    time.sleep(0.5)
    while enemy.health >0:
        choice = input("Type 1. standard attack (200 dmg)(1 energy) \nType 2. charged attack  (400 dmg)(2 energy) ")
        time.sleep(0.5)
        if character.energy <= 0:
            print("You have no energy left and must recharge this turn")
            time.sleep(0.5)
            character.health = character.health - enemy.str
            print("You took" , enemy.str, "damage from the wild", enemy.name,)
            time.sleep(0.5)
            print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
            time.sleep(0.5)
            character.energy = character.energy + 6
            print("You have", character.energy, "energy left")
            time.sleep(0.5)
            continue
        if choice == "1":
            print("You swing your weapon at the enemy")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 1:
                enemy.health = enemy.health - character.strength
                character.energy = character.energy - 1
                print("You dealt 200 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health >0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "Bean Giant":
                        enemy.health == 1100
                        tins = tins + 4
                        
                    time.sleep(0.7)
                    print("you have defeated the wild", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    character.energy = 10
                    enemy.health = 1100
                    return tins
                    break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 1
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
                
        elif choice == "2":
            print("you charge up for your next attack")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance >1:
                enemy.health = enemy.health - character.charge
                character.energy = character.energy - 2
                print("Your charged attack dealt 400 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health > 0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                   if enemy.name == "Bean Giant":
                        enemy.health == 1100
                        tins = tins + 4

                        time.sleep(0.7)
                        print("you have defeated the wild", enemy.name)
                        time.sleep(0.5)
                        print("They dropped some Tins of Beans")
                        time.sleep(0.5)
                        character.energy = 10
                        enemy.health = 1100
                        return tins
                        break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 2
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
        elif choice != 1 or 2:
            print("That is an invalid input please select another option")
            time.sleep(0.5)
            continue

def enemyselect(beangunman):
    enemylist = (beangunman)
    chance = random.randint(0,1)
    enemy = enemylist
    return enemy

def battlestate5(tins):
    enemy = enemyselect(beangunman)
    print(Fore.GREEN + "A wild", enemy.name, "has appeared it has", enemy.health, "Health")
    time.sleep(0.5)
    while enemy.health >0:
        choice = input("Type 1. standard attack (200 dmg)(1 energy) \nType 2. charged attack  (400 dmg)(2 energy) ")
        time.sleep(0.5)
        if character.energy <= 0:
            print("You have no energy left and must recharge this turn")
            time.sleep(0.5)
            character.health = character.health - enemy.str
            print("You took" , enemy.str, "damage from the wild", enemy.name,)
            time.sleep(0.5)
            print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
            time.sleep(0.5)
            character.energy = character.energy + 6
            print("You have", character.energy, "energy left")
            time.sleep(0.5)
            continue
        if choice == "1":
            print("You swing your weapon at the enemy")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 2:
                enemy.health = enemy.health - character.strength
                character.energy = character.energy - 1
                print("You dealt 200 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health >0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "damage from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "Bean Gunman":
                        enemy.health = 850
                        tins = tins + 3
                        
                    time.sleep(0.7)
                    print("you have defeated the wild", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    return tins
                    break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 1
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
                
        elif choice == "2":
            print("you charge up for your next attack")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 2:
                enemy.health = enemy.health - character.charge
                character.energy = character.energy - 2
                print("Your charged attack dealt 400 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health > 0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "damage from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "Bean Gunman":
                        enemy.health = 850
                        tins = tins + 3

                    time.sleep(0.7)
                    print("you have defeated the wild", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    return tins
                    break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 2
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
        elif choice != 1 or 2:
            print("That is an invalid input please select another option")
            time.sleep(0.5)
            continue
        
def enemyselect2(beansoldier):
    enemylist = (beansoldier)
    chance = random.randint(0,1)
    enemy = enemylist
    return enemy

def battlestate6(tins):
    enemy = enemyselect(beansoldier)
    print(Fore.LIGHTCYAN_EX + "A wild", enemy.name, "has appeared it has", enemy.health, "Health")
    time.sleep(0.5)
    while enemy.health >0:
        choice = input("Type 1. standard attack (200 dmg)(1 energy) \nType 2. charged attack  (400 dmg)(2 energy) ")
        time.sleep(0.5)
        if character.energy <= 0:
            print("You have no energy left and must recharge this turn")
            time.sleep(0.5)
            character.health = character.health - enemy.str
            print("You took" , enemy.str, "damage from the wild", enemy.name,)
            time.sleep(0.5)
            print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
            time.sleep(0.5)
            character.energy = character.energy + 6
            print("You have", character.energy, "energy left")
            time.sleep(0.5)
            continue
        if choice == "1":
            print("You swing your weapon at the enemy")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 2:
                enemy.health = enemy.health - character.strength
                character.energy = character.energy - 1
                print("You dealt 200 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health >0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "Bean Soldier":
                        enemy.health == 900
                        tins = tins + 4
                        
                    time.sleep(0.7)
                    print("you have defeated the wild", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    print("You also gained some health from that battle")
                    time.sleep(0.5)
                    character.health = 3000
                    print("Your current health is now", character.health)
                    time.sleep(0.5)
                    character.energy = 10
                    enemy.health = 900
                    return tins
                    break
            else:
                time.sleep(0.7)
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 1
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
                
        elif choice == "2":
            print("you charge up for your next attack")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 2:
                enemy.health = enemy.health - character.charge
                character.energy = character.energy - 2
                print("Your charged attack dealt 400 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health > 0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "damage from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                   if enemy.name == "Bean Soldier":
                        enemy.health == 900
                        tins = tins + 4

                        time.sleep(0.7)
                        print("you have defeated the wild", enemy.name)
                        time.sleep(0.5)
                        print("They dropped some Tins of Beans")
                        time.sleep(0.5)
                        print("You also gained some health from that battle")
                        time.sleep(0.5)
                        character.health = 3000
                        print("Your current health is now", character.health)
                        time.sleep(0.5)
                        character.energy = 10
                        enemy.health = 900
                        return tins
                        break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 2
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
        elif choice != 1 or 2:
            print("That is an invalid input please select another option")
            time.sleep(0.5)
            continue

def enemyselect(drybean):
    enemylist = (drybean)
    chance = random.randint(0,1)
    enemy = enemylist
    return enemy

def battlestate9(tins):
    enemy = enemyselect(drybean)
    print(Fore.LIGHTMAGENTA_EX + "A wild", enemy.name, "has appeared it has", enemy.health, "Health")
    time.sleep(0.5)
    while enemy.health >0:
        choice = input("Type 1. standard attack (200 dmg)(1 energy) \nType 2. charged attack  (400 dmg)(2 energy) ")
        time.sleep(0.5)
        if character.energy <= 0:
            print("You have no energy left and must recharge this turn")
            time.sleep(0.5)
            character.health = character.health - enemy.str
            print("You took" , enemy.str, "damage from the wild", enemy.name,)
            time.sleep(0.5)
            print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
            time.sleep(0.5)
            character.energy = character.energy + 6
            print("You have", character.energy, "energy left")
            time.sleep(0.5)
            continue
        if choice == "1":
            print("You swing your weapon at the enemy")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                character.energy = character.energy - 1
                print("You dealt 200 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health >0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "Dry Bean":
                        enemy.health = 1000
                        tins = tins + 5
                        
                    time.sleep(0.7)
                    print("you have defeated the wild", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    return tins
                    break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 1
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
                
                
        elif choice == "2":
            print("you charge up for your next attack")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance >3:
                enemy.health = enemy.health - character.charge
                character.energy = character.energy - 2
                print("Your charged attack dealt 400 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health > 0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "Dry Bean":
                        enemy.health = 1000
                        tins = tins + 5

                    time.sleep(0.7)
                    print("you have defeated the wild", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    return tins
                    break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 2
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
        elif choice != 1 or 2:
            print("That is an invalid input please select another option")
            time.sleep(0.5)
            continue

                
def enemyselect2(beanstatue):
    enemylist = (beanstatue)
    chance = random.randint(0,1)
    enemy = enemylist
    return enemy

def battlestate10(tins):
    enemy = enemyselect(beanstatue)
    print(Fore.LIGHTYELLOW_EX + "A wild", enemy.name, "has appeared it has", enemy.health, "Health")
    time.sleep(0.5)
    while enemy.health >0:
        choice = input("Type 1. standard attack (200 dmg)(1 energy) \nType 2. charged attack  (400 dmg)(2 energy) ")
        time.sleep(0.5)
        if character.energy <= 0:
            print("You have no energy left and must recharge this turn")
            time.sleep(0.5)
            character.health = character.health - enemy.str
            print("You took" , enemy.str, "damage from the wild", enemy.name,)
            time.sleep(0.5)
            print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
            time.sleep(0.5)
            character.energy = character.energy + 6
            print("You have", character.energy, "energy left")
            time.sleep(0.5)
            continue
        if choice == "1":
            print("You swing your weapon at the enemy")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.health = enemy.health - character.strength
                character.energy = character.energy - 1
                print("You dealt 200 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health >0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "Bean Statue":
                        enemy.health == 1200
                        tins = tins + 6
                        
                    time.sleep(0.7)
                    print("you have defeated the wild", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    print("You also gained some health from that battle")
                    time.sleep(0.5)
                    character.health = 3000
                    print("Your current health is now", character.health)
                    time.sleep(0.5)
                    character.energy = 10
                    enemy.health = 1200
                    return tins
                    break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 1
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
                
        elif choice == "2":
            print("you charge up for your next attack")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance >3:
                enemy.health = enemy.health - character.charge
                character.energy = character.energy - 2
                print("Your charged attack dealt 400 damage to the wild", enemy.name,)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                time.sleep(0.5)
                if enemy.health > 0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                   if enemy.name == "Bean Statue":
                        enemy.health == 1200
                        tins = tins + 6

                        time.sleep(0.7)
                        print("you have defeated the wild", enemy.name)
                        time.sleep(0.5)
                        print("They dropped some Tins of Beans")
                        time.sleep(0.5)
                        print("You also gained some health from that battle")
                        time.sleep(0.5)
                        character.health = 3000
                        print("Your current health is now", character.health)
                        time.sleep(0.5)
                        character.energy = 10
                        enemy.health = 1200
                        return tins
                        break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 2
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
        elif choice != 1 or 2:
            print("That is an invalid input please select another option")
            time.sleep(0.5)
            continue

def enemyselect(thebean):
    enemylist = (thebean)
    chance = random.randint(0,1)
    enemy = enemylist
    return enemy

def battlestate11(tins):
    enemy = enemyselect(thebean)
    print(Fore.BLUE + enemy.name, "has appeared it has", enemy.health, "Health")
    time.sleep(0.5)
    while enemy.health >0:
        choice = input("Type 1. standard attack (200 dmg)(1 energy) \nType 2. charged attack  (400 dmg)(2 energy) ")
        time.sleep(0.5)
        if character.energy <= 0:
            print("You have no energy left and must recharge this turn")
            time.sleep(0.5)
            character.health = character.health - enemy.str
            print("You took" , enemy.str, "damage from the wild", enemy.name,)
            time.sleep(0.5)
            print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
            time.sleep(0.5)
            character.energy = character.energy + 6
            print("You have", character.energy, "energy left")
            time.sleep(0.5)
            continue
        if choice == "1":
            print("You swing your weapon at the enemy")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 1:
                enemy.health = enemy.health - character.strength
                character.energy = character.energy - 1
                print("You dealt 200 damage to", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health >0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "from", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "The Beaninator":
                        enemy.health = 2000
                        tins = tins + 8
                        
                    time.sleep(0.7)
                    print("you have defeated", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    return tins
                    break
            else:
                print("You tried attacking" , enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 1
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
                
        elif choice == "2":
            print("you charge up for your next attack")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 1:
                enemy.health = enemy.health - character.charge
                character.energy = character.energy - 2
                print("Your charged attack dealt 400 damage to", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health > 0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "from", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "The Beaninator":
                        enemy.health = 2000
                        tins = tins + 8

                    time.sleep(0.7)
                    print("you have defeated", enemy.name)
                    time.sleep(0.5)
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    return tins
                    break
            else:
                print("You tried attacking", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 2
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
        elif choice != 1 or 2:
            print("That is an invalid input please select another option")
            time.sleep(0.5)
            continue

def enemyselect2(mrbean):
    enemylist = (mrbean)
    chance = random.randint(0,1)
    enemy = enemylist
    return enemy

def battlestate12(tins):
    enemy = enemyselect(mrbean)
    print(Fore.RED + "A wild", enemy.name, "has appeared it has", enemy.health, "Health")
    time.sleep(0.5)
    while enemy.health >0:
        choice = input("Type 1. standard attack (200 dmg)(1 energy) \nType 2. charged attack  (400 dmg)(2 energy) ")
        time.sleep(0.5)
        if character.energy <= 0:
            print("You have no energy left and must recharge this turn")
            time.sleep(0.5)
            character.health = character.health - enemy.str
            print("You took" , enemy.str, "damage from the wild", enemy.name, "you now have", character.health, "health left")
            time.sleep(0.5)
            character.energy = character.energy + 6
            print("You have", character.energy, "energy left")
            time.sleep(0.5)
            continue
        if choice == "1":
            print("You swing your weapon at the enemy")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 1:
                enemy.health = enemy.health - character.strength
                character.energy = character.energy - 1
                print("You dealt 200 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health >0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "Mr Bean":
                        enemy.health == 1750
                        tins = tins + 10
                        
                    time.sleep(0.7)
                    print("you have defeated the wild", enemy.name)
                    time.sleep(0.5)
                    print("You will now deal increased damage")
                    time.sleep(0.5)
                    character.strength = character.strength *2
                    print("They dropped some Tins of Beans")
                    time.sleep(0.5)
                    print("You also gained some health from that battle")
                    time.sleep(0.5)
                    character.health = 3000
                    print("Your current health is now", character.health)
                    time.sleep(0.5)
                    character.energy = 10
                    enemy.health = 1750
                    return tins
                    break
            else:
                time.sleep(0.7)
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 1
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
                
        elif choice == "2":
            print("you charge up for your next attack")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 1:
                enemy.health = enemy.health - character.charge
                character.energy = character.energy - 2
                print("Your charged attack dealt 400 damage to the wild", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                time.sleep(0.5)
                if enemy.health > 0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "from the wild", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                   if enemy.name == "Mr Bean":
                        enemy.health == 1750
                        tins = tins + 10

                        time.sleep(0.7)
                        print("you have defeated the wild", enemy.name)
                        time.sleep(0.5)
                        print("You will now deal increased damage")
                        time.sleep(0.5)
                        character.strength = character.strength *2
                        print("They dropped some Tins of Beans")
                        time.sleep(0.5)
                        print("You also gained some health from that battle")
                        time.sleep(0.5)
                        character.health = 3000
                        print("Your current health is now", character.health)
                        time.sleep(0.5)
                        character.energy = 10
                        enemy.health = 1750
                        return tins
                        break
            else:
                print("You tried attacking the wild", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 2
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
        elif choice != 1 or 2:
            print("That is an invalid input please select another option")
            time.sleep(0.5)
            continue

def enemyselect(supbean):
    enemylist = (supbean)
    chance = random.randint(0,1)
    enemy = enemylist
    return enemy

def bossbattlestate(tins):
    enemy = enemyselect(supbean)
    time.sleep(0.5)
    print(Fore.YELLOW)
    print ("  _____               _____            _ ")          
    print("  / ____|             |  __ \          | |   ")          
    print(" | (___   ___  _   _  | |__) |___  __ _| |_ __ ___  ")
    print("  \___ \ / _ \| | | | |  _  // _ \/ _` | | '_ ` _ \ ")
    print("  ____) | (_) | |_| | | | \ \  __/ (_| | | | | | | |")
    print(" |_____/ \___/ \__, | |_|  \_\___|\__,_|_|_| |_| |_|")
    print("                __/ |                               ")
    print("               |___/                               ")
    time.sleep(1)
    print("Heading to the soy realm, home to the supreme bean this is where your journey ends either with triumph or death ")
    time.sleep(0.5)
    print(enemy.name, "has appeared it has", enemy.health, "Health")
    time.sleep(0.5)
    while enemy.health >0:
        choice = input("Type 1. standard attack (200 dmg)(1 energy) \nType 2. charged attack  (400 dmg)(2 energy) ")
        time.sleep(0.5)
        if character.energy <= 0:
            print("You have no energy left and must recharge this turn")
            time.sleep(0.5)
            character.health = character.health - enemy.str
            print("You took" , enemy.str, "damage from the wild", enemy.name,)
            time.sleep(0.5)
            print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
            time.sleep(0.5)
            character.energy = character.energy + 6
            print("You have", character.energy, "energy left")
            time.sleep(0.5)
            continue
        if choice == "1":
            print("You swing your weapon at the enemy")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 1:
                enemy.health = enemy.health - character.strength
                character.energy = character.energy - 1
                print("You dealt 200 damage to", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health >0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "from", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "The Supreme Bean":
                        enemy.health = 2000
                        
                    time.sleep(0.7)
                    print ("You did it you beat the supreme Bean!")
                    time.sleep(0.5)
                    print("you can now to choose to kill or spare him")
                    time.sleep(0.5)
                    ending = input("1. Spare the Supreme Bean\n2. Finish him off ")
                    if ending == "1":
                        print("You decide to spare the supreme bean.")
                        time.sleep(0.5)
                        print("You exit the castle and all the inhabitants of the village")
                        time.sleep(0.5)
                        print("They grant you the rank of the General of the Bean Universe,")
                        time.sleep(0.5) 
                        print("with great pleasure you accept this title and begin to make a change in your new world.")
                        time.sleep(0.5)
                    if ending =="2":
                        print("You suddenly pass out...")
                        time.sleep(0.5)
                        print("you wake up in walmart in the tinned food isle, covered in Heinz Beans")
                        time.sleep(0.5)
                        print("It turns out that it was all a bad hallucination, that was caused by your hatred for beans.")
                        time.sleep(0.5)
                        print("You stand up but you are surrounded by people looking at you.")
                        time.sleep(0.5)
                        print("You caused a massive scene, the scene you caused was so big that upon waking up you are greeted by the police")
                        time.sleep(0.5)
                        print("You are arrested for damage of stock and property.")
                        time.sleep(0.5) 
                        print("Your hatrid of beans has gone too far this time")
                        time.sleep(0.5)
                    break
            else:
                print("You tried attacking", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 1
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)
                
        elif choice == "2":
            print("you charge up for your next attack")
            time.sleep(0.5)
            hitchance = random.randint(0,10)
            if hitchance > 1:
                enemy.health = enemy.health - character.charge
                character.energy = character.energy - 2
                print("Your charged attack dealt 400 damage to", enemy.name, "they now have", enemy.health, "health left")
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                if enemy.health > 0:
                    character.health = character.health - (enemy.str - character.defence)
                    print("You took" , enemy.str, "from", enemy.name,)
                    time.sleep(0.5)
                    print("but your defence negated", character.defence, "damage you now have", character.health, "health left")
                    time.sleep(0.5)
                    gameover(character, tins)
                    
                else:
                    if enemy.name == "The Supreme Bean":
                        enemy.health = 2000

                    
                    time.sleep(0.7)
                    print ("You did it you beat the supreme Bean!")
                    time.sleep(0.5)
                    print("you can now to choose to kill or spare him")
                    time.sleep(0.5)
                    ending = input("1. Spare the Supreme Bean\n2. Finish him off ")
                    if ending == "1":
                        print("You decide to spare the supreme bean.")
                        time.sleep(0.5)
                        print("You exit the castle and all the inhabitants of the village")
                        time.sleep(0.5)
                        print("They grant you the rank of the General of the Bean Universe,")
                        time.sleep(0.5) 
                        print("with great pleasure you accept this title and begin to make a change in your new world.")
                        time.sleep(0.5)
                    if ending =="2":
                        print("You suddenly pass out...")
                        time.sleep(0.5)
                        print("you wake up in walmart in the tinned food isle, covered in Heinz Beans")
                        time.sleep(0.5)
                        print("It turns out that it was all a bad hallucination, that was caused by your hatred for beans.")
                        time.sleep(0.5)
                        print("You stand up but you are surrounded by people looking at you.")
                        time.sleep(0.5)
                        print("You caused a massive scene, the scene you caused was so big that upon waking up you are greeted by the police")
                        time.sleep(0.5)
                        print("You are arrested for damage of stock and property.")
                        time.sleep(0.5) 
                        print("Your hatrid of beans has gone too far this time")
                        time.sleep(0.5)
                    break
            else:
                time.sleep(0.7)
                print("You tried attacking", enemy.name, "but it was able to dodge and attacks you while you are vulnerable")
                time.sleep(0.5)
                print("the", enemy.name, "hits you with all it's force dealing",enemy.crit,"damage")
                time.sleep(0.5)
                character.health = character.health - enemy.crit
                character.energy = character.energy - 2
                print("your current health is now", character.health)
                time.sleep(0.5)
                print("You have", character.energy, "energy left")
                time.sleep(0.5)
                gameover(character, tins)        
        elif choice != 1 or 2:
            print("That is an invalid input please select another option")
            time.sleep(0.5)
            continue

# SHOP SEQUENCES

def cvshop():
        global tins
        print("---------------------------------")
        print ("Welcome to the shop at Chickpea Village...")
        time.sleep(0.7)
        print("---------------------------------")
        print ("We have everything you need to continue your adventure!")
        time.sleep(0.7)
        print("---------------------------------")
        print ("Everything here costs just 15 Tins of Beans.")
        time.sleep(0.7)
        print("---------------------------------")
        print("You have", tins, "Tins of Beans")
        print("---------------------------------")
        print ("Enter the number of your choice:")
        choice111 = input("1 :> Health (Full Health) \n2 :> Defense (+5 Defense) \n3 :> Strength (+50 Strength) \n4 :> Energy (Full Energy) \n5 :> Nothing (I am Poor) \n:>>")
        time.sleep(0.7)
        print("---------------------------------")
        while choice111 != 1 or 2 or 3 or 4 or 5:
            if choice111 == "1":
                if tins >= 15:
                    character.health = 3000
                    tins -= 15
                    print("You purchased full health for 15 Tins of Beans")
                    print("You have", tins, "Tins of Beans")
                    print("---------------------------------")
                    return 1, cvshop2()
                else:
                    print("YOU DON'T HAVE ENOUGH TINS OF BEANS!")
                    print("---------------------------------")
                    choice111 = input("1 :> Health (Full Health) \n2 :> Defense (+5 Defense) \n3 :> Strength (+50 Strength) \n4 :> Energy (Full Energy) \n5 :> Nothing (I am Poor) \n:>>")
            elif choice111 == "2":
                if tins >= 15:
                    character.defence + 5
                    tins -= 15
                    print("You purchased Defense +5 for 15 Tins of Beans")
                    print("You have", tins, "Tins of Beans")
                    print("---------------------------------")
                    return 2, cvshop2()
                else:
                    print("YOU DON'T HAVE ENOUGH TINS OF BEANS!")
                    print("---------------------------------")
                    choice111 = input("1 :> Health (Full Health) \n2 :> Defense (+5 Defense) \n3 :> Strength (+50 Strength) \n4 :> Energy (Full Energy) \n5 :> Nothing (I am Poor) \n:>>")
            elif choice111 == "3":
                if tins >= 15:
                    character.strength + 50
                    tins -= 15
                    print("You purchased Strength +50 for 15 Tins of Beans")
                    print("You have", tins, "Tins of Beans")
                    print("---------------------------------")
                    return 3, cvshop2()
                else:
                    print("YOU DON'T HAVE ENOUGH TINS OF BEANS!")
                    print("---------------------------------")
                    choice111 = input("1 :> Health (Full Health) \n2 :> Defense (+5 Defense) \n3 :> Strength (+50 Strength) \n4 :> Energy (Full Energy) \n5 :> Nothing (I am Poor) \n:>>")
            elif choice111 == "4":
                if tins >= 15:
                    character.energy = 10
                    tins -= 15
                    print("You purchased full energy for 15 Tins of Beans")
                    print("You have", tins, "Tins of Beans")
                    print("---------------------------------")
                    return 4, cvshop2()
                else:
                    print("YOU DON'T HAVE ENOUGH TINS OF BEANS!")
                    print("---------------------------------")
                    choice111 = input("1 :> Health (Full Health) \n2 :> Defense (+5 Defense) \n3 :> Strength (+50 Strength) \n4 :> Energy (Full Energy) \n5 :> Nothing (I am Poor) \n:>>")
            elif choice111 == "5":
                print("Why so poor? Come back with more!")
                return 5, lshop()
            elif choice111 != 1 or 2 or 3 or 4 or 5:
                print("That is an invalid input please select another option")
                choice111 = input("1 :> Health (Full Health) \n2 :> Defense (+5 Defense) \n3 :> Strength (+50 Strength) \n4 :> Energy (Full Energy) \n5 :> Nothing (I am Poor) \n:>>")

def cvshop2():
    global tins
    time.sleep(0.7)
    print("---------------------------------")
    print ("Would you like to buy anything else?")
    time.sleep(0.5)
    print("---------------------------------")
    print ("Enter the number of your choice:")
    choice1 = input("1 :> Yes \n2 :> No \n:>>")
    time.sleep(0.7)
    print("---------------------------------")
    while choice1 != 1 or 2:
        if choice1 == "1":
                print("More shopping! YAY!")
                print("You have", tins, "Tins of Beans")
                print("---------------------------------")
                return 1, cvshop()
        elif choice1 == "2":
                print("Awww, no more shopping, shopkeeper very sad...")
                print("You have", tins, "Tins of Beans")
                print("---------------------------------")
                return 2, lshop2()
        elif choice1 != 1 or 2:
            print("That is an invalid input please select another option")
            choice = input("1 :> Yes \n2 :> No \n:>>")

def lshop():
    global tins
    print("---------------------------------")
    print ("Where would you like to go instead?")
    print("---------------------------------")
    print ("Enter the number of your choice:")
    choice11 = input("1. Pinto Fields :> \n2. Broad Mountains :> \n:>>")
    time.sleep(0.7)
    print("---------------------------------")
    while choice11 != 1 or 2:
        if choice11 == "1":
            print("Pinto Fields awaits!")
            print("---------------------------------")
            tins = battlestate3(tins)
            print("You now have", tins, "Tins of Beans")
            tins = battlestate4(tins)
            print("You now have", tins, "Tins of Beans")
            choice2=input("Choose your Path\n1. Cannellini Plaza\n2. Fava Castle\n3. Lentil Forest\n4. Shop at Chickpea Village\n:>> ")
            if choice2 == "1":
                time.sleep(1)
                print(Fore.GREEN)
                print("  ___                         _  _  _        _        ___  _  ")               
                print(" / __| __ _  _ _   _ _   ___ | || |(_) _ _  (_)      | _ \| | __ _  ___ __ _ ")
                print("| (__ / _` || ' \ | ' \ / -_)| || || || ' \ | |      |  _/| |/ _` ||_ // _` |")
                print(" \___|\__/_||_||_||_||_|\___||_||_||_||_||_||_|      |_|  |_|\__/_|/__|\__/_|")
                time.sleep(1.5)
                print("Heading to canellini plaza,") 
                print("what used to be a town is now a empty and dead town vines hanging from all the buildings and overgrown floras plauge the area.")
                time.sleep(1)
                tins = battlestate5(tins)
                print("You now have", tins, "Tins of Beans")
                tins = battlestate6(tins)
                print("You now have", tins, "Tins of Beans")
                tins = bossbattlestate(tins)
                print("Thank you for playing our game")
                break
            if choice2 =="2":
                time.sleep(1)
                print(Fore.LIGHTMAGENTA_EX)
                print(" ___                          ___            _    _ ")     
                print("| __| __ _ __ __ __ _        / __| __ _  ___| |_ | | ___ ")
                print("| _| / _` |\ V // _` |      | (__ / _` |(_-/|  _|| |/ -_)")
                print("|_|  \__/_| \_/ \__/_|       \___|\__/_|/__/ \__||_|\___|")
                time.sleep(1.5)
                print("Heading to fava castle, home to the royal family of beans including queen elizapea the III. watch out for the guards")
                time.sleep(1)
                tins = battlestate9(tins)
                print("You now have", tins, "Tins of Beans")
                tins = battlestate10(tins)
                print("You now have", tins, "Tins of Beans")
                tins = bossbattlestate(tins)
                print("Thank you for playing our game")
                break
            if choice2 == "3":
                time.sleep(1)
                print(Fore.BLUE)
                print(" _             _    _  _         __                     _ ")  
                print("| | ___  _ _  | |_ (_)| |       / _| ___  _ _  ___  ___| |_ ")
                print("| |/ -_)| ' \ |  _|| || |      |  _|/ _ \| '_|/ -_)(_-/|  _|")
                print("|_|\___||_||_| \__||_||_|      |_|  \___/|_|  \___|/__/ \__|")
                time.sleep(1.5)
                print("Heading to the lentil forest, lentil forest while quite peacefull is treacherous and filled with traps.")
                print("Be careful not to fall into a trap of the bean tribes.")
                time.sleep(1)
                tins = battlestate11(tins)
                print("You now have", tins, "Tins of Beans")
                tins = battlestate12(tins)
                print("You now have", tins, "Tins of Beans")
                tins = bossbattlestate(tins)
                print("Thank you for playing our game")
                break
            if choice2 == "4":
                time.sleep(1)
                print(Fore.YELLOW)
                print("     _     _      _    _ __                        _  _  _        __ _ ")     
                print(" __ | |_  (_) __ | |__| '_ \ ___  __ _       __ __(_)| || | __ _ / _` | ___ ")
                print("/ _||   \ | |/ _|| / /| .__// -_)/ _` |      \ V /| || || |/ _` |\__. |/ -_)")
                print("\__||_||_||_|\__||_\_\|_|   \___|\__/_|       \_/ |_||_||_|\__/_||___/ \___|")
                time.sleep(1.5)
                print("heading to chickpea Village, filled with non savage beans and the mighty bean wizard.")
                time.sleep(1)
                print("barter with the villagers with your tinned beans, and maybe visit the wizard for some health retrival")
                tins = cvshop()
            return 1
        elif choice11 == "2":
            print("Broad Mountains awaits!")
            print("---------------------------------")
            tins = battlestate7(tins)
            print("You now have", tins, "Tins of Beans")
            tins = battlestate8(tins)
            print("You now have", tins, "Tins of Beans")
            choice3=input("Choose your Path\n1. Cannellini Plaza\n2. Fava Castle\n3. Lentil Forest\n4. Shop at Chickpea Village\n:>>")
            if choice3 == "1":
                time.sleep(1)
                print(Fore.GREEN)
                print("  ___                         _  _  _        _        ___  _  ")               
                print(" / __| __ _  _ _   _ _   ___ | || |(_) _ _  (_)      | _ \| | __ _  ___ __ _ ")
                print("| (__ / _` || ' \ | ' \ / -_)| || || || ' \ | |      |  _/| |/ _` ||_ // _` |")
                print(" \___|\__/_||_||_||_||_|\___||_||_||_||_||_||_|      |_|  |_|\__/_|/__|\__/_|")
                time.sleep(1.5)
                print("Heading to canellini plaza,")
                time.sleep(1)
                print("what used to be a town is now a empty and dead town vines hanging from all the buildings and overgrown floras plauge the area.")
                time.sleep(1)
                tins = battlestate5(tins)
                print("You now have", tins, "Tins of Beans")
                tins = battlestate6(tins)
                print("You now have", tins, "Tins of Beans")
                tins = bossbattlestate(tins)
                print("Thank you for playing our game")
                break
            if choice3 =="2":
                time.sleep(1)
                print(Fore.LIGHTMAGENTA_EX)
                print(" ___                          ___            _    _ ")     
                print("| __| __ _ __ __ __ _        / __| __ _  ___| |_ | | ___ ")
                print("| _| / _` |\ V // _` |      | (__ / _` |(_-/|  _|| |/ -_)")
                print("|_|  \__/_| \_/ \__/_|       \___|\__/_|/__/ \__||_|\___|")
                time.sleep(1.5)
                print("Heading to fava castle, home to the royal family of beans including queen elizapea the III. watch out for the guards")
                time.sleep(1)
                tins = battlestate9(tins)
                print("You now have", tins, "Tins of Beans")
                tins = battlestate10(tins)
                print("You now have", tins, "Tins of Beans")
                tins = bossbattlestate(tins)
                print("Thank you for playing our game")
                break
            if choice3 == "3":
                time.sleep(1)
                print(Fore.BLUE)
                print(" _             _    _  _         __                     _ ")  
                print("| | ___  _ _  | |_ (_)| |       / _| ___  _ _  ___  ___| |_ ")
                print("| |/ -_)| ' \ |  _|| || |      |  _|/ _ \| '_|/ -_)(_-/|  _|")
                print("|_|\___||_||_| \__||_||_|      |_|  \___/|_|  \___|/__/ \__|")
                time.sleep(1.5)
                print("Heading to the lentil forest, lentil forest while quite peacefull is treacherous and filled with traps.")
                time.sleep(1)
                print("Be careful not to fall into a trap of the bean tribes.")
                time.sleep(1)
                tins = battlestate11(tins)
                print("You now have", tins, "Tins of Beans")
                tins = battlestate12(tins)
                print("You now have", tins, "Tins of Beans")
                tins = bossbattlestate(tins)
                print("Thank you for playing our game")
                break
            if choice3 == "4":
                time.sleep(1)
                print(Fore.YELLOW)
                print("     _     _      _    _ __                        _  _  _        __ _ ")     
                print(" __ | |_  (_) __ | |__| '_ \ ___  __ _       __ __(_)| || | __ _ / _` | ___ ")
                print("/ _||   \ | |/ _|| / /| .__// -_)/ _` |      \ V /| || || |/ _` |\__. |/ -_)")
                print("\__||_||_||_|\__||_\_\|_|   \___|\__/_|       \_/ |_||_||_|\__/_||___/ \___|")
                time.sleep(1.5)
                print("heading to chickpea Village, filled with non savage beans and the mighty bean wizard.")
                time.sleep(1) 
                print("barter with the villagers with your tinned beans, and maybe visit the wizard for some health retrival")
                time.sleep(1)
                tins = cvshop()
            return 2
        elif choice11 != 1 or 2:
            print("That is an invalid input please select another option")
            choice11 = input("1. Pinto Fields :> \n2. Broad Mountains :> \n:>>")  

def lshop2():
    global tins
    print("---------------------------------")
    print ("Where would you like to go instead?")
    print("---------------------------------")
    print ("Enter the number of your choice:")
    choice112 = input("1. Cannelinni Plaza :> \n2. Fava Castle :> \n3. Lentil Forest:> ")
    time.sleep(0.7)
    print("---------------------------------")
    while choice112 != 1 or 2 or 3:
        if choice112 == "1":
            time.sleep(1)
            print(Fore.GREEN)
            print("  ___                         _  _  _        _        ___  _  ")               
            print(" / __| __ _  _ _   _ _   ___ | || |(_) _ _  (_)      | _ \| | __ _  ___ __ _ ")
            print("| (__ / _` || ' \ | ' \ / -_)| || || || ' \ | |      |  _/| |/ _` ||_ // _` |")
            print(" \___|\__/_||_||_||_||_|\___||_||_||_||_||_||_|      |_|  |_|\__/_|/__|\__/_|")
            time.sleep(1.5)
            print("Heading to canellini plaza,") 
            print("what used to be a town is now a empty and dead town vines hanging from all the buildings and overgrown floras plauge the area.")
            time.sleep(1)
            tins = battlestate5(tins)
            print("You now have", tins, "Tins of Beans")
            tins = battlestate6(tins)
            print("You now have", tins, "Tins of Beans")
            tins = bossbattlestate(tins)
            print("Thank you for playing our game")
            break
        if choice112 =="2":
            time.sleep(1)
            print(Fore.LIGHTMAGENTA_EX)
            print(" ___                          ___            _    _ ")     
            print("| __| __ _ __ __ __ _        / __| __ _  ___| |_ | | ___ ")
            print("| _| / _` |\ V // _` |      | (__ / _` |(_-/|  _|| |/ -_)")
            print("|_|  \__/_| \_/ \__/_|       \___|\__/_|/__/ \__||_|\___|")
            time.sleep(1.5)
            print("Heading to fava castle, home to the royal family of beans including queen elizapea the III. watch out for the guards")
            time.sleep(1)
            tins = battlestate9(tins)
            print("You now have", tins, "Tins of Beans")
            tins = battlestate10(tins)
            print("You now have", tins, "Tins of Beans")
            tins = bossbattlestate(tins)
            print("Thank you for playing our game")
            break
        if choice112 == "3":
            time.sleep(1)
            print(Fore.BLUE)
            print(" _             _    _  _         __                     _ ")  
            print("| | ___  _ _  | |_ (_)| |       / _| ___  _ _  ___  ___| |_ ")
            print("| |/ -_)| ' \ |  _|| || |      |  _|/ _ \| '_|/ -_)(_-/|  _|")
            print("|_|\___||_||_| \__||_||_|      |_|  \___/|_|  \___|/__/ \__|")
            time.sleep(1.5)
            print("Heading to the lentil forest, lentil forest while quite peacefull is treacherous and filled with traps.")
            print("Be careful not to fall into a trap of the bean tribes.")
            time.sleep(1)
            tins = battlestate11(tins)
            print("You now have", tins, "Tins of Beans")
            tins = battlestate12(tins)
            print("You now have", tins, "Tins of Beans")
            tins = bossbattlestate(tins)
            print("Thank you for playing our game")
            break


# SHOP SEQUENCES

tins = 0
character = heroselect()
tins = battlestate1(tins)
print("You now have" , tins, "Tins of beans")
tins = battlestate2(tins)
print("You now have", tins, "Tins of Beans")
choice=input("Choose your Path\n1. Pinto Fields\n2. Broad Mountain ")
if choice == "1":
    time.sleep(1)
    print(Fore.LIGHTGREEN_EX)
    print(" _ __  _        _                __  _       _     _ ")    
    print("| '_ \(_) _ _  | |_  ___        / _|(_) ___ | | __| | ___")
    print("| .__/| || ' \ |  _|/ _ \      |  _|| |/ -_)| |/ _` |(_-/")
    print("|_|   |_||_||_| \__|\___/      |_|  |_|\___||_|\__/_|/__/")
    time.sleep(1.5)
    print("Heading to the pinto fields, the fields are empty and desolate.")
    time.sleep(1)
    print("Swarms of reckless beans alike fly,crawl and sprint threw this area")
    time.sleep(1)
    tins = battlestate3(tins)
    print("You now have", tins, "Tins of Beans")
    tins = battlestate4(tins)
    print("You now have", tins, "Tins of Beans")
    choice2=input("Choose your Path\n1. Cannellini Plaza\n2. Fava Castle\n3. Lentil Forest\n4. Shop at Chickpea Village\n:>> ")
    if choice2 == "1":
        time.sleep(1)
        print(Fore.GREEN)
        print("  ___                         _  _  _        _        ___  _  ")               
        print(" / __| __ _  _ _   _ _   ___ | || |(_) _ _  (_)      | _ \| | __ _  ___ __ _ ")
        print("| (__ / _` || ' \ | ' \ / -_)| || || || ' \ | |      |  _/| |/ _` ||_ // _` |")
        print(" \___|\__/_||_||_||_||_|\___||_||_||_||_||_||_|      |_|  |_|\__/_|/__|\__/_|")
        time.sleep(1.5)
        print("Heading to canellini plaza,") 
        time.sleep(1)
        print("what used to be a town is now a empty and dead town vines hanging from all the buildings and overgrown floras plauge the area.")
        time.sleep(1)
        tins = battlestate5(tins)
        print("You now have", tins, "Tins of Beans")
        tins = battlestate6(tins)
        print("You now have", tins, "Tins of Beans")
        tins = bossbattlestate(tins)
        print("Thank you for playing our game")
    if choice2 =="2":
        time.sleep(1)
        print(Fore.LIGHTMAGENTA_EX)
        print(" ___                          ___            _    _ ")     
        print("| __| __ _ __ __ __ _        / __| __ _  ___| |_ | | ___ ")
        print("| _| / _` |\ V // _` |      | (__ / _` |(_-/|  _|| |/ -_)")
        print("|_|  \__/_| \_/ \__/_|       \___|\__/_|/__/ \__||_|\___|")
        time.sleep(1.5)
        print("Heading to fava castle, home to the royal family of beans including queen elizapea the III. watch out for the guards")
        time.sleep(1)
        tins = battlestate9(tins)
        print("You now have", tins, "Tins of Beans")
        tins = battlestate10(tins)
        print("You now have", tins, "Tins of Beans")
        tins = bossbattlestate(tins)
        print("Thank you for playing our game")
    if choice2 == "3":
        time.sleep(1)
        print(Fore.BLUE)
        print(" _             _    _  _         __                     _ ")  
        print("| | ___  _ _  | |_ (_)| |       / _| ___  _ _  ___  ___| |_ ")
        print("| |/ -_)| ' \ |  _|| || |      |  _|/ _ \| '_|/ -_)(_-/|  _|")
        print("|_|\___||_||_| \__||_||_|      |_|  \___/|_|  \___|/__/ \__|")
        time.sleep(1.5)
        print("Heading to the lentil forest, lentil forest while quite peacefull is treacherous and filled with traps.")
        time.sleep(1)
        print("Be careful not to fall into a trap of the bean tribes.")
        time.sleep(1)
        tins = battlestate11(tins)
        print("You now have", tins, "Tins of Beans")
        tins = battlestate12(tins)
        print("You now have", tins, "Tins of Beans")
        tins = bossbattlestate(tins)
        print("Thank you for playing our game")
    if choice2 == "4":
        time.sleep(1)
        print(Fore.YELLOW)
        print("     _     _      _    _ __                        _  _  _        __ _ ")     
        print(" __ | |_  (_) __ | |__| '_ \ ___  __ _       __ __(_)| || | __ _ / _` | ___ ")
        print("/ _||   \ | |/ _|| / /| .__// -_)/ _` |      \ V /| || || |/ _` |\__. |/ -_)")
        print("\__||_||_||_|\__||_\_\|_|   \___|\__/_|       \_/ |_||_||_|\__/_||___/ \___|")
        time.sleep(1.5)
        print("heading to chickpea Village, filled with non savage beans and the mighty bean wizard.")
        time.sleep(1)
        print("barter with the villagers with your tinned beans, and maybe visit the wizard for some health retrival")
        time.sleep(1)
        tins = cvshop()
elif choice == "2":
    time.sleep(1)
    print(Fore.LIGHTBLUE_EX)
    print(" _                        _                                _          _        ")  
    print("| |__  _ _  ___  __ _  __| |       _ __   ___  _  _  _ _  | |_  __ _ (_) _ _   ___")
    print("|  _ \| '_|/ _ \/ _` |/ _` |      | '  \ / _ \| || || ' \ |  _|/ _` || || ' \ (_-/")
    print("|____/|_|  \___/\__/_|\__/_|      |_|_|_|\___/ \_._||_||_| \__|\__/_||_||_||_|/__/")
    time.sleep(1.5)
    print("Heading to the broad mountains, the air is cold and the view of the realm is almost breathtaking. dont trip!")
    time.sleep(1)
    tins = battlestate7(tins)
    print("You now have", tins, "Tins of Beans")
    tins = battlestate8(tins)
    print("You now have", tins, "Tins of Beans")
    time.sleep(1) 
    choice3=input("Choose your Path\n1. Cannellini Plaza\n2. Fava Castle\n3. Lentil Forest\n4. Shop at Chickpea Village\n:>>")
    if choice3 == "1":
        time.sleep(1)
        print(Fore.GREEN)
        print("  ___                         _  _  _        _        ___  _  ")               
        print(" / __| __ _  _ _   _ _   ___ | || |(_) _ _  (_)      | _ \| | __ _  ___ __ _ ")
        print("| (__ / _` || ' \ | ' \ / -_)| || || || ' \ | |      |  _/| |/ _` ||_ // _` |")
        print(" \___|\__/_||_||_||_||_|\___||_||_||_||_||_||_|      |_|  |_|\__/_|/__|\__/_|")
        time.sleep(1.5)
        print("Heading to canellini plaza,")
        time.sleep(1)
        print("what used to be a town is now a empty and dead town vines hanging from all the buildings and overgrown floras plauge the area.")
        time.sleep(1)
        tins = battlestate5(tins)
        print("You now have", tins, "Tins of Beans")
        tins = battlestate6(tins)
        print("You now have", tins, "Tins of Beans")
        tins = bossbattlestate(tins)
        print("Thank you for playing our game")
    if choice3 =="2":
        time.sleep(1)
        print(Fore.LIGHTMAGENTA_EX)
        print(" ___                          ___            _    _ ")     
        print("| __| __ _ __ __ __ _        / __| __ _  ___| |_ | | ___ ")
        print("| _| / _` |\ V // _` |      | (__ / _` |(_-/|  _|| |/ -_)")
        print("|_|  \__/_| \_/ \__/_|       \___|\__/_|/__/ \__||_|\___|")
        time.sleep(1.5)
        print("Heading to fava castle, home to the royal family of beans including queen elizapea the III. watch out for the guards")
        time.sleep(1)
        tins = battlestate9(tins)
        print("You now have", tins, "Tins of Beans")
        tins = battlestate10(tins)
        print("You now have", tins, "Tins of Beans")
        tins = bossbattlestate(tins)
        print("Thank you for playing our game")
    if choice3 == "3":
        time.sleep(1)
        print(Fore.BLUE)
        print(" _             _    _  _         __                     _ ")  
        print("| | ___  _ _  | |_ (_)| |       / _| ___  _ _  ___  ___| |_ ")
        print("| |/ -_)| ' \ |  _|| || |      |  _|/ _ \| '_|/ -_)(_-/|  _|")
        print("|_|\___||_||_| \__||_||_|      |_|  \___/|_|  \___|/__/ \__|")
        time.sleep(1.5)
        print("Heading to the lentil forest, lentil forest while quite peacefull is treacherous and filled with traps.")
        time.sleep(1)
        print("Be careful not to fall into a trap of the bean tribes.")
        time.sleep(1)
        tins = battlestate11(tins)
        print("You now have", tins, "Tins of Beans")
        tins = battlestate12(tins)
        print("You now have", tins, "Tins of Beans")
        tins = bossbattlestate(tins)
        print("Thank you for playing our game")
    if choice3 == "4":
        time.sleep(1)
        print(Fore.YELLOW)
        print("     _     _      _    _ __                        _  _  _        __ _ ")     
        print(" __ | |_  (_) __ | |__| '_ \ ___  __ _       __ __(_)| || | __ _ / _` | ___ ")
        print("/ _||   \ | |/ _|| / /| .__// -_)/ _` |      \ V /| || || |/ _` |\__. |/ -_)")
        print("\__||_||_||_|\__||_\_\|_|   \___|\__/_|       \_/ |_||_||_|\__/_||___/ \___|")
        time.sleep(1.5)
        print("heading to chickpea Village, filled with non savage beans and the mighty bean wizard.") 
        time.sleep(1)
        print("barter with the villagers with your tinned beans, and maybe visit the wizard for some health retrival")
        time.sleep(1)
        tins = cvshop()