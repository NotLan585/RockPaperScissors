import random
from time import sleep


print("Lets play a game of Rock Paper Scissor")

options = (
    "Rock",
    "Paper",
    "Scissor"
)


def rock_paper_scissor():
    user_selection = input("Choose your weapon for battle!(Rock/Paper/Scissor):")

    computer_selection = random.choice(options)

    outcomes = {
        "Rock Paper": "You Lose",
        "Rock Rock": "You Tie",
        "Rock Scissor": "You Win",
        "Paper Rock": "You Win",
        "Paper Paper": "You Tie",
        "Paper Scissor": "You Lose",
        "Scissor Paper": "You Win",
        "Scissor Rock": "You Lose",
        "Scissor Scissor": "You Tie"
    }

    count = 0
    while user_selection not in options and count != 5:
        user_selection = input("Wrong choice, Choose your weapon for battle!(Rock/Paper/Scissor):")
        count += 1
        if count == 5:
            print("You are so funny... \n -No one ever")
            exit()

    dict_value = f"{user_selection + ' ' + computer_selection}"

    fist = (""" 
           ,--.--._
    ------" _, \___)
            / _/____)
            \//(____)
    ------\     (__)
           `-----" 
           """)

    boom = ("""
         _.-^^---....,,--       
     _--                  --_  
    <                        >)
    |                         | 
     \._                   _./  
        ```--. . , ; .--'''       
              | |   |             
           .-=||  | |=-.   
           `-=#$%&%$#=-'   
              | ;  :|     
     _____.,-#%&$@%#&#~,._____
    """)

    print("\n 3 . . ."
          f"\n {fist} ")
    sleep(1)
    print("\n 2 . . ."
          f"\n {fist} ")
    sleep(1)
    print("\n 1 . . ."
          f"\n {fist} ")
    sleep(1)
    print("\n GO!"
          f"\n {boom}")
    sleep(1)
    print(f"\n The computer chose {computer_selection}")
    sleep(1)
    print(f"\n {outcomes.get(f'{dict_value}')}")

    return outcomes.get(f"{dict_value}")


def calculate_score(user_wins, game_outcome):
    if game_outcome == "You Win":
        user_wins['wins'] += 1
        return user_wins
    elif game_outcome == "You Lose":
        user_wins['loses'] += 1
        return user_wins
    else:
        user_wins['ties'] += 1
        return user_wins


rock_paper_scissor()

play_again = input("Play again:(Yes/No) ")

user_wins = {
    'wins': 0,
    'loses': 0,
    'ties': 0
}

while play_again == "Yes":
    game_outcome = rock_paper_scissor()

    user_wins = calculate_score(user_wins, game_outcome)
    print(f"\n Your stats are: \n Wins: {user_wins['wins']}, \n Loses: {user_wins['loses']}, \n Ties: {user_wins['ties']}")
    play_again = input("Play again:(Yes/No) ")

print("\n Thanks for playing!")


