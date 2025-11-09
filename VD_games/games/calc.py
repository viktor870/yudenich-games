import random

DESCRIPTION = "What is the result of the expression?"


def calculate_expression(num1, num2, operator):
    match operator:
        case '+':
            return str(num1 + num2)
        case '-':
            return str(num1 - num2)
        case '*':
            return str(num1 * num2)
        case _:
            raise ValueError(f"Unknown operator: {operator}")


def generate_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])
    question = f"{num1} {operator} {num2}"
    correct_answer = calculate_expression(num1, num2, operator)
    return question, correct_answer
