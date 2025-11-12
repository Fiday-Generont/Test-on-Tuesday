print("=============> Collaboration <=============")
def show_menu():
    print("\n", "=" * 20, "Generont_GitFlow_Calculator", "=" * 20)
def divide(a,b):
  return a // b
def add(a, b):
    return a + b
def show_result(result):
    print("Result:", result)
def handle_divide_by_zero(num2):
    while num2 == 0:
        print("Error: Cannot divide by zero. Please enter a new second number.")
        num2 = get_number_input("Enter second number: ", allow_zero=False)
    return num2
def get_operation():
    while True:
        operation = input("Enter operation (add/divide): ").lower()
        if operation in ["add", "divide"]:
            return operation
        print("Error: Please type 'add' or 'divide'.")

def get_number_input(prompt, allow_zero=True):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Negative numbers are not allowed.")
                continue
            if not allow_zero and value == 0:
                print("Error: Zero is not allowed for the second number.")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid number (not a string).")
def main():
    show_menu()

    num1 = get_number_input("Enter first number  : ", allow_zero=True)

    num2 = get_number_input("Enter second number : ", allow_zero=False)

    operation = get_operation()

    if operation == "add":
        result = add(num1, num2)
    elif operation == "divide":
        num2 = handle_divide_by_zero(num2)
        result = divide(num1, num2)

    show_result(result)

main()