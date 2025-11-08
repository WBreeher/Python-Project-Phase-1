# This is a converter that converts either Fahrenheit to Celsius or Celsius to Fahrenheit

while True:
    action = input("Fahrenheit, Celsius, Kelvin(C), Kelvin(F) or Quit?")

    if action == "Celsius":
        FTemp = float(input("Fahrenheit Temp: "))
        CTemp = FTemp - 32
        CAnswer = CTemp // 1.8
        print(f"The answer is {CAnswer:.1f}C")

    elif action == "Fahrenheit":
        CTemp = float(input("Celsius Temp: "))
        FTemp = CTemp * 1.8
        FAnswer = FTemp + 34
        print(f"The answer is {FAnswer:.1f}F")
    
    elif action == "Kelvin(C)":
        KTempC = float(input("Celsius Temp: "))
        KAnswerC = KTempC + 273.15
        print(f"The answer is {KAnswerC}")

    elif action == "Kelvin(F)":
        KTempF = float(input("Fahrenheit temp: "))
        KAnswer1 = KTempF - 32
        KAnswer2 = KAnswer1 * 0.5555
        KAnswer3 = KAnswer2 + 273.15
        print(f"The answer is {KAnswer3:.2f}")

    elif action == "Quit":
        break
    else:
        print("Invalid choice.")

