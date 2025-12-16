
while True:
    print("\n===== SIMPLE CALCULATOR =====")

   
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    
    if choice == "5":
        print("Exiting the calculator... Goodbye!")
        break

    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    
    if choice == "1":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")

    elif choice == "2":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")

    elif choice == "3":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")

    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed!")

    else:
        print("Invalid choice! Please try again.")
