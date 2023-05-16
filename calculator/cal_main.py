#Add
def add(n1, n2):
    return  (n1 + n2)
#substract
def substract(n1, n2):
    return (n1 - n2)
#multiply
def multiply(n1, n2):
    return (n1 * n2)
#divide
def divide(n1, n2):
    return (n1 / n2)
operation = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}
def calculator():

    from cal_art import logo
    print(logo)

    num1 = float(input("What is the first number?: "))

    for symbol in operation:
        print(symbol)
        should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What is the second number?: "))

        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculation with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()