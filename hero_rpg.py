#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
import random

class Character:
    def __init__(self, health, power, armor, evadePercentage, luckPercentage, coins):
        self.health = health
        self.power = power
        self.armor = armor
        self.evadePercentage = evadePercentage 
        self.luckPercentage = luckPercentage 
        self.coins = coins
    def alive(self):
        if self.health > 0:
            return self.health
        else:
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
    def printStatus(self):
        print("You have {} health and {} power.".format(self.health, self.power))
    def printAllStats()
        print("Your health{}, your power{}, your chance to evade{}, and your luck Percentage{} ".format(self.health, self.power, self.evadePercentage, self.luckPercentage))


class Amazon(Character):
    def __init__(self, health, power, armor, evadePercentage, luckPercentage, coins):
        self.health = 10
        self.power = 40
        self.armor = 7
        self.evadePercentage = 10
        self.luckPercentage = 0
        self.coins = 10
    def attack(self, attacked, attacker):
        attacked.health -= attacker.power 
    def printStatus(self):
        print("The {} has {} health and {} power.".format(self.attacker, self.health, self.power))       

class Paladin(Character):
        def __init__(self, health, power, armor, evadePercentage, luckPercentage, coins):
            self.health = 20
            self.power = 20
            self.armor = 30
            self.evadePercentage = 0
            self.luckPercentage = 5
            self.coins = 25
    def attack(self, attacked, attacker):
        attacked.health -= attacker.power 
    def printStatus(self):
        print("The {} has {} health and {} power.".format(self.attacker, self.health, self.power)) 

class Medic(Character):
        def __init__(self, health, power, armor, evadePercentage, luckPercentage, coins):
            self.health = 10
            self.power = 10
            self.armor = 10 
            self.evadePercentage = 50
            self.luckPercentage= 15
            self.coins = 7
class Matthew(Character):
        def __init__(self, health, power, armor, evadePercentage, luckPercentage, coins):
            self.health = 45
            self.power = 30
            self.armor = 5
            self.evadePercentage = 0
            self.luckPercentage= 10
            self.coins = 30
    def attack(self, attacked, attacker):
        randomNum = random.randint(1,10)
        if randomNum > 2:
            attacked.health -= attacker.power
        else:
            print("You missed your attack!")
    def printStatus(self):
        print("You have {} health and {} power.".format(self.health, self.power))

class Goblin(Character):   
    def __init__(self,health,power):
        super().__init__(health,power)
    def attack(self, attacked, attacker):                                  #hero attacks Goblin
            attacked.health -= attacker.power                
    def printStatus(self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))



class Zombie(Character):
    def __init__(self, health, power):
        super().__init__(health,power)
        if health < 0
            print("The zombie can never die! You get no gold because he still attacking, watch out!")
            coins += 1,000

class DemonImp(Character):
    def __init__(self, health, power):
        super().__init__(health,power)
        if (health < 0 )
            print("You received gold from killing a Demon Imp")
            coins += 7

class BigDemon(Character):
    def __init__(self, health, power):
        super().__init__(health,power)   
        if health < 0
            print(f"The Big Demon is dead. You collect {x} gold")
            coins += 20
class Shadow(Character):
    def __init__(self):
        self.health = 1
        self.power = 30
        if health  < 0
            print(f"Good job! You killed the shaow. You collect {x} amount of gold ")
            coins += 40
        

def sureCheck(item) 
    sure = input(f"Are you sure you would like to purchase {item}\n Type y or n")
    if(sure = "y")
        return True
    elif(sure = "n")
        return False
    else 
        print("Im sorry, Would you like to purchase this item or not?")
        sureCheck(item)
def checkCharacterStatus()
    choice = input("Your health{}, your power{}, your chance to evade{}, and your luck Percentage{} ".format(self.health, self.power, self.evadePercentage, self.luckPercentage))
    






def main():
    hero = TheHero()
    goblin = Goblin()
    zombie = Zombie()
    shadow = Shadow()
    coins = 10

    # ourHero.alive()
    # ourHero.attack()    

    while goblin.alive() > 0 and hero.alive() > 0:
        hero.printStatus()
        goblin.printStatus()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. Fight the Zombie!")
        print("3. flee")
        print("Buy Items at the Store"
    )
        print("> ", end=' ')
        raw_input = int(input())
        if raw_input == 1:
            print("You chose to attack, who would you like to attack?")
            print("1. Goblin")
            print("2. Shadow")
            print(3)
            hero.attack(goblin, hero)
            goblin.attack(hero, goblin)
            print("You do {} damage to the goblin.".format(hero.power))
            print("The goblin does {} damage to you.".format(goblin.power))
            if goblin.health <= 0:
                print("The goblin is dead.")
                print("You defeated the Golbin, here is +5 coins!")
        elif raw_input == 2:
            hero.attack(zombie,hero)
            zombie.attack(hero,zombie)
            print("You do {} damage to the zombie.".format(hero.power))
            print("The zombie does {} damage to you.".format(zombie.power))
        elif raw_input == 3:
            print("Goodbye.")
            break
        elif raw_input == 4
            print("**A raspy voice calls to you from behind the store's counter** 'Welcome to the Store friend. If you can't find what you're looking for here, then it doesnt too bad! hahah, cough cough' ")
            print("Listed Items")
            print("=" * 30)
            print("1)SuperTonic. 10 gold ")
            print("2)Armor. 25 gold")
            print("3)Evade Potion 50 Gold")
            print("4)Luck Charm. 50 Gold")
            print("5)Ring of power. 70 Gold")
            print("6)Leave the Shop")
            print("")
            print("=" * 30)
            choice = input("Type the number of the item you would like to purchase")
                if choice == 1 :
                    if(sureCheck("SuperTonic"))    
                        print("You just purchased the Super Tonic... no refunds!")
                elif choice == 2 :
                    if (sureCheck("Armor"))
                        print(" 'A soldier is only as good as the armor he wears. Too bad for you! Aha ( cough) '  ")
                elif choice == 3 :
                    if (sureCheck("evadePotion"))
                        print("Your chance of dogding will increase! Dont come running back if luck isn't on your side! ")
                elif choice == 4 :
                    if sureCheck("Luck Charm"))
                        print("This charm will increase you chance to find more gold from the enemies you kill")
                elif choice == 5: 
                    if sureCheck("Ring of Power"))
                        print("The Ring of power....It's precious to many. It will increase the chance you have to deal double damage by 2x")
                elif choice == 6:
                    if sureCheck("Exit"))
                        print("Get out of here then!")
                else:
                    print("I can't understand that! Try again!")
                    ## loop back to the menu once more. 

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

#
#
#
#
