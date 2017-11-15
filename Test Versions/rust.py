import sys,os,random,time
#https://www.youtube.com/watch?v=8F2MAJEeKjw

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.damage = 6
        self.weap = ["Rock"]
        self.curweap = ["Rock"]
        self.invis_inv = {"rockh":1,"rockp":1}
        self.materials = {" ":0,"wood":0,"stone":0,"metal":0,"cloth":0,"fuel":0,"animal_fat":0}
        self.ores = {"metal_ore":0}
        self.weapons = {"Rock":1,"Bow":0,"Semi Auto":0,"Ak47":0}
        self.ammo = {"arrow":0,"5.56":0}
        self.base = {"furnace":0}
        self.crafting = {"sp":0,"sh":0,"mp":0,"mh":0}
        
    @property
    def attack(self):
        attack = self.damage
        if self.curweap == "Rock":
            attack += 4
        elif self.curweap == "Bow":
            attack += 16
        elif self.curweap == "Semi Auto":
            attack += 26
        elif self.curweap == "Ak47":
            attack += 40
        return attack

class Dear:
    def __init__(self):
        self.name = "Dear"
        self.maxhealth = 80
        self.health = self.maxhealth
        self.cloth = 200
        self.animalfat = 200
        self.damage = 2
class Boar:
    def __init__(self):
        self.name = "Boar"
        self.maxhealth = 70
        self.health = self.maxhealth
        self.cloth = 200
        self.animalfat = 300
        self.damage = 10

def farming(name,list1,res1,list2,res2,n,n2,t,name2):
    print("Farming...")
    list1[res1]+=n
    list2[res2]+=n2
    time.sleep(t)
    print(name,"+",n)
    print(name2,"+",n2)
        
def start():
    while True:
        option = input("\n1.)Player Info\n2.)Farm\n3.)Hunt\n4.)Craft\n5.)Smelt\n6.)Base\n7.)Exit\n>>>")
        if option == "1":
            print("=INFO=Name:{}\nDamage:{}\nHealth:{}\nCurrent Weapon Equiped:{}".format(PlayerIG.name, PlayerIG.damage,PlayerIG.health,PlayerIG.curweap))
            print("-=INVENTORY=-\n=MATERIALS=\nWood:",PlayerIG.materials["wood"],"\nStone:",PlayerIG.materials["stone"],"\nMetal:",PlayerIG.materials["metal"],"\nCloth:",PlayerIG.materials["cloth"],"\nFuel:",PlayerIG.materials["fuel"],"\nAnimal Fat:",PlayerIG.materials["animal_fat"])
            print("=ORES=\nMetal Ore:",PlayerIG.ores["metal_ore"])
            
        elif option == "2":
            while True:
                cic = input("=FARMING=\n1.)Wood\n2.)Stone\n3.)Cloth\nb.)Back\n>>>")
                if cic == "1":
                    if PlayerIG.invis_inv["rockh"] == 1:
                        farming("Wood",PlayerIG.materials,"wood",PlayerIG.materials," ",100,0,3," ")
                    elif PlayerIG.crafting["sh"] == 1:
                        farming("Wood",PlayerIG.materials,"wood",PlayerIG.materials," ",200,0,2," ")
                    elif PlayerIG.crafting["mh"] == 1:
                        farming("Wood",PlayerIG.materials,"wood",PlayerIG.materials," ",450,0,1," ")

                elif cic == "2":
                    if PlayerIG.invis_inv["rockp"] == 1:
                        farming("Stone",PlayerIG.materials,"stone",PlayerIG.ores,"metal_ore",100,20,3,"Metal Ore")
                    elif PlayerIG.crafting["sp"] == 1:
                        farming("Stone",PlayerIG.materials,"stone",PlayerIG.ores,"metal_ore",200,35,2,"Metal Ore")
                    elif PlayerIG.crafting["mp"] == 1:
                        farming("Stone",PlayerIG.materials,"stone",PlayerIG.ores,"metal_ore",300,50,1,"Metal Ore")
                elif cic == "3":
                     farming("Cloth",PlayerIG.materials,"cloth",PlayerIG.materials," ",10,0,1," ")
                elif cic == "b":
                    break
                    
        elif option == "3":
            hunt()
        elif option == "4":
            craft()
        elif option == "5":
            smelt()
        elif option == "6":
            base()
        elif option == "7":
            return
        else:
            print("Invalid command")


def combat(enemy):
    while True:
        option = input("1.)Attack\n2.)Run\n>>>")
        playerAttack = random.randint(PlayerIG.damage / 2, PlayerIG.damage)
        enemyAttack = random.randint(enemy.damage / 2, enemy.damage)
        if option == "1":
            if playerAttack == PlayerIG.damage/2:
                print("You missed!")
            elif playerAttack > PlayerIG.damage/2:
                print("You delt {} damage!".format(playerAttack))
                PlayerIG.health -= enemyAttack
            elif enemyAttack == enemy.damage/2:
                print("The {} missed!".format(enemy.name))
            else:
                print("The enemy deals {} damage!".format(enemyAttack))
                PlayerIG.health -= enemyAttack

        elif option == "2":
            if random.randint(1,2) == 1:
                print("You fail to escape\n{}Hp - {}".format(PlayerIG.health, enemyAttack))
                PlayerIG.health -= enemyAttack
                      
            elif random.randint(1,2) == 2:
                print("You escaped!")
                return
        elif PlayerIG.health == 0:
            return
        elif enemy.health == 0:
            combatwin()
        else:
            print("Invalid input")

def combatwin():
    pass

option = input("Username:")
PlayerIG = Player(option)
print("Welcome {} to Rust Texted Based".format(PlayerIG.name))

    
while True:
    option = input("\n1.)Start\n2.)Load\n3.)Exit\n>>").lower()
    if option == "1":
        start()
    elif option == "2":
        pass
    elif option == "3":
        sys.exit()
    elif PlayerIG.health == 0:
        print("On your final breath you say 'wow that actually killed me'\nYour Dead")
        input("press enter to confirm\n")
        sys.exit()
    else:
        print("Invalid command")
        
