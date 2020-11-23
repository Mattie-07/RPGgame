#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random

class Character:
    def __init__(self, name, health, power, armor, evadePercentage, luckPercentage, coins):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        self.evadePercentage = evadePercentage 
        self.luckPercentage = luckPercentage 
        self.coins = coins
    def alive(self, Character):
        if self.health > 0:
            return self.health
        elif Character == Zombie:
            print("The Zombie can't die!")
            return self.health
        else:
            # print(f"The {Character.name} died.")
            return  0
    def attack(self,attacked, attacker):
        if(attacked == Shadow):
            randomNum = random.randint(1,10)
            if randonNum > 9:
                ("The shadow wasn't hit! You know he is sneaky!")
        if(attacked == Medic):
            randomNum = random.randint(1,10)
            if randomNum > 2:
                print("You healed yourself by 2 points because you are a medic!")    
        attacked.health -= attacker.power
        print(f"{attacker.name} does {attacker.power} damage to {attacked.name}.")
            # print("The goblin does {} damage to you.".format(goblin.power))
    def printStatus(self):
        print("You have {} health and {} power.".format(self.health, self.power))
    def useItem(self, item):
        print(f"{self.name} used the {item}")
    # def printAllStats(TheCharacter):
    #     print("Your health{}, your power{}, your chance to evade{}, and your luck Percentage{} ".format(self.health, self.power, self.evadePercentage, self.luckPercentage))
    # def checkCharacterStatus(Thecharacter):
    #     print("Your health{}, your power{}, your chance to evade{}, and your luck Percentage{} ".format(self.health, self.power, self.evadePercentage, self.luckPercentage))


class Amazon(Character):
    def __init__(self):
        super().__init__(name = "Amazon", health = 10, power = 40, armor = 7, evadePercentage = 10, luckPercentage = 0, coins = 10)
    def attack(self, attacked, attacker):
        attacked.health -= attacker.power 
    def printStatus(self):
        print("The {} has {} health and {} power.".format(self.attacker, self.health, self.power))       

class Paladin(Character):
    def __init__(self):
        super().__init__(name = "Paladin",health = 20, power = 20, armor = 30, evadePercentage = 0, luckPercentage = 5, coins = 25)
    def attack(self, attacked, attacker):
        attacked.health -= attacker.power 
    def printStatus(self):
        print("The {} has {} health and {} power.".format(self.attacker, self.health, self.power)) 

class Medic(Character):
    def __init__(self):
        super().__init__(name = "Medic", health = 10, power = 10, armor = 10, evadePercentage = 50, luckPercentage = 15, coins = 7)
    def attack(self, attacked, attacker):
        attacked.health -= attacker.power 

class Matthew(Character):
    def __init__(self):
        super().__init__(name = "Matthew", health = 45, power = 30 , armor = 5, evadePercentage = 0 , luckPercentage = 10, coins = 30)
    def attack(self, attacked, attacker):
        randomNum = random.randint(1,10)
        if randomNum > 2:
            attacked.health -= attacker.power 
            print(f"You did {self.power} to the {attacked.name}")
        else:
            print("You missed your attack!")
    def printStatus(self):
        print("You have {} health and {} power.".format(self.health, self.power))


class Goblin(Character):   
    def __init__(self):
        super().__init__(name = "goblin" , health = 15,power =7 , armor = 2, evadePercentage = 10, luckPercentage = 0, coins = 2)
    def attack(self, attacked, attacker):
        randomNum = random.randint(1,10)
        if(randomNum) > 1:
            attacked.health -= attacker.power
            print(f"The goblin did {attacker.power} damage to {attacked.name}")
        else:
            print(f"{attacker.name} missed!")
    def printStatus(self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))



class Zombie(Character):
    def __init__(self):
        super().__init__(name = "zombie", health = 1000, power = 2, armor = 3, evadePercentage = 10, luckPercentage=0, coins = 100000)
        if self.health < 0:
            print("The zombie can never die! You get no gold because he still attacking, watch out!")
            coins += 1,000

class DemonImp(Character):
    def __init__(self):
        super().__init__(name = "Demon Imp" , health = 30, power = 20, armor = 20, evadePercentage = 30, luckPercentage=0, coins = 100 )
        if (self.health < 0 ):
            print("You received gold from killing a Demon Imp")
            coins += 7

class BigDemon(Character):
    def __init__(self):
        super().__init__(name = "Big Demon" ,health = 70, power = 30, armor =40, evadePercentage = 20, luckPercentage=0, coins = 250 )  
        if self.health < 0:
            print(f"The Big Demon is dead. You collect {x} gold")
            coins += 20
class Shadow(Character):
    def __init__(self):
        super().__init__(name = "Shadow" , health = 70, power = 30, armor =40, evadePercentage = 20, luckPercentage=0, coins = 250 )  
        if self.health < 0:
            print(f"Good job! You killed the shaow. You collect {coins} amount of gold")
            coins += 40
    def attack(self, attacked, attacker):
        randomNum = random.randint(1,10)
        if(randomNum) > 1:
            attacked.health -= attacker.power
            print(f"The goblin did {attacker.power} damage to {attacked.name}")
        else:
            print(f"{attacker.name} missed!")
    # def printStatus(self):

