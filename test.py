# Persistent Python Calculator
# Member 1: Add function and main loop

def add(a, b):
    return a + b


def main():
    print("Persistent Python Calculator")

    while True:
        print("\nChoose an operation:")
        print("1 - Add")
        print("2 - Subtract")
        print("3 - Multiply")
        print("4 - Divide")
        print("5 - Exit")

        choice = input("Enter your choice: ")

        if choice == "5":
            print("Calculator closed.")
            break

        if choice != "1":
            print("Only ADD is available for now.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input.")
            continue

        result = add(num1, num2)
        print("Result:", result)


if __name__ == "__main__":
    main()
