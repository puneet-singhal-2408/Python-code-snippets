def main():

    import random
    number = random.randint(1,9)
    user_number = int(input("Guess the number between 1 to 9 : "))

    def guess(number,user_number):
        if number == user_number:
            return "You gussed right"
        elif number -1 <= user_number <= number + 1:
            return "you are too close"
        else:
            return "you are too far away"

    print(guess(number,user_number))


    quit_game = input("enter quit to end game")

    if quit_game == "quit":
        print("Game Over")

    else:
        print("new_game")
        main()



if __name__ == "__main__":
    main()