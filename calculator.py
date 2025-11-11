print("=============> Collaboration <=============")
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