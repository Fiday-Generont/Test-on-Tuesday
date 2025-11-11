print("=============> Collaboration <=============")
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