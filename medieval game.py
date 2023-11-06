from time import sleep
from random import *
from random import randint
#medieval
global HPup
HPup = False
global health
health = 100
global dmg
dmg = 10
print("you are a kninght and need to save a princess from the red dragon! you can choose things and encounter other dangers so you have to be carefull! you start with a stone sword that does 10 damage and you have 100 hearts. and to choose just type the number of the choice.")
sleep(5)

def Goblin():
    print("")
    global alive
    alive = True
    Gh = randint(80, 100)
    if HPup == True:
        health = 150
    else:
        health = 100
    while True and alive == True:
        sleep(1)
        goblin_attack = randint(8,15)
        if Gh == 10 or Gh < 0:
            print("you deafeated the goblin")
            break
        elif health < 1:
            print("You were defeated by the goblin")
            exit()
        fr = input("1. Fight. 2. Heal ")
        if fr == "1":
            Gh = Gh - dmg
            print("you deal", dmg,  "Damage! the goblin has", Gh, "HP left")
            sleep(1)
            health = health - goblin_attack
            print("the goblin attacked you. -",goblin_attack, "HP, you have", health, "left")
        elif fr == "2":
            if health < 81:
                health = health + 20
                print("You healed 20 HP you have", health, "HP")
                sleep(1)
                health = health - 10
                print("the goblin attacked you. -",goblin_attack, "HP, you have", health, "left")
            elif health < 121 and HPup == True:
                health = health + 30
                sleep(1)
                health = health - 10
                print("the goblin attacked you. -",goblin_attack, "HP, you have", health, "left")
            elif health > 80 and HPup == False:
                health = 100
                print("You healed to full HP")
                sleep(1)
                health = health - 10
                print("the goblin attacked you. -",goblin_attack, "HP, you have", health, "left")
            elif health > 120 and HPup == True:
                health = 150
                print("You healed to full HP")
                sleep(1)
                health = health - 10
                print("the goblin attacked you. -",goblin_attack, "HP, you have", health, "left")
            else:
                print("You couldnt heal you already have full health")
                sleep(1)
                health = health - 10
                print("the goblin attacked you. -",goblin_attack, "HP, you have", health, "left")


def outside1():
    print("")
    while True:
        sleep(1)
        print("you go outside and see a goblin!")
        sleep(1)
        fight1 = input("1. run away. 2. FIGHT! ")
        if fight1 == "1":
            print("you were caught")
            Goblin()
            break
        elif fight1 == "2":
            print("you challange the goblin")
            break


def choice1():
    print("")
    while True:
        housechoice = input("you are in a house what do you do? (1. look in the chest for gear. (2. sleep. (3. go outside. ")
        if housechoice == "1":
            print("You got a healing potion")
        elif housechoice == "2":
            print("you chose to sleep.")
            sleep(1)
            print("When you wake up you see that your roof is gone! and you suddenly see a Giant! You know that you cant defeat it so run")
            break
        elif housechoice == "3":
            print("you open the door")
            break
def dark_path():
    print("")
    while True:
        sleep(1)
        print("apperently this is the safe path! you walk the dark path and come to a castle.")
        break

def light_path():
    print("")
    while True:
        sleep(1)
        print("While you walk on the path you are being jumped by a goblin")
        Goblin()
        print("When you defeated the goblin you see a castle!")
        break

choice1()
outside1()
Goblin()
sleep(1)

def outsidechoice1():
    print("")
    while True:
        splitpath = input("you are now in the woods! You follow the path and the path splits up in 2! Do you follow the path to the dark (1)? or do you follow the path to the light (2)? ")
        if splitpath == "1":
            dark_path()
            break
        elif splitpath == "2":
            light_path()
            break
outsidechoice1()

def orc():
    print("")
    alive = True
    Oh = randint(100, 150)
    if HPup == True:
        health = 150
    else:
        health = 100
    while True and alive == True:
        sleep(1) 
        orc_attack = randint(15,35)
        if Oh == 10 or Oh < 0:
            print("you deafeated the orc")
            break
        elif health < 1:
            print("You were defeated by the orc")
            exit()
        orcc = input("1. Fight. 2. Heal ")
        if orcc == "1":
            Oh = Oh - dmg
            print("you deal", dmg,  "Damage! the Orc has", Oh, "HP left")
            sleep(1)
            health = health - orc_attack
            print("the Orc attacked you. -",orc_attack, "HP, you have", health, "left")
        elif orcc == "2":
            if health < 81 and HPup == False:
                health = health + 20
                print("You healed 20 HP you have", health, "HP")
                sleep(1)
                health = health - orc_attack
                print("the Orc attacked you. -",orc_attack, "HP, you have", health, "left")
            elif health < 121 and HPup == True:
                health = health + 30
                print("You healed 30 HP you have", health, "HP")
                sleep(1)
                health = health - orc_attack
                print("the Orc attacked you. -",orc_attack, "HP, you have", health, "left")
            elif health > 80 and HPup == False:
                health = 100
                print("You healed to full HP")
                sleep(1)
                health = health - orc_attack
                print("the Orc attacked you. -",orc_attack, "HP, you have", health, "left")
            elif health > 120 and HPup == True:
                health = 150
                print("You healed to full HP")
                sleep(1)
                health = health - orc_attack
                print("the Orc attacked you. -",orc_attack, "HP, you have", health, "left")
            else:
                print("You couldnt heal you already have full health")
                sleep(1)
                health = health - orc_attack
                print("the Orc attacked you. -",orc_attack, "HP, you have", health, "left")


