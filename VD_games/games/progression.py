import random

DESCRIPTION = "What number is missing in the progression?"


def generate_arithmetic_progression(start, step, length):
    """Генерирует арифметическую прогрессию"""
    progression = []
    for i in range(length):
        progression.append(str(start + i * step))
    return progression


def generate_round():
    """
    Генерирует один раунд для игры Арифметическая прогрессия
    """
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    
    progression = generate_arithmetic_progression(start, step, length)
    
    # Выбираем случайную позицию для скрытия
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    
    # Заменяем скрытый элемент на ".."
    progression[hidden_index] = ".."
    question = " ".join(progression)
    
    return question, correct_answer
