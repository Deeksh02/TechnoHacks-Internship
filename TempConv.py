def convert_temperature():
    print("Temperature Conversion Program")
    print("-------------------------------")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Exit")
    
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        print()
        convert_temperature()
    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        print()
        convert_temperature()
    elif choice == "3":
        print("Exiting the program. Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        print()
        convert_temperature()

convert_temperature()
