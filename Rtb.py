#Rust
import random,time
print("Hello welcome to RTB\nGet started by pressing ?")
unseen_inv = {"rockh":1,"rockp":1}
res={"wood":0,"stone":0,"metal":0,"cloth":0,"fuel":0}
smelting = {"metal_ore":0}
weapons = {"bow":0,"arrow":0}
base={"furnace":0}
craft={"sp":0,"sh":0,"mp":0,"mh":0}
#Farming//////////////////////////////////////////////////////////////////////////////////////
def farming(name,res,res2,n,n2,t,name2):
    print("Farming...")
    res+=n
    res2+=n2
    time.sleep(t)
    print(name,"+",n)
    if (res2 or n2 or name2 != ""):
        print(name2,"+",n2)
def farm_wood():
    if unseen_inv["rockh"] == 1:
        farming("Wood",res["wood"],"",100,"",3,"")
    elif craft["sh"] == 1:
        farming("Wood",res["wood"],"",200,"",2,"")
    elif craft["mh"] == 1:
        farming("Wood",["wood"],"",450,"",1,"")
    check_farm()
def farm_stone():
    if unseen_inv["rockp"] == 1:
        farming("Stone",res["stone"],smelting["metal_ore"],100,20,3,"Metal Ore")
    elif craft["sp"] == 1:
        farming("Stone",res["stone"],smelting["metal_ore"],200,35,2,"Metal Ore")
    elif craft["mp"] == 1:
        farming("Stone",res["stone"],smelting["metal_ore"],300,50,1,"Metal Ore")
    check_farm()
def farm_cloth():
    farming("Cloth",res["cloth"],"",10,"",1,"")
    check_farm()
def check_farm():
    cic = input("W - Wood\nS - Stone\nC - Cloth\n>>>").lower()
    if cic not in ["w","s","c","exit"]:
        print("Invalid command")
        check_farm()
    else:
        if cic == "w":
            farm_wood()
        elif cic == "s":
            farm_stone()
        elif cic == "c":
            farm_cloth()
        elif cic == "exit":
            pass

#/////////////////////////////////////////////////////////////////////////////////////////////
#Crafting////////////////////////////////////////////////////////////////////////////////////
def crafting(cc,name,name2,name3,res1,res2,crafted,n1,n2):
    if res1 < n1 or res2 < n2:
        print("You dont have enough resources to craft this item")
        check_crafting()
    else:
        print("Crafting...")
        res1-=n1
        res2-=n2
        if crafted == weapon["bow"]:
            if weapon["bow"] == 1:
                print("You already have a bow")
            else:
                crafted+=1
        elif crafted == weapon["arrow"]:
            crafted += 3
        elif crafted == res["fuel"]:
            crafted += 10
        elif crafted == craft["sp"]:
            crafted+=1
            unseen_inv["rockp"] -= 1
        elif crafted == craft["mp"]:
            crafted+=1
            craft["sp"] -= 1
        elif crafted == craft["sh"]:
            crafted+=1
            unseen_inv["rockh"] -= 1
        elif crafted == craft["mh"]:
            crafted+=1
            unseen_inv["sh"] -= 1
        print("Crafted a",name3)

def check_crafting():
        cc = input("Press the number you want to craft\n1:Stone Hatchet\n2:Stone Pickaxe\n3:Metal Hatchet\n4:Metal Pickaxe\n5:Bow\n6:Arrow\n7:Fuel\n8:Furnace\n>>>")
        if cc not in ["1","2","3","4","5","exit"]:
            print("Invalid command")
        else:
            if cc == "1":
                crafting(cc,"Stone Hatchet","Wood","Stone",res["wood"],res["stone"],craft["sh"],250,300)
            elif cc == "2":
                crafting(cc,"Stone Pickaxe","Wood","Stone",res["wood"],res["stone"],craft["sp"],250,350)
            elif cc == "3":
                crafting(cc,"Metal Hatchet","Wood","Metal",res["wood"],res["metal"],craft["mh"],300,400)
            elif cc == "4":
                crafting(cc,"Metal Pickaxe","Wood","Metal",res["wood"],res["metal"],craft["mp"],300,450)
            elif cc == "5":
                crafting(cc,"Bow","Wood","Cloth",res["wood"],res["cloth"],weapon["bow"],200,50)
            elif cc == "6":
                crafting(cc,"Arrow","Wood","Stone",res["wood"],res["stone"],weapon["arrow"],100,50)
            elif cc == "7":
                crafting(cc,"Fuel","Cloth","Animal Fat",res["cloth"],res["animal_fat"],res["fuel"],30,50)
            elif cc == "8":
                crafting(cc,"Furnace","Stone","Fuel",res["stone"],res["fuel"],base["furnace"],250,200)
            elif cc == "exit":
                pass
#/////////////////////////////////////////////////////////////////////////////////////////////
def smelt_check():
    if res["wood"] < 200:
        print("Not enough wood to smelt with")
    elif base["furnace"] == 0:
        print("You dont have a furnace")
    else:
        res["metal"]+=smelting["metal_ore"]
        res["wood"]-=200
        smelting["metal_ore"] -= smelting["metal_ore"]
        print("Smelted all your ores!\nWood - 200\nMetal +",smelting["metal_ore"],"")
        smelting["metal_ore"] -= smelting["metal_ore"]
#/////////////////////////////////////////////////////////////////////////////////////////////
def base_command():
    pass
def help_command():
    print("i - View inventory\nf - The farming Command,Use this when ever you wanna start farming\nh - Hunt animals\nc - View a crafting list and create new tools and furniture\ns - Smelt items\nb - Edit and upgrade your base!\n? - View the help list(What your reading)\nexit - Exit a question\nctrl+c - Exit program  ")
def check_commands():
    if command == "":
        print ("Please insert a command")
    if command not in ["i","h","f","c","s","b","?","exit",""]:
        print("Invalid command")
    else:
        if command == "i":
            print("Wood:",res["wood"],"\nStone:",res["stone"],"\nCloth:",res["cloth"],"\nMetal:",res["metal"],"\nFuel:",res["fuel"])
        elif command == "f":
            check_farm()
        elif command == "c":
            check_crafting()
        elif command == "s":
            smelt_check()
        elif command == "b":
            base_command()
        elif command == "?":
            help_command()
        elif command == "exit":
            pass

try:
    while True:
        command = input(">>").lower().strip(" ")
        check_commands()
except:
    exit
