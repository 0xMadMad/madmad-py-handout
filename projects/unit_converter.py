while(True):
    print("\n\n\n=== CONVERTER ===")
    print("1.temperature")
    print("2.weight")
    print("3.length")
    print("4.exit")
    choice = input("choose conversion type: ")

    if choice=="4":
        break


    elif choice=="1":
        print("\n1.Celsius to Fahrenheit")
        print("2.Fahrenheit to Celsius")
        print("3.Celsius to Kelvin")
        print("4.Kelvin to Celsius")

        unit = input("choose conversion: ")
        if unit not in ["1", "2", "3", "4"]:
            print("invalid conversion choice..")
            continue

        try:
            value = float(input("enter value: "))
        except ValueError:
            print("enter a valid number..")
            continue

        if unit=="1":
            result = (value*(9/5))+32
        elif unit=="2":
            result = (value-32)*(5/9)
        elif unit=="3":
            result = value+273.15
        elif unit=="4":
            result = value-273.15
        else:
            result = None


    elif choice=="2":
        print("\n1.Kilograms to Pounds")
        print("2.Pounds to Kilograms")
        print("3.Grams to Kilograms")
        print("4.Kilograms to Grams")

        unit = input("choose conversion: ")
        if unit not in ["1", "2", "3", "4"]:
            print("invalid conversion choice..")
            continue

        try:
            value = float(input("enter value: "))
        except ValueError:
            print("enter a valid number..")
            continue

        if unit=="1":
            result = value*2.20462
        elif unit=="2":
            result = value/2.20462
        elif unit=="3":
            result = value/1000
        elif unit=="4":
            result = value*1000
        else:
            result = None


    elif choice=="3":
        print("\n1.Meters to Kilometers")
        print("2.Kilometers to Meters")
        print("3.Centimeters to Meters")
        print("4.Meters to Centimeters")
        print("5.Inches to Centimeters")
        print("6.Feet to Meters")

        unit = input("choose conversion: ")
        if unit not in ["1", "2", "3", "4", "5", "6"]:
            print("invalid conversion choice..")
            continue

        try:
            value = float(input("enter value: "))
        except ValueError:
            print("enter a valid number..")
            continue

        if unit=="1":
            result = value/1000
        elif unit=="2":
            result = value*1000
        elif unit=="3":
            result = value/100
        elif unit=="4":
            result = value*100
        elif unit=="5":
            result = value*2.54
        elif unit=="6":
            result = value*0.3048
        else:
            result = None


    else:
        result = None


    if result is not None:
        print("\nResult:", round(result, 4))
    else:
        print("\ninvalid choice..")
#MadMad_114