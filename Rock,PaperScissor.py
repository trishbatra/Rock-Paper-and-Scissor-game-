def start_game():
    name = input("Enter you're name here : ")
    print(f" Hello {name} welcome to Rock-Paper-scissor Game  ")
    choices_list = ["rock", "paper", "scissor"]
    import random
    user_points = 0
    computer_points = 0
    while True:
        computer_pick = choices_list[random.randint(0, 2)]
        user_pick = input(" choose rock paper or  scissor press s to stop game: ")
        if user_pick == 's':
            break
        if user_pick == "rock" and computer_pick == "scissor":
            print(f" Computer Picked {computer_pick} ")
            print(f" User Picked {user_pick} ")
            user_points += 1
            print(f"1 point to you {name}")
        elif user_pick == "scissor" and computer_pick == "paper":
            print(f" Computer Picked {computer_pick} ")
            print(f" User Picked {user_pick} ")
            user_points += 1
            print(f"1 point to you {name}")
        elif user_pick == "paper" and computer_pick == "rock":
            print(f" Computer Picked {computer_pick} ")
            print(f" User Picked {user_pick} ")
            user_points += 1
            print(f"1 point to you {name}")
        elif user_pick == computer_pick:
            print(f" Computer Picked {computer_pick} ")
            print(f" User Picked {user_pick} ")
            print("TIE No Points to anyone")
        else:
            print(f" Computer Picked {computer_pick} ")
            print(f" User Picked {user_pick} ")
            computer_points += 1
            print(f"1 point to Computer")
    print(f" Points scores by {name} : {user_points} ")
    print(f" points scored by computer : {computer_points} ")
start_game()


