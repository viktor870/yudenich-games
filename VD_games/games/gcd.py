import random
import math

DESCRIPTION = "Find the greatest common divisor of given numbers."


def find_gcd(a, b):
    """
    Находит наибольший общий делитель двух чисел
    """
    return math.gcd(a, b)


def generate_round():
    """
    Генерирует один раунд для игры НОД
    """
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    question = f"{num1} {num2}"
    correct_answer = str(find_gcd(num1, num2))
    
    return question, correct_answer
