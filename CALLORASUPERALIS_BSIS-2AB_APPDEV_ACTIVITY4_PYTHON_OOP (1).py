# CC223-M     :   Applications Development and Emerging Technologies
# Activity 4  :   Python - Object Oriented Programming Game Character
# Name(s)     :   Joselle E. Callora (jsllcllr - Owner)
#                 John Louie C. Superalis (Jouls2001 - Collaborator)
#                 Section: BSIS - 2AB

import os
import sys
import csv

# It creates a class called charName.
class charName:
    selectedName = ""
    # Function for assigning the returned desired name
    def getuserName(self, _selectedName):
        self.selectedName = _selectedName
    # Function for accepting input of the user for desired name    
    def getName(self):
        valid = 1
        found = 0
        with open('characters_file.csv', mode = 'a', newline = "") as empty_file:
            empty_file.close()

        file_path = 'characters_file.csv'
        # Checks if File is NULL/Empty before choosing an option for action 
        if os.stat(file_path).st_size == 0:
            # Asking the user to input their username.
            self.selectedName = input("\nPlease Enter your username: ")
            print("\nYour character's name is " + self.selectedName)
            return self.selectedName
        else:# If file is not NULL/Empty checks and validates if user input already exists within the records
            while valid:
                with open('characters_file.csv') as csv_file:
                    read_characters = csv.reader(csv_file, delimiter = ',')
                    self.selectedName = input("\nPlease Enter your username: ")
                    for row in read_characters:
                        # Checking if the first column of the row is equal to the selected name.
                        if row[0].lower() == self.selectedName.lower():
                            found = 1
                            break
                        
                if found == 1:
                    print("\n\nUsername Taken, Please Try Again! Returning Main Menu")
                    os.system("pause")
                    os.system("cls")
                    mainMenu()
                else:
                    print("\nYour character's name is " + self.selectedName)
                    return self.selectedName 
                
    def setName(self):
        return self.selectedName

class charClass:
    selectedClass = ""

    def getUserCharacter(self, _selectedClass):
        self.selectedClass = _selectedClass

    def getClass(self):
        valid = 1
        # Printing out the character classes for the user to choose from.
        print("Please select your character class: ")
        print("[1] Wizard")
        print("[2] Knight")
        print("[3] Archer")
        print("[4] Assassin")
        # A while loop that will keep asking the user to choose a character until they choose a valid
        # option.
        while valid:
            option = input("Choose character: ")
            classList = ["Wizard", "Knight", "Archer", "Assassin"]
            if option == '1':
                self.selectedClass = classList[0]
                break
            elif option == '2':
                self.selectedClass = classList[1]
                break
            elif option == '3':
                self.selectedClass = classList[2]
                break
            elif option == '4':
                self.selectedClass = classList[3]
                break
            else:
                print("Invalid Input! Try again!")

        return self.selectedClass

    def setClass(self):
        # Returning the string "Character : " and the selectedClass variable.
        return self.selectedClass


