# CC223-M: Applications Development and Emerging Technologies
# Activity 3: Python - Object oriented Programming
# Name: Joselle E. Callora (jsllcllr - Owner)
#      John Louie C. Superalis (Jouls2001 - Collaborator)
# Section: BSIS - 2AB
import os

import character

class charClass:
    selectedClass = ""

    def getUserCharacter(self, _selectedClass):
        self.selectedClass = _selectedClass

    def getClass(self):
       # Printing out the character classes for the user to choose from.
        print("Please select your character class: ")
        print("[1] Wizard")
        print("[2] Knight")
        print("[3] Archer")
        print("[4] Assassin")
        # A while loop that will keep asking the user to choose a character until they choose a valid
        # option.
        while 1:
            option = int(input("Choose character: "))
            classList = ["Wizard", "Knight", "Archer", "Assassin"]
            if option == 1:
                self.selectedClass = classList[0]
                break
            elif option == 2:
                self.selectedClass = classList[1]
                break
            elif option == 3:
                self.selectedClass = classList[2]
                break
            elif option == 4:
                self.selectedClass = classList[3]
                break
            else:
                print("Invalid Input! Try again!")

        return self.selectedClass

    def setClass(self):
        # Returning the string "Character : " and the selectedClass variable.
        return "Character : " + self.selectedClass


class Weapon:
    weapon = ""

    def getUserWeapon(self, _weapon):
        self.weapon = _weapon

    def getWeapon(self):
       # Printing out the options for the user to choose from.
        print("Please select your desired weapon: ")
        print("[1] Wizard Staff")
        print("[2] Sword")
        print("[3] Bow & Arrow")
        print("[4] Katar")
        # Asking the user to input a number between 1 and 4. If the user inputs a number between 1 and
        # 4, the code will assign the user a weapon based on the number they input. If the user inputs
        # a number that is not between 1 and 4, the code will print "Invalid Input! Try again!"
        while 1:
            option = int(input("Enter weapon: "))
            weaponList = ["Wizard Staff", "Sword", "Bow & Arrow", "Katar"]
            if option == 1:
                self.weapon = weaponList[0]
                break
            elif option == 2:
                self.weapon = weaponList[1]
                break
            elif option == 3:
                self.weapon = weaponList[2]
                break
            elif option == 4:
                self.weapon = weaponList[3]
                break
            else:
                print("Invalid Input! Try again!")
        
        return self.weapon

    def setWeapon(self):
        return "Weapon : " + self.weapon


