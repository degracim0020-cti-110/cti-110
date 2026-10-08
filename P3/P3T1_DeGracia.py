# CTI 110
# P3T1 - Warmup with If Statements
# Michaelangleo De Gracia
#9/22/26


# Part 1 - Level Check
def main():
    print("Hello and welcome to the DUNGEON!")
    level = int(input("what level are you? "))
    if level >= 21:
        print("YOU may enter the dragons special dungeon.")
    else:
        print("YOU are unworthy young one go and level up before seeing me again")
    

# Part 2 - List potions
    print("Time to enter the dungeon")
    potions = int(input("How many health potions are you carrying on?"))
    if potions == 0:
        print("You are a fool to enter without health potions")
    elif potions == 1:
        print(f"you have {potions} health potion")
    elif potions >= 1:
        print(f"You have {potions} health potions")
    else:
        print(f"How do you acheive {potions}?!??! You imbecile you must turn back now!")

# Part 3 - Boss Battle 
    print ("You are facing the Deadly Ogre Giant")
    print ("This will be a hard fight prepare yourself")
    if level >= 25:
        # You're strong enough to fight the Ogre
        if potions > 3:
            print("It takes three potions to defeat this beast! You have enough potions to defeat the Ogre!")
            print("***You have defeated the Ogre!***")
        else:
            print("You run out of potions and the Ogre has defeated you! You have failed your quest and will rot in the dungeon forever!")
            print("***GAME OVER***")
    else:
        print("The Ogre is too strong and has overpowered you! You have been eaten by the Ogre and will die a slow and painful death!")
        print("***GAME OVER***")
# at the bottom - start the program
main()