def gate():
    print("")
    print("You go through the gate.")
    sleep(1)
    print("You are now inside the castle and you see a door and stairs.")
    while True:
        sleep(1)
        incastle = input("Do you go through the door (1) or up the stairs (2)? ")
        if incastle == "1":
            print("")
            print("You open the door and behind the door is an Orc!")
            sleep(1)
            Orc = input("Do you walk away and hope he didnt see you (1) or FIGHT! (2)? ")
            if Orc == "1":
                print("")
                print("He didn't see you and you are save!")
                sleep(1)
            elif Orc == "2":
                print("")
                print("you decide to fight him!")
                orc()
        elif incastle == "2":
            print("")
            print("You go upstairs and a big shadow comes closer to you.")
            sleep(1)
            print("You also see a cage with someone in it.")
            sleep(1)
            print("The princess in it it!")
            sleep(1)
            print("The shadow is gone but instead there is the red dragon!")
            sleep(1)
            print("The dragon sees you! Time for battle.")
            break


def aroundcastle1():
    print("")
    while True:
        sleep(1)
        print("You found a chest and inside there is a heart. When you pick up the heart the heart Disappears and you feel stronger.")
        sleep(2)
        health = 150
        print("+50 HP. you now have", health, "HP.")
        global HPup
        HPup = True
        sleep(1)
        further = input("do you want to go back (1) or keep going (2)? ")
        if further == "1":
            print("you head back to the gate.")
            HPup = True
            break
        elif further == "2":
            HPup = True
            print("you decide to go further around the castle.")
            sleep(1)
            print("You come across a Goblin! Quickly defeat him before he alarms anyone!")
            Goblin()
            sleep(1)
            print("Good job you defeated him.")
            sleep(1)
            aroundcastle = input("Do you want to head back (1) or go further (2)? ")
            if aroundcastle == "1":
                print("you head back to the gate.")
                break
            elif aroundcastle == "2":
                print("you find a big and heavy steel sword.")
                global dmg
                dmg = 20
                sleep(1)
                print("You now do", dmg, "damage")
                sleep(1)
                print("You went all around the castle so now you are back at the gate.")
                break

def castle1():
    print("")
    while True:
        forcastle = input("Do you want to go through the gate (1) or walk around the castle (2)? ")
        if forcastle == "1":
            print("you decide to go through the gate.")
            gate()
            break
        elif forcastle == "2":
            print("You walk around the castle.")
            aroundcastle1()
sleep(1.5)
print("You walk to the castle.")
castle1()

def dragon_fight():
    print("")
    Dh = 200
    alive = True
    if HPup == True:
        health = 150
    else:
        health = 100
    while True and alive == True:
        sleep(1)
        dragon_attack = randint(20,33)
        if Dh == 10 or Dh < 0:
            print("you deafeated the Dragon")
            break
        elif health < 1:
            print("You were defeated by the Dragon")
            exit()
        fr = input("1. Fight. 2. Heal ")
        if fr == "1":
            Dh = Dh - dmg
            print("you deal", dmg,  "Damage! the Dragon has", Dh, "HP left")
            sleep(1)
            health = health - dragon_attack
            print("the Dragon attacked you. -",dragon_attack, "HP, you have", health, "left")
        elif fr == "2":
            if health < 81 and HPup == False:
                health = health + 20
                print("You healed 20 HP you have", health, "HP")
                sleep(1)
                health = health - dragon_attack
                print("the Dragon attacked you. -",dragon_attack, "HP, you have", health, "left")
            elif health < 121 and HPup == True:
                health = health + 30
                print("You healed 30 HP you have", health, "HP")
                sleep(1)
                health = health - dragon_attack
                print("the Dragon attacked you. -",dragon_attack, "HP, you have", health, "left")
            elif health > 80 and HPup == False:
                health = 100
                print("You healed to full HP")
                sleep(1)
                health = health - dragon_attack
                print("the Dragon attacked you. -",dragon_attack, "HP, you have", health, "left")
            elif health > 120 and HPup == True:
                health = 150
                print("You healed to full HP")
                sleep(1)
                health = health - dragon_attack
                print("the Dragon attacked you. -",dragon_attack, "HP, you have", health, "left")
            else:
                print("You couldnt heal you already have full health")
                sleep(1)
                health = health - dragon_attack
                print("the Dragon attacked you. -",dragon_attack, "HP, you have", health, "left")
dragon_fight()

def notmarry():
    print("")
    while True:
        sleep(1)
        print("She walks to a room in the castle and locks you in that room.")
        sleep(1)
        print("everyday she comes to you and gives you food and water.")
        sleep(1)
        print("one day she wants kids and decides to rape you.")
        sleep(1)
        print("she does that until she has 3 childeren.")
        sleep(1)
        print("she and her kids live a happy life.")
        sleep(1)
        print("But you...")
        sleep(0.5)
        print("well you arent so happy.")
        break


def marry():
    print("")
    while True:
        sleep(1)
        print("you guys live together and have 3 kids.")
        sleep(1)
        print("and you live long and happily.")
        break


def princess():
    print("")
    while True:
        sleep(1)
        print("The princess wants to marry you!")
        marryh = input("do you want to marry her (1) or not (2)? ")
        if marryh == "1":
            print("You want to marry her and so you say yes")
            marry()
            break
        elif marryh == "2":
            print("she is mad at you and picks you up.")
            notmarry()
            break
print("")
print("You got a key from the dragon!")
sleep(1)
key = input("Do you want to use the key on the cage to free the princess (1) or leave the princess (2)? ")
if key == "1":
    print("Nice you freed the princess")
elif key == "2":
    print("The princess is mad and breaks the bars.")
    sleep(1)
    print("The princess walks up to you.")
princess()
print("but then you wake up!")
sleep(1)
print("and then you relise it was all a dream!")