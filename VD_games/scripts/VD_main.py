#!/usr/bin/env python3

import prompt
from VD_games.games import even, calc, gcd, progression, prime


def main():
    print("Welcome to the VD Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    
    print("Choose a game:")
    print("1 - Even Number")
    print("2 - Calculator") 
    print("3 - Greatest Common Divisor")
    print("4 - Arithmetic Progression")
    print("5 - Prime Number")
    
    choice = prompt.string("Enter your choice (1-5): ")
    
    games = {
        '1': even,
        '2': calc,
        '3': gcd,
        '4': progression,
        '5': prime
    }
    
    if choice in games:
        from VD_games.engine import run_game
        run_game(games[choice])
    else:
        print("Invalid choice!")


if __name__ == '__main__':
    main()
