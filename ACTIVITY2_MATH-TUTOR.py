"""
    Activity 2: Python Programming - Math Tutor
    Submitted By: Callora, Joselle
                  Superalis, John Louie
    
    Year & Sec.: BSIS-2AB-M
"""
# It imports the random module.
import random

"""
    This program contains code for a simple calculator that is able 
    to add, subtract, multiply, and divide two numbers
"""
def add(x, y):
    return x + y

def subtrct(x, y):
    return x - y

def multiply(x, y):
    return x * y

def dividiby(x, y):
    return x / y

while True:
    # Asking the user to choose the operation he/she wants to do.
    print ("Choose the operation you want:\n[1] Add\n[2] Subtract\n[3] Multiply\n[4] Divide\n")
    choice = input("Enter your choice: ")
    # Checking if the user input is in the list of choices.
    if choice in ('1', '2', '3', '4'):
        score = 0   
        if choice == '1':
            print ("-+-+-+-Addition Problems-+-+-+\n")
            # Asking the user how many problems he/she wants to answer.
            numProblems = int (input("How many problems do you want to answer?: "))
            i = 0
            while i < numProblems:
                # Generating random numbers from 0 to 9 and 2 to 10 with a step of 2.
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                # Calling the function add and passing the values of num1 and num2.
                num3 = add(num1, num2)
               # Asking the user to input the answer to the problem.
                print("\nWhat is the sum of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
               # It checks if the answer of the user is correct. If it is correct, it will print
               # "Correct" and add 1 to the score.
                if num3 == answer:
                    print("Correct")
                    score += 1
                else:
                    # Printing the correct answer if the user inputted the wrong answer.
                    print("Wrong! the correct answer is", num3)
                i += 1
        
        elif choice == '2':
            print ("-+-+-+-Subtraction Problems-+-+-+\n")
            i = 0
            numProblems = int (input("How many problems do you want to answer?: "))
            while i < numProblems:
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = subtrct(num1, num2)
                print("\nWhat is the difference of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    score += 1
                else:
                    print("Wrong! the correct answer is", num3)
                i += 1
        
        elif choice == '3':
            print ("-+-+-+-Multiplication Problems-+-+-+\n")
            i = 0
            numProblems = int (input("How many problems do you want to answer?: "))
            while i < numProblems:
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = multiply(num1, num2)
                print("\nWhat is the product of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    score += 1
                else:
                    print("Wrong! the correct answer is", num3)
                i += 1
        
        elif choice == '4':
            print ("-+-+-+-Division Problems-+-+-+\n")
            i = 0
            numProblems = int (input("How many problems do you want to answer?: "))
            while i < numProblems:
                num1 = round(float(random.randint(0, 9)),2)
                num2 = round(float(random.randrange(2, 10, 2)), 2)
                num3 = dividiby(num1, num2)
                print("\nWhat is the quotient of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    score += 1
                else:
                    print("Wrong! the correct answer is", num3)
                i += 1
            
        print ("\nYour Score is " + str(score) + "/" + str(numProblems))
        
    try_again = input("\nWant to try again? (yes/no): ")

    if try_again.lower() == "no":
        break

else:
    print("Invalid input")