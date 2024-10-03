# Tyler Mestery                             9-30-2024
# Assignment #3
#
# This is the classic game of NIM - here called NIMGRAB!

# importing the random module
import random

# creates a list that includes the visual part of the game
visual_dict = [
    """
|
    """,
    """
| |
    """,
    """
| | |
    """,
    """
| | | |
    """,
    """
| | | | |
    """,
    """
| | | | | |
    """,
    """
| | | | | | |
    """,
    """
| | | | | | | |
    """,
    """
| | | | | | | | |
    """,
    """
| | | | | | | | | |
    """,
    """
| | | | | | | | | | |
    """,
    """
| | | | | | | | | | | |
    """,
    """
| | | | | | | | | | | | |
    """,
    """
| | | | | | | | | | | | | |
    """,
    """
| | | | | | | | | | | | | | |
    """,
    """
| | | | | | | | | | | | | | | |
    """,
    """
| | | | | | | | | | | | | | | | |
    """,
    """
| | | | | | | | | | | | | | | | | |
    """,
    """
| | | | | | | | | | | | | | | | | | |
    """,
    """
| | | | | | | | | | | | | | | | | | | |
    """,
    """
| | | | | | | | | | | | | | | | | | | | |
    """,
    """
| | | | | | | | | | | | | | | | | | | | | |
    """,
    """
| | | | | | | | | | | | | | | | | | | | | | |
    """,
    """
| | | | | | | | | | | | | | | | | | | | | | | |
    """,
    """
| | | | | | | | | | | | | | | | | | | | | | | | |
    """
]

# starting code to present author and game name
def start():
    print("\nNIMGRAB!\n")
    print("By: Tyler Mestery")
    print("[COM S 127 A]\n")

def play_computer(count, data):
    # starting variable count for number of sticks left
    while(count > 0):

        user_play = int(input("How many items do you want to take [1-3]?: "))
        if (count >= 3):
            while ((user_play != 1) and (user_play != 2) and (user_play != 3)):
                print("ERROR: Invalid choice. Please choose again.")
                user_play = int(input("How many items do you want to take [1-3]?: "))
        elif (count == 2):
            while ((user_play != 1) and (user_play != 2)):
                print("ERROR: Invalid choice. Please choose again.")
                user_play = int(input("How many items do you want to take [1-2]?: "))
        elif (count == 1):
            while ((user_play != 1)):
                print("ERROR: Invalid choice. Please choose again.")
                user_play = int(input("How many items do you want to take [1-2]?: "))
        else:
            # another big error that shouldn't occur ever
            print(f"ERROR! YOU ENTERED: {user_play} WHICH IS NOT IN THE RANGE!")
            
        # executes if user wants to take 1
        if (user_play == 1):
            if (count <= 1):
                print("\nHuman took the last item. Computer wins!")
                break
            else:
                count = count - 1
                print(f"\nItems Left: {count}")
                print(visual_dict[count-1])

        # executes if user wants to take 2
        elif (user_play == 2):
            if (count <= 2):
                print("\nHuman took the last item. Computer wins!")
                break
            else:
                count = count - 2
                print(f"\nItems Left: {count}")
                print(visual_dict[count-1])

        # executes if user wants to take 3
        elif (user_play == 3):
            if (count <= 3):
                print("\nHuman took the last item. Computer wins!")
                break
            else:
                count = count - 3
                print(f"\nItems Left: {count}")
                print(visual_dict[count-1])

        # a very big error occured in the program if it gets to here...
        else:
            print(f"\nERROR: You typed {user_play} please type one of the following: [1, 2, 3]: ")

        # computers turn to take sticks away
        # makes it so the computer won't forfeit the game by taking the last stick (aka: losing the game due to itself)
        if count >= 4:
            computer_turn = random.choice(data)
            count = count - computer_turn
        elif count < 3:
            computer_turn = 1
            count = count - computer_turn
        elif count < 4:
            count_four_list = [1, 2]
            computer_turn = random.choice(count_four_list)
            count = count - computer_turn
        
        # players wins if it doesn't take the last stick!
        if count <= 0:
            print("\Computer took the last item. Human wins!")
            break
        else:
            print(f"Computer Takes {computer_turn}")
            print(f"\nItems Left: {(count)}")
            print(visual_dict[(count-1)])

