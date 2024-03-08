#File:CS112_A1_T2_Game 3-20231196
#Porpose:The is_square function checks if a given number is a perfect square.
#Author:Nayera Shaaban Rashad  
#ID:20231196

import math

# function to check if a number is a perfect square
def is_square(n):
    return math.isqrt(n) ** 2 == n

def possible_moves(coins):
    return [i for i in range(1, coins + 1) if is_square(i)]

# function to play the game
def play_game():
    n_coins = int(input("Enter a number of coins: "))
    
    if is_square(n_coins):
        print("Please enter a number that is not a square.")
        n_coins = int(input("Enter a number of coins:"))
    coins = n_coins

    # continue the game while there are still coins remaining
    while coins > 0:
        print("Coins left:", coins)
        move = int(input('Player 1: Please choose a square number less than or equal to the remaining coins: '))
        if move not in possible_moves(coins):
            print("Invalid move! Please choose a square number less than or equal to the remaining coins.")
            continue

        # update the number of remaining coins after player 1's move
        coins -= move
        # check if player 1 wins
        if coins == 0:
            print("Player 1 is the winner!")
            break

        print("Coins left:", coins)
        move = int(input('Player 2: Please choose a square number less than or equal to the remaining coins: '))
        if move not in possible_moves(coins):
            print("Invalid move! Please choose a square number less than or equal to the remaining coins.")
            continue

        # update the number of remaining coins after player 2's move
        coins -= move
        # check if player 2 wins
        if coins == 0:
            print("Player 2 is the winner!")
            break

play_game() 
