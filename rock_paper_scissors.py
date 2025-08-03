import random

def game():
    game_count = 0
    user_win = 0
    computer_win = 0

    def play_game():
        nonlocal game_count, user_win, computer_win

        choices = {1: "Stone", 2: "Paper", 3: "Scissors"}

        def get_user_choice():
            try:
                choice = int(input("\nEnter your choice:\n1: Stone\n2: Paper\n3: Scissors\n0: Exit\n> "))
                if choice in (0, 1, 2, 3):
                    return choice
                else:
                    print("Invalid input. Please enter 1, 2, 3, or 0 to exit.")
                    return get_user_choice()
            except ValueError:
                print("Invalid input. Please enter a number.")
                return get_user_choice()

        def decide_winner(user, computer):
            nonlocal user_win, computer_win
            print(f"\nYou chose: {choices[user]}")
            print(f"Computer chose: {choices[computer]}")

            if user == computer:
                return "It's a tie!"
            elif (user == 1 and computer == 3) or \
                 (user == 2 and computer == 1) or \
                 (user == 3 and computer == 2):
                user_win += 1
                return "You win!"
            else:
                computer_win += 1
                return "Computer wins!"

        while True:
            user_choice = get_user_choice()

            if user_choice == 0:
                print("\nGame ended.")
                print(f"Total games played: {game_count}")
                print(f"You won: {user_win}")
                print(f"Computer won: {computer_win}")
                break

            computer_choice = random.randint(1, 3)
            result = decide_winner(user_choice, computer_choice)

            game_count += 1
            print(result)
            print(f"Score - You: {user_win}, Computer: {computer_win}")

    return play_game

# Start the game using closure
play = game()
play()
