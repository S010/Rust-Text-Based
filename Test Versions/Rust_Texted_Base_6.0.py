#Rust
import random,time,os,json,pickle
name = str(input("Username:")).lower()
print("Hello {} welcome to RTB\nGet started by pressing ?".format(name))
try:
    if not os.path.exists("./savefolder/"):
        os.mkdir("./savefolder/")
except OSError:
    print("Error:Creating directory")
savefile = open("./savefolder/savefile"+name,"a+")
unseen_inv = {"rockh":1,"rockp":1}
res={"nothing":0,"wood":0,"stone":0,"metal":0,"cloth":0,"fuel":0,"animal_fat":0}
smelting = {"metal_ore":0}
weapons = {"bow":0,"arrow":0}
base_tier={" ":0,"t1":0,"t2":0,"t3":0,"t4":0}
base={"furnace":0}
craft={"sp":0,"sh":0,"mp":0,"mh":0}
def farming(name,list1,res1,list2,res2,n,n2,t,name2):
    print("Farming...")
    list1[res1]+=n
    list2[res2]+=n2
    time.sleep(t)
    print(name,"+",n,"\n",name2,"+",n2)
def farm_wood():
    if unseen_inv["rockh"] == 1:
        farming("Wood",res,"wood",res,"nothing",100,0,3,".")
    elif craft["sh"] == 1:
        farming("Wood",res,"wood",res,"nothing",200,0,2,".")
    elif craft["mh"] == 1:
        farming("Wood",res,"wood",res,"nothing",450,0,1,".")
    pass
def farm_stone():
    if unseen_inv["rockp"] == 1:
        farming("Stone",res,"stone",smelting,"metal_ore",100,20,3,"Metal Ore")
    elif craft["sp"] == 1:
        farming("Stone",res,"stone",smelting,"metal_ore",200,35,2,"Metal Ore")
    elif craft["mp"] == 1:
        farming("Stone",res,"stone",smelting,"metal_ore",300,50,1,"Metal Ore")
    check_farm()
def farm_cloth():
    farming("Cloth",res,"cloth",res,"nothing",10,0,1,".")
    check_farm()
def check_farm():
    while True:
        cic = input("W - Wood\nS - Stone\nC - Cloth\n>>>").lower()
        if cic not in ["w","s","c","exit"]:
            print("Invalid command")
        else:
            if cic == "w":
                farm_wood()
            elif cic == "s":
                farm_stone()
            elif cic == "c":
                farm_cloth()
            elif cic == "exit":
                return
def crafting(cc,name,name2,name3,res1,res2,crafted,n1,n2,n3):
    if res1 < n1 or res2 < n2 :
        print("You dont have enough resources to craft this item")
        check_crafting()
    else:
        print("Crafting...")
        res1-=n1
        res2-=n2
        crafted +=n3
        print("Crafted a",name3)
def check_crafting():
        cc = input("Press the number you want to craft\n1:Stone Hatchet\n2:Stone Pickaxe\n3:Metal Hatchet\n4:Metal Pickaxe\n5:Bow\n6:Arrow\n7:Fuel\n8:Furnace\n>>>")
        if cc not in ["1","2","3","4","5","exit"]:
            print("Invalid command")
        else:
            if cc == "1":
                crafting(cc,"Stone Hatchet","Wood","Stone",res["wood"],res["stone"],craft["sh"],250,300,1)
            elif cc == "2":
                crafting(cc,"Stone Pickaxe","Wood","Stone",res["wood"],res["stone"],craft["sp"],250,350,1)
            elif cc == "3":
                crafting(cc,"Metal Hatchet","Wood","Metal",res["wood"],res["metal"],craft["mh"],300,400,1)
            elif cc == "4":
                crafting(cc,"Metal Pickaxe","Wood","Metal",res["wood"],res["metal"],craft["mp"],300,450,1)
            elif cc == "5":
                if crafted == weapon["bow"]:
                    if weapon["bow"] == 1:
                        print("You already have a bow")
                    else:
                        crafting(cc,"Bow","Wood","Cloth",res["wood"],res["cloth"],weapon["bow"],200,50,1)
            elif cc == "6":
                crafting(cc,"Arrow","Wood","Stone",res["wood"],res["stone"],weapon["arrow"],100,50,3)
            elif cc == "7":
                crafting(cc,"Fuel","Cloth","Animal Fat",res["cloth"],res["animal_fat"],res["fuel"],30,50,10)
            elif cc == "8":
                crafting(cc,"Furnace","Stone","Fuel",res["stone"],res["fuel"],base["furnace"],250,200,1)
            elif cc == "exit":
                pass
def smelt_check():
    if res["wood"] < 200:
        print("Not enough wood to smelt with\n*You need 200 wood you have",res["wood"])
    elif base["furnace"] == 0:
        print("You dont have a furnace")
    else:
        res["metal"]+=smelting["metal_ore"]
        res["wood"]-=200
        smelting["metal_ore"] -= smelting["metal_ore"]
        print("Smelted all your ores!\nWood - 200\nMetal +",smelting["metal_ore"],"")
        smelting["metal_ore"] -= smelting["metal_ore"]
