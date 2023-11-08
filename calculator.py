from art import calc_logo
import os


def add_numbers(num1, num2):
    return num1 + num2


def substract_numbers(num1, num2):
    return num1 - num2


def divide_numbers(num1, num2):
    return num1 / num2


def multiply_numbers(num1, num2):
    return num1 * num2


def exponentiation_numbers(num1, num2):
    return num1 ** num2


operations = {
        "+": add_numbers,
        "-": substract_numbers,
        "*": multiply_numbers,
        "/": divide_numbers,
        "**": exponentiation_numbers,
    }


def calculator():

    print(calc_logo)

    pass_number1 = float(input("Podaj pierwszą liczbę:\n"))
    for key in operations:
        print(key)
    should_coninue = True

    while should_coninue:
        user_choice = input("Co chcesz zrobić? Wpisz '*', '-', '+', '/','**'.\n")
        pass_number2 = float(input("Podaj kolejną liczbę:\n"))
        calc_func = operations[user_choice]
        answer = calc_func(pass_number1, pass_number2)
        print(f"{pass_number1} {user_choice} {pass_number2} = {answer}")

        if input(
                f"Wpisz 'y' żeby kontynuować liczenie od {answer}, wpisz 'n' by zacząć od nowa.\n") == 'y':
            pass_number1 = answer
        else:
            should_coninue = False
            os.system('cls')
            calculator()


calculator()
