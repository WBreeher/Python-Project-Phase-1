# This is a simple Grade Averager that takes 5 grade points, averages them, and assigns a letter grade

print("Welcome to my simple Grade Averager!\n")
print("This program takes 5 grade points, averages them, and then assigns them a letter grade.\n")
print("This system uses a modified 4.0 grading scale, with the following: F below 59%, D 60-69%, C 70-79%, B 80-89%, and A 90-100%.\n")

while True:
    action = input("Average, or Quit").strip().lower()
    
    if action == "average":
        try:
            Grade1 = float(input("First Grade Point: "))
            Grade2 = float(input("Second Grade Point: "))
            Grade3 = float(input("Third Grade Point: "))
            Grade4 = float(input("Fourth Grade Point: "))
            Grade5 = float(input("Fifth Grade Point: "))
            Average = Grade1 + Grade2 + Grade3 + Grade4 + Grade5
            Letter = Average / 5
            if Letter <= 59:
                print("The assigned letter grade is F")
            elif Letter <= 69:
                print("The assigned letter grade is D")
            elif Letter <= 79:
                print("The assigned letter grade is C")
            elif Letter <= 89:
                print("The assinged letter grade is B")
            elif Letter > 90:
                print("The assigned letter grade is A")
        except ValueError:
            print("Invalid Input. Please type a number between 0-100.")
        else:
            print("Invalid Input. Please try again.") 

    elif action == "quit":
        print("Thank you for using my Grade Averager!")
        break
    else:
        print("Invalid Input. Please try again.")
        continue