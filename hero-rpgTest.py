#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

class Character:
    def __init__(self, startHealth, startPower):
        self.startHealth = startHealth
        self.startPower = startPower
    def alive(self):
        if self.startHealth > 0:
            return self.startHealth
        else:
            return  0

class TheHero(Character):
    def __init__(self,startHealth,startP):
        pass
    def attack(self, goblin):                                  #hero attacks Goblin
            goblin.goblinHealth -= self.heroPower
    def alive(self):
        if self.heroHealth > 0:
            return self.heroHealth
        else:
            return 0
    def printStatus(self):
        print("You have {} health and {} power.".format(self.heroHealth, self.heroPower))
class Goblin(Character):   
    # def __init__(self,startHealth,startPower):
    #     self.goblinHealth = startHealth
    def attack(self, hero):                                     #Golbin attacks hero
        hero.heroHealth -= self.goblinPower                 
    def alive(self):
        if goblinHealth > 0:
            return self.goblinHealth
        else:
            return 0
    def printStatus(self):
        print("The goblin has {} health and {} power.".format(self.goblinHealth, self.goblinPower))


        

def main():
    hero = TheHero(10,5)
    goblin = Goblin(6,2)
    # ourHero.alive()
    # ourHero.attack()    

    while goblin.alive() > 0 and hero.alive() > 0:
        hero.printStatus()
        goblin.printStatus()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = int(input())
        if raw_input == 1:
            hero.attack(goblin)
            goblin.attack(hero)
            print("You do {} damage to the goblin.".format(hero.heroPower))
            print("The goblin does {} damage to you.".format(goblin.goblinPower))
            if goblin.goblinHealth <= 0:
                print("The goblin is dead.")
        elif raw_input == 2:
            pass
        elif raw_input == 3:
            print("Goodbye.")
            break
        elif raw_input == 4:
            goblin.attack(hero)
            

        #     hero_health -= goblin_power
        #     print("The goblin does {} damage to you.".format(goblin_power))
        #     if hero_health <= 0:
        #         print("You are dead.")
        # else:
        #     print("Invalid input {}".format(raw_input))

        # if goblin_health > 0:



main()



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
# my objects of the classes. What would be better is 