class Ability:
    ability1 = ""
    ability2 = ""

    def getUserAbility(self, _ability1, _ability2):
        self.ability1 = _ability1
        self.ability2 = _ability2

    def getAbility(self, option):
         # Selection of abilities for Knight
        valid = 1
        valid1 = 1

        # Asking the user to choose 2 abilities.
        if option == "Wizard":
            print("Choose 2 Abilities: ")
            print("[1] Energy Ball")
            print("[2] Dragons Breath")
            print("[3] Crown of Flame")
            print("[4] Hail Storm")
            wizAbList = ["Energy Ball", "Dragons Breath", "Crown of Flame", "Hail Storm"]

            # A while loop that is asking the user to input a number between 1 and 4. If the user
            # inputs a number between 1 and 4, the loop will break and the user will be able to
            # continue. If the user inputs a number outside of the range, the loop will continue to
            # ask the user to input a number between 1 and 4.
            while valid:
                option = int(input("Enter Ability 1: "))
                
                if option == 1:
                    self.ability1 = wizAbList[0]
                    break
                elif option == 2:
                    self.ability1 = wizAbList[1]
                    break
                elif option == 3:
                    self.ability1 = wizAbList[2]
                    break
                elif option == 4:
                    self.ability1 = wizAbList[3]
                    break
                else:
                    print("Invalid Input! Try again!")    

            # Asking the user to input a number between 1 and 4. If the user inputs a number between 1
            # and 4, it will assign the corresponding ability to the variable "self.ability1". If the
            # user inputs a number that is not between 1 and 4, it will print "Invalid Input! Try
            # again!" and ask the user to input a number again.
            while valid1:
                checker = 0
                option1 = int(input("Enter Ability 2: "))
                if option1 == 1:
                    self.ability2 = wizAbList[0]
                    checker = 1
                elif option1 == 2:
                    self.ability2 = wizAbList[1]
                    checker = 1
                elif option1 == 3:
                    self.ability2 = wizAbList[2]
                    checker = 1
                elif option1 == 4:
                    self.ability2 = wizAbList[3]
                    checker = 1
                else:
                    print("Invalid Input! Try again!")
                    
                if checker == 1:
                    if self.ability1 == self.ability2:
                        print("Choose another skill! Try again!")
                    else:
                        break
            
            return self.ability1, self.ability2
                

        # Selection of abilities for Knight
        elif option == "Knight":
            print("Choose 2 Abilities: ")
            print("[1] Fire Slash")
            print("[2] Power Slash")
            print("[3] Gigantic Storm")
            print("[4] Chaotic Disaster")
            knightAbList= ["Fire Slash", "Power slash", "Gigantic Storm", "Chaotic Disaster"]

            while valid:
                option = int(input("Enter Ability 1: "))
                
                if option == 1:
                    self.ability1 = knightAbList[0]
                    break
                elif option == 2:
                    self.ability1 = knightAbList[1]
                    break
                elif option == 3:
                    self.ability1 = knightAbList[2]
                    break
                elif option == 4:
                    self.ability1 = knightAbList[3]
                    break
                else:
                    print("Invalid Input! Try again!")    

            while valid1:
                checker = 0
                option1 = int(input("Enter Ability 2: "))
                if option1 == 1:
                    self.ability2 = knightAbList[0]
                    checker = 1
                elif option1 == 2:
                    self.ability2 = knightAbList[1]
                    checker = 1
                elif option1 == 3:
                    self.ability2 = knightAbList[2]
                    checker = 1
                elif option1 == 4:
                    self.ability2 = knightAbList[3]
                    checker = 1
                else:
                    print("Invalid Input! Try again!")
                    
                if checker == 1:
                    if self.ability1 == self.ability2:
                        print("Choose another skill! Try again!")
                    else:
                        break
            
            return self.ability1, self.ability2
                

         # Selection of abilities for Knight
        elif option == "Archer":
            print("Choose 2 Abilities: ")
            print("[1] Take Aim")
            print("[2] Quick Shot")
            print("[3] Blazing Arrow")
            print("[4] Frost Arrow")
            arcAbList = ["Take Aim", "Quick Shot", "Blazing Arrow", "Frost Arrow"]

            while valid:
                option = int(input("Enter Ability 1: "))
                
                if option == 1:
                    self.ability1 = arcAbList[0]
                    break
                elif option == 2:
                    self.ability1 = arcAbList[1]
                    break
                elif option == 3:
                    self.ability1 = arcAbList[2]
                    break
                elif option == 4:
                    self.ability1 = arcAbList[3]
                    break
                else:
                    print("Invalid Input! Try again!")    

            while valid1:
                checker = 0
                option1 = int(input("Enter Ability 2: "))
                if option1 == 1:
                    self.ability2 = arcAbList[0]
                    checker = 1
                elif option1 == 2:
                    self.ability2 = arcAbList[1]
                    checker = 1
                elif option1 == 3:
                    self.ability2 = arcAbList[2]
                    checker = 1
                elif option1 == 4:
                    self.ability2 = arcAbList[3]
                    checker = 1
                else:
                    print("Invalid Input! Try again!")
                    
                if checker == 1:
                    if self.ability1 == self.ability2:
                        print("Choose another skill! Try again!")
                    else:
                        break
            
            return self.ability1, self.ability2

         # Selection of abilities for Knight
        elif option == "Assassin":
            print("Choose 2 Abilities: ")
            print("[1] Cloaking")
            print("[2] Enchant Poison")
            print("[3] Sonic Acceleration")
            print("[4] Meteor Assault")
            AssAbList = ["Cloaking", "Enchant Poision", "Sonic Acceleration", "Meteor Assault"]

            while valid:
                option = int(input("Enter Ability 1: "))
                
                if option == 1:
                    self.ability1 = AssAbList[0]
                    break
                elif option == 2:
                    self.ability1 = AssAbList[1]
                    break
                elif option == 3:
                    self.ability1 = AssAbList[2]
                    break
                elif option == 4:
                    self.ability1 = AssAbList[3]
                    break
                else:
                    print("Invalid Input! Try again!")    

            while valid1:
                checker = 0
                option1 = int(input("Enter Ability 2: "))
                if option1 == 1:
                    self.ability2 = AssAbList[0]
                    checker = 1
                elif option1 == 2:
                    self.ability2 = AssAbList[1]
                    checker = 1
                elif option1 == 3:
                    self.ability2 = AssAbList[2]
                    checker = 1
                elif option1 == 4:
                    self.ability2 = AssAbList[3]
                    checker = 1
                else:
                    print("Invalid Input! Try again!")
                    
                if checker == 1:
                    if self.ability1 == self.ability2:
                        print("Choose another skill! Try again!")
                    else:
                        break
            
            return self.ability1, self.ability2

    def setAbility1(self):
        return "Ability 1 : " + self.ability1

    def setAbility2(self):
        return "Ability 2 : " + self.ability2
