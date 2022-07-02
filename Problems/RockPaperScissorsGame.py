def main():
    player_1 = input("Enter your name : ")
    player_2 = input("Enter your name : ")

    p1 = input("Select one from Rock Paper Scissors : ")
    p2 = input("Select one from Rock Paper Scissors : ")

    p1.lower()
    p2.lower()

    def winner(input_1, input_2):
        if input_1 == "rock" and input_2 == "paper":
            return f"{player_1} Wins"
        elif input_1 == "rock" and input_2 == "scissors":
            return f"{player_1} Wins"
        elif input_1 == "paper" and input_2 == "rock":
            return f"{player_1} Wins"
        elif input_1 == "paper" and input_2 == "scissors":
            return f"{player_2} Wins"
        elif input_1 == "scissors" and input_2 == "rock":
            return f"{player_2} Wins"
        elif input_1 == "scissors" and input_2 == "paper":
            return f"{player_2} Wins"

    print(winner(p1, p2))
    play_again = input("play again ? 1: Press 1 to Play again , 2: Press 2 to Exit")
    if play_again == "1":
        main()
    else:
        exit()


if __name__ == "__main__":
    main()