def hunting(r):
    if r == "wolf":
        print("You killed a wolf\nCloth + 200\nAnimal Fat + 200")
        res["cloth"]+=200
        res["animal_cloth"]+=200
    elif r == "bear":
        print("You killed a bear\nCloth + 200\nAnimal Fat + 200")
        res["cloth"]+=200
        res["animal_cloth"]+=200
    elif r == "boar":
        print("You killed a boar\nCloth + 200\nAnimal Fat + 200")
        res["cloth"]+=200
        res["animal_cloth"]+=200
def hunting_check():
    randani = random.choice(["wolf","bear","boar"])
    if weapons["bow"] == 0:
        print("You dont have a Bow")
    else:
        if weapons["arrow"] < 3:
            print("You dont have any arrows")
        else:
            hunting(randani)
            weapons["arrow"] -= 3
def help_command():
    print("i - View inventory\nf - The farming Command,Use this when ever you wanna start farming\nh - Hunt animals\nc - View a crafting list and create new tools and furniture\ns - Smelt items\nb - Edit and upgrade your base!\n? - View the help list(What your reading)\nexit - Exit a question\nctrl+c - Exit program  ")
def base_create(name,prev,tier,res1,res2,res3,n1,n2,n3):
    if res1 < n1 or res2 < n2 or res3 < n3:
        print("You dont have enough resources, Try again later")
    else:
        print("Creating base...")
        res1-=n1
        res2 -=n2
        res3 -=n3
        tier += 1
        prev -= 1
        time.sleep(2)
        print("You created a {}\n{}-{}\n{}-{}\n{}-{}".format(name,res1,n1,res2,n2,res3,n3))
def base_check():
    base_con = input("!!!Are you sure you  want to create a base!!!\n!!!It will cost you alot of resources!!!\nY/N\n>>>").lower()
    if base_con not in ["y","n"]:
        print("Invalid command")
    else:
        if base_tier["t1"] and base_tier["t2"] and base_tier["t3"] and base_tier["t4"] == 0:
            base_create("Tier 1 Base",base_tier[" "],base_tier["t1"],res["wood"],res[" "],res[" "],2050,0,0)
        elif base_tier["t1"] == 1 and base_tier["t2"] == 0 and base_tier["t3"] == 0 and base_tier["t4"] == 0:
            base_create("Tier 2 Base",base_tier["t1"],base_tier["t2"],res["stone"],res[" "],res[" "],2500,0,0)
        elif base_tier["t1"] == 0 and base_tier["t2"] == 1 and base_tier["t3"] == 0 and base_tier["t4"] == 0:
            base_create("Tier 3 Base",base_tier["t2"],base_tier["t3"],res["metal"],res[" "],res[" "],1350,0,0)
        elif base_tier["t1"] == 0 and base_tier["t2"] == 0 and base_tier["t3"] == 1 and base_tier["t4"] == 0:
            base_create("Tier 4 Base",base_tier["t3"],base_tier["t4"],res["wood"],res["stone"],res["metal"],2700,3200,890)
        elif base_tier["t1"] == 0 and base_tier["t2"] == 0 and base_tier["t3"] == 0 and base_tier["t4"] == 1:
            print("You  already have the best base in the game!")
        else:
            print("WORK IN PROGRESS")



def check_commands():
    if command == "":
        print ("Please insert a command")
    elif command not in ["player","i","h","f","c","s","b","?","exit","save","load",KeyboardInterrupt]:
        print("Invalid command")
    else:
        if command == "i":
            print("Wood:",res["wood"],"\nStone:",res["stone"],"\nCloth:",res["cloth"],"\nMetal Ore:",smelting["metal_ore"],"\nMetal:",res["metal"],"\nFuel:",res["fuel"])
        elif command == "f":
            check_farm()
        elif command == "c":
            check_crafting()
        elif command == "s":
            smelt_check()
        elif command == "b":
            base_check()
        elif command == "h":
            hunting_check()
        elif command == "?":
            help_command()
        elif command == "save":
            with open("./savefolder/savefile"+name,"wb") as f:
                for i in [unseen_inv,res,smelting,weapons,base_tier,base,craft]:
                    pickle.dump(i,f)
                print("Game has been saved")
        elif command == "load":
            if os.path.exists("./savefolder/savefile"+name) == True:
                if os.path.getsize("./savefolder/savefile"+name)>0:
                    with open("./savefolder/savefile"+name,'rb')as f:
                        for i in [unseen_inv,res,smelting,weapons,base_tier,base,craft]:
                            unpickler=pickle.Unpickler(f)
                            i = unpickler.load()

                        print("Save file loaded")
                else:
                    print("No content in the save file")
            else:
                print("Save file not found")
        elif command == "player":
            for i in [unseen_inv,res,smelting,weapons,base_tier,base,craft]:
                print(i)
        elif command == "exit":
            pass

while True:
    command = input(">>").lower().strip(" ")
    check_commands()