def header():
    print("\t\t************************************")
    print("\t\t*---Welcome to MIR5: CROSSWORLDS---*")
    print("\t\t************************************")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

header()
print("Customize your first Character: ")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
# Creating an instance of the class.
character_obj1 = charClass()
weapon_obj1 = Weapon()
ability_obj1 = Ability()

# Asking the user to select a class for their character.
ch_option = character_obj1.getClass()
print("\nSelected Class: " + ch_option)
os.system("pause")
os.system("cls")

header()
# Calling the getWeapon() method from the Weapon class.
wp_option = weapon_obj1.getWeapon()
print("\nSelected Weapon: " + wp_option)
os.system("pause")
os.system("cls")

header()
# Creating a new object called ability_obj1 and then calling the getAbility method from the Ability
# class.
ab_option = ability_obj1.getAbility(ch_option)
print("\nSelected Abilities: " + ab_option[0] + " & " + ab_option[1])
os.system("pause")
os.system("cls")

# Calling the methods from the classes and passing the user input as arguments.

character_obj1.getUserCharacter(ch_option)
weapon_obj1.getUserWeapon(wp_option)
ability_obj1.getUserAbility(ab_option[0], ab_option[1])

header()
print("Customize for your second Character: ")
character_obj2 = charClass()
weapon_obj2 = Weapon()
ability_obj2 = Ability()

ch_option = character_obj2.getClass()
print("\nSelected Class: " + ch_option)
os.system("pause")
os.system("cls")

header()
wp_option = weapon_obj2.getWeapon()
print("\nSelected Weapon: " + wp_option)
os.system("pause")
os.system("cls")

header()
ab_option = ability_obj2.getAbility(ch_option)
print("\nSelected Abilities: " + ab_option[0] + " & " + ab_option[1])
os.system("pause")
os.system("cls")

character_obj2.getUserCharacter(ch_option)
weapon_obj2.getUserWeapon(wp_option)
ability_obj2.getUserAbility(ab_option[0], ab_option[1])

header()
print("Here are your available characters: ")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# Printing the class, weapon, and abilities of the character.
print("Character 1: ")
print(character_obj1.setClass())
print(weapon_obj1.setWeapon())
print(ability_obj1.setAbility1())
print(ability_obj1.setAbility2())
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

print("Character 2: ")
print(character_obj2.setClass())
print(weapon_obj2.setWeapon())
print(ability_obj2.setAbility1())
print(ability_obj2.setAbility2())
