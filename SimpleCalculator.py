# This is a simple calculator that is capable of addition, subtraction, multiplication, and division.

print("Welcome to my simple calculator!\n")
print("This calculator is capable of addition, subtraction, multiplication, and division.\n")
print("Please type your selection below!\n")

Lists = []

while True:
    action = input("History, Adding, Subtracting, Multiplying, Dividing, or Quit?").strip().lower()

    if action == "history":
        for item in Lists:
            print(item or "(No entries yet!)")

    elif action.strip().lower() == "adding":
        try:
            A1Input = float(input("First Number: "))
            A2Input = float(input("Second Number: "))
            AAnswer = A1Input + A2Input
            Lists.append(f"{A1Input} + {A2Input} = {AAnswer}")
            print(f"The answer is {AAnswer}")
        except ValueError:
            print("Invalid Input. Please enter a number.")

    elif action.strip().lower() == "subtracting":
        try:
            S1Input = float(input("First Number: "))
            S2Input = float(input("Second Number: "))
            SAnswer = S1Input - S2Input
            Lists.append(f"{S1Input} - {S2Input} = {SAnswer}")
            print(f"The asnwer is {SAnswer}")
        except ValueError:
            print("Invalid Input. Please enter a number.")

    elif action.strip().lower() == "multiplying":
        try:
            M1Input = float(input("First Number: "))
            M2Input = float(input("Second Number: "))
            MAnswer = M1Input * M2Input
            Lists.append(f"{M1Input} * {M2Input} = {MAnswer}")
            print(f"The answer is {MAnswer}")
        except ValueError:
            print("Invalid Input. Please enter a number.")

    elif action.strip().lower() == "dividing":
        try:
            D1Input = float(input("First Number: "))
            D2Input = float(input("Second Number: "))
            DAnswer = D1Input / D2Input
            Lists.append(f"{D1Input} / {D2Input} = {DAnswer}")
            print(f"The answer is {DAnswer}.0f")
        except ValueError:
            print("Invalid Input. Please enter a number.")
        except ZeroDivisionError:
            print("Cannot divide by Zero. Please try again.")

    elif action.strip().lower() == "quit":
        print("Thanks for using my simple calculator!")
        break

    else:
        print("Invalid Option. Try Again.")
        continue