def sureCheck(item):
    sure = input(f"Are you sure you would like to purchase {item}?\n Type y or n\n")
    if(sure == "y"):
        return True
    elif(sure == "n"):
        return False
    else: 
        print("Im sorry, Would you like to purchase this item or not?")
        sureCheck(item)

def printAllStats(aHero):
        print("{} has health of {}, power of {}, evade chance of {}, and luck percentage of {} ".format(aHero.name, aHero.health, aHero.power, aHero.evadePercentage, aHero.luckPercentage))   

def noMoneyMesssage():
    return "Sorry, you dont have the money for that! Go out and fight to get some more!"

def evadeCheck(aHero):
    if aHero.evadePercentage > 60:
        print("Your chance to evade enemies attack can't be higher than 60 percent.")
        return False
    else:
        return True

def main():
    # Heros
    hero = Matthew()
    amazon = Amazon()
    paladin = Paladin()
    medic = Medic()
    #Villans
    goblin = Goblin()
    zombie = Zombie()
    shadow = Shadow()
    demonImp = DemonImp()
    bigDemon = BigDemon()
    gameStatus = True
    coinTotal = hero.coins + amazon.coins + paladin.coins + medic.coins
    items = {}

    # ourHero.alive()
    # ourHero.attack()    
    # goblin.alive(goblin.name) > 0 or hero.alive(hero.name) > 0:   original game status loop
    print("You're in the safety of the town with a little gold in your pocket. What would you like to do?")
    while (gameStatus):
        # hero.printStatus()
        
        print()
        print("What would you like to do?")
        print("1. Leave the town and go into the woods for adventure!")
        print("2. Go to sleep.")
        print("3. flee")
        print("4. Buy Items at the Store")
        print("5. Use an item")
        print("6. Check the status of the heros.")
        print("9. Quit")
        print("> ", end=' ')
        raw_input = int(input())
        if raw_input == 1:
            print("You left the town and ran into a group of monsters! Who would you like to attack?")
            print("1. Goblin")
            print("2. Shadow")
            print("3. Zombie")
            print("4. The Demon Imp")
            print("5. Big Demon")
            attacking = input()            
            if(attacking == 1 or attacking == "1"):
                while hero.alive(hero) > 0 or goblin.alive(goblin) > 0:
                    hero.attack(goblin, hero)
                    print("Oh no! However, goblin attacked you.")
                    goblin.attack(hero, goblin)
                    if goblin.alive(goblin) <= 0:
                        print("You killed the goblin")
                        break
                    else:
                        print("The fight continues!")
            elif (attacking == 2 or attacking == "2"):
                    while hero.alive(hero) > 0 or shadow.alive(shadow) > 0:
                        hero.attack(shadow, hero)
                        print("The shadow attemps his attack!")
                        shadow.attack(hero, shadow)
                        if shadow.alive(shadow) <= 0:
                            print("The shadow falls!")
                            break
                        else:
                            print("The fight continues!")
        elif raw_input == 2:
            print("You went to sleep feeling rested and well. Ok - now what?")
        elif raw_input == 3:
            print("You ran away and never became the Hero")
            break
        elif raw_input == 4:
            print("**A raspy voice calls to you from behind the store's counter** \n'Welcome to the Store friend. If you can't find what you're looking for here, then too bad! hahah, cough cough'\n The Items are cut into a old wood board' ")
            print("Listed Items")
            print("=" * 80)
            print("//////////////////          1)SuperTonic. 10 gold                ///////////")                 
            print("/////////////////           2)Armor. 25 gold                     ///////////")
            print("/////////////////           3)Evade Potion 50 Gold               ///////////") 
            print("/////////////////           4)Luck Charm. 50 Gold                ///////////")
            print("/////////////////           5)Ring of power. 150 Gold             ///////////")
            print("/////////////////           6)Leave the Shop                     ///////////")
            print("")
            print("=" * 80)
            shopping = True
            while shopping:
                print(f"You and your party has {coinTotal} coins")
                choice = int(input("Type the number of the item you would like to purchase or 6 to leave the shop.\n"))
                if choice == 1 :    
                    if coinTotal >= 10 and (sureCheck("SuperTonic")):
                            print("This will give you an extra 10 health...probably. N5o refunds!")
                            coinTotal -= 10    
                    else:
                        print(noMoneyMesssage())
                elif choice == 2 :
                    if (coinTotal >= 25 and sureCheck("Armor")):
                        print(" 'A soldier is only as good as the armor he wears. Too bad for you! Aha (cough)")
                        coinTotal -= 25
                    else:
                        print(noMoneyMesssag())
                elif choice == 3 :
                    if (coinTotal >= 50 and sureCheck("evadePotion")):
                        print("Your chance of dodging will increase! Dont come running back if luck isn't on your side! ")
                        if(evadeCheck(hero)):
                            hero.evadePercentage += 20
                            coinTotal -= 50
                    else:
                        print(noMoneyMesssage())
                elif choice == 4 :
                    if coinTotal >= 50 and sureCheck("Luck Charm"):
                        print("This charm will increase you chance to find more gold from the enemies you kill")
                        coinTotal -= 50
                    else:
                        print(noMoneyMesssage())
                elif choice == 5: 
                    if coinTotal >= 150 and sureCheck("Ring of Power"):
                        print("The Ring of power....It's precious to many. It will increase the chance you have to deal double damage by 2x")
                        coinTotal -= 150
                    else:
                        print(noMoneyMesssage())
                elif choice == 6:
                    if sureCheck("Exit"):
                        print("Get out of here then!")
                        shopping = False
                else:
                    print("I can't understand that jiberish! Try again!")
                            ## loop back to the menu once more. 
        elif raw_input == 5 :
            print("Here is a list of the items you currently have.")
            whichHero = input("Which hero would you like to use the item on?\n")
        elif raw_input == 6:
            validInput = True
            while validInput:
                print("*" * 20)
                print("1) Matthew")
                print("2) The Amazon")
                print("3) The Medic")
                print("4) The Paladin")
                print("5) All heros")
                print("6) Leave the stat checking menu")
                print("*" * 20)
                whichHero = int(input("Which hero would you like to have the stats for?\n"))
                if whichHero == 1:
                    printAllStats(hero)
                elif whichHero == 2:
                    printAllStats(amazon)
                elif whichHero == 3:
                    printAllStats(medic)
                elif whichHero == 4: 
                    printAllStats(paladin)
                elif whichHero == 5:
                    printAllStats(hero)
                    printAllStats(amazon)
                    printAllStats(medic)
                    printAllStats(paladin)
                elif whichHero == 6:
                    print("You left the stat Checking menu")
                    validInput = False
                else: 
                    print("There was an invalid input. Try again")
        elif raw_input == 9:
            gameStatus = False
        else:  
            print("You typed an invalid input - try again")

        #     hero_health -= goblin_power
        #     print("The goblin does {} damage to you.".format(goblin_power))
        #     if hero_health <= 0:
        #         print("You are dead.")
        # else:
        #     print("Invalid input {}".format(raw_input))

        # if goblin_health > 0:



