# This is a simple Number Comparison Game, the final project of Phase 1

import random

print("Welcome to my simple Number Comparison Game!\n")
print("This program will think of a number for you to guess.\n")
print("Do you have what it takes to beat it 3 times?\n")
print("At anytime, you can type quit to leave the program.")

while True:
    try:
        action = input("Easy, Medium, Hard, or Insane mode?").strip().lower()
        
        if action == "easy":
            PlVictory = 0
            PrVictory = 0

            while True:
                print("The program is thinking of a number between 1 and 5!")
                print("You get 10 guesses in this round, but only need 3 wins!")
                Answer = random.randint(1, 3)
                Guess = int(input("What is your guess: "))
                if Guess == Answer:
                    print("Correct Guess!")
                    PlVictory += 1
                if Guess != Answer:
                    print("Incorrect Guess!")
                    print(f"{Answer}")
                    PrVictory += 1
                if PlVictory == 3:
                    print("You won!")
                    break
                if PrVictory == 10:
                    print("Try again!")
                    break

        if action == "medium":
            PlVictory = 0
            PrVictory = 0

            while True:
                print("The program is thinking of a number between 1 and 10!")
                print("You get 8 guesses this round, but only need 3 wins!")
                Answer = random.randint(1, 10)
                Guess = input("What is your guess: ")
                if Guess == Answer:
                    print("Correct Guess!")
                    PlVictory += 1
                if Guess != Answer:
                    print("Incorrect Guess!")
                    print(f"{Answer}")
                    PrVictory += 1
                if PlVictory == 3:
                    print("You won!")
                    break
                if PrVictory == 8:
                    print("Try again!")
                    break

        if action == "hard":
            PlVictory = 0
            PrVictory = 0

            while True:
                print("The program is thinking of a number between 1 and 20!")
                print("You get 5 guesses, and need 3 wins!")
                Answer = random.randint(1, 20)
                Guess = input("What is your guess: ")
                if Guess == Answer:
                    print("Correct Guess!")
                    PlVictory += 1
                if Guess != Answer:
                    print("Incorrect Guess!")
                    print(f"{Answer}")
                    PrVictory += 1
                if PlVictory == 3:
                    print("You won!")
                    break
                if PrVictory == 5:
                    print("Try again!")
                    break

        if action == "insane":
            PlVictory = 0
            PrVictory = 0

            while True:
                print("The program is thinking of a number between 1 and 40!")
                print("For insane mode, you only have 10 guesses but you only need 1 win!")
                Answer = random.randint(1, 40)
                Guess = input("What is your guess: ")
                if Guess == Answer:
                    print("Correct Guess!")
                    PlVictory += 1
                if Guess != Answer:
                    print("Incorrect Guess!")
                    print(f"{Answer}")
                    PrVictory += 1
                if PlVictory == 1:
                    print("You won!")
                    break
                if PrVictory == 10:
                    print("Try again!")
                    break

        if action == "quit":
            break
        
        else:
            print("Invalid Choice. Please try again!")

    except ValueError:
        print("Invalid Choice. Please try again.")