class Weapon:
    weapon = ""
    
    def getUserWeapon(self, _weapon):
        self.weapon = _weapon

    def getWeapon(self):
        valid = 1
        # Printing out the options for the user to choose from.
        print("Please select your desired weapon: ")
        print("[1] Wizard Staff")
        print("[2] Sword")
        print("[3] Bow & Arrow")
        print("[4] Katar")
        # Asking the user to input a number between 1 and 4. If the user inputs a number between 1 and
        # 4, the code will assign the user a weapon based on the number they input. If the user inputs
        # a number that is not between 1 and 4, the code will print "Invalid Input! Try again!"
        while valid:
            option = input("Enter weapon: ")
            weaponList = ["Wizard Staff", "Sword", "Bow & Arrow", "Katar"]
            if option == '1':
                self.weapon = weaponList[0]
                break
            elif option == '2':
                self.weapon = weaponList[1]
                break
            elif option == '3':
                self.weapon = weaponList[2]
                break
            elif option == '4':
                self.weapon = weaponList[3]
                break
            else:
                print("Invalid Input! Try again!")
        
        return self.weapon

    def setWeapon(self):
        return self.weapon


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
                option = input("Enter Ability 1: ")
                
                if option == '1':
                    self.ability1 = wizAbList[0]
                    break
                elif option == '2':
                    self.ability1 = wizAbList[1]
                    break
                elif option == '3':
                    self.ability1 = wizAbList[2]
                    break
                elif option == '4':
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
                option1 = input("Enter Ability 2: ")
                if option1 == '1':
                    self.ability2 = wizAbList[0]
                    checker = 1
                elif option1 == '2':
                    self.ability2 = wizAbList[1]
                    checker = 1
                elif option1 == '3':
                    self.ability2 = wizAbList[2]
                    checker = 1
                elif option1 == '4':
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
                option = input("Enter Ability 1: ")
                
                if option == '1':
                    self.ability1 = knightAbList[0]
                    break
                elif option == '2':
                    self.ability1 = knightAbList[1]
                    break
                elif option == '3':
                    self.ability1 = knightAbList[2]
                    break
                elif option == '4':
                    self.ability1 = knightAbList[3]
                    break
                else:
                    print("Invalid Input! Try again!")    

            while valid1:
                checker = 0
                option1 = input("Enter Ability 2: ")
                if option1 == '1':
                    self.ability2 = knightAbList[0]
                    checker = 1
                elif option1 == '2':
                    self.ability2 = knightAbList[1]
                    checker = 1
                elif option1 == '3':
                    self.ability2 = knightAbList[2]
                    checker = 1
                elif option1 == '4':
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
                option = input("Enter Ability 1: ")
                
                if option == '1':
                    self.ability1 = arcAbList[0]
                    break
                elif option == '2':
                    self.ability1 = arcAbList[1]
                    break
                elif option == '3':
                    self.ability1 = arcAbList[2]
                    break
                elif option == '4':
                    self.ability1 = arcAbList[3]
                    break
                else:
                    print("Invalid Input! Try again!")    

            while valid1:
                checker = 0
                option1 = input("Enter Ability 2: ")
                if option1 == '1':
                    self.ability2 = arcAbList[0]
                    checker = 1
                elif option1 == '2':
                    self.ability2 = arcAbList[1]
                    checker = 1
                elif option1 == '3':
                    self.ability2 = arcAbList[2]
                    checker = 1
                elif option1 == '4':
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
                option = input("Enter Ability 1: ")
                
                if option == '1':
                    self.ability1 = AssAbList[0]
                    break
                elif option == '2':
                    self.ability1 = AssAbList[1]
                    break
                elif option == '3':
                    self.ability1 = AssAbList[2]
                    break
                elif option == '4':
                    self.ability1 = AssAbList[3]
                    break
                else:
                    print("Invalid Input! Try again!")    

            while valid1:
                checker = 0
                option1 = input("Enter Ability 2: ")
                if option1 == '1':
                    self.ability2 = AssAbList[0]
                    checker = 1
                elif option1 == '2':
                    self.ability2 = AssAbList[1]
                    checker = 1
                elif option1 == '3':
                    self.ability2 = AssAbList[2]
                    checker = 1
                elif option1 == '4':
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
        return self.ability1

    def setAbility2(self):
        return self.ability2
        
name_obj1 = charName()
character_obj1 = charClass()
weapon_obj1 = Weapon()
ability_obj1 = Ability()

def header():
    #It prints the header for the program.
    print("\t\t************************************")
    print("\t\t*---Welcome to MIR5: CROSSWORLDS---*")
    print("\t\t************************************")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

def noRecords():
    # It displays a string that says "No records found"
    print("\n\nNO RECORDS FOUND, RETURNING TO MAIN MENU\n\n")
    os.system("pause")
    os.system("cls")
    mainMenu()

