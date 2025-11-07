"""Module for the even number game."""

import random


def is_even(number):
    """Check if a number is even.
    
    Args:
        number (int): The number to check
        
    Returns:
        bool: True if number is even, False otherwise
    """
    return number % 2 == 0


def generate_round():
    """Generate a round for the even number game.
    
    Returns:
        tuple: (question, correct_answer)
    """
    number = random.randint(1, 100)
    correct_answer = "yes" if is_even(number) else "no"
    return str(number), correct_answer


def run_even_game():
    """Run the even number game.
    
    Returns:
        bool: True if player wins, False otherwise
    """
    print("Welcome to the VD-games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    rounds_to_win = 3
    
    for _ in range(rounds_to_win):
        question, correct_answer = generate_round()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip().lower()
        
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return False
        
        print("Correct!")
    
    print(f"Congratulations, {name}!")
    return True


if __name__ == "__main__":
    run_even_game()
