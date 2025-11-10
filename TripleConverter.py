# This is a converter that converts either Fahrenheit to Celsius or Celsius to Fahrenheit\n

print("Welcome to my Triple Temperature Converter!\n")
print("You can convert Fahrenheit to Celsius, Celsius to Fahrenheit, and either Fahrenheit or Celsius to Kelvin.\n")
print("Please type your selection below.\n") 

Lists = []

while True:
    action = input("History, Convert, or Quit?").strip().lower()

    if action == "history":
        for item in Lists:
            print(item or "(no entries yet).")

    elif action.strip().lower() == "convert":
        while True:
            sub = input("Fahrenheit, Celsius, Kelvin(C), Kelvin(F) or Back?").strip().lower()

            if sub == "celsius":
                FTemp = float(input("Fahrenheit Temp:  "))
                CTemp = FTemp - 32
                CAnswer = CTemp // 1.8
                Lists.append(f"{FTemp:.1f}°F = {CAnswer:.1f}°C")
                print(f"The answer is {CAnswer:.1f}°C.")

            elif sub == "fahrenheit":
                CTemp = float(input("Celsius Temp:  "))
                FTemp = CTemp * 1.8
                FAnswer = FTemp + 34
                Lists.append(f"{CTemp:.1f}°C = {FAnswer:.1f}°F")
                print(f"The answer is {FAnswer:.1f}°F.")
    
            elif sub == "kelvin(c)":
                KTempC = float(input("Celsius Temp:  "))
                KAnswerC = KTempC + 273.15
                Lists.append(f"{KTempC:.1f}°C = {KAnswerC:.2f}°K")
                print(f"The answer is {KAnswerC:.2f}°K.")

            elif sub == "kelvin(f)":
                KTempF = float(input("Fahrenheit temp:  "))
                KAnswer1 = KTempF - 32
                KAnswer2 = KAnswer1 * 0.5555
                KAnswer3 = KAnswer2 + 273.15
                Lists.append(f"{KTempF:.1f}°F = {KAnswer3:.2f}°K")
                print(f"The answer is {KAnswer3:.2f}°K.")

            elif sub == "back":
                break
            else:
                print("Invalid choice. Try Again.")
                continue
    elif action == "quit":
        print("Thank you for using my Triple Temperature Converter!")
        break
    else:
        print("Invalid Choice. Try Again.")
        continue