def play_human(count, data):
     # starting variable count for number of sticks left
    while(count > 0):

        # PLAYER 1 TURN
        user_play = int(input("How many items do you want to take, Player 1? [1-3]?: "))
        if (count >= 3):
            while ((user_play != 1) and (user_play != 2) and (user_play != 3)):
                print("ERROR: Invalid choice. Please choose again.")
                user_play = int(input("How many items do you want to take, Player 1? [1-3]?: "))
        elif (count == 2):
            while ((user_play != 1) and (user_play != 2)):
                print("ERROR: Invalid choice. Please choose again.")
                user_play = int(input("How many items do you want to take, Player 1? [1-2]?: "))
        elif (count == 1):
            while ((user_play != 1)):
                print("ERROR: Invalid choice. Please choose again.")
                user_play = int(input("How many items do you want to take, Player 1? [1]?: "))
        else:
            # another big error that shouldn't occur ever
            print(f"ERROR! YOU ENTERED: {user_play} WHICH IS NOT IN THE RANGE!")

        # executes if PLAYER 1 wants to take 1
        if (user_play == 1):
            if (count <= 1):
                print("\nPlayer 1 took the last item. Player 2 wins!")
                break
            else:
                count = count - 1
                print(f"\nItems Left: {count}")
                print(visual_dict[count-1])

        # executes if PLAYER 1 wants to take 2
        elif (user_play == 2):
            if (count <= 2):
                print("\nPlayer 1 took the last item. Player 2 wins!")
                break
            else:
                count = count - 2
                print(f"\nItems Left: {count}")
                print(visual_dict[count-1])

        # executes if PLAYER 1 wants to take 3
        elif (user_play == 3):
            if (count <= 3):
                print("\nPlayer 1 took the last item. Player 2 wins!")
                break
            else:
                count = count - 3
                print(f"\nItems Left: {count}")
                print(visual_dict[count-1])

        # PLAYER 2 TURN

        user_play2 = int(input("How many items do you want to take, Player 2? [1-3]?: "))
        if (count >= 3):
            while ((user_play2 != 1) and (user_play2 != 2) and (user_play2 != 3)):
                print("ERROR: Invalid choice. Please choose again.")
                user_play2 = int(input("How many items do you want to take, Player 2? [1-3]?: "))
        elif (count == 2):
            while ((user_play2 != 1) and (user_play2 != 2)):
                print("ERROR: Invalid choice. Please choose again.")
                user_play2 = int(input("How many items do you want to take, Player 2? [1-2]?: "))
        elif (count == 1):
            while ((user_play2 != 1)):
                print("ERROR: Invalid choice. Please choose again.")
                user_play2 = int(input("How many items do you want to take, Player 2 [1]?: "))
        else:
            # another big error that shouldn't occur ever
            print(f"ERROR! YOU ENTERED: {user_play2} WHICH IS NOT IN THE RANGE!")

        # executes if PLAYER 2 wants to take 1
        if (user_play2 == 1):
            if (count <= 1):
                print("\nPlayer 2 took the last item. Player 1 wins!")
                break
            else:
                count = count - 1
                print(f"\nItems Left: {count}")
                print(visual_dict[count-1])

        # executes if PLAYER 2 wants to take 2
        elif (user_play2 == 2):
            if (count <= 2):
                print("\nPlayer 2 took the last item. Player 1 wins!")
                break
            else:
                count = count - 2
                print(f"\nItems Left: {count}")
                print(visual_dict[count-1])

        # executes if PLAYER 2 wants to take 3
        elif (user_play2 == 3):
            if (count <= 3):
                print("\nPlayer 2 took the last item. Player 1 wins!")
                break
            else:
                count = count - 3
                print(f"\nItems Left: {count}")
                print(visual_dict[count-1])

def rules():
    print("""
-The goal of the game is to take items from a row of items and to avoid being the player who takes the very last item (stick)
-Can by played against either human vs. human or computer vs. human
-20 to 25 items are placed in a row (referred too as sticks)
-Players take turns removing items from the row
-Take between 1 - 3 items at a time
-Last one to pick up an item (stick) loses
    """)

# main() function where most code falls 
def main():
    count = random.randint(20, 26)
    data = [1, 2, 3]
    start()
    running = True
    # while the game is running, complete:
    while running:
        # prompts user to either play, read rules, or quit
        user_menu = input("Do you want to [p]lay, read the [r]ules, or [q]uit?: ")
        while ((user_menu != 'p') and (user_menu != 'r') and (user_menu != 'q')):
            user_menu = input("Do you want to [p]lay, read the [r]ules, or [q]uit?: ")
        
        # user wants to play the game
        if (user_menu == 'p'):
            play_menu = input("Do you want to play against [h]uman or [c]omputer?: ")
            while ((play_menu != 'h') and (play_menu != 'c')):
                play_menu = input("Do you want to play against [h]uman or [c]omputer?: ")

            # play against a human
            if (play_menu == 'h'):
                print(f"\nItems Left: {count}")
                print(visual_dict[19])
                play_human(count, data)

            # play against the computer
            elif (play_menu == 'c'):
                print(f"\nItems Left: {count}")
                print(visual_dict[19])
                play_computer(count, data)

            # a very big error occured in the program if it gets to here...
            else:
                print(f"ERROR: You typed {user_menu} please type one of the following: [h]uman or [c]omputer?: ")
        
        # user wants to read the rules of the game
        elif (user_menu == 'r'):
            rules()
        # user wants to quit
        elif (user_menu == 'q'):
            running = False
        else:
            print(f"ERROR: You typed {user_menu} please type one of the following: [p]lay, read the [r]ules, or [q]uit: ")

# function to initiate main() and get it running
if __name__ == ("__main__"):
    main()