main()


#Since the is Alive method checks to see whether a character is alive or not, I might as well offer the award for when that charater is dead to the Hero and the team after that happens. 
##Everything b  elow is the stay alive method - which includes the loop for the goblin's and hero's attack

    # # def alive(self):
    #         if ourHero.hero_health > 0:
    #             print(f"Hero's Health at {hero_health}")
    #             print("You have {} health and {} power.".format(hero_health, hero_power))
    #             print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
    #             print()
    #             print("What do you want to do?")
    #             print("1. fight goblin")
    #             print("2. do nothing")
    #             print("3. flee")
    #             print("> ", end=' ')
    #             raw_input = int(input())
    #         if raw_input == 1:
    #             ourHero.attack(theGoblin)
    #         # if raw_input == "1":
    #         #     # Hero attacks goblin
    #         #     goblin_health -= hero_power
    #         #     print("You do {} damage to the goblin.".format(hero_power))
    #         #     if goblin_health <= 0:
    #         #         print("The goblin is dead.")
            # elif raw_input == 2:
            #     pass
            # elif raw_input == 3:
            #     print("Goodbye.")
        
            # elif raw_input == 4:
            #     TheGoblin.attack(Ourhero)
            #     hero_health -= goblin_power
            #     print("The goblin does {} damage to you.".format(goblin_power))
            #     if hero_health <= 0:
            #         print("You are dead.")
            # else:
            #     print("Invalid input {}".format(raw_input))


# Code that I removed from the original copy
                    # if goblin_health > 0:
        #     hero_health -= goblin_power
        #     print("The goblin does {} damage to you.".format(goblin_power))
        #     if hero_health <= 0:
        #         print("You are dead.")  


            # print("You do {} damage to the goblin.".format(self.heroPower))
            # if goblin.goblinHealth <= 0:
            #     print("The goblin is dead.")

## Notes
# From what I saw in the video, what would be helpful is not to use The Goblin and Hero to intialize
# my objects of the classes. What would be better is if I use the Character super class to initali
#It would make better sense to use general variables names when it comes to things like health
# and power - because that is something that is shared between all characters
# The specifics, like the name of the character, the character type, and any of the values 
# that might seperate one character from another should deserve different names. 



## Fixes that need to be made!
## 1) after i miss the attack make sure that it doesn't print that I have actually done x amount of damage to the characters. 
## 2 ) I added two attriputes to the super class - make sure that for every character that I create, that they have the correct parameters for no errors~
#  3 ) do the calculations for the evade percentage - I beleive that every monster should also have an evade chance as well. 
# 4 ) Ditto above, but with the armor. 
# 5 ) Do I really need the attacker parameter in my attack method?? I  don't think I do. Try and see what would happen if I were to take it away as a paramter 
## 6) this might be too much for this program, but there has to be a way for everyone to attack once a turn, and maybe i could come up with a different variabble
        # that determins how that order is chosen

## Fix the indent error!#
#
#