#Function for the process of customizing the character
def customizeChar():
    os.system("cls")
    header()
    print("\nCustomize your Character: ")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    #Getting the desired name of the user
    name = name_obj1.getName()
    os.system("pause")
    os.system("cls")

    header()
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
    name_obj1.getuserName(name)
    character_obj1.getUserCharacter(ch_option)
    weapon_obj1.getUserWeapon(wp_option)
    ability_obj1.getUserAbility(ab_option[0], ab_option[1])
    
    # Display the details of the created character
    header()
    print("Your created Character ")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    print("Your character name: " + name_obj1.setName())
    print("Character Class: " + character_obj1.setClass())
    print("Weapon: " + weapon_obj1.setWeapon())
    print("1st Ability: " + ability_obj1.setAbility1())
    print("2nd Ability: " + ability_obj1.setAbility2())
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

    with open('characters_file.csv', mode = 'a', newline = "") as save_character:
        character_writer = csv.writer(save_character, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        character_writer.writerow([name_obj1.setName(), character_obj1.setClass(), weapon_obj1.setWeapon(), ability_obj1.setAbility1() ,ability_obj1.setAbility2()])

    print("\n\nCharacter Creation Done!")
    os.system("pause")
    os.system("cls")
    mainMenu()

#Function for searching a single character and displaying its details
def displayChar():
    os.system("cls")
    header()
    found = 0
   # Checking if the file exists.
    if os.path.exists('characters_file.csv'):
       # Reading the csv file and checking if the username is in the file.
        userName = input("\nPlease Enter your username: ")
        with open('characters_file.csv') as csv_file:
            read_characters = csv.reader(csv_file, delimiter = ',')
            print("\n\nDisplaying Character Details: ")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
            for row in read_characters:
                if row[0].lower() == userName.lower():
                    found = 1
                    break

            # Printing the character that the user has created.
            if found == 1:
                print("Your created Character ")
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
                print("Character name      :  " + row[0])
                print("Character Class     :  " + row[1])
                print("Weapon              :  " + row[2])
                print("1st Ability         :  " + row[3])
                print("2nd Ability         :  " + row[4])
                print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
            else:
                print("\nCharacter Not Found!\n\n")
        os.system("pause")
        os.system("cls")
        mainMenu()
    else:
        noRecords()

#Function to display all recorded characters in the csv file
def displayAllchar():
    os.system("cls")
    header()
    # Checking if the file exists.
    if os.path.exists('characters_file.csv'):
        # Opening the file and reading the file.
        with open('characters_file.csv') as csv_file:
            headcount = 0
            read_characters = csv.reader(csv_file, delimiter = ',')
            # Printing out the characters that are available to the user.
            print("\n\nHere are all your available characters: ")
            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
            print(f"{'Character Name:':30}{'Character Class:':30}{'Weapon:':30}{'1st Ability:':30}{'2nd Ability:':30}\n\n")
            for row in read_characters:
                print(f"{row[0]:30}{row[1]:30}{row[2]:30}{row[3]:30}{row[4]:30}\n")
                headcount += 1

            print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
            print(f"\n\nYou have a total of {headcount} character(s)\n")
        os.system("pause")
        os.system("cls")
        mainMenu()
    else:
        noRecords()
# Printing out the options for the user to choose from.

def deleteRecords():
    file_path = 'characters_file.csv'
    os.system("cls")
    header()
    
    print("Do you wish to continue in deleting all records?")
    print("[1] Yes")
    print("[2] No")

    option = input("Your choice: ")
    if option == '1':
        if(os.path.exists(file_path) and os.path.isfile(file_path)):
            os.remove(file_path)
            print("\n\nFile Successfully Deleted! Returning to Main Menu")
            os.system("pause")
            os.system("cls")
            mainMenu()
        else:
            print("\n\nFile not Found! Returning to Main Menu")
            os.system("pause")
            os.system("cls")
            mainMenu()
    elif option == '2':
        print("\n\nDeletion Cancelled! Returning to Main Menu")
        os.system("pause")
        os.system("cls")
        mainMenu()

def mainMenu():
    looper = 1
    while looper:
        header()
        print("Plase select what do you want to do?: ")
        print("[1] Customize a Character")
        print("[2] Display a Character")
        print("[3] Display all Characters")
        print("[4] Delete all Records")
        print("[5] Exit")

        option = input("Your choice: ")
        if option == '1':
            customizeChar()
            break
        elif option == '2':
            displayChar()
            break
        elif option == '3':
            displayAllchar()
            break
        elif option == '4':
            deleteRecords()
            break
        elif option == '5':
            os.system("pause")
            sys.exit()
            break
        else:
            print("Invalid Input! Try again!")
            os.system("pause")
            os.system("cls")


header()
print("Welcome to a new and long journey in a mystical and amazing world!")
os.system("pause")
os.system("cls")
mainMenu()